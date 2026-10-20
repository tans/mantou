# Unit 1 问候镜头

第一段动画草稿：早晨，Wu Binbin 在家向妈妈打招呼。教材和分镜图作为内容、场景参考；对白和具体镜头仍需按教材原文核对。

## 当前最佳生成稿

- 推荐查看：[`renders/unit-1-helping-at-home-greeting-1280x768-h3-20step-5s.mp4`](renders/unit-1-helping-at-home-greeting-1280x768-h3-20step-5s.mp4)
- 服务任务：`job_e78c35dfaf7c4eb098c16d0021561559`
- 模型与任务：MiniMax H3 标准型，`text_to_video`，1280×768，20 steps，无 LoRA，seed `20261020`
- 文件信息：H.264/AAC，1280×768，5.175 秒，3,814,478 bytes
- SHA-256：`902f6a1cfad10b1fa702f7bd712a6f4f664e43653c94bf2c0f325646659a87d7`
- 服务报告：124 帧；conditioning 42.19 秒、DiT 484.09 秒、decode 58.47 秒；峰值显存 13,094 MiB。
- 视觉检查：男孩和妈妈同时入镜，动作、场景和问候关系可读，较原 512×320 稿明显清楚。细节仍有柔化，定位为分镜草稿，不作为最终成片。

## 画质对照记录

| 方案 | 文件 | 结果 |
| --- | --- | --- |
| 旧默认 T2V | `renders/unit-1-helping-at-home-greeting-5s.mp4` | 512×320，画面偏糊。 |
| Fast T2V 高分辨率 | `renders/unit-1-helping-at-home-greeting-864x480-t2v-5s.mp4` | 864×480，较旧默认改善，但细节仍软。 |
| 标准 H3 Turbo 8 steps | `renders/unit-1-helping-at-home-greeting-1280x768-h3-t2v-5s.mp4` | 1280×768，5.175 秒，峰值显存 13,098 MiB；构图可读，细节仍偏软。 |
| 标准 H3 参考生成 | `renders/unit-1-helping-at-home-greeting-reference-864x480-5s.mp4` | 864×480，完整角色参考有效，但角色画面偏近、母亲未稳定入镜，未选作推荐稿。 |
| 标准 H3 20 steps | `renders/unit-1-helping-at-home-greeting-1280x768-h3-20step-5s.mp4` | 当前最佳。两位角色及场景关系更清楚，仍需后续镜头级修整。 |

尝试将 1280×768 稿交给 SeedVR2 放大至 2048×1152 时，作业触发服务器主机内存 OOM，AIserver 被 systemd 自动重启。该超分路线暂不用于默认流程，也没有将失败作业标为成功。

## 服务默认质量档

服务器 H3 服务此前在调用方未指定宽高时使用 512×320，容易产出不适合成片预览的低分辨率视频。现将 `text_to_video` 默认画布调整为 1280×768（服务允许的最大面积，983,040 像素），保留 `ref2av` 的 512×320 默认画布以控制其更高的参考编码显存；调用方显式传入尺寸时行为不变。默认步数仍为 21（实际 infer steps 为 steps + 1）。

服务部署目录没有 Git 元数据，远端源文件差异、API 文档差异和修改前备份记录在根目录 [`operations/patches/aiserver-video-quality-default.patch`](../../../../operations/patches/aiserver-video-quality-default.patch)。修改前备份为 `/home/minixm/AIserver/backups/minimax-pre-t2v-quality-default-20261020.py` 与 `/home/minixm/AIserver/backups/API-pre-t2v-quality-default-20261020.md`；修改后已重启服务并确认 `/health` 返回 HTTP 200。

## 参考资产

- 完整角色参考裁图：[`references/wu-binbin-full-body-reference.png`](references/wu-binbin-full-body-reference.png)
- 旧的错误角色裁图（只剩下半身和靴子，保留作问题记录）：[`references/wu-binbin-character-reference.png`](references/wu-binbin-character-reference.png)
- 原角色海报：[`assets/characters/character-redesign-concept.png`](../../../../assets/characters/character-redesign-concept.png)
- 分镜图：[`assets/storyboards/unit-1-helping-at-home-storyboard.png`](../../../../assets/storyboards/unit-1-helping-at-home-storyboard.png)
- 教材：[`assets/textbook/pep-grade-4-volume-1.pdf`](../../../../assets/textbook/pep-grade-4-volume-1.pdf)

## 此前服务修复

先前的参考生成失败由两处配置错误引起：

1. `ref2av` 错误使用 TP6；参考分区有 56 个 heads，按服务文档和已有成功配置应使用 TP4。
2. Fast 参考任务错误复用普通文生视频权重路径。参考任务需要 `data/h3ref_deploy_20261020/model_root` 作为模型根目录，并将 `data/h3ref_deploy_20261020/ref_fp8_tp4` 单独传为 FP8 checkpoint。

修复后 `/v1/models` 报告标准和 Fast 型号的 `ref2av` TP 为 4。服务端文件及 `OPERATIONS.md` 的对应差异记录在根目录 [`operations/patches/aiserver-ref2av-tp4.patch`](../../../../operations/patches/aiserver-ref2av-tp4.patch)。服务目录无 Git；此前修改前备份位于 `/home/minixm/AIserver/backups/pre-ref2av-tp4-20261020-154105/` 与 `/home/minixm/AIserver/backups/pre-ref2av-model-root-20261020-154527/`。

## 教材对白依据

参考图动画当前用到的 `Hi, Mum!` / `Hi, Wu Binbin!` 对白已按 Unit 1 场景暂用。开始最终配音前仍应对照教材页核对英文标点和出场角色。
