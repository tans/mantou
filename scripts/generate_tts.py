#!/usr/bin/env python3
"""Synthesize a WAV narration track with Xiaomi MiMo TTS."""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BASE_URL = "https://api.xiaomimimo.com/v1"


class TTSError(Exception):
    pass


def load_env_file() -> None:
    env_path = ROOT / ".env"
    if not env_path.exists():
        return
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        key, separator, value = line.partition("=")
        if not separator:
            continue
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        if key.strip() and key.strip() not in os.environ:
            os.environ[key.strip()] = value


def parse_args() -> argparse.Namespace:
    load_env_file()
    parser = argparse.ArgumentParser(description="Generate a WAV narration track with Xiaomi MiMo TTS.")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--text", help="Text to synthesize")
    source.add_argument("--text-file", type=Path, help="UTF-8 text file to synthesize")
    parser.add_argument("--voice", default="Mia", help="Built-in voice ID (default: Mia; English voices: Mia, Chloe, Milo, Dean)")
    parser.add_argument("--style", help="Natural-language instructions for delivery style")
    parser.add_argument("--model", default="mimo-v2.5-tts")
    parser.add_argument("--base-url", default=os.getenv("MIMO_BASE_URL", DEFAULT_BASE_URL))
    parser.add_argument("--output", type=Path, required=True, help="Destination .wav path")
    parser.add_argument("--dry-run", action="store_true", help="Show effective options without contacting Xiaomi")
    args = parser.parse_args()
    if args.text_file:
        try:
            args.text = args.text_file.expanduser().read_text(encoding="utf-8").strip()
        except (OSError, UnicodeError) as exc:
            parser.error(f"cannot read --text-file ({type(exc).__name__})")
    if not args.text:
        parser.error("text is empty")
    if not args.output.suffix.lower() == ".wav":
        parser.error("--output must use the .wav extension")
    return args


def synthesize(args: argparse.Namespace) -> bytes:
    api_key = os.environ.get("MIMO_API_KEY", "").strip()
    if not api_key:
        raise TTSError("Set MIMO_API_KEY in .env or the environment")
    messages: list[dict[str, str]] = []
    if args.style:
        messages.append({"role": "user", "content": args.style})
    messages.append({"role": "assistant", "content": args.text})
    payload = json.dumps({
        "model": args.model,
        "messages": messages,
        "audio": {"format": "wav", "voice": args.voice},
    }, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        f"{args.base_url.rstrip('/')}/chat/completions",
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            result: Any = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        raise TTSError(f"Xiaomi TTS request failed (HTTP {exc.code})") from None
    except (urllib.error.URLError, TimeoutError) as exc:
        reason = getattr(exc, "reason", None)
        raise TTSError(f"Xiaomi TTS request failed ({type(reason or exc).__name__})") from None
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise TTSError("Xiaomi TTS returned invalid JSON") from None
    try:
        encoded_audio = result["choices"][0]["message"]["audio"]["data"]
        audio = base64.b64decode(encoded_audio, validate=True)
    except (KeyError, IndexError, TypeError, ValueError):
        raise TTSError("Xiaomi TTS response did not contain valid audio data") from None
    if not audio.startswith(b"RIFF") or audio[8:12] != b"WAVE":
        raise TTSError("Xiaomi TTS response is not a WAV file")
    return audio


def main() -> int:
    args = parse_args()
    if args.dry_run:
        print(json.dumps({
            "provider": "xiaomi-mimo",
            "base_url": args.base_url,
            "model": args.model,
            "voice": args.voice,
            "style": args.style,
            "text_sha256": hashlib.sha256(args.text.encode("utf-8")).hexdigest(),
            "output": str(args.output),
        }, ensure_ascii=False, indent=2))
        return 0
    try:
        audio = synthesize(args)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(audio)
        print(f"Saved narration WAV: {args.output}")
        print(f"Audio size: {len(audio)} bytes")
        return 0
    except (TTSError, OSError) as exc:
        print(f"TTS generation failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
