# 人教版 PEP 二年级上册 Unit 2 “A great picture” Fun Time

课次制作记录，依照 [教材动画生产标准](../../grade-4-english-term-1/PRODUCTION_STANDARD.md) 按流程逐步推进。本目录只收录本课制作文件；目前通过公开页面扫描核对了教材第 16–17 页，尚未归档本地教材 PDF。

GitHub 跟踪：[Issue #7](https://github.com/tans/mantou/issues/7)。

## 制作流程状态

| 步骤 | 状态 | 产物 / 结论 |
| --- | --- | --- |
| 1. 确定对话和旁白 | 进行中 | [`script/dialogue-v1.md`](script/dialogue-v1.md)。文本、顺序及主要对话人已对照第 16–17 页扫描；集体朗读形式待配套音频核实。 |
| 2. 确定角色 | 进行中 | [`characters/character-bible-v1.md`](characters/character-bible-v1.md)。外观依原页记录；教材未给角色姓名，台词 6–8 的说话方式待音频核实。 |
| 3. 生成 Storyboard | 已完成 | [`storyboards/storyboard-v1.md`](storyboards/storyboard-v1.md) 与五格概念图 [`storyboard-v1.png`](storyboards/storyboard-v1.png)。 |
| 4. 生成 TTS | 等待配置 | [`audio/manifest-v1.md`](audio/manifest-v1.md)；5 条已核实对白的输入已放入 [`script/tts-input/`](script/tts-input/)，需在本机配置 `MIMO_API_KEY` 后才能合成。 |
| 5. 分镜生成 | 待制作 | 依赖 Storyboard 和角色设定。 |
| 6. 合并 | 待制作 | 依赖通过复核的镜头、配音与字幕。 |

## 课次简报

- 教材：人教版 PEP《英语（二年级上册）》（新教材，一年级起点预备级）；Unit 2 “A great picture”；Fun Time。
- 教材位置：Unit 2 Fun Time，教材第 16–17 页；已通过公开页面中的整页扫描确认。
- 当前来源：人民教育出版社新教材简介用于确认教材体系；Sohu 文章中的教材页扫描用于核对内容、页码和角色画面；配套课文转录用于交叉检查台词。Sohu 扫描不是官方教材分发渠道，本地尚未归档原 PDF。
- 教学主题：发挥创造力，以手掌印画完成一幅画（教材第 16–17 页）。
- 当前制作范围：脚本和角色设定已落盘，分镜概念图已生成；按流程继续完成配音、镜头和成片。

## 来源核对

| 素材 | 路径 / 页码 | 用途 | 状态 |
| --- | --- | --- | --- |
| 人教版 PEP 新教材简介 | [pep.com.cn](https://www.pep.com.cn/xw/zt/hd/12/xjcjs/xx/202409/t20240920_1995564.html) | 确认 PEP 一、二年级预备级教材定位 | 已核对 |
| FreePEP 电子课本清单 | [piclist.md](https://github.com/siknet/FreePEP/blob/main/piclist.md) | 核对是否收录本册教材 | 已核对；清单未列二年级英语，无法从此处取得本册原页 |
| Unit 2 教材第 16–17 页扫描 | [Sohu 电子课本页面](https://www.sohu.com/a/1035154855_122740674) | 核对 Fun Time 原文、页码、角色和画面 | 已浏览核对；未下载或归档教材 PDF |
| Unit 2 配套课文转录 | [51jiaoxi.com](https://yyld.51jiaoxi.com/ershang/rjbp_danyuan02.html) | 提取 Fun Time 台词初稿 | 已与页面扫描交叉检查 |

## 当前交付

- 脚本 v1 和角色 Bible v1 已落盘；台词 6–8 的朗读/说话方式待核教材音频。
- Storyboard v1 镜头方案和五格概念图已落盘；line-006–008 的朗读分配仍需教材音频确认。
- 已准备 5 条已核实对白的 TTS 输入；因本地未配置 `MIMO_API_KEY`，尚未调用合成服务或生成 WAV。line-006–008 的朗读分配仍需教材音频确认。
- 本阶段未生成视频；后续产物按流程依赖核实结果。
