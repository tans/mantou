# 配音返修与栏目包装 manifest v2

2026-10-23，按用户中文童声片头、语音关注提示与实际提速要求制作。教材正文脚本仍为 `script/dialogue-v1.md` 的六句，不改词。

| 用途 | 采用音频 | 配置与状态 |
| --- | --- | --- |
| 栏目中文片头/片尾 | `assets/branding/primary-english-child-zh-v1/audio/opening-v1.wav`、`closing-v1.wav` | 独立合成童声profile；模型、style、SHA、实际长度和原件见全局manifest，直接跨课复用 |
| line-001 | `tts/line-001-clean-v2.wav` | MiMo mimo-v2.5-tts / Milo；保留原声线，首句局部重配，筛查为“Mom, I have a new friend.”；Mum/Mom只作为转写地区拼写归一，教材字幕仍Mum |
| line-002–006 | 原 `tts/line-002…006-v1.wav` | 继续原模型、voice与文字，参见manifest-v1 |

首句候选原件 `tts/line-001-v2.wav` 有多读的Mum，不作为完整take入片。清理版保留第一个完整教材句子，收紧长静音并排除后段加词；所取区间、输入/输出SHA、完整style和原件状态见 [`line-001-revision-v2.json`](line-001-revision-v2.json)，没有覆盖旧配音。普通横屏母版只替换首句0–3.84秒音轨槽位，其余源音频和视频保留，保存为 `renders/unit-2-my-friends-corrected-master-v2.mp4`。

正文提速在合成阶段使用同一setpts/atempo=1.2，不改变声线音高，不再次请求教材配音。完整人工听检和用户对童声质感/提速可懂度的验收仍待完成；ASR结果是筛查证据，不能代替听检。
