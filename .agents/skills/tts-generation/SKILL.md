---
name: tts-generation
description: Generate textbook dialogue, narration, or character voice audio with Xiaomi MiMo TTS in this project. Use when creating, revising, checking, or saving TTS audio for a lesson.
---

# TTS generation

Use `scripts/generate_tts.py` for Xiaomi MiMo speech synthesis. Produce a saved audio file for each eligible script line and record it in the lesson manifest.

## Generate audio

1. Read `script/dialogue-vN.md`. Check exact text, speaker, textbook page/location, and status for each line. Research unclear source text in the textbook pages and record the evidence. Synthesize only verified lines or explicitly identified adaptations/supplemental narration; leave unresolved lines out of TTS and record the blocker. Do not wait for routine user confirmation or infer textbook wording from model output.
2. Choose a MiMo voice that fits each script speaker and language. The built-in English voices are `Mia`, `Chloe`, `Milo`, and `Dean`; pass `--style` for delivery direction. The current script uses one voice per request. Generate different speakers as separate files when their voices need distinct timbres.
3. Read `MIMO_API_KEY` from `.env` or the process environment. Keep the credential private; never print it, put it in a command-line argument, store it in audio metadata, or commit it. The default endpoint is `https://api.xiaomimimo.com/v1` and can be overridden by `MIMO_BASE_URL`.
4. Run `--dry-run` first to confirm model, voice, output path, and text hash. Then generate the WAV:

   ```bash
   python3 scripts/generate_tts.py \
     --text-file projects/grade-4-english-term-1/unit-1-helping-at-home/script/tts-input/line-001-v1.txt \
     --voice Mia \
     --style "Clear, warm English for a primary school textbook dialogue, at a natural pace." \
     --output projects/grade-4-english-term-1/unit-1-helping-at-home/audio/tts/line-001-v1.wav
   ```

5. Verify the output is a readable WAV with `file` or `ffprobe`, then listen to the full clip. Check wording, pronunciation, pauses, speed, clipping, and voice fit. Record defects and revise failed lines.
6. Save each line to `audio/tts/<line-id>-vN.wav`. Update `audio/manifest-vN.md` with the script line ID, model, voice, style, output path, audio properties, SHA-256, and QA status. API credentials never enter files or metadata.
7. After eligible lines have saved WAVs and manifest entries, continue with the `video-generation` skill to generate silent shots and merge them in storyboard order with the TTS tracks.

## Request and output details

- The default model is `mimo-v2.5-tts`; the script requests WAV and validates that the response contains RIFF/WAVE audio.
- `--text` and `--text-file` are mutually exclusive. Use the versioned per-line text file copied from the canonical script so headings and speaker labels are not synthesized.
- Use `--dry-run` to inspect parameters without contacting Xiaomi. A regular invocation makes a live API request.
- If macOS Python cannot verify Xiaomi's certificate chain, set `SSL_CERT_FILE` to the installed `certifi` bundle for that command. Keep TLS verification enabled.
- Xiaomi currently describes these TTS models as free for a limited time. Check the official [MiMo speech synthesis guide](https://mimo.mi.com/docs/usage-guide/speech-synthesis-v2.5) for current models, voices, and terms.
