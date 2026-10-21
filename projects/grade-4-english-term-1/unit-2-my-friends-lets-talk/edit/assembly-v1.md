# Assembly v1 — Unit 2 “My friends” A “Let’s talk”

## 当前状态

已生成两种 25.7 秒预览，均按六句 TTS 实测长度顺序合成：软字幕版 `../renders/unit-2-my-friends-lets-talk-audio-preview-v1.mp4` 含英语字幕轨；烧录字幕版 `../renders/unit-2-my-friends-lets-talk-burned-subtitles-preview-v1.mp4` 将英语字幕直接绘入画面，适合不支持字幕轨的播放器。共用字幕源 `subtitles-preview-v1.srt` 与连续配音 WAV `../audio/preview-mix-v1.wav`。视频时长末尾留有静帧余量，避免截断最后一句音频。当前仍是预览，需人工完整试听并在播放器确认字幕/对白同步后再标记验收。

## 竖屏英中双语预览

- 输出：[`../renders/unit-2-my-friends-vertical-bilingual-white-v1.mp4`](../renders/unit-2-my-friends-vertical-bilingual-white-v1.mp4)；元数据和哈希见同名 JSON sidecar。
- 版式：`vertical-bilingual-white-v1`，白底 1080×1920、24 fps。上方显示“小学英语 · 四年级上册 / Unit 2 / My friends / A. Let's talk”。
- 原动画输入：[`../renders/unit-2-my-friends-lets-talk-audio-preview-v1.mp4`](../renders/unit-2-my-friends-lets-talk-audio-preview-v1.mp4)，显示比例 1.8:1。居中等比放大到 1026×570（x=27,y=500），无裁切、无拉伸；源横屏/静音镜头文件保留。
- 字幕源：[`subtitles-bilingual-vertical-v1.srt`](subtitles-bilingual-vertical-v1.srt)。六句英文原文逐句配中文翻译，英文在上、中文在下；时间码复用 TTS 实际对白时间。下方字幕卡固定于 x=62..1018、y=1240..1710。
- 合成脚本：仓库 `scripts/compose_vertical_lesson.py`；未来课程只替换输入视频、字幕和标题字段，固定其余版式。
- 探测：H.264 1080×1920 24 fps；AAC 24 kHz 单声道；25.25 s。抽查 2 s、9 s、20 s 画面，标题、动画比例、英中字幕卡及长句均完整可见。
- **待验收**：本次自动探测与抽帧目视通过；完整播放/试听及字幕同步人工验收仍待完成。

| SRT cue | 脚本行 | English | 中文 | 时间范围 |
| --- | --- | --- | --- | --- |
| 1 | line-001 | Mum, I have a new friend. | 妈妈，我有一个新朋友。 | 00:00:00.000–00:00:03.840 |
| 2 | line-002 | Really? What's your friend's name? | 真的吗？你的朋友叫什么名字？ | 00:00:04.040–00:00:07.720 |
| 3 | line-003 | His name is Zhang Peng. | 他叫张鹏。 | 00:00:07.970–00:00:11.010 |
| 4 | line-004 | Look! He's tall and strong. | 看！他又高又壮。 | 00:00:11.260–00:00:15.580 |
| 5 | line-005 | He has nice short hair too. | 他还有一头漂亮的短发。 | 00:00:15.780–00:00:19.140 |
| 6 | line-006 | Yes. He's also kind. He often helps me. | 是的。他也很友善。他经常帮助我。 | 00:00:19.390–00:00:24.990 |

## 镜头与脚本映射

| 顺序 | 镜头 | 脚本行 | 原始镜头 | 合成使用素材 | 实际素材时长 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | shot-01 | line-001–002 | `../renders/shot-01-xiaoguai-minimax-h3-480p-v1.mp4` | 同名 `-silent-v1.mp4` | 8.000 s | 已探测；去除供应商附带音轨 |
| 2 | shot-02 | line-003 | `../renders/shot-02-xiaoguai-minimax-h3-480p-v1.mp4` | 同名 `-silent-v1.mp4` | 5.167 s，剪辑取约 3.29 s | 已探测；去除供应商附带音轨 |
| 3 | shot-03 | line-004–005 | `../renders/shot-03-xiaoguai-minimax-h3-480p-v1.mp4` | 同名 `-silent-v1.mp4` | 8.000 s，末帧延长约 0.13 s | 已探测；去除供应商附带音轨 |
| 4 | shot-04 | line-006 | `../renders/shot-04-xiaoguai-minimax-h3-480p-v1.mp4` | 同名 `-silent-v1.mp4` | 6.583 s，剪辑取约 5.85 s | 已探测；去除供应商附带音轨 |

## 合成参数与验收状态

- 对白次序与教材六句一致；角色声线按角色 Bible：child=Milo，mother=Mia。
- WAV 混音：24 kHz、单声道、16-bit PCM；按每句实测时长连接，同镜头对话间隔 0.20 秒，镜头间隔 0.25 秒。
- 输出预览：H.264 864×480、24 fps；AAC 24 kHz 单声道。软字幕版含英文 mov_text 轨；烧录字幕版字幕直接进入画面，不含额外字幕流。两版共用 `subtitles-preview-v1.srt`。
- 四条生成镜头请求关闭音频，但实际都含 AAC 32 kHz 立体声音轨；未覆盖原件，按 manifest 保存去音轨派生片并用于合成。
- 工具探测确认软字幕版包含视频、音频和字幕流；烧录版包含视频和音频流。抽查烧录版开头、中段、结尾帧，字幕清晰并处于底部安全区，未遮挡主要角色及朋友照片。镜头画面角色、服装和室内环境保持一致。
- **待验收**：人工完整试听 TTS/混音，并在播放器中完整播放检查软字幕轨/烧录字幕同步、音量、发音及最终镜头表现。完成前只称“预览”，不称最终成片。

## 竖屏字幕可读性优化 v2

- 输出：[`../renders/unit-2-my-friends-vertical-bilingual-white-v2.mp4`](../renders/unit-2-my-friends-vertical-bilingual-white-v2.mp4)；完整参数、输入/字幕/输出 SHA-256 见同名 JSON sidecar。v1 保留归档，不覆盖。
- 字幕字号提升为英文 52 px 粗体、中文 54 px，母版按 1080×1920 计；在 360 px 宽设备上约为 17–18 px。语言标签同步增至 25 px。
- 长字幕按卡片可用宽度换至最多两行；英文行数决定分隔线与中文区域位置，确保两种语言都留在 x=62..1018、y=1240..1710 字幕卡内。
- 合成命令新增 `--preset-version 2`，当前为默认值；使用 `--preset-version 1` 可以复现历史小字号布局。
- 抽帧检查短句（2 s）与最长对白（20 s）：中英文在两行布局下仍完整落入卡片；媒体探测为 H.264 1080×1920、24 fps，AAC 24 kHz 单声道，25.25 s。短句样张见 [`../references/vertical-layout-sample-v2.png`](../references/vertical-layout-sample-v2.png)。
- **待验收**：加大字号的竖屏预览已完成探测与抽帧目视检查；完整播放和试听仍待人工确认。
