# TTS manifest v1 — Unit 2 “A great picture” Fun Time

## 状态

- 已准备 line-001 至 line-005 的逐句文本输入，来源为 [`script/dialogue-v1.md`](../script/dialogue-v1.md) 中已核实的教材原文。
- 尚未请求 MiMo API，也未生成 WAV：仓库 `.env` 和当前进程均未配置 `MIMO_API_KEY`。
- line-006 至 line-008 暂不合成，待教材配套音频确认朗读方式和说话人。
- MiMo 当前模型、英文内置音色以[官方语音合成文档](https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/speech-synthesis-v2.5)为准。

## 计划与产物

| 脚本行 | 输入文件 | 声音 | 模型 / 风格 | 输出 WAV | 音频属性 / SHA-256 | QA 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| line-001 | [`line-001-v1.txt`](../script/tts-input/line-001-v1.txt) | Milo（男声） | `mimo-v2.5-tts`；清晰、温暖、自然语速的小学英语对话 | `tts/line-001-v1.wav` | 尚未生成 | 等待本机配置 `MIMO_API_KEY` |
| line-002 | [`line-002-v1.txt`](../script/tts-input/line-002-v1.txt) | Mia（女声） | `mimo-v2.5-tts`；清晰、温暖、自然语速的小学英语对话 | `tts/line-002-v1.wav` | 尚未生成 | 等待本机配置 `MIMO_API_KEY` |
| line-003 | [`line-003-v1.txt`](../script/tts-input/line-003-v1.txt) | Milo（男声） | `mimo-v2.5-tts`；清晰、温暖、自然语速的小学英语对话 | `tts/line-003-v1.wav` | 尚未生成 | 等待本机配置 `MIMO_API_KEY` |
| line-004 | [`line-004-v1.txt`](../script/tts-input/line-004-v1.txt) | Mia（女声） | `mimo-v2.5-tts`；清晰、温暖、自然语速的小学英语对话 | `tts/line-004-v1.wav` | 尚未生成 | 等待本机配置 `MIMO_API_KEY` |
| line-005 | [`line-005-v1.txt`](../script/tts-input/line-005-v1.txt) | Milo（男声） | `mimo-v2.5-tts`；清晰、温暖、自然语速的小学英语对话 | `tts/line-005-v1.wav` | 尚未生成 | 等待本机配置 `MIMO_API_KEY` |

## 音色依据

MiMo 官方文档列出英文内置女声 Mia、Chloe 和男声 Milo、Dean。此处按画面中的小男孩/小女孩分别暂配 Milo/Mia；不模拟教材配音演员。
