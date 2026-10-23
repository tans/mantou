# 快节奏片头预览 v1

日期：2026-10-23。跟踪：[Issue #14](https://github.com/tans/mantou/issues/14)。

## 本次要求与产物

用户要求“节奏更快，开头做一个片头 课本英语跟我学”。先应用到刚才账号分析中讨论的 Unit 2 “My friends”短片。

- [快节奏预览](../renders/unit-2-my-friends-fast-opening-v1.mp4)：H.264、1080×1920、24 fps；视频 21.708333 秒，AAC 24 kHz 单声道音频 21.698 秒。
- [剪辑映射与媒体元数据](../renders/unit-2-my-friends-fast-opening-v1.json)。源输入有效时长 25.240 秒；9 处静音共缩短 3.541667 秒，约 14%。视频/音频编码后时长差约 10 毫秒。
- [重新对轴的双语 SRT](../renders/unit-2-my-friends-fast-opening-v1.srt)：保留原来六句中英文本，字幕时间跟随音视频剪辑映射。
- [QA 记录](fast-opening-v1-qa.json)与[代表帧](../references/fast-opening-v1/contact-sheet.jpg)。
- 输出 SHA-256：`553b1853496724a00d797f47460cffb4afb08d5dbdc32a0534bf833f1dd18d13`。

## 开场与节奏

“课本英语跟我学”来自用户明确指定的包装文字，不属于教材原文。首镜顶部覆盖 1.25 秒，最后 0.15 秒淡出，随后恢复本课标题；不新增空屏等待，不另加旁白或音乐，首句英语与角色画面从起点进入。

沿用横屏配音预览、已核实的六句脚本、原角色与 v2 竖屏布局；没有重新生成角色或镜头，也没有使用付费供应商。以 -38 dB、持续至少 0.35 秒检测静音，只从静音中部剪除片段，各端至少保留 0.12 秒并向内按 24 fps 整帧量化。对白朗读速度为 1.0，不使用 atempo，不改词、不改变音高。首句 Mum 后停顿也随此映射收紧。

字幕 cue 1–6 仍对应 `script/dialogue-v1.md` 的 line-001–006。裁剪发生在静音，不改变教材内容顺序。源视频、配音 WAV、原双语 SRT 与历史成片保持原样。

## 复现

在仓库根目录运行；输出已存在时脚本拒绝覆盖，重做时使用下一个版本名。

```bash
python3 scripts/compose_vertical_lesson.py \
  --input projects/grade-4-english-term-1/unit-2-my-friends-lets-talk/renders/unit-2-my-friends-lets-talk-audio-preview-v1.mp4 \
  --srt projects/grade-4-english-term-1/unit-2-my-friends-lets-talk/edit/subtitles-bilingual-vertical-v1.srt \
  --grade '小学英语 · 四年级上册' \
  --unit 'Unit 2' --title 'My friends' --lesson "A. Let's talk" \
  --tighten-pauses --opening-text '课本英语跟我学' --opening-seconds 1.25 \
  --output projects/grade-4-english-term-1/unit-2-my-friends-lets-talk/renders/unit-2-my-friends-fast-opening-v1.mp4
```

新参数均显式启用；不传参数时继续原版式和原时间轴，不自动批量修改其他课次。

## 验收状态

- 已用 ffprobe 核对真实视频/音频流与时长；FFmpeg 全片解码通过。
- 已核对新旧六个字幕 cue 文本一致、时序有序且不重叠；最后字幕在 21.542 秒结束，未超出输出。
- 已目视核对 0.25、1.5、8、17、21.5 秒画面：片头文字完整，淡出后原标题恢复，中段和末句中英字幕可见且在卡片内。
- 完整人工播放、听检停顿剪辑点与口型同步、用户验收仍待完成；本文件称为预览，不将解码与抽帧等同于听检通过。
- 本次仅导出本地预览，没有发布或修改线上作品。
