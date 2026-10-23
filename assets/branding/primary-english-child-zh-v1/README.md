# 小学英语中文童声包装 v1

用于栏目片头和关注提示。由用户于2026-10-23明确指定，属于补充旁白，不是教材原文或课文人物对白。两句在一次 MiMo voicedesign 请求中生成，再分开存档，今后各课直接复用同一WAV，保证包装声线一致。

| 段落 | 文字 | 固定音频 | 实测时长 |
| --- | --- | --- | --- |
| 片头 | 课本英语跟我学！ | `audio/opening-v1.wav` | 1.738708秒 |
| 片尾 | 关注我，学习更多小学英语！ | `audio/closing-v1.wav` | 3.062375秒 |

- 唯一脚本：[`script/dialogue-v1.md`](script/dialogue-v1.md)，逐句及合并输入在 `script/tts-input/`。
- 可复用配置：[`profile.json`](profile.json)。正文默认1.2倍；包装WAV已经过1.1倍保音高处理，合成时不再次提速。
- 合成原件：`audio/branding-pair-raw-v1.wav`，保留原样。分割取片头0–1.9秒、片尾2.08–5.44秒；间隙经静音检测核对，不裁掉语音。
- 模型、完整style、文字/音频SHA、处理区间和人工听检状态：[`manifest-v1.json`](manifest-v1.json)。voice design没有本项目可持久化的供应商voice ID，以本地固定音频和profile ID保持复用。
- 本次官方依据：[MiMo语音合成文档](https://mimo.mi.com/docs/zh-CN/quick-start/usage-guide/audio/speech-synthesis-v2.5)，2026-10-23读取，确认voicedesign支持中文文字描述定制音色。请求未开启自动润色。设计目标为七到九岁女孩、普通话、清亮活泼；具体童声听感仍待人工验收，不声称是真实儿童录音。
- v2成片抽取的中文开头、结尾已由faster-whisper/small反向转写，均对应指定文字；base模型曾将“关注”误识别为“观众”，保留原始机器记录，不把机器转写等同于人工听检。

## 后续课次

从已核实的无烧录字幕横屏母版和双语SRT出发，使用 `compose_vertical_lesson.py --tighten-pauses --packaging-profile assets/branding/primary-english-child-zh-v1/profile.json`。完整命令和收尾检查见 [`projects/SOCIAL_VIDEO_GUIDE.md`](../../../projects/SOCIAL_VIDEO_GUIDE.md)。此步骤只用本地固定WAV，不重新请求供应商。

## 修改包装文字或声音

建立新版本目录和profile ID，先更新脚本、逐句/合并输入，再运行现有 `scripts/generate_tts.py --model mimo-v2.5-tts-voicedesign --style <完整童声描述> --text-file <合并输入> --output <新版本原始WAV> --dry-run`，核对后生成。模型参数不传英文voice；风格描述存入manifest。新的分割点按新音频静音区和转写重新确定，保留两句完整字音，再派生保音高音频；不能把本版时间码直接套到新录音。更新profile的文字、路径、SHA及试听状态，然后只重合成依赖该包装的交付版，不重生成课文镜头。

凭据只从本机忽略的.env或环境读取。WAV为本项目合成并归档的栏目包装，独立于 `assets/sfx/` 的第三方音乐许可记录。
