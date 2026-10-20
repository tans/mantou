# 馒头工作室

教科书教学视频制作工程。当前起步项目：人教版 PEP 小学英语四年级上册，Unit 1 “Helping at home” 动画。

## 素材目录

| 分类 | 文件 | 用途 |
| --- | --- | --- |
| 角色图 | `assets/characters/character-redesign-concept.png` | 友谊班级角色重塑概念海报，作为角色视觉参考。海报列有 Wu Binbin、Amy、Mike、Sarah、Chen Jie、Zhang Peng、John、Zoom、Zip。 |
| 教科书 | `assets/textbook/pep-grade-4-volume-1.pdf` | 英语（PEP）（三年级起点）四年级上册，核对教材内容的来源文件。 |
| 分镜图 | `assets/storyboards/unit-1-helping-at-home-storyboard.png` | Unit 1 “Helping at home” A “Let’s talk” 家庭帮忙场景参考。图面标题标注“共16镜头”，可见分镜格为12格；镜头总数需在正式制作前确认。 |

## 教材下载来源

FreePEP 的[人教版小学电子课本汇总清单](https://github.com/siknet/FreePEP/blob/main/piclist.md)列有“英语（PEP）（三年级起点）四年级上册”（四年级条目）。对应 PDF 下载地址：<https://p.20190723.xyz/file/r2%3Ar2_1789021515658_ew6t80.pdf>。该直链本次访问超时，后续下载时需确认链接仍可用；当前归档副本为 `assets/textbook/pep-grade-4-volume-1.pdf`。

## 当前制作范围

第一支动画暂定为四年级上册 Unit 1 “Helping at home”。制作文件预留在 `projects/grade-4-english-term-1/unit-1-helping-at-home/`。归档图片及教材是原始参考素材，具体制作约束见 [`AGENTS.md`](AGENTS.md)。

## 视频生成

项目视频生成脚本支持 xiaoguai MiniMax H3 和 minixm/AIserver。复制 [`.env.example`](.env.example) 为本地 `.env` 并填入供应商配置后，运行 `python3 scripts/generate_video.py --help` 查看参数；调用会创建真实生成任务，供应商可能按时长计费。项目级流程见 [video-generation 技能](.agents/skills/video-generation/SKILL.md)。

跨课次生产清单见 [教材动画生产标准](projects/grade-4-english-term-1/PRODUCTION_STANDARD.md) 和 [课次记录模板](projects/grade-4-english-term-1/LESSON_TEMPLATE.md)。
