# 蜡笔小新教学角色组 · 当前采用设定 v4

本课角色替换依据用户2026-10-22指令。教学内容来自已核对教材，人物身份/场景为动画改编。官方角色原PNG保存在课次references与assets/characters/shinchan-official，来源为电视朝日角色页；保持原图不变。正式视频每次同时传入三张参考。

| 角色ID | 外观连续性 | 当前voice profile / voice |
| --- | --- | --- |
| shinchan | 小新；大圆脸、粗黑眉、黑短发；红色上衣、黄色短裤、黄色鞋 | shinchan-en-milo-v1 / Milo |
| kazama | 风间彻；深蓝尖形侧分头、大头短肢的五岁幼儿；浅蓝上衣、蓝短裤 | kazama-en-dean-v1 / Dean |
| nene | 妮妮；橘红双马尾；浅粉上衣、粉裙、粉色鞋 | nene-en-mia-v1 / Mia |
| narrator | 教学旁白，不出镜，不冒充角色原声 | teacher-en-mia-clarity-v1 / Mia |

风格：经典蜡笔小新TV二维赛璐璐，粗黑轮廓、平涂色、柔和日常社区背景。三位主要角色年龄感相近、幼儿比例；成人仅为邻居、太极练习者和医生。保持服装主色、发型、脸型，场景在社区中自然转场。禁止成人笑话、三维重制、角色融合、模型对白/字幕作为教学内容。

## 配音配置

服务商/模型：Xiaomi MiMo `mimo-v2.5-tts`；所有声音是内置英语合成声线，不声称原动画演员配音。同角色后续继续沿用voice ID，默认style与局部返修style分开记录。

### teacher-en-mia-clarity-v1

- 角色：教学旁白；voice：Mia
- 默认style：Clear, measured English for young learners.
- 台词：line-001, line-002, line-012, line-016, line-025, line-028, line-031, line-034, line-037, line-038, line-039, line-040, line-041, line-046, line-047, line-048, line-049
- 局部style以lesson-v8.json对应行和实际WAV JSON为准；不随机换voice。

### shinchan-en-milo-v1

- 角色：野原新之助（小新）；voice：Milo
- 默认style：Playful cheerful young boy speaking clear standard English for a primary school lesson. Light comic confidence, natural childlike rhythm, never nasal or slurred. Read exactly the supplied text. No music.
- 台词：line-003, line-006, line-007, line-008, line-010, line-013, line-014, line-020, line-024, line-035, line-036
- 局部style以lesson-v8.json对应行和实际WAV JSON为准；不随机换voice。

### kazama-en-dean-v1

- 角色：风间彻；voice：Dean
- 默认style：Bright, polite young male character speaking clear standard English. Curious and thoughtful, light youthful delivery at a measured natural pace. Read exactly the supplied text. No music.
- 台词：line-005, line-011, line-018, line-019, line-021, line-023, line-026, line-027, line-032, line-033, line-044, line-045
- 局部style以lesson-v8.json对应行和实际WAV JSON为准；不随机换voice。

### nene-en-mia-v1

- 角色：樱田妮妮；voice：Mia
- 默认style：Lively friendly young female character speaking clear standard English for children. Warm curious tone, natural unhurried rhythm. Read exactly the supplied text. No music.
- 台词：line-004, line-009, line-015, line-017, line-022, line-029, line-030, line-042, line-043
- 局部style以lesson-v8.json对应行和实际WAV JSON为准；不随机换voice。

## 修订与质量证据

- 无参考首样的风间成人化，已否决；v2起归档官方三角色参考，正式v3镜头采用。
- 旧Chloe旁白短词出现疑点，v5起统一Mia旁白；旧版保留。最终选用音频49/49通过small.en逐词反向核对，完整人工听感待验收。
- line-035与line-007同文本、同Milo、同style，显式复用同一已核验WAV；其它局部修订见配置与manifest。
- 原教材说话人按气泡位置留在脚本文档；动画角色映射为制作改编，不把小新/风间/妮妮说成教材原角色。
