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
| 6. 字幕制作与合成 | 横屏两版与竖屏双语版已生成，待人工视听 | [`edit/subtitles-preview-v1.srt`](edit/subtitles-preview-v1.srt) 为横屏字幕源；[`edit/subtitles-bilingual-vertical-v1.srt`](edit/subtitles-bilingual-vertical-v1.srt) 为竖屏英中字幕源。 |
| 7. 合并与验收 | 横屏与竖屏预览已生成，待人工视听 | [`edit/assembly-v1.md`](edit/assembly-v1.md)；软字幕/烧录字幕横屏预览、[1080×1920 双语大字幕竖屏预览](renders/unit-2-my-friends-vertical-bilingual-white-v2.mp4)及混音 WAV。 |

## 课次简报

- 教材版本：人教版 PEP《英语（PEP）（三年级起点）四年级上册》，仓库归档 PDF 共 96 页。
- 单元：Unit 2 “My friends”；本次范围为 A “Who are your friends?” / “Let’s talk”。
- 教材位置：印刷 p.16；归档 PDF 第 22 页。Unit 2 首页为印刷 p.14 / PDF 第 20 页。
- 语言内容：介绍新朋友、询问姓名，并描述朋友的外形与性格。
- 教材原文：六句对话均逐字录入 [`script/dialogue-v1.md`](script/dialogue-v1.md)。
- 来源状态：本地正式教材 PDF；逐页目视检查，非 OCR 推断。p.16 衍生页图保存在 [`references/textbook-p16-render.png`](references/textbook-p16-render.png)，原 PDF 保持不变。
- 角色音色：`child` 固定 MiMo `Milo`，`mother` 固定 MiMo `Mia`；服务商、模型、默认语气与变更规则见角色 Bible。
- 生成镜头源画幅：16:9；竖屏交付：1080×1920 白底；横屏动画等比居中，顶部课程标题，底部英中双语字幕。版式由项目固定预设生成。

## 当前进度

- 2026-10-23 语音包装修订：新增 [24秒中文童声片头片尾预览 v4](renders/unit-2-my-friends-spoken-bookends-v4.mp4)。开场真实朗读“课本英语跟我学”，六句正文保音高1.2倍提速，末句完整后接“关注我，学习更多小学英语”，关注提示结束后保留0.604秒画面。首句沿用Milo局部重配并登记原始候选/所选区间，其余原配音和动画复用。完整SRT、正文SRT、profile、时间轴、SHA、ASR与QA见 [合成记录](edit/assembly-spoken-bookends-v4.md)；片头/片尾实际转写相符，英文最后一句完整，全片解码与代表帧检查通过，完整人工听检和用户验收仍待完成。固定包装与提速/收尾规则已接入 [短视频流程](../../SOCIAL_VIDEO_GUIDE.md)与项目技能，后续课程直接复用。跟踪 [Issue #15](https://github.com/tans/mantou/issues/15)。

- 2026-10-23：按用户“节奏更快，开头做一个片头 课本英语跟我学”要求，新增 [21.7 秒快节奏片头预览](renders/unit-2-my-friends-fast-opening-v1.mp4)。片头在首镜顶部显示 1.25 秒并淡出，正文立即开始；无额外中文配音。六句教材对白保持原速，9 处较长静音共缩短 3.542 秒；画面、音频和双语字幕使用同一剪辑映射。保留所有旧版，未向抖音发布。命令、元数据和验收边界见 [快节奏合成记录](edit/assembly-fast-opening-v1.md)；已通过完整解码、字幕文本/时序核对和代表帧目视检查，完整人工播放听检及用户验收待完成。跟踪 [Issue #14](https://github.com/tans/mantou/issues/14)。

- 已落盘教材原文、说话人映射、角色库和四镜头 Storyboard 草案。
- 六句 TTS 已生成；待完成逐条试听。四条镜头已生成、探测，并检查画面连续性；横屏软字幕/烧录字幕预览已生成。竖屏双语白底预览现按 `vertical-bilingual-white-v2` 固定模板重新压制（1080×1920、24 fps；源动画 1.8:1 等比居中在 1026×570 区域，未裁切/拉伸）。顶部有课程标题，底部英文 52 px、中文 54 px；样张见 [`references/vertical-layout-sample-v2.png`](references/vertical-layout-sample-v2.png)。完整听检与播放确认仍待完成。
- 后续制作遵循 Issue #8 方案，不把其它页面未核实内容混入本片。

## 抖音发布记录

### 2026-10-23：中文童声片头片尾 v4

- 用户在本次对话中明确要求“发布新的这个视频，注意标签，标题”；使用 [抖音发布技能](../../../.agents/skills/douyin-video-publishing/SKILL.md) 通过 BrowserOS Neo 提交。
- 账号：馒头工作室（抖音号 `69260421328`）。
- 文件：[unit-2-my-friends-spoken-bookends-v4.mp4](renders/unit-2-my-friends-spoken-bookends-v4.mp4)，24.000 秒，1080×1920；SHA-256：`886814b40514d9f2b3bf1009b98e2fb6e04141e06a686ca281bed24ef86a2f23`。
- 标题：**新朋友怎么介绍？四年级英语跟我学**。
- 话题：`#四年级英语`、`#小学英语`、`#人教版英语`、`#英语跟读`、`#亲子英语`；均已在发布编辑器中选择对应话题建议，并核对五个实际话题标签。
- 发布设置：公开、立即发布、不同时发布到其它平台；自主声明“内容由AI生成”。
- 封面：选取本片首帧，在平台编辑器中加入“四年级英语 / 新朋友怎么介绍？”文字，分别保存 3:4 竖封面与 4:3 横封面；截图核对文字及人物，平台显示“封面效果检测通过”“作品未见异常”。
- 平台显示的提交时间：**2026年10月23日 12:25**（北京时间）。
- 提交后核验：内容管理中出现标题及文案完全匹配的新作品，时长 **00:24**，状态为 **审核中**；未编辑、删除或重复提交。
- 作品 ID / 公开 URL：本次审核中卡片未提供可取得的公开链接或作品 ID，暂未取得；未确认公开上线。
- 证据位置：[创作者中心内容管理](https://creator.douyin.com/creator-micro/content/manage?enter_from=publish)，BrowserOS Neo 的 `codex/publish-english-lesson` 页面；保留该页面供查看。该记录证明提交与审核状态，不改变前述完整人工听检的验收边界。
- 可复用浏览器任务已保存为 `/neo-douyin-lesson-publish`，包含核对文件、选择真实话题、AI 声明、双封面、单次提交及状态归档步骤。

发布正文：

```text
人教版PEP四年级上册 Unit 2《My friends》A. Let's talk。
和孩子一起跟读：介绍新朋友，描述朋友的外貌和性格。
收藏起来，陪孩子一起练英语。
#四年级英语 #小学英语 #人教版英语 #英语跟读 #亲子英语
```
