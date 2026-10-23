# Unit 4 v4 export and review record

Date: 2026-10-23
Status: complete exports and media/frame checks; full human listening and user acceptance remain pending.

## Final exports

| File | Video / audio | Duration | Bytes | SHA-256 |
| --- | --- | ---: | ---: | --- |
| [Horizontal master](../renders/unit-4-helping-in-the-community-master-v4.mp4) | H.264, 1280×720, 24 fps / AAC, 48 kHz mono | 72.438 s | 36,184,645 | `2bf607e05117d37edadf43f98f40cdba433b071e6061e6c141cb06c8998fb4b3` |
| [Horizontal bilingual burned](../renders/unit-4-helping-in-the-community-bilingual-burned-v4.mp4) | H.264, 1280×720, 24 fps / AAC, 48 kHz mono | 72.437 s | 31,727,709 | `06d58ddf1aa280aefca868f96afc6d8d998d1ad244c53f0028e348a90bffc570` |
| [Vertical bilingual](../renders/unit-4-helping-in-the-community-vertical-bilingual-white-v4.mp4) | H.264, 1080×1920, 24 fps / AAC, 48 kHz mono | 72.417 s | 24,013,338 | `175da1e1b31a799f0724c5ccba2e5fb505ac2320e75556c2eaee301f72363ee1` |

All three outputs completed full FFmpeg decode. On the burned version, FFmpeg's default null muxer emitted one DTS-rounding warning; the 1,738 video packet DTS values and decoded frame timestamps are strictly increasing, and a 24 fps full decode completed without warnings. The master retains the dialogue mix; the burned and vertical versions use the same 14-cue bilingual SRT. The vertical output uses the fixed `vertical-bilingual-white-v2` preset.

## Image and subtitle review

- Start, middle, and end frames from each of the 14 assembled cuts are in [shots 01–07](../storyboards/qa-v4-assembled-01-07.jpg) and [shots 08–14](../storyboards/qa-v4-assembled-08-14.jpg).
- Shot-03 v4 shows the firefighter and fire engine without the medical-cross artifact from v2/v3. Shot-11 v3 shows a child helping an older woman. Other selected shots use v2.
- Shot-09's provider-generated lower-edge text is removed by the recorded 44 px bottom crop; the original source remains unchanged.
- The vertical contact sheet `../storyboards/qa-v4-vertical-contact.jpg` shows the title treatment, early dialogue, mid-lesson scene, and final dialogue/subtitle layout.
- 14 subtitles are in order and map one-to-one to the 14 script lines in `timeline-v4.json`. The ending cue finishes before the picture ends.

## Audio text review

`../audio/asr-review-v2.json` was generated with local faster-whisper `small.en` (CPU int8, beam size 5). After normalizing number formatting, punctuation, and British/American spelling, 13 of 14 lines match the script. The initial report `../audio/asr-review-v1.json` is retained; it flagged number and spelling variants that v2 now normalizes. Line-006 contains the expected sentence plus an uncertain trailing ASR token, `This...`; keep it flagged for human listening. Measured master loudness is -17.5 LUFS integrated, 5.6 LU LRA, and -1.3 dBFS true peak. These machine checks do not verify pronunciation, voice quality, pauses, clipping, or the complete soundtrack.

## Remaining acceptance

Listen to the full horizontal or vertical cut and specifically resolve line-006's tail; confirm English pronunciation, volume, subtitle sync, and the final audio tail. Then record user acceptance in the lesson README and close the linked production issue. Until then these files remain review drafts.
