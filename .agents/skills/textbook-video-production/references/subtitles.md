# Subtitle production reference

## Text source and timing

- Use the verified canonical script as the only source for dialogue captions. Keep spelling, contractions, punctuation, capitalization and character names exact. Do not silently paraphrase or translate.
- Give each cue a traceable script line ID in the assembly mapping. Preserve speaker separation when turns change; do not merge different speakers into one cue.
- Time cues from the approved audio mix or each final WAV's measured duration. Start/end cues on audible words, leave natural pauses clear, and check all timecodes against the final picture. Scene duration is not a substitute for speech duration.
- Keep captions readable: normally one or two short lines, sensible phrase breaks, sufficient bottom safe margin, high contrast and an outline or backing where the picture varies. Keep important faces and teaching objects unobstructed. Use a font installed in the render environment and inspect actual output because font fallback can change wrapping.

## Output choice

- **Burned-in captions:** rasterized into the video picture and visible in any player. Make this the primary preview/final when the user asks for a subtitled video or does not specify a format.
- **Soft subtitles:** a selectable subtitle stream or sidecar SRT/ASS. Retain an editable source; include a selectable track when the user requests switchable captions or accessibility options. Verify the subtitle stream with `ffprobe` and ensure a sidecar is named with the same video stem.
- When producing both, make the burned-in and soft-subtitle outputs from the same subtitle source and keep their wording/timecodes identical. Label output names clearly.

## Verification

1. Compare every cue against the script and line-ID mapping; check for missing, duplicated or reordered lines.
2. Parse or inspect every start/end time and ensure the final cue does not outlast audio or get cut off by the video.
3. Probe the final file: confirm video and intended audio streams; confirm a soft subtitle stream when requested. A burned-in output need not have a subtitle stream.
4. Extract representative frames near the beginning, middle and ending, including at least one caption transition. Check safe margins, contrast, wrapping, spelling and whether captions cover faces/objects. Play the full video to confirm synchronization.
5. Record format, dimensions, duration, subtitle mode, source SRT path and SHA-256 in the assembly record/sidecar. Mark human visual/playback checks separately from automated probes.
