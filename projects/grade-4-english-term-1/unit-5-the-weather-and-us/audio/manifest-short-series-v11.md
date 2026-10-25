# Unit 5 短集声音复用清单 v11

新TTS请求0；复用v7已选WAV与v9母版声音。Milo/Dean/Mia固定英语声线分别对应小新/风间/妮妮，不是原动画演员配音。未替换人物/模型/voice。问题卡无语音、无额外背景音乐。机器ASR筛查不是完整人工听检。

| 集 | 原行 | 人物 / voice | 原WAV | 原WAV SHA-256 | 速度 |
| --- | --- | --- | --- | --- | --- |
| ep01 | line-013 | 风间 / Dean | `audio/tts/line-013-v3.wav` | `b7da0de2ec4c87ee5c159a8f832b9a907aee32cddf6150ceac1c878569377d73` | 1.2倍保音高 |
| ep01 | line-014 | 小新 / Milo | `audio/tts/line-014-v1.wav` | `9e5e0072372027d948faaf804a1e9f285b8bb5884875fea60496b94d10279a23` | 1.2倍保音高 |
| ep01 | line-015 | 风间 / Dean | `audio/tts/line-015-v2.wav` | `645c1a2626171d04549673c70c134101b027945c6fa387e4f58b967602ee07f1` | 1.2倍保音高 |
| ep01 | line-016 | 小新 / Milo | `audio/tts/line-016-v1.wav` | `704a4b2aa34b6f02e31c2d7aa36861590b2e79326028b759c2ecf0fcfdb99cf5` | 1.2倍保音高 |
| ep01 | line-017 | 风间 / Dean | `audio/tts/line-017-v1.wav` | `fa3de8c822176ece3c014aa3570f7187c82e4793edc4db04aa1a03364f45398c` | 1.2倍保音高 |
| ep01 | line-018 | 小新 / Milo | `audio/tts/line-018-v1.wav` | `95305ca24a2dba9d95554916cadf093761ba1e57d39cb0529bce78582c4381ee` | 1.2倍保音高 |
| ep02 | line-007 | 风间 / Dean | `audio/tts/line-007-v1.wav` | `29ccb0f35259430f1007566e03cc65f394863dda69b163b21bf99cd80be9d862` | 1.0倍保音高 |
| ep02 | line-008 | 风间 / Dean | `audio/tts/line-008-v1.wav` | `0efdaa10fc6fda13930f734ddf4c6fa3edac925b920866fa744b2e9bfdfe9254` | 1.0倍保音高 |
| ep02 | line-009 | 妮妮 / Mia | `audio/tts/line-009-v1.wav` | `3cfd80a63d2433d2d2c291d922748dab8fc11d4f1bb0ba6627ea06f47c2c0481` | 1.0倍保音高 |
| ep02 | line-010 | 妮妮 / Mia | `audio/tts/line-010-v1.wav` | `8e14194646c47c4da3783c011a3a33b2d510652f5b3b9a0b5951c03d10d88ef7` | 1.0倍保音高 |
| ep03 | line-011 | 小新 / Milo | `audio/tts/line-011-v1.wav` | `c6c045bb7253d74a95c3de8fb3b6e2205ae6d0fe2c35ac192792a1de4fe31e7a` | 1.0倍保音高 |
| ep03 | line-012 | 小新 / Milo | `audio/tts/line-012-v1.wav` | `bbbb2f7eb53c8454ba0848d3094e15aa6d38d71f00b575bac72f7610a968062e` | 1.0倍保音高 |
| ep03 | line-005 | 小新 / Milo | `audio/tts/line-005-v1.wav` | `4935d916582885e2e408fa2fe22deaba3cd919001f4dd363659327f3db96b014` | 1.0倍保音高 |
| ep03 | line-006 | 小新 / Milo | `audio/tts/line-006-v1.wav` | `0da3b6afa74676cf0dfc5b61970a32e72d46e60e51c2a3e2b622428a15357d19` | 1.0倍保音高 |

line-014原WAV在正文后的独立尾声，多个ASR识别为笑声；line-017长停顿后也有短尾声。v11只在剪辑中提前收尾，原WAV和v10候选保留。源区间、原因、英文完整性和实际MP4复核见各集assembly.json与`export-asr-short-series-v11.json`。EP02/03输出SHA与v10相同。
