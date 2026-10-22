# 换课制作指南

下次直接说：

> 沿用四年级 Unit 3 的制作流程，做【年级】【上/下册】【Unit/课时】，继续使用【蜡笔小新角色组/其它角色】，给我完整双语视频。

已有教材、角色和版式可复用时，不用重新讨论常规流程。制作助手先核对教材，再逐阶段把文件落盘，处理真实阻塞，最后交付可播放视频和可编辑源文件。单课实际示例见 `grade-4-english-term-1/unit-3-places-we-live-in-shinchan/README.md`。

## 六步制作

| 步骤 | 做什么 | 必须留下什么 | 通过条件 |
| --- | --- | --- | --- |
| 1. 核对教材与脚本 | 确定出版社、版次/册次、单元、页码、范围；逐句写正文与翻译，标明改编/补充 | 教材页图、`script/dialogue-vN.md`、`script/tts-input/` | 每句有证据；UNRESOLVED 不进入生成 |
| 2. 固定角色和分镜 | 选角色外观、服装、voice profile、场景、动作；一个画面突出一个教学地点/物件 | 角色 Bible、角色参考、Storyboard、每镜头 prompt | 角色比例/衣着统一，分镜覆盖全部台词 |
| 3. 配音与核对 | 逐行生成，检查格式/音量，反向转写定位加词/漏词，再试听与局部返修 | WAV、逐行元数据、音频 manifest、ASR 报告 | 音频文字收敛；不加速/截断对白适配镜头 |
| 4. 动画镜头 | 按合格配音实测长度选5–15秒；先检查代表镜头，再继续；持久化任务ID | 源 MP4、task JSON、prompt/参考SHA、日志 | 角色/物件/动作可用；超时按同ID恢复 |
| 5. 字幕与合成 | 对轴英中SRT、去供应商音轨、混入TTS、按需二次构图、统一响度和输出规格 | 静音衍生片、SRT、剪辑时间轴、横屏母版、双语烧录版、竖屏版 | 49句之类的实际行数一一对应；无供应商对白/字幕误混 |
| 6. 检查与交付 | 完整文件解码、首中尾/切换帧检查、全片播放听检；记录边界 | SHA、媒体探测、视听记录、课次README和素材索引 | 已生成、机器检查、人工听检、用户验收分开记；main提交推送 |

本项目用 `scripts/run_lesson.py` 做单课编排，继续调用已有 `generate_tts.py`、`generate_video.py` 和 `compose_vertical_lesson.py`。没有多课队列服务；多课任务按 `BATCH_PRODUCTION_GUIDE.md` 另行建立清单与预算。不新增测试代码。

## 换课时只改五类输入

1. `README.md` / `references/`：教材来源、页码、范围和证据。
2. `script/dialogue-vN.md`：稳定行ID、角色、英文、中文、原文/改编状态和镜头。
3. `lesson-vN.json`：标题、声音、台词顺序、停顿、镜头与素材路径。英文/译文/说话人/镜头必须匹配脚本，逐行输入必须一致。
4. `characters/` / `storyboards/`：沿用已固定角色组，重做新课场景和动作。
5. `shots/shot-NN/prompt-vN.txt`：一个镜头一个动作重点，明确连续性、静音和避免文字的要求。

蜡笔小新参考原图在 `assets/characters/shinchan-official/`；英语 voice ID 在 `assets/characters/voice-library.md`。教学旁白使用 `teacher-en-mia-clarity-v1`，不沿用被否决的 Chloe 候选。角色声音是合成英语，不声称原动画演员配音。

## 单课执行命令

新课通常从 v1 开始；下例的课程目录替换成新课。已有课次续做时，使用课次 README 指定的实际配置，保留旧版。

```bash
LESSON=projects/<教材与年级>/<课次>
CONFIG="$LESSON/lesson-v1.json"

# 零费用：校验教材脚本、角色映射、逐行输入与镜头覆盖
python3 scripts/run_lesson.py plan --config "$CONFIG"

# TTS：先查看参数，再真实生成；最多并发三条
python3 scripts/run_lesson.py tts --config "$CONFIG" --dry-run
python3 scripts/run_lesson.py tts --config "$CONFIG" --workers 3

# 完成音频复核/疑点返修后，再固定视频秒数
python3 scripts/run_lesson.py video --config "$CONFIG" --dry-run
python3 scripts/run_lesson.py video --config "$CONFIG" --shot shot-01
# 首镜检查后继续；不传--shot时顺序执行全部镜头
python3 scripts/run_lesson.py video --config "$CONFIG"

# 本地合成：保留源片，派生静音片、混音、SRT、横屏母版和双语烧录版
python3 scripts/run_lesson.py assemble --config "$CONFIG" --dry-run
python3 scripts/run_lesson.py assemble --config "$CONFIG"
```

