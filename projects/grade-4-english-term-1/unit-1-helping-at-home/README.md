# Unit 1 问候镜头

第一段动画草稿：早晨，Wu Binbin 在家向妈妈打招呼。对白和具体镜头仍需按教材原文核对。该课 Storyboard 参考文件保存在本目录：[`unit-1-helping-at-home-storyboard.png`](unit-1-helping-at-home-storyboard.png)。

## 当前最佳画面草稿（仅供视觉比较，非批准成片镜头）

- 推荐查看：[`renders/unit-1-helping-at-home-greeting-1280x768-h3-20step-5s.mp4`](renders/unit-1-helping-at-home-greeting-1280x768-h3-20step-5s.mp4)
- 服务任务：`job_e78c35dfaf7c4eb098c16d0021561559`
- 模型与任务：MiniMax H3 标准型，`text_to_video`，1280×768，20 steps，无 LoRA，seed `20261020`
- 文件信息：H.264/AAC，1280×768，5.175 秒，3,814,478 bytes
- SHA-256：`902f6a1cfad10b1fa702f7bd712a6f4f664e43653c94bf2c0f325646659a87d7`
- 服务报告：124 帧；conditioning 42.19 秒、DiT 484.09 秒、decode 58.47 秒；峰值显存 13,094 MiB。
- 视觉检查：男孩和妈妈同时入镜，动作、场景和问候关系可读，较原 512×320 稿明显清楚。细节仍有柔化，定位为分镜草稿，不作为最终成片。

## 可复用提示词

- 当前镜头基线提示词：[unit-1-helping-at-home-greeting-v1.txt](prompts/unit-1-helping-at-home-greeting-v1.txt)。它从最佳 minixm H3 文生视频任务的原始请求中恢复，保存为纯文本；无参考图。
- 后续运行使用 `--prompt-file` 指向该文件。改写提示词时保留 v1 并递增版本号。
- 跨课次通用制作流程与质量量表：[教材动画生产标准](../../PRODUCTION_STANDARD.md)。

## TTS 配音样稿

- 文件：[unit-1-helping-at-home-greeting-mimo-v2.5-tts-mia-v1.wav](renders/unit-1-helping-at-home-greeting-mimo-v2.5-tts-mia-v1.wav)
- 模型/音色：Xiaomi MiMo `mimo-v2.5-tts` / `Mia`；明亮、温暖、清晰的少儿英语语气，两句之间短停顿。
- 音频：3.84 秒，24 kHz，单声道，PCM 16-bit；SHA-256：`1bf2b128aeb73e71f9a3df17397777915e1a1b7bdaba2cfcad3a3e8b508f1b6f`
- 来源状态：该对白尚未逐字核对到教材页码；音频仅为技术样稿，不得作为正式配音或合并进成片。先将教材行文核实并登记到 `script/dialogue-v1.md`，再为可核实台词重生成。
- 状态：脚本来源核对进行中；TTS 样稿仍需人工试听发音与角色适配。

## 对话与旁白脚本表

以下仅登记旧 TTS 样稿使用过的文字，不代表教材原文。先查证并把每句台词的页面出处、文本及状态写入脚本文件；不等待例行确认。没有核实的内容不送入 TTS 或依赖它的镜头生成。

| 行号 | 说话人（旧样稿假设） | 对话/旁白文字 | 教材页码/位置 | 原文/改编 | 状态 |
| --- | --- | --- | --- | --- | --- |
| line-001 | Wu Binbin（待核实） | Hi, Mum! | 待核实 | 待核实 | UNRESOLVED |
| line-002 | 妈妈（待核实） | Hi, Wu Binbin! | 待核实 | 待核实 | UNRESOLVED |

## 画质对照记录

| 方案 | 文件 | 结果 |
| --- | --- | --- |
| 旧默认 T2V | `renders/unit-1-helping-at-home-greeting-5s.mp4` | 512×320，画面偏糊。 |
| Fast T2V 高分辨率 | `renders/unit-1-helping-at-home-greeting-864x480-t2v-5s.mp4` | 864×480，较旧默认改善，但细节仍软。 |
| 标准 H3 Turbo 8 steps | `renders/unit-1-helping-at-home-greeting-1280x768-h3-t2v-5s.mp4` | 1280×768，5.175 秒，峰值显存 13,098 MiB；构图可读，细节仍偏软。 |
| 标准 H3 参考生成 | `renders/unit-1-helping-at-home-greeting-reference-864x480-5s.mp4` | 864×480，完整角色参考有效，但角色画面偏近、母亲未稳定入镜，未选作推荐稿。 |
| 标准 H3 20 steps | `renders/unit-1-helping-at-home-greeting-1280x768-h3-20step-5s.mp4` | 当前最佳。两位角色及场景关系更清楚，仍需后续镜头级修整。 |
| xiaoguai MiniMax H3 768p | `renders/unit-1-helping-at-home-greeting-xiaoguai-minimax-h3-768p-5s-v1.mp4` | 使用相同提示词、5 秒、16:9、无参考图；实际 1376×768、5.167 秒。画面比 minixm 清楚、细节更利落；开场男孩贴近左侧边缘，构图需再收敛。 |

### 供应商对照记录

