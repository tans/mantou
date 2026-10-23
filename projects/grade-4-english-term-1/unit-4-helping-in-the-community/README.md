# 四年级上册 Unit 4 · Helping in the community · 蜡笔小新版

当前交付为 v5，复用 8188 生成的 14 个动画镜头。针对 `line-006` 的尾音疑点重新生成 MiMo 配音，并据此重做横屏与竖屏双语成片；媒体探测、完整解码和代表帧检查已完成。人工完整试听及用户验收仍待完成。

## 直接观看

| 用途 | 当前文件 |
| --- | --- |
| 手机竖屏，1080×1920，英中大字幕 | [竖屏双语 v5](renders/unit-4-helping-in-the-community-vertical-bilingual-white-v5.mp4) |
| 课堂/电脑横屏，1280×720，双语烧录 | [横屏双语 v5](renders/unit-4-helping-in-the-community-bilingual-burned-v5.mp4) |
| 再剪辑的无字幕母版，含最终英语配音 | [横屏母版 v5](renders/unit-4-helping-in-the-community-master-v5.mp4) |
| 检查镜头与字幕 | [v4 14 镜头检查图](storyboards/qa-v4-assembled-01-07.jpg)、[v4 镜头 08–14](storyboards/qa-v4-assembled-08-14.jpg)、[v5 开头/line-006/结尾](storyboards/qa-v5-contact.jpg) |
| 查阅字幕、时间轴与合成来源 | [双语 SRT](edit/subtitles-bilingual-v5.srt)、[时间轴](edit/timeline-v5.json)、[合成记录](edit/assembly-v5.md)、[质量记录](edit/qa-v5.md) |

## 教材与范围

- 人民教育出版社《英语（PEP）（三年级起点）四年级上册》，使用本地扫描 PDF `assets/textbook/pep-grade-4-volume-1.pdf`；本片核对 Unit 4 印刷 p.38–49 / PDF 第44–55页。教材索引和来源说明见根目录 README。
- 14 句脚本见 `script/dialogue-v4.md`；`line-013` 为 `There are three elephants in the photo.`。角色替换为小新、风间、妮妮，教材英文句子和明确补充旁白均在脚本中标识。
- 角色沿用 Unit 3 的视觉和 MiMo 配音 profile，参考图为 `references/cast-sheet-shinchan-v1.png`；14 条 WAV 及属性、SHA-256 记录在 `audio/manifest-v1.md`。

## 8188 生成与返修

- 视频服务为 `http://minixm.minapp.xin:8188`，模型 profile `turbo8`；本课没有使用 xiaoguai。服务恢复缺失权重后，文本生成与单图 ref2av canary 均成功，完整镜头任务也已产出可解码动画。
- 8188 当前仅提供 512×320 源画面，并会在请求静音时附带意外音轨。保留供应商原片，另存无音轨派生片；合成使用既有 MiMo 配音。放大由横屏合成流程完成。
- v4 采用 shot-01 至 shot-14 的 14 个动画镜头：shot-03 使用 v4，shot-11 使用 v3，其余使用 v2。shot-03 v3 因错误医疗十字被否决；v4 改为开放街道、消防员与消防车。shot-09 合成时裁去底部 44 px，去除模型生成的乱码字幕；原片保留。
- v5 仅修复 `line-006` 配音：使用原 Mia 旁白 profile，增加句尾立即结束的朗读约束；ASR 识别为 `A cleaner cleans the community.`，未识别到多余尾词。其余 13 条配音与 14 个动画镜头复用。v5 文件、哈希和解码状态见 `edit/qa-v5.md`。
- 原 v1 本地动态分镜成片继续保留为历史版本；v4 首次替换为生成动画，当前成片为 v5。生成任务与 canary 记录见 `renders/canary-log-v2.md`、`renders/canary-log-v3.md` 和各镜头目录。

## 检查与状态

| 阶段 | 状态 | 证据 |
| --- | --- | --- |
| 教材/脚本 | 已核对 | `script/dialogue-v4.md`、本地教材扫描页 |
| 配音 | 14 条可用；line-006 为 v2；旧 13 条复用；ASR 合计 14/14 匹配 | `audio/manifest-v1.md`、`audio/manifest-v2.md`、`audio/asr-review-v2.json`、`audio/asr-review-v3.json` |
| 动画镜头 | 14 个采用镜头已探测并检查代表帧 | `renders/shot-*-minixm-8188-*-silent.mp4`、上方抽帧拼图 |
| 横屏/竖屏输出 | v5 已导出；H.264/AAC，完整解码通过 | `renders/*v5.mp4` 及 sidecar |
| 人工全片视听 | 待完成 | ASR 和抽帧检查不能替代完整播放、听感、发音、音量、同步与尾音确认 |
| 用户验收 | 待完成 | 验收完成前不称为正式通过 |

横屏母版约 69.85 秒、1280×720、24 fps、48 kHz 单声道 AAC；横屏双语版约 69.85 秒；竖屏双语版约 69.83 秒、1080×1920。v4 保留为历史版本。最终输出 SHA-256 与质量记录见 `edit/qa-v5.md`。
