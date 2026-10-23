# Unit 4 8188 generation and repair log v3

Date: 2026-10-23
Endpoint: `http://minixm.minapp.xin:8188`
Selected profile: `turbo8`

## Recovery and production result

- The first Unit 4 requests failed because model weights were missing. The archived text encoder and DiT weights were restored; subsequent text-to-video and single-image `ref2av` canaries succeeded. Canary task IDs and the recovery trail are preserved in [v2](canary-log-v2.md).
- The service admitted 512×320 output at 24 fps. It attached an AAC track even when audio generation was disabled. Provider originals remain intact; selected silent derivatives are used in the edit, with the existing MiMo WAVs supplying dialogue.
- All 14 selected scenes are 8188 outputs: shot-01/02/04–10/12–14 v2, shot-03 v4, and shot-11 v3. Job IDs, prompts, logs, provider originals, and silent derivatives are retained in the corresponding shot and render files.

## Visual selection

| Shot | Selection | Review |
| --- | --- | --- |
| shot-03 | v2 and v3 rejected; v4 selected | v2/v3 included an incorrect medical cross. v4 shows the children meeting a firefighter beside a fire engine on an open street; the medical-cross artifact is absent. |
| shot-09 | v2 selected with edit crop | Provider output included garbled Chinese text at the lower edge. The assembly crops 44 px from the bottom before adding the verified bilingual subtitle; the source is preserved. |
| shot-11 | v3 selected | The children help an older woman carry groceries; character group and neighborhood animation remain consistent. |
| other shots | v2 selected | Representative start/middle/end frames are archived in `../storyboards/qa-v4-assembled-01-07.jpg` and `../storyboards/qa-v4-assembled-08-14.jpg`. |

## Final outputs

The v4 master, horizontal burned-subtitle cut, and vertical bilingual cut are all H.264/AAC and fully decoded. Frame sizes are 1280×720 and 1080×1920, at 24 fps with 48 kHz mono AAC. The full file details and hashes are recorded in `../edit/qa-v4.md`.

This repair replaces the v1 local-motion-board fallback as the current draft. It does not mark full human audio/video acceptance complete; continuous listening and user acceptance remain pending.
