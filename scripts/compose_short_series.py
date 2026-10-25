#!/usr/bin/env python3
"""Cut verified lesson lines and silent question cards into short episodes."""
import argparse
import hashlib
import json
import math
import subprocess
import sys
import tempfile
from pathlib import Path

from compose_vertical_lesson import FPS, probe, tighten_pauses, write_srt


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(args):
    subprocess.run([str(x) for x in args], check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', required=True, type=Path)
    parser.add_argument('--episode', help='Render only this episode ID')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    lesson = args.config.resolve().parent
    cfg = json.loads(args.config.read_text())
    source = lesson / cfg['source_master']
    timeline = json.loads((lesson / cfg['source_timeline']).read_text())
    dialogue = json.loads((lesson / cfg['source_lesson']).read_text())
    lines = {line['line']: line for line in timeline}
    originals = {line['id']: line for line in dialogue['lines']}
    media = probe(source, 'ffprobe')
    episodes = [ep for ep in cfg['episodes'] if not args.episode or ep['id'] == args.episode]
    if not episodes:
        parser.error('Unknown episode ID')
    for ep in episodes:
        if not 1 <= ep['speech_speed'] <= 1.2:
            parser.error('Speech speed must be between 1 and 1.2')
        for item in ep['items']:
            for line_id in item.get('lines', []):
                line, original = lines[line_id], originals[line_id]
                if original['status'] != 'verified' or line['english'] != original['text'] or line['chinese'] != original['zh']:
                    parser.error(f'Unverified or inconsistent source: {line_id}')
                if sha(lesson / original['audio']) != line['audio_sha256']:
                    parser.error(f'Source WAV changed: {line_id}')
            ids = item.get('lines', [])
            if ids and [r['line'] for r in timeline if lines[ids[0]]['start'] <= r['start'] <= lines[ids[-1]]['start']] != ids:
                parser.error('Each line group must be contiguous in the source timeline')
            if 'source_end' in item and (len(ids) != 1 or not item.get('trim_reason') or not lines[ids[0]]['start'] < item['source_end'] <= lines[ids[0]]['end']):
                parser.error('A reviewed tail trim needs one line, a valid source end, and its reason')
        output = lesson / ep['output']
        work = lesson / 'edit' / cfg['id'] / ep['id']
        if output.exists() or work.exists():
            parser.error(f'Output already exists; choose a new version: {ep["id"]}')
        print(json.dumps({'episode': ep['id'], 'output': str(output), 'speech_speed': ep['speech_speed'], 'items': ep['items']}, ensure_ascii=False), flush=True)
    if args.dry_run:
        return
    fingerprints = {key: {'path': cfg[key], 'sha256': sha(lesson / cfg[key])} for key in ('source_master', 'source_timeline', 'source_lesson')}
    for ep in episodes:
        work = lesson / 'edit' / cfg['id'] / ep['id']
        work.mkdir(parents=True)
        output = lesson / ep['output']
        output.parent.mkdir(parents=True, exist_ok=True)
        cues, mapping, parts = [], [], []
        cursor = 0.0
        with tempfile.TemporaryDirectory(prefix='lesson-short-series-') as directory:
            temp = Path(directory)
            for index, item in enumerate(ep['items']):
                raw, compact, final = [temp / f'{index}-{kind}.mkv' for kind in ('raw', 'compact', 'final')]
                if 'lines' in item:
                    selected = [lines[line_id] for line_id in item['lines']]
                    start = max(0, math.floor((selected[0]['start'] - 0.06) * FPS) / FPS)
                    end = min(float(media['duration']), math.ceil((selected[-1]['end'] + 0.12) * FPS) / FPS)
                    if 'source_end' in item:
                        end = math.ceil(item['source_end'] * FPS) / FPS
                    local = [{'start': row['start'] - start, 'end': min(row['end'], end) - start, 'english': row['english'], 'chinese': row['chinese']} for row in selected]
                    run(['ffmpeg', '-v', 'error', '-n', '-ss', start, '-i', source, '-t', end-start, '-map', '0:v:0', '-map', '0:a:0', '-c:v', 'libx264', '-preset', 'fast', '-crf', '18', '-r', FPS, '-c:a', 'pcm_s16le', raw])
                    duration = float(probe(raw, 'ffprobe')['duration'])
                    cuts = tighten_pauses(raw, compact, local, duration, 'ffmpeg')
                    compact_duration = float(probe(compact, 'ffprobe')['duration'])
                    duration = math.ceil(compact_duration / ep['speech_speed'] * FPS) / FPS
                    run(['ffmpeg', '-v', 'error', '-n', '-i', compact, '-vf', f'setpts=(PTS-STARTPTS)/{ep["speech_speed"]},tpad=stop_mode=clone:stop_duration=0.1', '-af', f'atempo={ep["speech_speed"]},aresample=24000,apad,atrim=duration={duration}', '-t', duration, '-r', FPS, '-c:v', 'libx264', '-preset', 'fast', '-crf', '18', '-c:a', 'pcm_s16le', final])
                    for row, cue in zip(selected, local):
                        cue['start'] = cursor + cue['start'] / ep['speech_speed']
                        cue['end'] = cursor + cue['end'] / ep['speech_speed']
                        cues.append(cue)
                        mapping.append({**cue, 'kind': 'textbook-dialogue', 'line': row['line'], 'speaker': row['speaker'], 'audio_sha256': row['audio_sha256']})
                    record = {'lines': item['lines'], 'source_range': [start, end], 'reviewed_tail_trim': {k: item[k] for k in ('source_end', 'trim_reason') if k in item}, 'silence_cuts_relative_to_source_range': cuts, 'speech_speed': ep['speech_speed']}
                else:
                    duration = math.ceil(item['duration'] * FPS) / FPS
                    frame = temp / f'{index}-hold.png'
                    run(['ffmpeg', '-v', 'error', '-n', '-ss', item['source_time'], '-i', source, '-frames:v', '1', frame])
                    run(['ffmpeg', '-v', 'error', '-n', '-loop', '1', '-framerate', FPS, '-i', frame, '-f', 'lavfi', '-i', 'anullsrc=r=24000:cl=mono', '-t', duration, '-c:v', 'libx264', '-preset', 'fast', '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'pcm_s16le', final])
                    cue = {'start': cursor, 'end': cursor + duration, 'english': item['english'], 'chinese': item['chinese']}
                    cues.append(cue)
                    mapping.append({**cue, 'kind': 'editorial-card-no-voice', 'id': item['id']})
                    record = {**item, 'speech_speed': None}
                parts.append(final)
                record.update({'start': cursor, 'end': cursor + duration})
                mapping.append({'kind': 'picture-edit', **record})
                cursor += duration
            tail = max(ep['tail_seconds'], ep.get('minimum_seconds', 0) - cursor)
            duration = math.ceil((cursor + tail) * FPS) / FPS
            if not cfg['duration_range'][0] <= duration <= cfg['duration_range'][1]:
                raise ValueError(f'{ep["id"]}: {duration}s outside configured duration range')
            concat = temp / 'parts.ffconcat'
            concat.write_text('ffconcat version 1.0\n' + ''.join(f"file '{p.as_posix()}'\n" for p in parts))
            master = work / 'master.mp4'
            run(['ffmpeg', '-v', 'error', '-n', '-f', 'concat', '-safe', '0', '-i', concat, '-vf', f'tpad=stop_mode=clone:stop_duration={duration-cursor}', '-af', f'apad,atrim=duration={duration}', '-t', duration, '-c:v', 'libx264', '-preset', 'fast', '-crf', '18', '-c:a', 'aac', '-b:a', '96k', '-movflags', '+faststart', master])
        if ep.get('hold_last_card'):
            cues[-1]['end'] = duration
            for row in reversed(mapping):
                if row['kind'] == 'editorial-card-no-voice':
                    row['end'] = duration
                    break
        srt = work / 'subtitles.srt'
        write_srt(srt, cues)
        run([sys.executable, Path(__file__).with_name('compose_vertical_lesson.py'), '--input', master, '--srt', srt, '--grade', cfg['grade'], '--unit', cfg['unit'], '--title', cfg['title'], '--lesson', ep['label'], '--theme', 'black', '--preset-version', '2', '--opening-text', ep['hook'], '--opening-seconds', ep['hook_seconds'], '--output', output])
        sidecar = {'recipe': str(args.config), 'recipe_sha256': sha(args.config), 'renderer_sha256': sha(Path(__file__)), 'sources': fingerprints, 'episode': ep, 'timeline': mapping, 'master': str(master.relative_to(lesson)), 'master_sha256': sha(master), 'subtitles': str(srt.relative_to(lesson)), 'subtitle_sha256': sha(srt), 'output': str(output.relative_to(lesson)), 'output_sha256': sha(output), 'duration_seconds': duration, 'tail_seconds': duration-cursor, 'new_provider_requests': 0, 'qa': {'human_full_listening': 'pending', 'user_acceptance': 'pending'}}
        (work / 'assembly.json').write_text(json.dumps(sidecar, ensure_ascii=False, indent=2) + '\n')
        print(json.dumps({'episode': ep['id'], 'duration': duration, 'output_sha256': sha(output)}, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()
