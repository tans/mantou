---
name: tts-generation
description: Generate textbook dialogue, narration, or character voice audio with Xiaomi MiMo TTS in this project. Use when creating, revising, checking, or saving TTS audio for a lesson.
---

# TTS generation

Use `scripts/generate_tts.py` for Xiaomi MiMo speech synthesis. Keep each run grounded in dialogue that has already been confirmed for the lesson.

## Generate audio

1. Read the lesson's dialogue and narration confirmation table. Require every spoken line to have exact text, a speaker, a textbook page/location or an explicit adaptation/narration basis, and user confirmation. If any line or source is unresolved, stop synthesis and help resolve the script first. Never use a sample prompt, storyboard text, model output, or memory as a substitute for a confirmed script.
2. Choose a MiMo voice that fits the confirmed speaker and language. The built-in English voices are `Mia`, `Chloe`, `Milo`, and `Dean`; pass `--style` for delivery direction. The current script uses one voice per request. Generate different speakers as separate files when their voices need to differ.
3. Read `MIMO_API_KEY` from `.env` or the process environment. Keep the credential private; never print it, put it in a command-line argument, store it in audio metadata, or commit it. The default endpoint is `https://api.xiaomimimo.com/v1` and can be overridden by `MIMO_BASE_URL`.
4. Run `--dry-run` first to confirm model, voice, output path, and text hash. Then generate the WAV:

   ```bash
   python3 scripts/generate_tts.py \
     --text-file projects/grade-4-english-term-1/unit-1-helping-at-home/dialogue.txt \
     --voice Mia \
     --style "Clear, warm English for a primary school textbook dialogue, at a natural pace." \
     --output projects/grade-4-english-term-1/unit-1-helping-at-home/renders/unit-1-speaker-v1.wav
   ```

5. Verify the output is a readable WAV with `file` or `ffprobe`, then listen to the full clip. Check wording, pronunciation, pauses, speed, clipping, and whether the voice fits the character. A successful API response alone does not mean the audio is approved.
6. Save lesson audio under its lesson directory with a stable, versioned filename. Record the source text, model, voice, style, file path, technical audio properties, and SHA-256 in the lesson README. Keep dialogue text and audio together; keep API credentials out of both.
7. When the audio is approved for a video, continue with the `video-generation` skill to generate silent shots and merge them in storyboard order with the TTS track.

## Request and output details

- The default model is `mimo-v2.5-tts`; the script requests WAV and validates that the response contains RIFF/WAVE audio.
- `--text` and `--text-file` are mutually exclusive. Prefer a versioned lesson text file for reusable dialogue.
- Use `--dry-run` to inspect parameters without contacting Xiaomi. A regular invocation makes a live API request.
- If macOS Python cannot verify Xiaomi's certificate chain, set `SSL_CERT_FILE` to the installed `certifi` bundle for that command. Keep TLS verification enabled.
- Xiaomi currently describes these TTS models as free for a limited time. Check the official [MiMo speech synthesis guide](https://mimo.mi.com/docs/usage-guide/speech-synthesis-v2.5) for current models, voices, and terms.
