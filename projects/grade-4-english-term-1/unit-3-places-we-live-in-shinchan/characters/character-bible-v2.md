# 蜡笔小新角色与视觉设定 v2

用户于 2026-10-22 指定蜡笔小新角色及动画风格。视觉 profile：`shinchan-community-tv-v1`。内置分镜生图首请求网络失败；改从电视朝日官方角色页归档三张角色原图，用于视频生成时锁定外形。官方参考来源见 assets/characters/shinchan-official/README.md。使用英语合成声线，不复刻或冒充原动画演员的声音。

| 角色 ID | 外观固定项 | 配音 profile / voice |
| --- | --- | --- |
| shinchan | 小新；粗黑眉、圆脸、黑短发；红色短袖、黄色短裤、黄色鞋 | shinchan-en-milo-v1 / Milo |
| kazama | 风间；深蓝侧分发；浅蓝短袖上衣、深蓝短裤 | kazama-en-dean-v1 / Dean |
| nene | 妮妮；橘红双马尾；浅粉上衣、粉裙、粉色鞋 | nene-en-mia-v1 / Mia |
| narrator | 教学旁白，不出镜，不冒充任何教材人物 | teacher-en-chloe-v1 / Chloe |

风格：经典蜡笔小新 TV 二维赛璐璐，粗黑线、平涂、柔和色彩、春日部日常社区、轻喜剧表情。固定午后光照与幼儿身高比例；不切成三维，不生成文字/水印，不加入成人笑话。图中成人仅为友好背景邻居/太极练习者。

## 固定配音参数

模型：Xiaomi MiMo `mimo-v2.5-tts`。跨课继续沿用以下 profile，变更时新增版本。

### teacher-en-chloe-v1

- 角色：narrator；voice ID：Chloe
- 默认风格：Clear, warm English for primary school learners. Gentle encouraging teacher, measured natural pace, precise word endings. Read only the supplied text. No music.
- 配置首次用于本课，需完整听检后评估角色适配，不声称原动画配音。

### shinchan-en-milo-v1

- 角色：shinchan；voice ID：Milo
- 默认风格：Playful cheerful young boy speaking clear standard English for a primary school lesson. Light comic confidence, natural childlike rhythm, never nasal or slurred. Read exactly the supplied text. No music.
- 配置首次用于本课，需完整听检后评估角色适配，不声称原动画配音。

### kazama-en-dean-v1

- 角色：kazama；voice ID：Dean
- 默认风格：Bright, polite young male character speaking clear standard English. Curious and thoughtful, light youthful delivery at a measured natural pace. Read exactly the supplied text. No music.
- 配置首次用于本课，需完整听检后评估角色适配，不声称原动画配音。

### nene-en-mia-v1

- 角色：nene；voice ID：Mia
- 默认风格：Lively friendly young female character speaking clear standard English for children. Warm curious tone, natural unhurried rhythm. Read exactly the supplied text. No music.
- 配置首次用于本课，需完整听检后评估角色适配，不声称原动画配音。

## 本次质量修订

无参考的5秒样片虽可解码，但风间过高、脸型成人化，否决。正式镜头每次同时传入三张官方参考图，并约束五岁幼儿、等高、大头短肢。原样片作为失败证据保留。
