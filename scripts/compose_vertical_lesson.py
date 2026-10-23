#!/usr/bin/env python3
"""Compose a landscape lesson video into the project's fixed vertical white layout."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

CANVAS = (1080, 1920)
VIDEO_X, VIDEO_Y, VIDEO_W = 27, 500, 1026
CARD = (62, 1240, 1018, 1710)
FPS = 24


def require_bin(name: str) -> str:
    found = shutil.which(name)
    if not found:
        raise SystemExit(f"Required program not found: {name}")
    return found


def font_from(paths: list[str], size: int) -> ImageFont.FreeTypeFont:
    for candidate in paths:
        if Path(candidate).is_file():
            return ImageFont.truetype(candidate, size)
    raise SystemExit(f"No supported font found. Install a font or pass a font path: {paths}")


def parse_time(value: str) -> float:
    hours, minutes, rest = value.split(":")
    seconds, millis = rest.split(",")
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds) + int(millis) / 1000


def read_srt(path: Path) -> list[dict[str, object]]:
    text = path.read_text(encoding="utf-8-sig").strip()
    cues = []
    for block in re.split(r"\n\s*\n", text):
        rows = block.splitlines()
        if len(rows) < 3 or "-->" not in rows[1]:
            raise SystemExit(f"Malformed bilingual SRT cue: {block!r}")
        start_text, end_text = (part.strip() for part in rows[1].split("-->"))
        caption_lines = [row.strip() for row in rows[2:] if row.strip()]
        if len(caption_lines) != 2:
            raise SystemExit(f"Each cue must have exactly 2 lines (English + Chinese): {block!r}")
        start, end = parse_time(start_text), parse_time(end_text)
        if start < 0 or end <= start:
            raise SystemExit(f"Invalid SRT time range: {block!r}")
        cues.append({"start": start, "end": end, "english": caption_lines[0], "chinese": caption_lines[1]})
    if not cues:
        raise SystemExit("SRT contains no subtitle cues")
    return cues


def probe(path: Path, ffprobe: str) -> dict[str, object]:
    data = json.loads(subprocess.check_output([
        ffprobe, "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)
    ], text=True))
    video = next((stream for stream in data["streams"] if stream["codec_type"] == "video"), None)
    audio = next((stream for stream in data["streams"] if stream["codec_type"] == "audio"), None)
    if not video:
        raise SystemExit(f"Input has no video stream: {path}")
    if not audio:
        raise SystemExit(f"Input has no audio stream: {path}")
    ratio_text = video.get("display_aspect_ratio")
    if ratio_text and ":" in ratio_text:
        left, right = ratio_text.split(":", 1)
        ratio = float(left) / float(right)
    else:
        sar = video.get("sample_aspect_ratio", "1:1")
        sar_left, sar_right = (float(part) for part in sar.split(":")) if ":" in sar else (1.0, 1.0)
        ratio = int(video["width"]) * sar_left / (int(video["height"]) * sar_right)
    audio_duration = float(audio.get("duration", data["format"].get("duration")))
    duration = float(video.get("duration", data["format"].get("duration")))
    frame_h = round(VIDEO_W / ratio)
    if frame_h % 2:
        frame_h += 1
    return {
        "video": video,
        "audio": audio,
        "duration": min(duration, audio_duration),
        "original_display_aspect_ratio": ratio,
        "animation_width": VIDEO_W,
        "animation_height": frame_h,
    }


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    is_cjk = any("\u4e00" <= char <= "\u9fff" for char in text)
    # Keep closing punctuation with the preceding character when wrapping Chinese.
    tokens = re.findall(r".[，。！？；：、）】》”’]*", text) if is_cjk else text.split()
    lines: list[str] = []
    current = ""
    for token in tokens:
        candidate = current + token if is_cjk or not current else current + " " + token
        if current and draw.textlength(candidate, font=font) > max_width:
            lines.append(current)
            current = token
        else:
            current = candidate
    if current:
        lines.append(current)
    if len(lines) > 2:
        raise SystemExit(f"Caption exceeds the fixed two-line layout: {text}")
    return lines


def draw_centered(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, font: ImageFont.FreeTypeFont, fill: str) -> None:
    draw.text(xy, text, font=font, fill=fill, anchor="mm")


def create_base(path: Path, grade: str, unit: str, title: str, lesson: str, en_fonts: dict[str, list[str]], zh_fonts: list[str]) -> None:
    regular = font_from(en_fonts["regular"], 30)
    unit_font = font_from(en_fonts["bold"], 48)
    title_font = font_from(en_fonts["bold"], 66)
    lesson_font = font_from(zh_fonts if any('\u4e00' <= char <= '\u9fff' for char in lesson) else en_fonts["bold"], 28)
    zh_title_font = font_from(zh_fonts, 30)
    img = Image.new("RGB", CANVAS, "#FFFFFF")
    d = ImageDraw.Draw(img)
    draw_centered(d, (540, 112), grade, zh_title_font, "#66758A")
    draw_centered(d, (540, 202), unit, unit_font, "#35506B")
    draw_centered(d, (540, 292), title, title_font, "#172B43")
    pill_width = int(d.textlength(lesson, font=lesson_font)) + 56
    pill = (540 - pill_width // 2, 356, 540 + pill_width // 2, 408)
    d.rounded_rectangle(pill, radius=26, fill="#EAF2FB")
    draw_centered(d, (540, 382), lesson, lesson_font, "#315D85")
    d.rounded_rectangle((24, 497, 1056, 1073), radius=8, outline="#DDE5ED", width=2)
    d.rounded_rectangle(CARD, radius=28, fill="#FFFFFF", outline="#DDE5ED", width=2)
    img.save(path)


def create_caption(path: Path, english: str, chinese: str, en_fonts: dict[str, list[str]], zh_fonts: list[str], version: int) -> None:
    img = Image.new("RGBA", CANVAS, (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if version == 1:
        en_label_size, en_size, zh_label_size, zh_size = 21, 35, 21, 38
    else:
        en_label_size, en_size, zh_label_size, zh_size = 25, 52, 25, 54
    en_label = font_from(en_fonts["bold"], en_label_size)
    en_font = font_from(en_fonts["bold"], en_size)
    zh_label = font_from(zh_fonts, zh_label_size)
    zh_font = font_from(zh_fonts, zh_size)
    max_width = 850
    en_lines = wrap_text(d, english, en_font, max_width)
    zh_lines = wrap_text(d, chinese, zh_font, max_width)
    if version == 1:
        en_label_y, en_text_y, en_line_height = 1294, 1330, 43
        divider_y, zh_label_y, zh_text_y, zh_line_height = 1445, 1470, 1508, 47
    else:
        en_label_y, en_text_y, en_line_height = 1274, 1314, 62
        divider_y = max(1400, en_text_y + len(en_lines) * en_line_height + 14)
        zh_label_y, zh_text_y, zh_line_height = divider_y + 25, divider_y + 64, 64
    d.text((104, en_label_y), "ENGLISH", font=en_label, fill="#6C87A1")
    for index, line in enumerate(en_lines):
        d.text((104, en_text_y + index * en_line_height), line, font=en_font, fill="#183B5B")
    d.line((104, divider_y, 976, divider_y), fill="#E7EDF3", width=2)
    d.text((104, zh_label_y), "中文", font=zh_label, fill="#748092")
    for index, line in enumerate(zh_lines):
        d.text((104, zh_text_y + index * zh_line_height), line, font=zh_font, fill="#2D3748")
    img.save(path)


def tighten_pauses(source: Path, output: Path, cues: list[dict[str, object]], duration: float, ffmpeg: str) -> list[dict[str, float]]:
    """Shorten long quiet pauses; use one edit map for audio, video and subtitles."""
    detected = subprocess.run([
        ffmpeg, '-hide_banner', '-i', str(source), '-af', 'silencedetect=n=-38dB:d=0.35',
        '-vn', '-f', 'null', '-',
    ], check=True, capture_output=True, text=True)
    cuts = []
    silence_start = None
    for kind, value in re.findall(r'silence_(start|end):\s*([0-9.]+)', detected.stderr):
        if kind == 'start':
            silence_start = float(value)
        elif silence_start is not None:
            # Preserve 120 ms at either side; round inward to whole frames.
            start = (int((silence_start + 0.12) * FPS) + 1) / FPS
            end = int((min(float(value), duration) - 0.12) * FPS) / FPS
            if end - start >= 2 / FPS:
                cuts.append({'start': start, 'end': end})
            silence_start = None
    kept, cursor = [], 0.0
    for cut in cuts:
        kept.append((cursor, cut['start']))
        cursor = cut['end']
    kept.append((cursor, duration))
    parts = []
    for index, (start, end) in enumerate(kept):
        parts += [f'[0:v]trim=start={start:.9f}:end={end:.9f},setpts=PTS-STARTPTS[v{index}]',
                  f'[0:a]atrim=start={start:.9f}:end={end:.9f},asetpts=PTS-STARTPTS[a{index}]']
    inputs = ''.join(f'[v{i}][a{i}]' for i in range(len(kept)))
    parts.append(f'{inputs}concat=n={len(kept)}:v=1:a=1[v][a]')
    subprocess.run([
        ffmpeg, '-v', 'error', '-n', '-i', str(source), '-filter_complex', ';'.join(parts),
        '-map', '[v]', '-map', '[a]', '-r', str(FPS), '-c:v', 'libx264', '-preset', 'fast',
        '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'pcm_s16le', str(output),
    ], check=True)
    for cue in cues:
        for boundary in ('start', 'end'):
            time = float(cue[boundary])
            cue[boundary] = time - sum(max(0.0, min(time, cut['end']) - cut['start']) for cut in cuts)
    return cuts


def write_srt(path: Path, cues: list[dict[str, object]]) -> None:
    def stamp(seconds: object) -> str:
        millis = round(float(seconds) * 1000)
        hours, millis = divmod(millis, 3600000)
        minutes, millis = divmod(millis, 60000)
        seconds, millis = divmod(millis, 1000)
        return f'{hours:02d}:{minutes:02d}:{seconds:02d},{millis:03d}'
    path.write_text('\n\n'.join(
        f"{i}\n{stamp(c['start'])} --> {stamp(c['end'])}\n{c['english']}\n{c['chinese']}"
        for i, c in enumerate(cues, 1)) + '\n', encoding='utf-8')


def create_opening(path: Path, text: str, zh_fonts: list[str]) -> None:
    """Brief title over the first shot, without adding a waiting screen."""
    img = Image.new('RGBA', CANVAS, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 1080, 460), fill='#FFFFFF')
    draw.rounded_rectangle((54, 130, 1026, 352), radius=44, fill='#EAF2FB')
    font = font_from(zh_fonts, 108)
    if draw.textlength(text, font=font) > 900:
        raise SystemExit('Opening title is too long for the fixed layout')
    draw_centered(draw, (540, 241), text, font, '#183B5B')
    img.save(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="Landscape video with approved audio")
    parser.add_argument("--srt", required=True, type=Path, help="Two-line bilingual SRT: English then Chinese")
    parser.add_argument("--grade", required=True, help="Top label, e.g. 小学英语 · 四年级上册")
    parser.add_argument("--unit", required=True, help="Unit label, e.g. Unit 2")
    parser.add_argument("--title", required=True, help="Unit title, e.g. My friends")
    parser.add_argument("--lesson", required=True, help="Activity label, e.g. A. Let's talk")
    parser.add_argument("--preset-version", type=int, choices=(1, 2), default=2, help="Layout version; defaults to the current larger-caption preset")
    parser.add_argument('--tighten-pauses', action='store_true', help='Shorten long quiet pauses without speeding up speech')
    parser.add_argument('--opening-text', help='Brief title overlay on the first shot')
    parser.add_argument('--opening-seconds', type=float, default=1.25)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    sidecar = args.output.with_suffix('.json')
    retimed_srt = args.output.with_suffix('.srt')
    for destination in (args.output, sidecar, retimed_srt):
        if destination.exists():
            raise SystemExit(f"Refusing to overwrite existing output: {destination}")
    if not 0.25 <= args.opening_seconds <= 2:
        parser.error('--opening-seconds must be between 0.25 and 2')
    for source in (args.input, args.srt):
        if not source.is_file():
            raise SystemExit(f"Input not found: {source}")

    ffmpeg, ffprobe = require_bin("ffmpeg"), require_bin("ffprobe")
    en_fonts = {
        "regular": ["/System/Library/Fonts/Supplemental/Arial.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"],
        "bold": ["/System/Library/Fonts/Supplemental/Arial Bold.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"],
    }
    zh_fonts = ["/System/Library/Fonts/PingFang.ttc", "/System/Library/Fonts/STHeiti Medium.ttc", "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"]
    cues = read_srt(args.srt)
    media = probe(args.input, ffprobe)
    if cues[-1]["end"] > media["duration"]:
        raise SystemExit(f"Last subtitle ends after output duration ({cues[-1]['end']} > {media['duration']})")
    if any(right['start'] < left['end'] for left, right in zip(cues, cues[1:])):
        raise SystemExit('Bilingual subtitle cues must be ordered and non-overlapping')

    with tempfile.TemporaryDirectory(prefix="vertical-lesson-") as temporary:
        temp = Path(temporary)
        source_duration = float(media['duration'])
        source = args.input
        cuts = []
        if args.tighten_pauses:
            source = temp / 'tightened.mkv'
            cuts = tighten_pauses(args.input, source, cues, source_duration, ffmpeg)
            media = probe(source, ffprobe)
        if float(cues[-1]['end']) > float(media['duration']) + 1 / FPS:
            raise SystemExit('Retimed subtitles exceed the tightened video')
        base = temp / "base.png"
        create_base(base, args.grade, args.unit, args.title, args.lesson, en_fonts, zh_fonts)
        cards = []
        for index, cue in enumerate(cues):
            card = temp / f"caption-{index:03d}.png"
            create_caption(card, str(cue["english"]), str(cue["chinese"]), en_fonts, zh_fonts, args.preset_version)
            cards.append(card)
        # One timed background stream avoids a full-canvas overlay per cue.
        # Quantize every boundary independently so rounding does not accumulate.
        total_frames = round(float(media['duration']) * FPS)
        frame_cursor = 0
        entries = []
        def add_frame(path: Path, frames: int) -> None:
            if frames > 0:
                entries.extend([f"file '{path.as_posix()}'", f'option framerate {FPS}', f'duration {frames / FPS:.9f}'])
        for index, cue in enumerate(cues):
            start = round(float(cue['start']) * FPS)
            end = round(float(cue['end']) * FPS)
            add_frame(base, start - frame_cursor)
            with Image.open(base) as background, Image.open(cards[index]) as caption:
                frame = Image.alpha_composite(background.convert('RGBA'), caption.convert('RGBA')).convert('RGB')
                composed = temp / f'layout-{index:03d}.png'
                frame.save(composed)
            add_frame(composed, end - start)
            frame_cursor = end
        add_frame(base, total_frames - frame_cursor)
        entries.extend([f"file '{base.as_posix()}'", f'option framerate {FPS}'])
        backgrounds = temp / 'layout.ffconcat'
        backgrounds.write_text('ffconcat version 1.0\n' + '\n'.join(entries) + '\n')
        video_h = int(media["animation_height"])
        video_y = VIDEO_Y
        filter_parts = [
            f'[0:v]fps={FPS},setsar=1[background]',
            f"[1:v]scale={VIDEO_W}:{video_h}:flags=lanczos,setsar=1[clip]",
            f"[background][clip]overlay={VIDEO_X}:{video_y}:eof_action=repeat[stage0]",
        ]
        command = [ffmpeg, '-n', '-f', 'concat', '-safe', '0', '-i', str(backgrounds), '-i', str(source)]
        video_output = '[stage0]'
        if args.opening_text:
            opening = temp / 'opening.png'
            create_opening(opening, args.opening_text, zh_fonts)
            opening_seconds = min(args.opening_seconds, float(media['duration']))
            command += ['-loop', '1', '-framerate', str(FPS), '-i', str(opening)]
            filter_parts += [
                f'[2:v]format=rgba,fade=t=out:st={max(0, opening_seconds - 0.15):.3f}:d=0.15:alpha=1[opening]',
                f'[stage0][opening]overlay=0:0:enable=\'lt(t,{opening_seconds:.3f})\'[branded]',
            ]
            video_output = '[branded]'
        command += [
            "-filter_complex", ";".join(filter_parts), "-map", video_output, "-map", "1:a:0",
            "-t", f"{media['duration']:.3f}", "-r", str(FPS), "-c:v", "libx264", "-preset", "medium",
            "-crf", "19", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "96k", "-movflags", "+faststart",
            str(args.output),
        ]
        args.output.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(command, check=True)

    result = probe(args.output, ffprobe)
    if args.tighten_pauses:
        write_srt(retimed_srt, cues)
    metadata = {
        "preset": f"vertical-bilingual-white-v{args.preset_version}",
        "caption_style": {"english_px": 35 if args.preset_version == 1 else 52, "chinese_px": 38 if args.preset_version == 1 else 54},
        "input": str(args.input),
        "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
        "subtitle_source": str(args.srt),
        "subtitle_sha256": hashlib.sha256(args.srt.read_bytes()).hexdigest(),
        "pacing": {
            "tighten_pauses": args.tighten_pauses,
            "speech_speed": 1.0,
            "silence_detection": {"threshold_db": -38, "minimum_seconds": 0.35, "padding_each_side_seconds": 0.12},
            "source_duration_seconds": source_duration,
            "removed_silence_seconds": sum(c['end'] - c['start'] for c in cuts),
            "cuts_in_source_seconds": cuts,
            "retimed_subtitles": str(retimed_srt) if args.tighten_pauses else None,
            "retimed_subtitle_sha256": hashlib.sha256(retimed_srt.read_bytes()).hexdigest() if args.tighten_pauses else None,
        },
        "opening": {"text": args.opening_text, "seconds": min(args.opening_seconds, float(media['duration'])) if args.opening_text else 0, "mode": "first-shot-overlay", "audio": "original-dialogue"},
        "headers": {"grade": args.grade, "unit": args.unit, "title": args.title, "lesson": args.lesson},
        "canvas": {"width": CANVAS[0], "height": CANVAS[1], "background": "white"},
        "animation": {
            "placement": {"x": VIDEO_X, "y": VIDEO_Y, "width": VIDEO_W, "height": media["animation_height"]},
            "original_display_aspect_ratio": media["original_display_aspect_ratio"],
            "preserve_aspect_ratio": True,
            "crop": False,
        },
        "subtitle_layout": {"region": list(CARD), "language_order": ["English", "Chinese"], "cue_count": len(cues)},
        "output": str(args.output),
        "output_sha256": hashlib.sha256(args.output.read_bytes()).hexdigest(),
        "duration_seconds": result["duration"],
        "video": {"codec": "h264", "width": CANVAS[0], "height": CANVAS[1], "fps": FPS},
        "audio": {
            "codec": result["audio"].get("codec_name"),
            "sample_rate": result["audio"].get("sample_rate"),
            "channels": result["audio"].get("channels"),
        },
    }
    sidecar.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(metadata, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
