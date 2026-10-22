# 换一课就能继续用的制作流程

这套入口在四年级上册 Unit 3 蜡笔小新版实际使用。它复用仓库现有 TTS、视频与竖屏脚本，只新增 `scripts/run_lesson.py` 做单课编排；不调度多课批次，不把素材生成等同于视听验收。

本课编排遵循 Ponytail 的复用原则：继续调用现有生成脚本，不新增供应商SDK、队列系统或测试代码。

## 下次给制作助手的一句话

> 沿用四年级 Unit 3 的流程，制作【年级/册次/单元/课时】，使用【蜡笔小新角色组/其它角色】，输出完整双语视频。先核对教材，把素材逐阶段落盘，复用固定声线和字幕版式。

年级、册次和单元足够定位时可直接制作；存在多个版本时先查已归档教材。用户指定新教材时归档原件，不能复制上一课的正文。

## 每课只改五类输入

| 输入 | 位置 | 需要修改的内容 |
| --- | --- | --- |
| 教材与范围 | `README.md`、`references/` | 出版社/册次/版本、单元和印刷/PDF页码、页图、来源等级、未决项 |
| 台词和翻译 | `script/dialogue-vN.md` | 稳定行 ID、说话人、英文、中文、页码、原文/改编状态、镜头、verified 状态 |
| 课程配置 | `lesson-vN.json` | 标题、voice profile、台词顺序、镜头映射、停顿、输出版本；文字必须和脚本表一致 |
| 角色与分镜 | `characters/`、`storyboards/`、`references/panel-*.png` | 同一角色组沿用外观、服装和英语声线；场景/动作按新课重做 |
| 镜头提示词 | `shots/shot-NN/prompt-vN.txt` | 动作、构图、连续性、静音与不生成文字要求 |

参考课：`projects/grade-4-english-term-1/unit-3-places-we-live-in-shinchan/`。每课保留自己的文件，不跨课覆盖。教材版次未核实但正文有证据时，记录未决范围；看不清的具体句子必须留为 UNRESOLVED，不能进入生成。

## 可执行顺序

以下以参考课为例；下次替换 `LESSON` 路径和 `vN`，先完整核实并保存新课脚本/配置。凭据仍只保存在忽略的 `.env` 或本机环境；不要把密钥放命令参数。

```bash
LESSON=projects/grade-4-english-term-1/unit-3-places-we-live-in-shinchan

# 1. 零费用校验：脚本文字/译文/角色/镜头/逐行输入一致，所有行已核实
python3 scripts/run_lesson.py plan --config "$LESSON/lesson-v6.json"

# 2. 逐行配音：先核对参数，再真实生成。最多并发三条；失败可按 --line 局部续做
python3 scripts/run_lesson.py tts --config "$LESSON/lesson-v6.json" --dry-run
python3 scripts/run_lesson.py tts --config "$LESSON/lesson-v6.json" --workers 3

# 3. 动画：先生成/检查参考图，音频生成后按实际长度申请 5–15 秒镜头
python3 scripts/run_lesson.py video --config "$LESSON/lesson-v3.json" --dry-run
python3 scripts/run_lesson.py video --config "$LESSON/lesson-v3.json" --shot shot-01
# 第一镜检查后继续其它镜头；不传 --shot 时逐镜顺序执行所有镜头
python3 scripts/run_lesson.py video --config "$LESSON/lesson-v3.json"

# 4. 零费用合成：供应商原片保留；自动派生静音片、配音混音、横屏母版、双语烧录版和 SRT
python3 scripts/run_lesson.py assemble --config "$LESSON/lesson-v6.json" --dry-run
python3 scripts/run_lesson.py assemble --config "$LESSON/lesson-v6.json"

# 5. 竖屏母版，使用项目固定大字双语版式；输入没有横屏字幕，避免双重字幕
python3 scripts/compose_vertical_lesson.py \
  --input "$LESSON/renders/unit-3-places-we-live-in-shinchan-master-v6.mp4" \
  --srt "$LESSON/edit/subtitles-bilingual-v6.srt" \
  --grade '小学英语 · 四年级上册' --unit 'Unit 3' \
  --title 'Places we live in' --lesson 'Community adventure · 单元核心' \
  --preset-version 2 \
  --output "$LESSON/renders/unit-3-shinchan-vertical-bilingual-v6.mp4"
```

