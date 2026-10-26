#!/usr/bin/env python3
"""Render social-story-v1 comparisons from existing, verified short-series edits."""
import argparse
import copy
import json
from pathlib import Path
import subprocess
import tempfile

from PIL import Image, ImageDraw

from compose_vertical_lesson import FPS, font_from, probe, wrap_text
from review_short_series import audit, read, sha

EN = ['/System/Library/Fonts/Supplemental/Arial Bold.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf']
ZH = ['/System/Library/Fonts/PingFang.ttc', '/System/Library/Fonts/STHeiti Medium.ttc', '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc']
COLORS = {'kazama': '#77CCFF', 'shinchan': '#FFD270', 'nene': '#FFA5D0', 'narrator': '#FFFFFF'}


def run(args):
    subprocess.run([str(arg) for arg in args], check=True)


def overlay(path, cfg, ep, row, at, height):
    img = Image.new('RGBA', (1080, 1920))
    d = ImageDraw.Draw(img)
    # Gradient keeps captions readable while leaving all foreground faces visible.
    for y in range(1920):
        alpha = round(155 * max(0, min(1, (y - 1050) / 260))) if y > 1050 else 0
        d.line((0, y, 1080, y), fill=(8, 14, 25, alpha))
    d.rounded_rectangle((64, 88, 550, 150), radius=25, fill='#152334')
    d.text((88, 118), cfg['corner_label'], font=font_from(ZH, 28), fill='#ECF4FF', anchor='lm')
    if at < ep['hook_seconds']:
        for i, text in enumerate(wrap_text(d, ep['hook'], font_from(ZH, 72), 900)):
            d.text((64, 245 + i * 90), text, font=font_from(ZH, 72), fill='white', stroke_width=2, stroke_fill='#142231')
    if row:
        if row['kind'] == 'textbook-dialogue':
            speaker = row['speaker']
            color = COLORS.get(speaker, '#FFFFFF')
            name = cfg['speaker_names'][speaker]
            d.rounded_rectangle((64, 1140, 410, 1210), radius=28, fill=color)
            d.text((88, 1175), name + ' · 正在说', font=font_from(ZH, 36), fill='#0B1829', anchor='lm')
            if not row['voiceover']:
                x = 40 + round(1000 * cfg['speaker_positions'][row['shot_id']][speaker])
                y = 480 + height
                d.polygon(((x, y - 14), (x - 20, y + 20), (x + 20, y + 20)), fill=color)
                d.rounded_rectangle((x - 44, y + 20, x + 44, y + 28), radius=4, fill=color)
        y = 1280
        for text, fonts, size, gap, color in ((row['english'], EN, 54, 68, 'white'), (row['chinese'], ZH, 46, 62, '#DBE7F5')):
            for line in wrap_text(d, text, font_from(fonts, size), 875):
                d.text((64, y), line, font=font_from(fonts, size), fill=color, stroke_width=1, stroke_fill='#0B1829')
                y += gap
            y += 24
        if y > 1640:
            raise ValueError('Caption exceeds phone safe area')
    img.save(path)


