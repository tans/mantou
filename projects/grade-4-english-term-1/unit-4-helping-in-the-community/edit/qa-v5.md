# Unit 4 v5 export and review record

Date: 2026-10-23
Status: exports, full decode, stream timestamps, ASR, and representative frame review complete; full human listening and user acceptance remain pending.

## Repair scope

v4's local ASR report flagged `line-006` with an uncertain trailing `This...` after the expected sentence. v5 keeps the verified script text, narrator voice, all 14 selected 8188 shots, and the other 13 v1 narration files. Only `line-006` was regenerated as v2, with a clear stop-after-final-word direction. Its duration changed from 5.60 s to 3.04 s, so the subtitle timing and downstream cue positions were rebuilt from the v2 WAV. The original v1 audio and all v4 exports remain unchanged.

The v2 line was recognized as `A cleaner cleans the community.` by local faster-whisper `small.en` (CPU int8, beam size 5), with no trailing token. Combining this result with the 13 matching lines in `asr-review-v2.json`, all 14 current lines have an exact normalized ASR match. ASR does not replace human listening.

## Final exports

| File | Video / audio | Duration | Bytes | SHA-256 |
| --- | --- | ---: | ---: | --- |
| [Horizontal master](../renders/unit-4-helping-in-the-community-master-v5.mp4) | H.264, 1280×720, 24 fps / AAC, 48 kHz mono | 69.855 s | 35,436,339 | `2cbd407ac50906786eeeacc42a1fa6499fb6ff26c6bec92d5ae89a587885532c` |
| [Horizontal bilingual burned](../renders/unit-4-helping-in-the-community-bilingual-burned-v5.mp4) | H.264, 1280×720, 24 fps / AAC, 48 kHz mono | 69.854 s | 31,136,447 | `df9826199f5a159919b645a127946e72161b4885a19cf4e8d3b5d7ea8533ecfb` |
| [Vertical bilingual](../renders/unit-4-helping-in-the-community-vertical-bilingual-white-v5.mp4) | H.264, 1080×1920, 24 fps / AAC, 48 kHz mono | 69.833 s | 23,348,078 | `4ec386837e8788fca14fb6d0f81bc06be3804d95aa78ae371d70c593edfc69c7` |

The vertical export uses `vertical-bilingual-white-v2`. Its JSON sidecar records the master and v5 SRT hashes, 14 subtitle cues, and the 1080×1920 layout.

All three exports completed `ffmpeg -v error -xerror` full decode with exit code 0. `ffprobe` found 1,676 video packets and 3,270 audio packets per export; DTS values are strictly increasing within each stream. The horizontal null-muxer decode emitted a single boundary-rounding DTS warning, while the saved file's packet DTS remained strictly increasing. Master integrated loudness measured -17.48 LUFS, -1.32 dBTP, and 5.10 LU LRA.

## Subtitle and frame review

- The v5 timeline maps all 14 subtitle cues to their WAVs. `line-006` runs from 24.433 s to 27.473 s; `line-007` begins at 28.767 s after the repair shortened the previous cue and scene.
- The [v5 contact sheet](../storyboards/qa-v5-contact.jpg) shows the opening, the repaired line with its English/Chinese subtitle card, and the ending. The subtitle text fits its card; the animation remains within the white vertical canvas without cropping or stretching.
- The v4 contact sheets remain the representative review of all 14 unchanged generated shots.

## Remaining acceptance

Listen to the complete v5 cut and confirm the new `line-006` delivery, pronunciation, pauses, subtitle sync, overall volume, and ending. Record user acceptance in the lesson README and close Issue #13 only after that review. Until then these exports remain review drafts.
