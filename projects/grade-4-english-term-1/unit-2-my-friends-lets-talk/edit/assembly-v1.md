# Assembly v1 — Unit 2 “My friends” A “Let’s talk”

## 当前状态

已生成两种 25.7 秒预览，均按六句 TTS 实测长度顺序合成：软字幕版 `../renders/unit-2-my-friends-lets-talk-audio-preview-v1.mp4` 含英语字幕轨；烧录字幕版 `../renders/unit-2-my-friends-lets-talk-burned-subtitles-preview-v1.mp4` 将英语字幕直接绘入画面，适合不支持字幕轨的播放器。共用字幕源 `subtitles-preview-v1.srt` 与连续配音 WAV `../audio/preview-mix-v1.wav`。视频时长末尾留有静帧余量，避免截断最后一句音频。当前仍是预览，需人工完整试听并在播放器确认字幕/对白同步后再标记验收。

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