def cover(path, source_frame, cfg):
    """Independent poster layout; source animation is a referenced illustration."""
    img = Image.new('RGB', (1080, 1920), '#122337')
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((64, 110, 620, 178), radius=25, fill='#FFD270')
    d.text((88, 144), cfg['corner_label'], font=font_from(ZH, 32), fill='#122337', anchor='lm')
    for i, text in enumerate(cfg['cover']['title_lines']):
        d.text((64, 290 + i * 120), text, font=font_from(ZH, 92), fill='white')
    with Image.open(source_frame) as frame:
        frame = frame.convert('RGB')
        frame.thumbnail((1000, 680))
        frame = frame.resize((1000, round(1000 * frame.height / frame.width)))
        img.paste(frame, (40, 700))
    d.rounded_rectangle((64, 1450, 960, 1580), radius=32, fill='#FFD270')
    d.text((98, 1515), cfg['cover']['question'], font=font_from(ZH, 58), fill='#122337', anchor='lm')
    d.text((64, 1660), '15秒英语小剧场 · 雨天计划', font=font_from(ZH, 36), fill='#D2E2F4')
    img.save(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', required=True, type=Path)
    parser.add_argument('--episode')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    config = args.config.resolve()
    lesson, cfg = config.parent, read(config)
    if cfg['template'] != 'social-story-v1':
        parser.error('Expected social-story-v1 template')
    binding = lesson / cfg['speaker_bindings']
    eps = [ep for ep in cfg['episodes'] if not args.episode or ep['id'] == args.episode]
    if not eps:
        parser.error('Unknown episode')
    prepared = []
    for ep in eps:
        source_qa = audit(lesson / cfg['source_series'], binding, ep['source_episode'])
        if source_qa['static_errors']:
            parser.error('Source edit failed static QA: ' + json.dumps(source_qa['static_errors']))
        source_cfg = read(lesson / cfg['source_series'])
        path = lesson / 'edit' / source_cfg['id'] / ep['source_episode'] / 'assembly.json'
        assembly = read(path)
        if ep['items'] != assembly['episode']['items']:
            parser.error('Reuse items must exactly match source edit')
        if ep['speech_speed'] != assembly['episode']['speech_speed']:
            parser.error('Reused edit speech speed cannot change')
        work, output = lesson / 'edit' / cfg['id'] / ep['id'], lesson / ep['output']
        if work.exists() or output.exists():
            parser.error('Output exists; choose a new version')
        media = probe(lesson / assembly['master'], 'ffprobe')
        font_from(ZH, 28)
        font_from(EN, 54)
        for row in source_qa['lines']:
            if not row['voiceover'] and not 0 <= cfg['speaker_positions'][row['shot_id']][row['speaker']] <= 1:
                parser.error('Speaker position must be normalized to foreground width')
        prepared.append((ep, assembly, source_qa, work, output, media, path))
        print(json.dumps({'episode': ep['id'], 'template': cfg['template'], 'source_static': 'pass', 'human': 'pending', 'provider_requests': 0}, ensure_ascii=False), flush=True)
    if args.dry_run:
        return
    for ep, assembly, source_qa, work, output, media, path in prepared:
        work.mkdir(parents=True)
        output.parent.mkdir(parents=True, exist_ok=True)
        master = lesson / assembly['master']
        duration = assembly['duration_seconds']
        mapping = copy.deepcopy(assembly['timeline'])
        bindings = read(binding)['lines']
        for row in mapping:
            if row['kind'] == 'textbook-dialogue':
                row.update(bindings[row['line']])
                row['focus_method'] = 'timed speaker badge and below-frame directional marker'
                row['audio_interval'] = [row['start'], row['end']]
        cues = [r for r in mapping if r['kind'] in ('textbook-dialogue', 'editorial-card-no-voice')]
        (work / 'subtitles.srt').write_bytes((lesson / assembly['subtitles']).read_bytes())
        height = round(1000 / media['original_display_aspect_ratio']) // 2 * 2
        with tempfile.TemporaryDirectory(prefix='mantou-social-') as directory:
            temp = Path(directory)
            frames = round(duration * FPS)
            bounds = sorted({0, frames, round(ep['hook_seconds'] * FPS)} | {round(r[k] * FPS) for r in cues for k in ('start', 'end')})
            entries = ['ffconcat version 1.0']
            for index, (start, end) in enumerate(zip(bounds, bounds[1:])):
                at = (start + end) / (2 * FPS)
                row = next((r for r in cues if r['start'] <= at < r['end']), None)
                card = temp / f'overlay-{index}.png'
                overlay(card, cfg, ep, row, at, height)
                entries += [f"file '{card.as_posix()}'", f'option framerate {FPS}', f'duration {(end - start) / FPS:.9f}']
            entries += [f"file '{card.as_posix()}'", f'option framerate {FPS}']
            concat = temp / 'overlays.ffconcat'
            concat.write_text('\n'.join(entries) + '\n')
            filters = (f'[0:v]split=2[b][f];[b]scale=288:512:force_original_aspect_ratio=increase,crop=288:512,'
                       f'gblur=sigma=16,scale=1080:1920,eq=brightness=-0.12[bg];'
                       f'[f]scale=1000:{height}:flags=lanczos,setsar=1[fg];'
                       f'[bg][fg]overlay=40:480[stage];[1:v]fps={FPS},format=rgba[ui];'
                       f'[stage][ui]overlay=0:0:eof_action=repeat[v]')
            run(['ffmpeg', '-v', 'error', '-n', '-i', master, '-f', 'concat', '-safe', '0', '-i', concat,
                 '-filter_complex', filters, '-map', '[v]', '-map', '0:a:0', '-t', duration, '-r', FPS,
                 '-c:v', 'libx264', '-preset', 'fast', '-crf', '19', '-pix_fmt', 'yuv420p', '-c:a', 'copy', '-movflags', '+faststart', output])
            source_frame = work / 'cover-source.png'
            run(['ffmpeg', '-v', 'error', '-n', '-ss', cfg['cover']['source_time'], '-i', master, '-frames:v', 1, source_frame])
            cover(work / 'cover.png', source_frame, cfg)
        run(['ffmpeg', '-v', 'error', '-xerror', '-i', output, '-f', 'null', '-'])
        metadata = {**assembly, 'recipe': str(config), 'recipe_sha256': sha(config), 'renderer_sha256': sha(Path(__file__)),
                    'template': cfg['template'], 'episode': ep, 'timeline': mapping,
                    'source_assembly': {'path': str(path.relative_to(lesson)), 'sha256': sha(path)},
                    'speaker_bindings': {'path': cfg['speaker_bindings'], 'sha256': sha(binding)},
                    'subtitles': str((work / 'subtitles.srt').relative_to(lesson)), 'subtitle_sha256': sha(work / 'subtitles.srt'),
                    'cover': {'path': str((work / 'cover.png').relative_to(lesson)), 'sha256': sha(work / 'cover.png'), 'design': cfg['cover'], 'kind': 'independent poster using source animation frame'},
                    'output': ep['output'], 'output_sha256': sha(output),
                    'visual_limitations': cfg['visual_limitations'], 'media': probe(output, 'ffprobe'),
                    'qa': {'full_decode': 'pass', 'human_full_listening': 'pending', 'phone_visual_review': 'pending', 'publishable': False}}
        (work / 'assembly.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n')
        print(json.dumps({'episode': ep['id'], 'output': ep['output'], 'sha256': metadata['output_sha256']}, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()
