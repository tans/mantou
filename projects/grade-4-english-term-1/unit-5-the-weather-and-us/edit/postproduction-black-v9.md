# Unit 5 黑底后期 v9

用户要求：黑色后期背景。采用纯黑画布、深灰字幕卡、柔和浅色文字，减少原白底的大面积亮区。标题、字幕、片头、片尾一起改色；动画颜色、人物、配音、语速和字幕内容沿用 v7。当前交付为完整导出预览，人工全片听检/用户验收仍由 Issue #16 跟踪。

## 文件和关系

| 输出 | 实测时长 | 内容 |
| --- | --- | --- |
| `renders/unit-5-the-weather-and-us-spoken-bookends-black-v9.mp4` | 50.083333秒 | 1080×1920/24fps，中文童声片头片尾，正文1.2倍保音高 |
| `renders/unit-5-the-weather-and-us-vertical-bilingual-black-v9.mp4` | 77.562秒 | 1080×1920/24fps，普通语速，18条双语字幕 |
| `renders/unit-5-the-weather-and-us-master-black-v9.mp4` | 约77.58秒封装；视频/音频流实长见QA | 1280×720，无烧录字幕，只将旧补边改黑，音轨直接复制 |

每个输出旁的 JSON 记录参数与输出 SHA。v7 白底和原始动画/配音保持不变；本次不调用TTS或视频服务。

## 补边处理

`black-matte-v9.json` 从 v7 每镜头来源尺寸、裁切和时间轴计算补边区域，保存完整 FFmpeg 命令与源SHA。前八镜原图512×320，合成后为1152×720，左右各64像素补黑。后两镜已在v7按复核裁去底部44像素；缩放后1280×690，YUV420的pad实际向偶数坐标对齐，因此补边是上14、下16像素。只覆盖这些已知区域，保留动画内的眼白、雪景、服装和书本等白色。

首次黑底 v8 误按15/15补边，留下1像素白线并覆盖首行画面，故拒用；v9按源帧实测修正。v8中间稿与QA保留用于追溯，采用v9。shot-09样本61.67秒的第704行由白色255改为黑色0，第14行仍为动画颜色，见QA记录。

## 验证

- 黑底母版、普通竖屏、栏目包装版均完整解码通过，FFmpeg错误日志为空；H.264/AAC流及尺寸/时长见 `export-qa-black-v9.json`。
- 三个输出分别与对应v7输出解码为PCM，SHA-256逐一完全相同，证明本次没有改变语音或其采样位置。栏目版仍50.083333秒，普通版仍77.562秒。
- 包装版完整SRT和18条正文SRT与v7逐字节相同；片头片尾profile、字幕字号、标题、静音裁剪时间点和正文1.2倍速度相同。pacing对象的文件名随版本变化，实际时间点和SRT不变。
- 已目视检查0.7、4、16、24、36、44.5、47.5、50秒代表帧；浅色英中字幕清晰，长句换行留在卡片内，片尾保持至最后一帧。拼图为 `storyboards/black-review-v9.jpg`。
- 50.083333秒栏目版和77.562秒普通语速版均在BrowserOS Neo以1倍播放到ended，0丢帧，状态另存 `browser-playback-black-v9.json`；静音播放与抽帧不代表人工全片听检。原v7已做的ASR可由音频一致性沿用，本次没有重复声称新增ASR或听检完成。

## 复现与后续制作

参数化配方为 `postproduction-black-v9.json`；从仓库根目录执行其中的命令，重新生成时使用未占用的版本名。黑底母版先按 `black-matte-v9.json` 的命令生成，再执行竖屏合成。

```bash
python3 scripts/compose_vertical_lesson.py --input projects/grade-4-english-term-1/unit-5-the-weather-and-us/renders/unit-5-the-weather-and-us-master-black-v9.mp4 --srt projects/grade-4-english-term-1/unit-5-the-weather-and-us/edit/subtitles-bilingual-v7.srt --grade '小学英语 · 四年级上册' --unit 'Unit 5' --title 'The weather and us' --lesson 'Weather & activities · 单元核心' --preset-version 2 --theme black --output projects/grade-4-english-term-1/unit-5-the-weather-and-us/renders/unit-5-the-weather-and-us-vertical-bilingual-black-v9.mp4
```

```bash
python3 scripts/compose_vertical_lesson.py --input projects/grade-4-english-term-1/unit-5-the-weather-and-us/renders/unit-5-the-weather-and-us-master-black-v9.mp4 --srt projects/grade-4-english-term-1/unit-5-the-weather-and-us/edit/subtitles-bilingual-v7.srt --grade '小学英语 · 四年级上册' --unit 'Unit 5' --title 'The weather and us' --lesson 'Weather & activities · 单元核心' --preset-version 2 --theme black --tighten-pauses --packaging-profile assets/branding/primary-english-child-zh-v1/profile.json --output projects/grade-4-english-term-1/unit-5-the-weather-and-us/renders/unit-5-the-weather-and-us-spoken-bookends-black-v9.mp4
```

新课按项目技能显式使用 `--theme black --preset-version 2`，配置写入 `"background_color": "black"`，从横屏合成阶段得到黑色补边；历史白底可用 `--theme white` 复现。布局继续沿用既有v2，不重做角色和教材镜头。黑底后期由 Issue #17 跟踪；人工听检和用户验收保留在 Issue #16。
