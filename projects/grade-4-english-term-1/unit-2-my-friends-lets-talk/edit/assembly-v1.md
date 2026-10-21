# Assembly v1 — Unit 2 “My friends” A “Let’s talk”

## 当前状态

已生成 25.7 秒预览，按六句 TTS 实测长度顺序合成；包含英语软字幕。文件为 `../renders/unit-2-my-friends-lets-talk-audio-preview-v1.mp4`，字幕源 `subtitles-preview-v1.srt`，连续配音 WAV `../audio/preview-mix-v1.wav`。视频时长末尾留有静帧余量，避免截断最后一句音频。当前仍是预览，需人工完整试听并在播放器确认字幕/对白同步后再标记验收。

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
- 输出预览：H.264 864×480、24 fps；AAC 24 kHz 单声道；英文软字幕轨（mov_text）。
- 四条生成镜头请求关闭音频，但实际都含 AAC 32 kHz 立体声音轨；未覆盖原件，按 manifest 保存去音轨派生片并用于合成。
- 工具探测确认输出包含视频、音频和字幕流；镜头画面已目视检查，角色及室内环境保持一致。
- **待验收**：人工完整试听 TTS/混音，播放器检查字幕显示与同步、音量、发音及最终镜头表现。完成前只称“预览”，不称最终成片。
