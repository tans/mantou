# Audio manifest v2

This is a one-line repair manifest. Lines 001–005 and 007–014 continue to use the v1 WAVs documented in `manifest-v1.md`.

| Line | Provider / model | Voice profile | Text | Style change | Duration / format | SHA-256 | QA |
| --- | --- | --- | --- | --- | --- | --- | --- |
| line-006 | Xiaomi MiMo / `mimo-v2.5-tts` | narrator, Mia, `teacher-en-mia-clarity-v1` | `A cleaner cleans the community.` | Kept the v1 delivery direction and added an explicit stop after the final word. | 3.04 s; WAV, PCM16, mono, 24 kHz | `59565344c6ef2e7292e41bd1de328fb6e6fb42a167f3f3e82538549fc0c3a731` | Local `small.en` ASR exactly matched the script; full human listening pending. |

Input: `script/tts-input/line-006-v2.txt`. Audio: `audio/tts/line-006-v2.wav`. Request fingerprint and output hash: `audio/tts/line-006-v2.json`. Lesson configuration: `lesson-v5.json`.
