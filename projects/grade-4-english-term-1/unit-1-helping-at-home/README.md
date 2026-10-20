# Unit 1 问候镜头

第一段动画草稿：早晨，Wu Binbin 在家向妈妈打招呼。教材和分镜图作为内容、场景参考；对白和具体镜头仍需按教材原文核对。

## 当前生成结果

- 参考图版视频：`renders/unit-1-helping-at-home-greeting-ref2av-cropped-5s.mp4`
- 服务任务：`job_a8fd621ec0c34b09895faf593b245bd8`
- 模型与任务：MiniMax H3 Fast，`ref2av`，Wu Binbin 单人裁切参考图、参考专用 LoRA，TP4，8 steps，seed `20261021`
- 文件信息：H.264/AAC，512×320，5.175 秒，1,014,499 bytes
- SHA-256：`67378f2a4d5b97f0c7e999a4b731bd1708806602d1e8a2a959b03e458e69375b`
- 服务解码报告：pass；124 帧、32 kHz 双声道音频，峰值采样显存 14,924 MiB，生成总耗时约 467 秒。
- 技术上生成成功，但抽帧显示画面仍过度贴近参考角色图，没有达到可用动画质量。整张海报版保留在 `renders/unit-1-helping-at-home-greeting-ref2av-5s.mp4`；无参考图 T2V 版保留在 `renders/unit-1-helping-at-home-greeting-5s.mp4`。两版参考图结果仅作为服务链路验收样片，不作为成片。

此前的无参考图文生视频草稿保留在 `renders/unit-1-helping-at-home-greeting-5s.mp4`，对应任务 `job_1f0c2535313847008b16a635d5a796df`。

## 参考资产

- 角色单人裁切图：[`references/wu-binbin-character-reference.png`](references/wu-binbin-character-reference.png)，由根目录角色概念海报裁切，仅作为 Wu Binbin 外观参考。
- 原角色海报：[`assets/characters/character-redesign-concept.png`](../../../../assets/characters/character-redesign-concept.png)
- 分镜图：[`assets/storyboards/unit-1-helping-at-home-storyboard.png`](../../../../assets/storyboards/unit-1-helping-at-home-storyboard.png)
- 教材：[`assets/textbook/pep-grade-4-volume-1.pdf`](../../../../assets/textbook/pep-grade-4-volume-1.pdf)

## 服务修复记录

先前的参考生成失败由两处配置错误引起：

1. `ref2av` 错误使用 TP6；参考分区有 56 个 heads，按服务文档和已有成功配置应使用 TP4。
2. Fast 参考任务错误复用普通文生视频权重路径。参考任务需要 `data/h3ref_deploy_20261020/model_root` 作为模型根目录，并将 `data/h3ref_deploy_20261020/ref_fp8_tp4` 单独传为 FP8 checkpoint。

修复后 `/v1/models` 报告标准和 Fast 型号的 `ref2av` TP 为 4。服务端文件及 `OPERATIONS.md` 的对应差异记录在根目录 [`operations/patches/aiserver-ref2av-tp4.patch`](../../../../operations/patches/aiserver-ref2av-tp4.patch)。服务仓库目录没有 `.git`，所以无法在服务目录内提交；修改前备份位于 `/home/minixm/AIserver/backups/pre-ref2av-tp4-20261020-154105/`，以及 `/home/minixm/AIserver/backups/pre-ref2av-model-root-20261020-154527/`。

## 当前状态

参考图 API 链路已通过端到端验收，服务配置修复并已记录；可交付画面仍需调整提示词、参考策略或改用分镜逐镜制作。教材对白也需先核对原文。
