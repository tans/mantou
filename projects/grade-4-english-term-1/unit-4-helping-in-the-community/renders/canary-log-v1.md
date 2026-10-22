# 8188 canary log v1

Endpoint: `http://minixm.minapp.xin:8188` (Diffusers API behind the 8188 proxy). No Unit 4 video was generated through xiaoguai.

| Job | Request | Status | Evidence |
| --- | --- | --- | --- |
| `job_de82c6165a7d4a2684626cc573ea2a61` | text-to-video, quality, 512x320, 124 frames | `INFERENCE_FAILED` at DiT | Conditioning loaded all 915 encoder weights and encoded text. DiT loader found zero safetensors in `/srv/models/lightx2v/h3/diT/bf16_tp6`; only config/index were present. The 10 BF16 master shards existed in `/tan/ac922-model-archive-20261021/diT/bf16_tp6`. |

The text encoder's 14 master shards have been restored to `/srv/models/lightx2v/h3/model_root/text_encoder`. The BF16 DiT master restore is now in progress. The same terminal job will not be resubmitted; run a fresh canary after the checkpoint inventory is restored.
