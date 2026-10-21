# 全局配音音色库

此表用于跨课次固定供应商 voice ID，避免同一角色或角色类型续配时随意更换音色。角色 Bible 仍负责记录某一课的具体角色、逐句风格和映射；每课 README 引用本库的 profile ID。更换 voice ID 时保留旧配置，注明日期、原因和受影响课程。

| Profile ID | 适用角色/场景 | 服务商/模型 | Voice ID | 默认风格 | 已使用课次 |
| --- | --- | --- | --- | --- | --- |
| `child-en-milo` | 英语儿童角色对白 | Xiaomi MiMo `mimo-v2.5-tts` | `Milo` | `Clear, warm English for a primary school child dialogue, at a natural pace.` | 四年级上册 Unit 2 `child`；二年级上册 Unit 2 `boy`（各课具体 style 见角色 Bible） |
| `female-en-mia` | 英语女性角色对白；按具体人物设定调整语气，不代表人物身份相同 | Xiaomi MiMo `mimo-v2.5-tts` | `Mia` | `Warm, clear English dialogue for a primary school textbook scene, at a natural pace.` | 四年级上册 Unit 2 `mother`；二年级上册 Unit 2 `girl`（各课具体 style 见角色 Bible） |

## 变更规则

- Voice ID 是持久配置；每课角色 Bible 记录引用的 profile ID、当前模型、逐角色 style 和脚本行号。
- 默认风格可为角色性格/情境做细化，但不更换 voice ID；确需更换时新增 profile 版本，旧行不删除。
- 同一 voice ID 不代表两个角色是同一人物；人物身份仍由每课教材和角色 Bible 决定。
- 只记录公开模型/voice 配置，不写 API key、账号信息或其它凭据。
