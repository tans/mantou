# Character Bible v1 — Unit 2 “My friends” A “Let’s talk”

## 来源

角色外观来自本地教材 PDF 的教材印刷 p.16（PDF 第 22 页），参见 [`../references/textbook-p16-render.png`](../references/textbook-p16-render.png)。教材画面中的孩子未在本板块对白气泡中标出姓名；本 Bible 稳定称为 `child`，不自行绑定为 John、Wu Binbin 或其它教材人物。

## 角色与配音表

| 角色 ID | 称呼 | 脚本行 | 画面描述与服装 | 持久化 TTS 音色 | 依据 |
| --- | --- | --- | --- | --- | --- |
| `child` | 孩子 | line-001、003、004、006 | 小学生，深棕肤色，短卷黑发；黄色长袖上衣，肩部和袖子有蓝紫色条纹；蓝色长裤。保持与教材 p.16 的形象一致。 | Xiaomi MiMo `mimo-v2.5-tts`，voice `Milo`；默认风格：`Clear, warm English for a primary school child dialogue, at a natural pace.` | 教材 p.16 插图和对话气泡 |
| `mother` | 妈妈 | line-002、005 | 成年女性，深色头发扎低马尾，黄色发圈；砖红色长袖上衣、深灰长裤。保持与教材 p.16 的形象一致。 | Xiaomi MiMo `mimo-v2.5-tts`，voice `Mia`；默认风格：`Warm, clear English for a mother speaking naturally to a primary school child.` | 教材 p.16 插图和对话气泡 |
| `zhang-peng-photo` | Zhang Peng（照片中的朋友） | 无对白 | 孩子向妈妈展示的照片中出现；短黑发，绿色外套，按 p.16 照片保持连续。 | 无对白，不合成声音。 | 教材 p.16 照片和 line-003 文本 |

## 音色锁定与续配规则

- `child` 固定使用 MiMo `mimo-v2.5-tts` / `Milo`；`mother` 固定使用同一模型 / `Mia`。后续本项目同角色续配沿用此 voice ID 和默认语气。
- 若服务商弃用模型/音色或确需换声，保留旧配置与旧音频版本，在新 Bible 版本记录原因、生效范围和新配置；不得静默替换。
- API 凭据仅从本机 `.env` 或进程环境读取，不写入角色库、音频元数据或 Git。

## 连续性约束

- 孩子固定黄色上衣和蓝紫色条纹；妈妈固定砖红色上衣、深色低马尾；Zhang Peng 照片中的绿色外套/短发保持一致。
- 家庭场景保持教材插图中的室内会面氛围、坐卧家具和孩子带回的书包/朋友照片；后续镜头可调整镜位，不改人物衣着与角色关系。
- 说话人身份按脚本表，不因 TTS 音色选择改变教材角色身份。
