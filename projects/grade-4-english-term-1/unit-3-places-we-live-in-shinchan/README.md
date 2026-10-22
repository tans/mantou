# 四年级上册 Unit 3 · Places we live in · 蜡笔小新版

跟踪：[Issue #12](https://github.com/tans/mantou/issues/12)。2026-10-22 用户要求：蜡笔小新角色与画风，完整教学视频，同时整理下次换课复用流程。

## 教材与范围

- 人民教育出版社《英语（PEP）（三年级起点）四年级上册》，本地 `assets/textbook/pep-grade-4-volume-1.pdf`，共96页。教材正文为本地归档扫描件，索引来自第三方 FreePEP，未把第三方下载站称为官方原件。
- Unit 3 标题 Places we live in，印刷 p.26–37 / PDF 第32–43页；主片覆盖 p.28–32 A/B 对话、地点词汇、社区活动、ck 拼读，以及 p.34–35 社区介绍项目与复习。
- 完整指单支有开场、教学主线、复习、结尾的成片；不包含歌曲、听力练习答案、p.33 博物馆全文与 p.36–37 成都拓展阅读，不称为全单元逐页朗读。
- 来源路径：根 README → FreePEP 清单（本次已复查有目标册）→ 本地PDF → `references/unit3-32…43.png` 页图目视核对；版权页见 `references/textbook-copyright.png`。
- 具体版次/出版年份：`UNRESOLVED`，版权页未载，不用 PDF 创建时间冒充出版年份。教材原文、册次、单元和印刷页已经逐页核实，可继续主片；若换官方版本须重新核对。原配套音频未归档，使用独立英语TTS，不提供原听力答题答案。

## 阶段状态

| 阶段 | 状态 | 产物 |
| --- | --- | --- |
| 来源与脚本 | 完成 | `script/dialogue-v1.md`；页图与逐句证据 |
| 角色 | 已固定，参考图生成中 | `characters/character-bible-v1.md` |
| Storyboard | 16镜头文字已落盘 | `storyboards/storyboard-v1.md` |
| TTS | 待生成 | `script/tts-input/`，计划逐行 WAV |
| 动画镜头 | 待生成 | `shots/shot-01…16/prompt-v1.txt` |
| 字幕/合成 | 待制作 | 实测音频对轴，保留双语SRT |
| 视听验收 | 未开始 | 生成/解码/抽帧/听检/用户验收分别记录 |

## 可编辑入口

`script/dialogue-v1.md` 是唯一脚本文字来源；`lesson-v1.json` 保存编排、翻译、声音和镜头路径；二者逐行匹配才允许生成。修改须新增版本并更新配置，原始生成资产不覆盖。
