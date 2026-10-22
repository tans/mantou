# Unit 4 8188 canary log v2

Endpoint: `http://minixm.minapp.xin:8188` (Diffusers API behind the 8188 proxy). Unit 4 v2 uses this endpoint only; no video was generated through xiaoguai.

| Job | Request | Status | Evidence |
| --- | --- | --- | --- |
| `job_de82c6165a7d4a2684626cc573ea2a61` | text-to-video, quality, 512x320, 124 frames | `INFERENCE_FAILED` | Text encoder restored and encoded successfully; the DiT checkpoint was missing from the active model directory. |
| `job_f774d2b635b94209ae9b1c14e5bddb0b` | text-to-video, quality, 512x320, 124 frames | `succeeded` | `canary-text-quality-v2.mp4`, 5.175 s, H.264 512x320 24 fps plus unexpected AAC 32 kHz stereo. Six-frame contact sheet showed a consistent anime scene and cast. |
| `job_7dab8b16e63b42cda5b542ff43813aa0` | ref2av, `turbo8`, one Unit 3 frame, 512x320, 124 frames | `succeeded` | `shot-01-minixm-8188-v2.mp4`, 5.175 s, H.264 512x320 24 fps plus unexpected AAC 32 kHz stereo. First/middle/last contact sheet shows the three distinct children, neighborhood background, and visible character/camera motion. |
| `job_b6b8ff32490c46049c93ddad740e6421` | ref2av, `turbo8`, one Unit 3 frame, 512x320, 124 frames | `succeeded` | Downloaded as `shot-02-minixm-8188-v2.mp4`; two distinct production prompts successfully used the one-image ref2av path. |

The initial failure was caused by missing local model weights, not an invalid request. The missing 14 text-encoder shards and 10 BF16 DiT shards were restored from the host archive; text encoding, DiT inference, video decode, and image-reference conditioning have now succeeded. The endpoint `/ready` reports both `text_to_video` and `ref2av`, with a single supported geometry of 512x320. It also reports two workers; observed jobs ran sequentially on worker-a while worker-b remained idle.

The provider attaches an audio track even when `generate_audio` is false. Preserve each original provider file and let assembly derive a video-only copy; final dialogue continues to use the existing MiMo WAVs. The low 512x320 source geometry is a service limit and will be upscaled only by the existing assembly path.

Visual review is preliminary and per-shot. Shot 01's six-frame contact sheet was reviewed for character continuity and motion; review every remaining shot and final media streams, subtitle timing, complete decode, and full playback/listening before calling the lesson accepted.