`tts` / `video` 会调用真实供应商；`plan` / `assemble` 不发起生成请求。视频入口当前明确使用 xiaoguai MiniMax H3，时长按WAV实测，分辨率来自课程配置。其它供应商按对应专用技能直接调用 `generate_video.py`，不声称本runner支持全部适配。密钥只放本机忽略的 `.env` 或环境。

本机证书链有问题时，为命令设置 `SSL_CERT_FILE` 为 `python3 -m certifi` 给出的文件；保持TLS校验。

## 本地语音反向核对

首次需要独立环境与开源模型下载，随后在本机运行；不依赖语音云服务。已实际使用的PyAV版本如下，避免本次遇到的 metadata_errors 参数不兼容。

```bash
uv venv /tmp/mantou-asr
uv pip install --python /tmp/mantou-asr/bin/python faster-whisper av==16.1.0
/tmp/mantou-asr/bin/python scripts/review_lesson_audio.py \
  --config "$CONFIG" --output "$LESSON/audio/asr-review-v1.json"
```

逐行输出转写、输入音频SHA和差异列表，支持重复 `--line line-001` 局部检查。大小写、标点、three/3、neighbours/neighbors等书写差异不算可听错误。ASR有误识别，报告是返修线索，不能代替完整听检；不要为了分数静默改教材原文。补充教学例句必须明确标注依据与改动。

## 手机竖屏版

使用无烧录字幕的横屏母版，避免双重字幕。保持项目固定 `vertical-bilingual-white-v2`：白底1080×1920、等比动画、上方标题、下方英中大字幕。

```bash
python3 scripts/compose_vertical_lesson.py \
  --input "$LESSON/renders/<lesson-id>-master-v1.mp4" \
  --srt "$LESSON/edit/subtitles-bilingual-v1.srt" \
  --grade '小学英语 · 四年级上册' --unit 'Unit 3' \
  --title 'Places we live in' --lesson 'Community adventure · 单元核心' \
  --preset-version 2 --output "$LESSON/renders/<lesson-id>-vertical-bilingual-v1.mp4"
```

长片字幕使用单条按时间变化的背景流，保持既有版式并避免几十层全尺寸字幕同时参与每帧计算。时间边界按24fps分别量化，不累积舍入误差；中英文混排使用可覆盖汉字的字体，中文句尾标点随前字换行，避免句号单独成行。

## 断点与局部返修

- 已有WAV必须输入文字SHA、voice、style、model和输出SHA吻合才复用；不是仅判断文件存在。
- 视频提交前记录输入指纹，收到任务ID立即落盘。连接/轮询超时按同ID恢复；提交结果未知且没有ID时停止，先查供应商任务列表，不盲目重提。
- 同镜头由本地文件锁拒绝并发。不同镜头可以并行，整课命令与逐镜命令互斥；状态文件不是本地进程是否存活的证明。
- 修改一句台词/voice，只重配受影响行；修改一个prompt/场景，只重生成该镜头；改译文/字号，只重导出字幕版；不重做未受影响素材。
- `lines[].input`、`lines[].audio`、`lines[].style` 可显式引用旧输入/音频或局部朗读配置。`character_references` 是课程角色图列表，`shots[].reference` 是可选场景图。
- 原始素材保留。模型生成了错误教学物件或多余字幕时，返修该镜头，或用合格素材做独立剪辑衍生片，记录源SHA、选段/裁切、顺序和原因。`crop_bottom` / `framing_reason` 只用于已检查镜头，不全片盲裁。
- 镜头过短时记录末帧延长；动作关键处应重生成。合成不加速/截断配音，最终按镜头做响度处理，目标-18 LUFS、真峰值-1.5dB、48kHz AAC；原WAV保持不变。
- 最终输出拒绝覆盖，修订时新增版本。本课曾迭代多个候选，详细关系在课次README；新课不用预建这些历史版本。

课次README是产物和验收状态索引，GitHub Issue跟踪尚未解决的工作。完整人工视听未完成时，交付称“完整导出预览，待验收”，并明确剩余检查。
