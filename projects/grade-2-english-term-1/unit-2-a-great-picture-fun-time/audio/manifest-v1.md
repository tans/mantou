# TTS manifest v1 — Unit 2 “A great picture” Fun Time

## 状态

- 已准备 line-001 至 line-005 的逐句文本输入，来源为 [`script/dialogue-v1.md`](../script/dialogue-v1.md) 中已核实的教材原文。
- 已使用本机 `.env` 中的 `MIMO_API_KEY` 调用 MiMo 生成 line-001 至 line-005；密钥未写入产物或日志。
- 五条 WAV 均已通过文件格式、采样率、声道数、位深、时长和 SHA-256 检查。尚未完成逐条试听，发音、停顿、语速、削波和音色适配仍待人工听检。
- line-006 至 line-008 暂不合成，待教材配套音频确认朗读方式和说话人。
- MiMo 当前模型、英文内置音色以[官方语音合成文档](https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/speech-synthesis-v2.5)为准。

## 计划与产物

| 脚本行 | 输入文件 | 声音 | 模型 / 风格 | 输出 WAV | 音频属性 / SHA-256 | QA 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| line-001 | [`line-001-v1.txt`](../script/tts-input/line-001-v1.txt) | Milo（男声） | `mimo-v2.5-tts`；Clear, warm English for a primary school textbook dialogue, at a natural pace. | [`tts/line-001-v1.wav`](tts/line-001-v1.wav) | WAV PCM s16le，24 kHz，单声道，16-bit，2.400 s；SHA-256 `575eebfe343892ef30a969ca2b4b088f71b68aaefdfe9ac9c4c153dded7dbeb8` | 文件检查通过；待完整试听 |
| line-002 | [`line-002-v1.txt`](../script/tts-input/line-002-v1.txt) | Mia（女声） | `mimo-v2.5-tts`；Clear, warm English for a primary school textbook dialogue, at a natural pace. | [`tts/line-002-v1.wav`](tts/line-002-v1.wav) | WAV PCM s16le，24 kHz，单声道，16-bit，1.280 s；SHA-256 `83c382b4b5b76d1d29c2bbe2dc2aa8f33307c265393c6c92e11453ec13edd5ef` | 文件检查通过；待完整试听 |
| line-003 | [`line-003-v1.txt`](../script/tts-input/line-003-v1.txt) | Milo（男声） | `mimo-v2.5-tts`；Clear, warm English for a primary school textbook dialogue, at a natural pace. | [`tts/line-003-v1.wav`](tts/line-003-v1.wav) | WAV PCM s16le，24 kHz，单声道，16-bit，3.200 s；SHA-256 `f7c5d940a3cd0fb4852489865611a2d5e7bd0151218678dbeb3f7cc6678b9765` | 文件检查通过；待完整试听 |
| line-004 | [`line-004-v1.txt`](../script/tts-input/line-004-v1.txt) | Mia（女声） | `mimo-v2.5-tts`；Clear, warm English for a primary school textbook dialogue, at a natural pace. | [`tts/line-004-v1.wav`](tts/line-004-v1.wav) | WAV PCM s16le，24 kHz，单声道，16-bit，2.880 s；SHA-256 `84ce4c705578055c754fa11f90849e6aaa531c96661fb5509817f5aab7ae2bcf` | 文件检查通过；待完整试听 |
| line-005 | [`line-005-v1.txt`](../script/tts-input/line-005-v1.txt) | Milo（男声） | `mimo-v2.5-tts`；Clear, warm English for a primary school textbook dialogue, at a natural pace. | [`tts/line-005-v1.wav`](tts/line-005-v1.wav) | WAV PCM s16le，24 kHz，单声道，16-bit，4.000 s；SHA-256 `98e534400d45885a187f000431e4f09deb056bf6e4d970adb5d98499283ec21d` | 文件检查通过；待完整试听 |

## 音色依据

MiMo 官方文档列出英文内置女声 Mia、Chloe 和男声 Milo、Dean。此处按画面中的小男孩/小女孩分别暂配 Milo/Mia；不模拟教材配音演员。
