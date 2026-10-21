# 人教版 PEP 四年级上册 Unit 2 “My friends” — A “Let’s talk”

本课先制作 Unit 2 A 部分 “Who are your friends?” / “Let’s talk” 首支短片，依照[教材动画生产标准](../PRODUCTION_STANDARD.md)逐步推进。主教材是仓库归档的人民教育出版社《英语（PEP）（三年级起点）四年级上册》PDF。

GitHub 跟踪：[Issue #8](https://github.com/tans/mantou/issues/8)。

## 制作流程状态

| 步骤 | 状态 | 产物 / 结论 |
| --- | --- | --- |
| 1. 确定对话和旁白 | 已完成 | [`script/dialogue-v1.md`](script/dialogue-v1.md)。逐句核对教材印刷 p.16（PDF 第 22 页），六句对话及说话人按气泡尾端记录。 |
| 2. 确定角色 | 已完成 | [`characters/character-bible-v1.md`](characters/character-bible-v1.md)。人物外观依 p.16；孩子暂称 `child`，不将未见于对话框的姓名臆定为说话人；TTS 音色在角色库固定记录。 |
| 3. 生成 Storyboard | 已完成 | [`storyboards/storyboard-v1.md`](storyboards/storyboard-v1.md) 与四格概念图 [`storyboard-v1.png`](storyboards/storyboard-v1.png)；概念图已检查人物连续性。 |
| 4. 生成 TTS | 已生成 6 条，待试听 | [`audio/manifest-v1.md`](audio/manifest-v1.md)；按角色库持久化音色生成，格式、时长和 SHA-256 已记录；完整听检未完成。 |
| 5. 分镜生成 | 4 条已生成并探测 | `renders/shot-01…04-*.mp4`；xiaoguai MiniMax H3、16:9、480p；供应商虽收到静音请求仍返回 AAC，已保留原稿并另存无音轨副本。 |
| 6. 字幕制作与合成 | 两种预览已生成，待人工视听 | [`edit/subtitles-preview-v1.srt`](edit/subtitles-preview-v1.srt) 为字幕源；软字幕版和烧录字幕版均已生成。 |
| 7. 合并与验收 | 预览已完成，待人工视听 | [`edit/assembly-v1.md`](edit/assembly-v1.md)；约 25 秒 H.264/AAC 预览，软字幕/烧录字幕两版及混音 WAV。 |

## 课次简报

- 教材版本：人教版 PEP《英语（PEP）（三年级起点）四年级上册》，仓库归档 PDF 共 96 页。
- 单元：Unit 2 “My friends”；本次范围为 A “Who are your friends?” / “Let’s talk”。
- 教材位置：印刷 p.16；归档 PDF 第 22 页。Unit 2 首页为印刷 p.14 / PDF 第 20 页。
- 语言内容：介绍新朋友、询问姓名，并描述朋友的外形与性格。
- 教材原文：六句对话均逐字录入 [`script/dialogue-v1.md`](script/dialogue-v1.md)。
- 来源状态：本地正式教材 PDF；逐页目视检查，非 OCR 推断。p.16 衍生页图保存在 [`references/textbook-p16-render.png`](references/textbook-p16-render.png)，原 PDF 保持不变。
- 角色音色：`child` 固定 MiMo `Milo`，`mother` 固定 MiMo `Mia`；服务商、模型、默认语气与变更规则见角色 Bible。
- 目标画幅：16:9；视频提示词与输出规格待 dry-run 后记录。

## 当前进度

- 已落盘教材原文、说话人映射、角色库和四镜头 Storyboard 草案。
- 六句 TTS 已生成；待完成逐条试听。四条镜头已生成、探测，并检查画面连续性；静音派生片、25 秒带英文软字幕预览和烧录字幕预览已生成；烧录版字幕抽帧检查通过。配音/成片仍待人工完整听检与播放确认。
- 后续制作遵循 Issue #8 方案，不把其它页面未核实内容混入本片。
