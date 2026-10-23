# 全局配音音色库

此表用于跨课次固定供应商 voice ID，避免同一角色或角色类型续配时随意更换音色。角色 Bible 仍负责记录某一课的具体角色、逐句风格和映射；每课 README 引用本库的 profile ID。更换 voice ID 时保留旧配置，注明日期、原因和受影响课程。

| Profile ID | 适用角色/场景 | 服务商/模型 | Voice ID | 默认风格 | 已使用课次 |
| --- | --- | --- | --- | --- | --- |
| `child-en-milo` | 英语儿童角色对白 | Xiaomi MiMo `mimo-v2.5-tts` | `Milo` | `Clear, warm English for a primary school child dialogue, at a natural pace.` | 四年级上册 Unit 2 `child`；二年级上册 Unit 2 `boy`（各课具体 style 见角色 Bible） |
| `female-en-mia` | 英语女性角色对白；按具体人物设定调整语气，不代表人物身份相同 | Xiaomi MiMo `mimo-v2.5-tts` | `Mia` | `Warm, clear English dialogue for a primary school textbook scene, at a natural pace.` | 四年级上册 Unit 2 `mother`；二年级上册 Unit 2 `girl`（各课具体 style 见角色 Bible） |

## 变更规则

- 栏目中文童声使用 `brand-child-zh-designed-v1`：MiMo `mimo-v2.5-tts-voicedesign`，设计为七到九岁女孩的清亮普通话童声；供应商无固定voice ID，直接复用 [`assets/branding/primary-english-child-zh-v1/`](../branding/primary-english-child-zh-v1/README.md) 的固定开场/结尾WAV和SHA。它是独立栏目旁白，不取代教材孩子或母亲的英语声线。完整风格、生成原件和试听状态见资产manifest；变更时新增版本。

- Voice ID 是持久配置；每课角色 Bible 记录引用的 profile ID、当前模型、逐角色 style 和脚本行号。
- 默认风格可为角色性格/情境做细化，但不更换 voice ID；确需更换时新增 profile 版本，旧行不删除。
- 同一 voice ID 不代表两个角色是同一人物；人物身份仍由每课教材和角色 Bible 决定。
- 只记录公开模型/voice 配置，不写 API key、账号信息或其它凭据。

## 蜡笔小新英语教学角色组 v1（2026-10-22）

用户指定角色与画风。以下是固定的英语合成 voice，不是原动画演员配音；完整试听状态以课次 manifest 为准。跨课继续沿用，变更新增 profile 版本。

| Profile ID | 角色 | 服务商/模型 | Voice ID | 默认风格 |
| --- | --- | --- | --- | --- |
| `teacher-en-chloe-v1` | 教学旁白 | Xiaomi MiMo `mimo-v2.5-tts` | `Chloe` | Clear, warm English for primary school learners. Gentle encouraging teacher, measured natural pace, precise word endings. Read only the supplied text. No music. |
| `shinchan-en-milo-v1` | 野原新之助（小新） | Xiaomi MiMo `mimo-v2.5-tts` | `Milo` | Playful cheerful young boy speaking clear standard English for a primary school lesson. Light comic confidence, natural childlike rhythm, never nasal or slurred. Read exactly the supplied text. No music. |
| `kazama-en-dean-v1` | 风间彻 | Xiaomi MiMo `mimo-v2.5-tts` | `Dean` | Bright, polite young male character speaking clear standard English. Curious and thoughtful, light youthful delivery at a measured natural pace. Read exactly the supplied text. No music. |
| `nene-en-mia-v1` | 樱田妮妮 | Xiaomi MiMo `mimo-v2.5-tts` | `Mia` | Lively friendly young female character speaking clear standard English for children. Warm curious tone, natural unhurried rhythm. Read exactly the supplied text. No music. |
| `teacher-en-mia-clarity-v1` | 英语教学旁白（Unit 3复核后替代Chloe候选；旧版保留） | Xiaomi MiMo `mimo-v2.5-tts` | `Mia` | `Clear, measured English for young learners.` |

2026-10-22：Unit 3教学旁白因短词串机器复核疑点统一从 teacher-en-chloe-v1 改用 teacher-en-mia-clarity-v1；实际采用行/文件和复核结果见课程最终配置与manifest。
