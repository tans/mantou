# Character Bible v1 — Unit 2 “A great picture” Fun Time

## 来源和核对状态

- 依据：教材第 16–17 页的公开整页扫描，见课次 [`README.md`](../README.md) 来源表。
- 教材没有给这两位孩子的姓名；本项目用“小男孩”和“小女孩”作稳定称呼，不补造姓名。
- 以下外观只取自教材插图。后续镜头保持本课人物的脸型、发型、服装和主色连贯。

## 角色表

| 角色 ID | 项目称呼 | 脚本行 | 出场 | 外观和服装 | 配音音色 | 参考来源 |
| --- | --- | --- | --- | --- | --- | --- |
| `boy` | 小男孩 | line-001、line-003、line-005 | Fun Time 画面 1–5 | 小学生；黑色短发；白/浅灰上衣配深蓝袖口；红色领巾。画画时穿着保持一致。 | Xiaomi MiMo `mimo-v2.5-tts`，voice `Milo`；默认风格：`Clear, warm English for a primary school textbook dialogue, at a natural pace.` | 教材 p.16–17 扫描；见课次 README 的来源链接 |
| `girl` | 小女孩 | line-002、line-004；line-008 说话人待原音确认 | Fun Time 画面 1–5 | 小学生；橙棕色头发扎起；浅绿色上衣，粉色领口。画画时穿着保持一致。 | Xiaomi MiMo `mimo-v2.5-tts`，voice `Mia`；默认风格：`Clear, warm English for a primary school textbook dialogue, at a natural pace.` | 教材 p.16–17 扫描；见课次 README 的来源链接 |

## 配音配置（持久化）

- 全局配音音色 profile 见 [`assets/characters/voice-library.md`](../../../../assets/characters/voice-library.md)：`boy` 引用 `child-en-milo`，`girl` 引用 `female-en-mia`。

- 本课小男孩固定使用 Xiaomi MiMo 模型 `mimo-v2.5-tts` 的英文 voice `Milo`；小女孩固定使用同模型英文 voice `Mia`。后续同一角色续配时沿用此映射和默认风格，避免音色漂移。
- 若服务商弃用该模型/音色或确需换声，先保留旧配置与旧音频版本，再在新的角色 Bible 版本记录变更原因、生效范围和新音色；不得静默替换。
- line-006–008 的教材朗读者尚未核实。目前生成的版本使用 voice `Mia`、风格 `Clear, warm English narration for a primary school textbook dialogue, at a natural pace.`，仅作为旁白试配，不归属 `girl` 角色；待取得教材配套音频后再决定是否重配。
- 凭据只从本机 `.env` 或进程环境读取，不记录到角色库。

## 连续性约束

- 小男孩固定红领巾和白/浅灰上衣、深蓝袖口；小女孩固定浅绿上衣和橙棕色扎发。
- 故事发生在画画桌边，角色共同用手印完成树形画；按教材插图保持颜料、画纸、调色盘和手印画面连续。
- 同一角色沿用本 Bible 的持久化 TTS 音色配置；line-006–008 当前按旁白试配，教材角色/合读方式仍待配套音频确认，不能把旁白试配当作角色分配。
