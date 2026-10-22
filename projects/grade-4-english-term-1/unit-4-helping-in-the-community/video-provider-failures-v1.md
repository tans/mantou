# 8188 视频服务记录 v1

请求服务：`http://minixm.minapp.xin:8188`

服务检查：`/health` 与 `/ready` 均返回正常；当前模型状态为 `experimental`，只公布 `512x320x124` 几何。

| Job | Task/profile | 结果 | 记录 |
|---|---|---|---|
| `job_bb58642caaa245c687b81d9d2adcbbf8` | `ref2av` / `turbo8` | `INFERENCE_FAILED` | `Diffusers conditioning stage failed` |
| `job_a1fd031f71d0476cab64344d5c891aa1` | `text_to_video` / `quality` | `INFERENCE_FAILED` | `Diffusers conditioning stage failed` |
| `job_4fb7b9bd8d2d425fa491c3bbc6f4920b` | 最小文本提示 / `turbo8` | `INFERENCE_FAILED` | `Diffusers conditioning stage failed` |

以上任务均已查询到终态，没有重复提交同一任务。由于 8188 在本次运行中不能产出 MP4，镜头使用课次内本地动态分镜兜底：角色参考图/教材页作为画面源，加入轻微运动后与正式 MiMo TTS、双语字幕合成。兜底文件明确标记为 `minixm-8188-local-fallback`，不是供应商生成片；后续 8188 恢复后可仅重做 `renders/shot-*-minixm-8188-v1.mp4` 及其下游。
