# 四年级上册 Unit 3 · Places we live in · 蜡笔小新版

2026-10-22 已完整导出：3分12.25秒、20个剪辑镜头、49段英语配音、英中双语字幕。当前为**完整导出预览，待人工全片听检与用户验收**。[Issue #12](https://github.com/tans/mantou/issues/12)保留跟踪验收。

## 直接观看与编辑

| 用途 | 当前文件 |
| --- | --- |
| 手机竖屏观看，1080×1920，英中大字幕 | [竖屏双语 v9](renders/unit-3-shinchan-vertical-bilingual-v9.mp4) |
| 课堂/电脑横屏观看，1280×720，双语烧录 | [横屏双语 v8](renders/unit-3-places-we-live-in-shinchan-bilingual-burned-v8.mp4) |
| 再剪辑的无字幕母版（含最终英语配音） | [横屏母版 v8](renders/unit-3-places-we-live-in-shinchan-master-v8.mp4) |
| 修改文字/字幕 | [逐句脚本 v8](script/dialogue-v8.md)、[双语SRT](edit/subtitles-bilingual-v8.srt)、[逐句时间轴](edit/timeline-v8.json) |
| 修改编排/声音/素材选择 | [课程配置 v8](lesson-v8.json)、[角色设定 v4](characters/character-bible-v4.md) |
| 查看镜头 | [Storyboard v4](storyboards/storyboard-v4.md)、[最终20镜头总览](storyboards/storyboard-final-v8.jpg) |
| 查看检查证据 | [交付检查记录](edit/qa-v9.md)、[机器检查JSON](edit/qa-v9.json)、[音频逐词复核](audio/asr-review-v4.json) |
| 下次制作其它课程 | [换课制作指南](../../LESSON_QUICKSTART.md) |

竖屏v9沿用横屏v8的画面/配音/字幕时间轴，仅修正中文换行时句号单独成行的问题。旧版保留，不覆盖源稿。

## 教材与本片范围

- 人民教育出版社《英语（PEP）（三年级起点）四年级上册》，本地归档 `assets/textbook/pep-grade-4-volume-1.pdf`，共96页。索引来自第三方FreePEP，扫描件不描述为官方原件。
- Unit 3 **Places we live in**，印刷p.26–37 / PDF第32–43页。主片覆盖p.28–32的A/B对话、地点词汇、社区活动、ck词汇/歌谣，以及p.34–35的社区介绍项目与复习。
- 完整指有开场、教学主线、复习和结尾的单支教学短片；不含歌曲、听力答案、p.33博物馆全文、p.36–37成都拓展阅读，不称为全单元逐页朗读。
- 查找路径：根README → FreePEP清单（已复查目标册）→ 本地PDF → `references/unit3-32.png`至`unit3-43.png`逐页目视核对；版权页在`references/textbook-copyright.png`，源文件哈希在references内。
- 具体版次/出版年份：**UNRESOLVED**，版权页未载。不用PDF创建时间冒充出版年份。册次、单元、页码和所用正文已核实；换其它教材版本须重查。原配套音频未归档，本片采用独立英语TTS。
- 教材人物替换为小新/风间/妮妮，英文原对话与补充例句逐行标注。line-016公交站/厕所、line-031看医生使用有依据的完整补充例句，非教材逐字原文。

## 当前阶段状态

| 阶段 | 实际状态 | 证据 |
| --- | --- | --- |
| 教材/脚本 | 所用49句已核实并标注原文/改编 | dialogue-v8、页图 |
| 角色与声音 | 小新Milo、风间Dean、妮妮Mia；教学旁白Mia | character-bible-v4、全局voice-library |
| 分镜 | 20镜头文字、提示词和最终实拍帧已归档 | storyboard-v4 / final-v8.jpg |
| TTS | 49条最终采用音频，共153.92秒；无削波；49/49机器转写逐词匹配 | manifest-selected-v6 / probe / asr-review-v4 |
| 动画 | 20个计划源镜头已下载、探测并检查首中尾帧；另有否决初样与医院返修 | task-v3、probe-selected-v8、renders/manifest-v1 |
| 字幕/剪辑 | 49条字幕对轴；原供应商音轨去除，混入TTS；横屏/竖屏完整导出 | assembly-v8、timeline-v8、导出sidecar |
| 媒体/画面检查 | 全文件解码、时间戳、字幕对应、代表帧/切换帧检查已记录 | qa-v9 |
| 人工全片视听/用户验收 | **待完成**；机器复核不能证明完整听感/逐字口型同步 | Issue #12保持开放 |

声音为合成英语角色声音，不是动画原演员。生成动画按独立TTS后期配音，未做逐字音素口型匹配。角色参考使用电视朝日官方角色图，见`assets/characters/shinchan-official/README.md`。

## 已处理的画面问题

内置分镜生图两次因网络错误失败。用户选择“仅重试内置生图”，未切换图片API；已归档官方角色原图作为视频参考，并从实际生成视频提取Storyboard图。

文本无参考初样中风间成人化，已否决。正式镜头同时传三张官方图并检查人物比例/衣着。shot-06原画面把厕所和医疗十字混用，最终按公交/厕所、正确医院、游乐场三段重新剪辑；[修复配方](edit/repair-shot-06-v1.py)与静音衍生片保留来源。shot-12重生成了医院主体始终在场的版本。shot-08/17裁掉模型擅自生成的底部字幕，源片保留。

## 续做与局部修订

当前编辑配置是`lesson-v8.json`，脚本为`dialogue-v8.md`。原视频生成参数冻结在`lesson-v3.json`；医院补片在`hospital-shot-v4.json`，避免拿最终编辑配置重新发起已完成的生成。每行采用旧版WAV的路径已显式固定，旧音频/任务/素材不删除。

执行入口与真实生成/本地合成边界见[换课指南](../../LESSON_QUICKSTART.md)。改一句只重配该行；改一镜只重做该镜；改翻译/字号只重导出字幕版。最终文件拒绝覆盖，修订时递增版本。

| 历史阶段 | 作用 |
| --- | --- |
| v1–v2 | 初始49句、实测音频后从16拆成20镜头 |
| v3 | 官方角色参考与正式20镜头请求冻结 |
| v4–v6 | 配音逐词返修、统一教学旁白、两处补充例句明确标注 |
| v7–v8 | 教学物件修复、裁去源片字幕、统一响度、完成横屏与时间轴 |
| 竖屏v9 | 中文句尾标点随前字换行，其余沿用v8 |

已完成生产与机器检查；人工全片听检和用户验收是剩余工作，不把文件成功导出等同于已验收。