- xiaoguai 任务：`xg_P2Reh18PeHObNX9cMZIvf`；旁边 JSON 记录任务状态、提示词 SHA-256、参数和输出路径。
- 对比对象是 minixm 任务 `job_e78c35dfaf7c4eb098c16d0021561559`。两次提示词、无参考图和 24fps 一致；时长均约 5.17 秒。minixm 输出 1280×768、20 steps、seed `20261020`；xiaoguai 输出 1376×768，steps 和 seed 无法在其接口锁定。因此这是同内容的供应商对比，不能解释成所有参数完全相同的实验。
- 人工抽查开场、中段、结尾帧：xiaoguai 版本人物边缘和衣物更清楚，男孩从左侧入画的动作可读；开场边缘留白不足。minixm 版本整体更柔、更糊，但母子都稳定留在画面内。此判断是本次样片的初步观感，正式定稿仍需逐帧看片和对照教材对白。
- 下一轮若要更公平地区分供应商质量，应先统一输出宽高与时长；若接口无法锁定 steps/seed，报告中继续注明不可控项。需要角色更稳定时，再开启图生视频对比，并让所有供应商使用同一张参考图。

尝试将 1280×768 稿交给 SeedVR2 放大至 2048×1152 时，作业触发服务器主机内存 OOM，AIserver 被 systemd 自动重启。该超分路线暂不用于默认流程，也没有将失败作业标为成功。

## 服务默认质量档

服务器 H3 服务此前在调用方未指定宽高时使用 512×320，容易产出不适合成片预览的低分辨率视频。现将 `text_to_video` 默认画布调整为 1280×768（服务允许的最大面积，983,040 像素），保留 `ref2av` 的 512×320 默认画布以控制其更高的参考编码显存；调用方显式传入尺寸时行为不变。默认步数仍为 21（实际 infer steps 为 steps + 1）。

服务部署目录没有 Git 元数据，远端源文件差异、API 文档差异和修改前备份记录在根目录 [`operations/patches/aiserver-video-quality-default.patch`](../../../../operations/patches/aiserver-video-quality-default.patch)。修改前备份为 `/home/minixm/AIserver/backups/minimax-pre-t2v-quality-default-20261020.py` 与 `/home/minixm/AIserver/backups/API-pre-t2v-quality-default-20261020.md`；修改后已重启服务并确认 `/health` 返回 HTTP 200。

## 参考资产

- 完整角色参考裁图：[`references/wu-binbin-full-body-reference.png`](references/wu-binbin-full-body-reference.png)
- 旧的错误角色裁图（只剩下半身和靴子，保留作问题记录）：[`references/wu-binbin-character-reference.png`](references/wu-binbin-character-reference.png)
- 原角色海报：[`assets/characters/character-redesign-concept.png`](../../../../assets/characters/character-redesign-concept.png)
- 分镜图：[`unit-1-helping-at-home-storyboard.png`](unit-1-helping-at-home-storyboard.png)
- 教材：[`assets/textbook/pep-grade-4-volume-1.pdf`](../../../../assets/textbook/pep-grade-4-volume-1.pdf)

## 此前服务修复

先前的参考生成失败由两处配置错误引起：

1. `ref2av` 错误使用 TP6；参考分区有 56 个 heads，按服务文档和已有成功配置应使用 TP4。
2. Fast 参考任务错误复用普通文生视频权重路径。参考任务需要 `data/h3ref_deploy_20261020/model_root` 作为模型根目录，并将 `data/h3ref_deploy_20261020/ref_fp8_tp4` 单独传为 FP8 checkpoint。

修复后 `/v1/models` 报告标准和 Fast 型号的 `ref2av` TP 为 4。服务端文件及 `OPERATIONS.md` 的对应差异记录在根目录 [`operations/patches/aiserver-ref2av-tp4.patch`](../../../../operations/patches/aiserver-ref2av-tp4.patch)。服务目录无 Git；此前修改前备份位于 `/home/minixm/AIserver/backups/pre-ref2av-tp4-20261020-154105/` 与 `/home/minixm/AIserver/backups/pre-ref2av-model-root-20261020-154527/`。

## AIserver 8189 同参数复跑

- 使用独立项目技能 [AIserver 8189 视频生成](../../../../.agents/skills/aiserver-8189-video/SKILL.md)，复用相同提示词、`text_to_video`、1280×768、5.1666667 秒、20 steps、seed `20261020`，无参考图。
- 任务 `job_b6084401f1b64387ac6dc9227f6578e8` 已被 `http://minixm.minapp.xin:8189` 接受；截至 2026-10-20 21:57（北京时间），提交超过一小时后 API 仍返回 `running`，`backend_id` 和结果为空，`updated_at` 未离开提交时间。恢复轮询 30 分钟后超时；MP4 尚未生成，因此不纳入画质对照。
- 同时观察到 `/health` 返回 200，但 `/ready` 仅报告 LightX2V 模型；H3 在 `/v1/models` 中标记为 `experimental`。轮询期间遇到 HTTP 502，已通过原任务 ID 重试查询，没有重复提交。待任务进入终态后补记成功文件或服务端错误。

## 教材对白依据

参考图动画当前用到的 `Hi, Mum!` / `Hi, Wu Binbin!` 对白已按 Unit 1 场景暂用。开始最终配音前仍应对照教材页核对英文标点和出场角色。
