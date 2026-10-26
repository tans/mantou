#!/usr/bin/env python3
"""Validate speaker bindings and gate publication on hash-bound human review."""
import argparse
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
import subprocess

from compose_vertical_lesson import probe, read_srt

CHECKS = ('speaker_voice', 'intelligibility', 'subtitle_timing', 'tail', 'lip_mismatch')


def sha(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def dated(value):
    try:
        return datetime.fromisoformat(value.replace('Z', '+00:00')).tzinfo is not None
    except (ValueError, TypeError, AttributeError):
        return False


def bindings_for(lesson, cfg, path, line_ids):
    """Check declarations against actual inputs, never infer visual correctness."""
    data = read(path)
    errors, waived = [], []
    originals = {row['id']: row for row in cfg['lines']}
    shots = {row['id']: row for row in cfg['shots']}
    voices = cfg['voices']
    bindings = data['lines']

    def problem(rule, line_id, message):
        waiver = next((w for w in data.get('waivers', [])
                       if w.get('rule') == rule and w.get('line') == line_id
                       and w.get('reason', '').strip() and w.get('reviewer', '').strip()
                       and dated(w.get('reviewed_at'))), None)
        record = {'rule': rule, 'line': line_id, 'message': message}
        # Only intentional visual staging can be waived; provenance never can.
        if waiver and rule in ('active_character', 'speaker_focus'):
            waived.append({**record, 'waiver': waiver})
        else:
            errors.append(record)

    for line_id in line_ids:
        original, binding = originals.get(line_id), bindings.get(line_id)
        if not original or not binding:
            problem('missing_mapping', line_id, 'Missing script line or binding')
            continue
        speaker, shot_id = original['speaker'], original['shot']
        voice, shot = voices.get(speaker), shots.get(shot_id)
        if not voice or not shot or line_id not in shot['lines']:
            problem('source_reference', line_id, 'Unknown speaker/shot or line outside shot')
            continue
        if original['status'] != 'verified':
            problem('unverified', line_id, 'Script is not verified')
        if any(binding.get(k) != v for k, v in {
            'speaker': speaker, 'shot_id': shot_id, 'voice_profile': voice['profile'],
        }.items()):
            problem('identity', line_id, 'Speaker, voice profile or shot differs from script')
        active = binding.get('active_character')
        others = binding.get('other_characters', [])
        if not isinstance(others, list) or len(set(others)) != len(others) or any(c not in voices for c in others):
            problem('character_id', line_id, 'Invalid other_characters')
            others = []
        if active is not None and (active not in voices or active in others):
            problem('character_id', line_id, 'Unknown or duplicate active character')
        if binding.get('shot_type') not in ('wide', 'single', 'two-shot', 'group', 'insert'):
            problem('shot_type', line_id, 'Declare shot_type')
        if type(binding.get('voiceover')) is not bool or type(binding.get('on_screen_speaker')) is not bool:
            problem('speaker_focus', line_id, 'Declare voiceover and on_screen_speaker booleans')
        elif binding['voiceover']:
            if binding['on_screen_speaker'] or not binding.get('staging_reason', '').strip():
                problem('speaker_focus', line_id, 'Voiceover needs off-screen staging reason')
        elif active != speaker or not binding['on_screen_speaker']:
            problem('active_character', line_id, 'On-screen active character differs from speaker')
        if others and not binding.get('focus_method', '').strip():
            problem('speaker_focus', line_id, 'Multiple characters need explicit focus method')
        audio = lesson / original['audio']
        metadata = read(audio.with_suffix('.json'))
        expected = {'text_sha256': sha(lesson / original['input']), 'voice': voice.get('voice'),
                    'style': original.get('style', voice['style']), 'speed': cfg.get('tts_speed'),
                    'model': cfg.get('tts_model', 'mimo-v2.5-tts')}
        if metadata['input'] != expected or metadata['sha256'] != sha(audio):
            problem('audio_fingerprint', line_id, 'Actual WAV or synthesis parameters changed')
        if (lesson / original['input']).read_text().strip() != original['text']:
            problem('text_fingerprint', line_id, 'TTS text differs from script')
        video = lesson / shot['output']
        if read(video.with_suffix('.json'))['output_sha256'] != sha(video):
            problem('shot_fingerprint', line_id, 'Actual source shot changed')
    return bindings, errors, waived


def audit(config_path, binding_path, episode_id, review_path=None):
    config_path = config_path.resolve()
    lesson, cfg = config_path.parent, read(config_path)
    original = read(lesson / cfg['source_lesson'])
    ep = next(ep for ep in cfg['episodes'] if ep['id'] == episode_id)
    assembly_path = lesson / 'edit' / cfg['id'] / ep['id'] / 'assembly.json'
    assembly = read(assembly_path)
    spoken = [row for row in assembly['timeline'] if row['kind'] == 'textbook-dialogue']
    expected_ids = [lid for item in ep['items'] for lid in item.get('lines', [])]
    bindings, errors, waived = bindings_for(lesson, original, binding_path, expected_ids)

    def error(rule, message):
        errors.append({'rule': rule, 'message': message})

    output, master, srt = (lesson / assembly[key] for key in ('output', 'master', 'subtitles'))
    if assembly['output'] != ep['output'] or assembly['episode'] != ep:
        error('episode_identity', 'Assembly episode differs from selected recipe')
    for name, path in (('output', output), ('master', master), ('subtitle', srt)):
        if sha(path) != assembly[name + '_sha256']:
            error('assembly_fingerprint', f'{name} changed since assembly')
    if sha(config_path) != assembly['recipe_sha256']:
        error('recipe_fingerprint', 'Recipe changed since assembly')
    source_keys = ('source_master', 'source_timeline', 'source_lesson')
    if set(assembly.get('sources', {})) != set(source_keys):
        error('source_coverage', 'Assembly must identify master, timeline and lesson sources')
    for key in source_keys:
        source = assembly.get('sources', {}).get(key)
        if not source:
            continue
        if source['path'] != cfg[key] or sha(lesson / source['path']) != source['sha256']:
            error('source_fingerprint', f'{key} changed since assembly')
    cover = assembly.get('cover')
    cover_sha256 = None
    if cfg.get('template') == 'social-story-v1' and not cover:
        error('cover_coverage', 'Social-story output needs an independently rendered cover')
    if cover:
        cover_path = lesson / cover['path']
        if cover_path.is_file():
            cover_sha256 = sha(cover_path)
            if cover_sha256 != cover['sha256']:
                error('cover_fingerprint', 'Actual cover changed since assembly')
        else:
            error('cover_fingerprint', 'Actual cover file is missing')
        if cfg.get('template') == 'social-story-v1' and cover.get('design') != cfg.get('cover'):
            error('cover_design', 'Cover design differs from selected recipe')
    if assembly.get('speaker_bindings') and assembly['speaker_bindings']['sha256'] != sha(binding_path):
        error('binding_fingerprint', 'Bindings changed since assembly')
    if assembly.get('source_assembly'):
        parent = assembly['source_assembly']
        if sha(lesson / parent['path']) != parent['sha256']:
            error('parent_fingerprint', 'Reused edit assembly changed')
    media = probe(output, 'ffprobe')
    duration = float(media['duration'])
    if abs(duration - assembly['duration_seconds']) > .12:
        error('duration', 'Media duration differs from assembly')
    if [row['line'] for row in spoken] != expected_ids:
        error('coverage', 'Spoken line sequence differs from recipe')
    captions = [r for r in assembly['timeline'] if r['kind'] in ('textbook-dialogue', 'editorial-card-no-voice')]
    srt_cues = read_srt(srt)
    if len(captions) != len(srt_cues):
        error('subtitles', 'SRT cue coverage differs from assembly')
    for cue, subtitle in zip(captions, srt_cues):
        if any(cue[k] != subtitle[k] for k in ('english', 'chinese')) or any(abs(cue[k] - subtitle[k]) > .002 for k in ('start', 'end')):
            error('subtitles', 'SRT text or timing differs from assembly')
    for index, row in enumerate(captions):
        if not all(math.isfinite(row[k]) for k in ('start', 'end')) or not 0 <= row['start'] < row['end'] <= duration + .002:
            error('interval', f'Invalid interval at cue {index + 1}')
        if index and row['start'] < captions[index - 1]['end'] - .002:
            error('interval', f'Overlapping interval at cue {index + 1}')
    originals = {row['id']: row for row in original['lines']}
    checklist = []
    for row in spoken:
        line_id = row['line']
        source = originals.get(line_id)
        binding = bindings.get(line_id, {})
        if any(key in row and row[key] != value for key, value in binding.items() if key != 'focus_method'):
            error('binding_identity', f'Assembly binding differs from current declaration: {line_id}')
        if source:
            if row['speaker'] != source['speaker'] or row['audio_sha256'] != sha(lesson / source['audio']) or row['english'] != source['text'] or row['chinese'] != source['zh']:
                error('line_identity', f'Assembly line differs from verified input: {line_id}')
            if not any(r['kind'] == 'picture-edit' and line_id in r.get('lines', []) and r['start'] <= row['start'] and r['end'] + .002 >= row['end'] for r in assembly['timeline']):
                error('picture_interval', f'No picture edit covers {line_id}')
        checklist.append({**binding, **row, 'audio_interval': [row['start'], row['end']],
                          'audio': source['audio'] if source else None,
                          'checks': {key: 'pending' for key in CHECKS}})
    identity = {'output_sha256': sha(output), 'assembly_sha256': sha(assembly_path),
                'bindings_sha256': sha(binding_path), 'config_sha256': sha(config_path)}
    if cover:
        identity['cover_sha256'] = cover_sha256
    human_errors = []
    human = read(review_path) if review_path else None
    if not human:
        human_errors.append('Full audiovisual human review pending')
    else:
        if any(human.get(k) != v for k, v in identity.items()):
            human_errors.append('Review hashes do not match current artifacts')
        if not human.get('reviewer', '').strip() or not dated(human.get('reviewed_at')) or human.get('full_playback_with_sound') is not True:
            human_errors.append('Named reviewer, zoned date and full playback with sound required')
        reviewed = human.get('lines', [])
        if [r.get('line') for r in reviewed] != expected_ids:
            human_errors.append('Human review must cover every spoken line in order')
        for row in reviewed:
            if any(row.get('checks', {}).get(key) != 'pass' for key in CHECKS):
                human_errors.append(f'{row.get("line")}: pending or failed human check')
        if any(human.get(key) != 'pass' for key in ('visual_safety', 'hook_payoff')):
            human_errors.append('Visual safety and hook/payoff review must pass')
        if cover and human.get('cover_visual') != 'pass':
            human_errors.append('Independent cover visual review must pass')
    human_failed = bool(human and (any(human.get(k) != v for k, v in identity.items())
                        or any(value == 'fail' for row in human.get('lines', []) for value in row.get('checks', {}).values())
                        or any(human.get(key) == 'fail' for key in ('visual_safety', 'hook_payoff', 'cover_visual'))))
    return {'schema_version': 1, 'episode': ep['id'], 'output': str(output), **identity,
            'duration_seconds': duration, 'cover': cover, 'static_errors': errors, 'waivers': waived,
            'static_status': 'fail' if errors else 'pass', 'human_errors': human_errors,
            'human_status': 'pass' if not human_errors else ('fail' if human_failed else 'pending'),
            'publishable': not errors and not human_errors, 'lines': checklist,
            'scope': 'Input provenance and declared staging only; visual/voice correctness requires human review'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', required=True, type=Path)
    parser.add_argument('--bindings', required=True, type=Path)
    parser.add_argument('--episode', required=True)
    parser.add_argument('--review', type=Path, help='Completed human review, bound to these hashes')
    parser.add_argument('--report', type=Path, help='New JSON report plus Markdown checklist')
    parser.add_argument('--require-publishable', action='store_true', help='Exit 2 if any gate remains open')
    args = parser.parse_args()
    try:
        result = audit(args.config, args.bindings, args.episode, args.review)
    except (OSError, ValueError, KeyError, TypeError, StopIteration, subprocess.CalledProcessError) as exc:
        print(json.dumps({'static_status': 'fail', 'publishable': False,
                          'input_error': f'{type(exc).__name__}: {exc}'}, ensure_ascii=False))
        raise SystemExit(2)
    if args.report:
        markdown_path = args.report.with_suffix('.md')
        if args.report.exists() or markdown_path.exists():
            parser.error('Report exists; choose a new version')
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
        text = ['# 逐句声画复核', '', f'文件：{result["output"]}', '',
                '封面：' + (result['cover']['path'] if result['cover'] else '无本地独立封面；平台封面须在发布时核对'), '',
                f'静态：{result["static_status"]}；人工：{result["human_status"]}；可发布：{result["publishable"]}', '',
                '按以下秒数带声音完整播放，逐句检查声线归属、可懂度、字幕、尾音和显著口型错位。', '',
                '| 行 | 秒数 | 人物/声线 | 镜头 | 英文 | 检查 |', '| --- | --- | --- | --- | --- | --- |']
        for row in result['lines']:
            text.append(f'| {row["line"]} | {row["start"]:.3f}–{row["end"]:.3f} | {row.get("speaker")}/{row.get("voice_profile")} | {row.get("shot_id")} | {row["english"]} | pending |')
        text += ['', '机器检查不代表实际声画一致。人工记录使用同名 JSON 中的全部 *_sha256（有独立封面时含 cover_sha256）和逐行 checks，另填 reviewer、reviewed_at、full_playback_with_sound、visual_safety、hook_payoff；有独立封面时另填 cover_visual。', '',
                 '静态错误：' + json.dumps(result['static_errors'], ensure_ascii=False),
                 '人工阻塞：' + json.dumps(result['human_errors'], ensure_ascii=False), '']
        markdown_path.write_text('\n'.join(text))
    print(json.dumps({k: v for k, v in result.items() if k != 'lines'}, ensure_ascii=False, indent=2))
    if result['static_errors'] or (args.require_publishable and not result['publishable']):
        raise SystemExit(2)


if __name__ == '__main__':
    main()