`run_lesson.py video` 明确使用本项目已配置的 xiaoguai MiniMax H3（768p 由课配置指定）。需要其它供应商时直接按对应技能调用 `generate_video.py` 并记录配置；此 runner 不声称自动适配所有供应商。`tts`/`video` 是真实服务调用，`plan`/`assemble` 只做本地处理。

## 断点与返修

- TTS 已有 WAV 且输入文字哈希、voice、style、model 一致时复用。未知来源或输入变化则停止，使用新版本重新生成，不覆盖旧音频。
- 视频发起前把输入哈希写入每镜头 `task-vN.json`；收到任务 ID 立即保存。超时继续同一个 ID；提交结果未知时停止，先查供应商任务列表，禁止盲目重复计费。
- 所有时长按最终采用 WAV 计算，音频不加速不截断。源视频不足时仅延长末帧并在每镜头 assembly JSON 写出秒数；动作要求较高时改镜头版本重新生成。
- 修改一句英文或 voice：只重新生成该句 WAV；修改一个镜头：只重新生成该镜头；修改译文/字号：复用全部音视频，只重新导出字幕版。
- 修订后保留旧稿并创建新配置版本。配置中的 `version` 决定 script/tts/audio/task/输出后缀；镜头 `prompt/reference/output` 使用显式路径，未变素材可引用旧版。脚本需匹配新版本；每行可用 `input`、`audio` 显式引用未变的旧输入/WAV。runner 校验文字、声音参数和输出SHA，不改原件。
- 合成拒绝覆盖最终成片；中断恢复已导出的中间文件时，核对后为新导出版本留独立路径。runner 不计算复杂失效图，多课依赖仍按 `BATCH_PRODUCTION_GUIDE.md` 管理。

## 一课交付的完成标准

1. 教材页图可检查，脚本逐句有证据；改编与补充明确。
2. 角色外观、固定 voice profile、分镜和 prompt 可复用；真实任务 ID 和原始素材都保留。
3. 每句配音、每镜头及完整成片可解码；记录实际时长、音视频流、哈希、峰值和静音处理。
4. 字幕按最终 WAV 对轴，英文逐字一致、中文忠实、每轮说话人分开。主交付烧录字幕，SRT 可编辑。
5. 逐镜检查角色/动作/物件，完整播放并逐句听检；未完成人工听检时标“完整导出预览，待视听验收”。
6. 课次 README、根索引、Issue 与 Git 状态一致。main 提交并推送；缺项写清恢复条件，不把未验收步骤写成完成。

本次默认使用内置 image_gen 生成分镜基线图，保留完整提示词与生成信息；不把模型图中的文字当教材内容。蜡笔小新英语角色配置见 `assets/characters/voice-library.md`，外观见参考课的角色 Bible。

## 长片字幕合成

固定竖屏版式保持不变。合成器把标题/字幕卡预先排成按时间变化的背景流，再叠加一条动画视频，避免几十条全尺寸字幕层同时参与每帧计算；时间边界按24fps独立量化，误差不累计。

## 本次实例的版本关系

v1：初始脚本和49条配音；v2：按实测时长拆为20镜头；v3：三张官方角色参考与正式视频任务；v4：仅返修ASR发现疑点的12条配音并重新合成。视频在途任务沿用v3配置和ID，合成采用v4配置；镜头仍可引用v3原片。新课没有返修时只需一套版本，不必预先创建这四版。

`character_references` 是课程级角色图列表，`shot.reference` 是可选场景图；正式镜头同时传入前者与后者，记录全部输入SHA。角色图来源明确时不依赖模型生图才能启动；概念分镜与实际动画接触表分开记录。

`lines[].input`、`lines[].audio` 可显式引用已核验旧资产；`lines[].style` 可记录局部返修朗读提示，同时保留角色 voice ID。可用本地ASR反向转写发现明显加词/漏词/同音词疑点，但不能以ASR代替完整听检或强行按ASR改教材正文。

本课最终候选采用v6：v5统一旁白Mia，v6将两个有识别歧义的孤立短语改为明确标注的完整教学例句。原文对话、改编、补充仍分开，不能为了ASR分数静默改教材。所有历史版本只是本次质量修订记录，新课不需要预设六个版本。
