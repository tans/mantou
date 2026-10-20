#!/usr/bin/env python3
"""Submit, wait for, and download videos from configured project providers."""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import mimetypes
import math
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MINIXM_BASE_URL = "http://minixm.minapp.xin:8443"
DEFAULT_XIAOGUAI_BASE_URL = "https://xiaoguai123.xyz"


class VideoError(Exception):
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
        key = key.strip()
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        if key and key not in os.environ:
            os.environ[key] = value


def json_request(url: str, *, method: str = "GET", payload: dict[str, Any] | None = None,
                 headers: dict[str, str] | None = None, timeout: int = 60) -> Any:
    request_headers = {"Accept": "application/json", **(headers or {})}
    body = None
    if payload is not None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        request_headers.setdefault("Content-Type", "application/json")
    request = urllib.request.Request(url, data=body, headers=request_headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            content = response.read()
    except urllib.error.HTTPError as exc:
        # Do not print response bodies: providers may echo request data.
        raise VideoError(f"HTTP {exc.code} from provider") from None
    except (urllib.error.URLError, TimeoutError) as exc:
        reason = getattr(exc, "reason", None)
        raise VideoError(f"Provider request failed ({type(reason or exc).__name__})") from None
    try:
        return json.loads(content.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise VideoError("Provider returned an invalid JSON response") from None


def download(url: str, output: Path, *, headers: dict[str, str] | None = None) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    partial = output.with_suffix(output.suffix + ".part")
    request = urllib.request.Request(url, headers=headers or {})
    try:
        with urllib.request.urlopen(request, timeout=120) as response, partial.open("wb") as stream:
            while chunk := response.read(1024 * 1024):
                stream.write(chunk)
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as exc:
        partial.unlink(missing_ok=True)
        if isinstance(exc, urllib.error.HTTPError):
            raise VideoError(f"Video download failed (HTTP {exc.code})") from None
        raise VideoError("Video download failed") from None
    partial.replace(output)


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def image_value(value: str) -> str:
    if value.startswith(("https://", "http://", "data:")):
        return value
    path = Path(value).expanduser().resolve()
    if not path.is_file():
        raise VideoError(f"Reference image not found: {path}")
    content_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{content_type};base64,{encoded}"


def multipart_file(path: Path, boundary: str) -> bytes:
    content_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    safe_name = path.name.replace('"', "")
    return (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{safe_name}"\r\n'
        f"Content-Type: {content_type}\r\n\r\n"
    ).encode() + path.read_bytes() + f"\r\n--{boundary}--\r\n".encode()


def unwrap_xiaoguai(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise VideoError("Unexpected xiaoguai response")
    data = value.get("data", value)
    if isinstance(data, list):
        data = data[0] if data else {}
    if not isinstance(data, dict):
        raise VideoError("Unexpected xiaoguai task response")
    return data


def provider_xiaoguai(args: argparse.Namespace) -> tuple[str, str, dict[str, Any]]:
    api_key = os.environ.get("XIAOGUAI_API_KEY", "").strip()
    if not api_key:
        raise VideoError("Set XIAOGUAI_API_KEY in .env or the environment")
    base = (args.base_url or os.environ.get("XIAOGUAI_BASE_URL", DEFAULT_XIAOGUAI_BASE_URL)).rstrip("/")
    headers = {"Authorization": f"Bearer {api_key}"}
    task_id = args.task_id
    if not task_id:
        payload: dict[str, Any] = {
            "model": args.model or "minimax-h3",
            "prompt": args.prompt,
            "duration": args.duration if args.duration is not None else 5,
            "resolution": args.resolution or "480p",
            "aspect_ratio": args.aspect_ratio or "16:9",
            "generate_audio": args.with_video_audio,
            "watermark": args.watermark,
        }
        if args.seed is not None:
            payload["seed"] = args.seed
        if args.first_frame:
            payload["image"] = image_value(args.first_frame)
        if args.last_frame:
            payload["last_frame"] = image_value(args.last_frame)
        if args.reference_image:
            payload["image_urls"] = [image_value(item) for item in args.reference_image]
        response = json_request(f"{base}/v1/videos", method="POST", payload=payload, headers=headers)
        task = unwrap_xiaoguai(response)
        task_id = str(task.get("id") or task.get("task_id") or "")
        if not task_id:
            raise VideoError("Provider accepted no task ID")
        print(f"Submitted xiaoguai task {task_id}", flush=True)
    else:
        payload = {}
    status_url = f"{base}/v1/videos/{urllib.parse.quote(task_id, safe='')}"
    end = time.monotonic() + args.timeout
    while True:
        task = unwrap_xiaoguai(json_request(status_url, headers=headers))
        status = str(task.get("status", "")).lower()
        if status == "completed":
            outputs = task.get("outputs") or []
            result = task.get("result") or {}
            if isinstance(outputs, dict):
                outputs = [outputs]
            urls = [item.get("url") for item in outputs if isinstance(item, dict) and item.get("url")]
            videos = result.get("videos", []) if isinstance(result, dict) else []
            if isinstance(videos, str):
                videos = [videos]
            urls.extend(videos if isinstance(videos, list) else [])
            if not urls or not isinstance(urls[0], str):
                raise VideoError("Task completed without a video URL")
            return task_id, str(urls[0]), {
                "provider": "xiaoguai",
                "base_url": base,
                "status": status,
                "model": task.get("model"),
                "progress": task.get("progress"),
            }
        if status == "failed":
            error = task.get("error")
            code = error.get("code") if isinstance(error, dict) else None
            raise VideoError(f"Task {task_id} failed: {code or 'provider error'}")
        if time.monotonic() >= end:
            raise VideoError(f"Task still running; resume with --provider xiaoguai --task-id {task_id}")
        print(f"Task {task_id}: {status or 'pending'}", flush=True)
        time.sleep(args.poll_interval)


def minixm_dimensions(resolution: str, aspect_ratio: str,
                      width: int | None = None, height: int | None = None) -> tuple[int, int]:
    if (width is None) != (height is None):
        raise VideoError("set both --width and --height for minixm")
    if width is not None and height is not None:
        if width <= 0 or height <= 0 or width % 32 or height % 32 or width * height > 983_040:
            raise VideoError("minixm width/height must be positive multiples of 32 with area at most 983040")
        return width, height
    landscape = {"480p": (864, 480), "720p": (1024, 576), "768p": (1280, 768)}
    if resolution not in landscape:
        raise VideoError("minixm resolution must be 480p, 720p, or 768p")
    width, height = landscape[resolution]
    if aspect_ratio == "9:16":
        return height, width
    if aspect_ratio != "16:9":
        raise VideoError("minixm aspect ratio must be 16:9 or 9:16")
    return width, height


def provider_minixm(args: argparse.Namespace) -> tuple[str, str, dict[str, Any]]:
    base = (args.base_url or os.environ.get("MINIXM_BASE_URL", DEFAULT_MINIXM_BASE_URL)).rstrip("/")
    task_id = args.task_id
    headers = {"Accept": "application/json"}
    if not task_id:
        if not args.prompt:
            raise VideoError("--prompt is required when submitting a new task")
        refs = []
        for source in args.reference_image or []:
            if source.startswith(("https://", "http://", "data:")):
                raise VideoError("minixm reference images must be local files")
            path = Path(source).expanduser().resolve()
            if not path.is_file():
                raise VideoError(f"Reference image not found: {path}")
            boundary = f"mantou-{os.urandom(16).hex()}"
            request = urllib.request.Request(
                f"{base}/v1/files",
                data=multipart_file(path, boundary),
                headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
                method="POST",
            )
            try:
                with urllib.request.urlopen(request, timeout=120) as response:
                    uploaded = json.loads(response.read().decode("utf-8"))
            except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError, json.JSONDecodeError):
                raise VideoError("minixm reference upload failed") from None
            refs.append(uploaded["file_id"])
        duration = args.duration if args.duration is not None else 5.17
        if abs((duration * 24 - 5) / 17 - round((duration * 24 - 5) / 17)) > 0.01:
            raise VideoError("minixm H3 duration must map to a valid 24 fps frame slot (for example 5.17 seconds)")
        width, height = minixm_dimensions(
            args.resolution or "768p", args.aspect_ratio or "16:9", args.width, args.height,
        )
        task = "ref2av" if refs else "text_to_video"
        payload = {
            "model": args.model or "minimax-h3",
            "task": task,
            "input": {"prompt": args.prompt},
            "parameters": {"duration_seconds": duration, "width": width, "height": height},
        }
        if args.steps is not None:
            payload["parameters"]["steps"] = args.steps
        if args.seed is not None:
            payload["parameters"]["seed"] = args.seed
        if refs:
            payload["input"]["references"] = {"images": refs, "videos": [], "audios": []}
        submitted = json_request(f"{base}/v1/jobs", method="POST", payload=payload)
        task_id = str(submitted.get("job_id") or "")
        if not task_id:
            raise VideoError("minixm accepted no job ID")
        print(f"Submitted minixm task {task_id}", flush=True)
    end = time.monotonic() + args.timeout
    while True:
        task = json_request(f"{base}/v1/jobs/{urllib.parse.quote(task_id, safe='')}")
        status = str(task.get("status", "")).lower()
        if status == "succeeded":
            result = task.get("result") or {}
            result_path = result.get("download_url") or f"/v1/jobs/{urllib.parse.quote(task_id, safe='')}/result"
            result_url = urllib.parse.urljoin(f"{base}/", str(result_path))
            return task_id, result_url, {
                "provider": "minixm",
                "base_url": base,
                "status": status,
                "model": task.get("model"),
            }
        if status in ("failed", "cancelled"):
            raise VideoError(f"Task {task_id} {status}: {task.get('error_code', 'unknown error')}")
        if time.monotonic() >= end:
            raise VideoError(f"Task still running; resume with --provider minixm --task-id {task_id}")
        print(f"Task {task_id}: {status or 'pending'}", flush=True)
        time.sleep(args.poll_interval)


def parse_args() -> argparse.Namespace:
    load_env_file()
    parser = argparse.ArgumentParser(description="Generate and download a video from a configured provider.")
    parser.add_argument("--provider", choices=("xiaoguai", "minixm"), default=os.getenv("VIDEO_PROVIDER", "xiaoguai"))
    parser.add_argument("--base-url", help="Override this provider's API base URL")
    parser.add_argument("--model", help="Provider model ID (defaults to minimax-h3)")
    parser.add_argument("--prompt", help="Video prompt; required for a new task")
    parser.add_argument("--prompt-file", type=Path, help="UTF-8 text file containing the prompt")
    parser.add_argument("--duration", type=float, help="Seconds; defaults to 5 for xiaoguai, 5.17 for minixm")
    parser.add_argument("--resolution", choices=("480p", "720p", "768p"))
    parser.add_argument("--width", type=int, help="Exact minixm output width")
    parser.add_argument("--height", type=int, help="Exact minixm output height")
    parser.add_argument("--steps", type=int, help="minixm H3 inference steps (8–64)")
    parser.add_argument("--aspect-ratio", default="16:9")
    parser.add_argument("--reference-image", action="append", help="Local path or URL; repeat for multiple references")
    parser.add_argument("--first-frame", help="xiaoguai first-frame image path or URL")
    parser.add_argument("--last-frame", help="xiaoguai last-frame image path or URL")
    parser.add_argument("--with-video-audio", action="store_true", help="Keep audio generated by the video model (often unsuitable for narration)")
    parser.add_argument("--watermark", action="store_true", help="Request provider watermark")
    parser.add_argument("--seed", type=int)
    parser.add_argument("--output", type=Path, required=True, help="Destination .mp4 path")
    parser.add_argument("--task-id", help="Resume polling/downloading an existing task")
    parser.add_argument("--poll-interval", type=float, default=5)
    parser.add_argument("--timeout", type=int, default=1800, help="Maximum polling time in seconds")
    parser.add_argument("--dry-run", action="store_true", help="Show effective options without contacting a provider")
    args = parser.parse_args()
    if args.prompt and args.prompt_file:
        parser.error("use either --prompt or --prompt-file, not both")
    if not args.task_id and not (args.prompt or args.prompt_file):
        parser.error("--prompt or --prompt-file is required unless --task-id is supplied")
    if args.prompt_file:
        try:
            args.prompt = args.prompt_file.expanduser().read_text(encoding="utf-8").strip()
        except (OSError, UnicodeError) as exc:
            parser.error(f"cannot read --prompt-file ({type(exc).__name__})")
        if not args.prompt:
            parser.error("--prompt-file is empty")
    if args.duration is not None and not 5 <= args.duration <= 15:
        parser.error("--duration must be between 5 and 15 seconds")
    if args.poll_interval <= 0 or args.timeout <= 0:
        parser.error("--poll-interval and --timeout must be positive")
    if args.provider == "xiaoguai" and args.duration is not None and not args.duration.is_integer():
        parser.error("xiaoguai MiniMax H3 duration must be an integer from 5 to 15")
    if args.provider == "minixm" and (args.first_frame or args.last_frame or args.with_video_audio or args.watermark):
        parser.error("--first-frame, --last-frame, --with-video-audio, and --watermark are xiaoguai-only options")
    if args.provider == "xiaoguai" and (args.width is not None or args.height is not None or args.steps is not None):
        parser.error("--width, --height, and --steps are minixm-only options")
    if args.steps is not None and not 8 <= args.steps <= 64:
        parser.error("--steps must be between 8 and 64")
    if (args.width is None) != (args.height is None):
        parser.error("--width and --height must be supplied together")
    if args.provider == "minixm":
        try:
            minixm_dimensions(args.resolution or "768p", args.aspect_ratio, args.width, args.height)
        except VideoError as exc:
            parser.error(str(exc))
        duration = args.duration if args.duration is not None else 5.17
        if abs((duration * 24 - 5) / 17 - round((duration * 24 - 5) / 17)) > 0.01:
            parser.error("minixm H3 duration must map to a valid 24 fps frame slot (for example 5.17 seconds)")
    return args


def main() -> int:
    args = parse_args()
    if args.dry_run:
        base_url = args.base_url or (
            os.getenv("XIAOGUAI_BASE_URL", DEFAULT_XIAOGUAI_BASE_URL)
            if args.provider == "xiaoguai"
            else os.getenv("MINIXM_BASE_URL", DEFAULT_MINIXM_BASE_URL)
        )
        width = height = None
        aspect_ratio = args.aspect_ratio
        if args.provider == "minixm":
            width, height = minixm_dimensions(args.resolution or "768p", args.aspect_ratio, args.width, args.height)
            divisor = math.gcd(width, height)
            aspect_ratio = f"{width // divisor}:{height // divisor}"
        print(json.dumps({
            "provider": args.provider,
            "base_url": base_url,
            "model": args.model or "minimax-h3",
            "duration": args.duration if args.duration is not None else (5 if args.provider == "xiaoguai" else 5.17),
            "resolution": args.resolution or ("480p" if args.provider == "xiaoguai" else "768p"),
            "width": width,
            "height": height,
            "steps": args.steps,
            "seed": args.seed,
            "aspect_ratio": aspect_ratio,
            "reference_images": args.reference_image or [],
            "output": str(args.output),
            "task_id": args.task_id,
        }, ensure_ascii=False, indent=2))
        return 0
    try:
        if args.provider == "xiaoguai":
            task_id, video_url, metadata = provider_xiaoguai(args)
        else:
            task_id, video_url, metadata = provider_minixm(args)
        headers = {}
        if args.provider == "xiaoguai" and urllib.parse.urlparse(video_url).hostname == "xiaoguai123.xyz":
            headers["Authorization"] = f"Bearer {os.environ['XIAOGUAI_API_KEY']}"
        download(video_url, args.output, headers=headers)
        sidecar = args.output.with_suffix(".json")
        actual_width = actual_height = None
        actual_aspect_ratio = args.aspect_ratio
        if args.provider == "minixm":
            actual_width, actual_height = minixm_dimensions(args.resolution or "768p", args.aspect_ratio, args.width, args.height)
            divisor = math.gcd(actual_width, actual_height)
            actual_aspect_ratio = f"{actual_width // divisor}:{actual_height // divisor}"
        metadata.update({
            "task_id": task_id,
            "output": str(args.output.resolve()),
            "output_sha256": file_sha256(args.output),
            "downloaded_at": datetime.now(timezone.utc).isoformat(),
            "prompt_file": str(args.prompt_file.expanduser().resolve()) if args.prompt_file else None,
            "prompt_sha256": hashlib.sha256(args.prompt.encode("utf-8")).hexdigest() if args.prompt else None,
            "duration_seconds": args.duration if args.duration is not None else (5 if args.provider == "xiaoguai" else 5.17),
            "resolution": args.resolution or ("480p" if args.provider == "xiaoguai" else "768p"),
            "width": actual_width,
            "height": actual_height,
            "steps": args.steps,
            "aspect_ratio": actual_aspect_ratio,
            "reference_images": args.reference_image or [],
            "seed": args.seed,
            "generate_audio_requested": args.with_video_audio,
            "watermark_requested": args.watermark,
        })
        sidecar.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Saved video: {args.output}")
        print(f"Task ID: {task_id}")
        print(f"Metadata: {sidecar}")
        return 0
    except VideoError as exc:
        print(f"video generation failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
