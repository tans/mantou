# Unit 5 约15秒三集制作与交付 v11

2026-10-25，按用户反馈将社媒产出改为每单元2–3集、每集约15秒，以冲突或猜题开场。采用v11；v10为本次第一轮候选，EP01发现既有TTS尾声后返修，两个版本与旧长片均保留。制作跟踪：[Issue #18](https://github.com/tans/mantou/issues/18)；完整人工听检和用户验收继续由[Issue #16](https://github.com/tans/mantou/issues/16)跟踪。

## 可播放文件

| 集 | 实测视频时长 | 开头、推进与答案 | 主视频 |
| --- | --- | --- | --- |
| EP01 打球不成又碰壁 | 15.292秒 | 雨天不能打球→提议图书馆→已经关门→去看电影；本集完整给出解法 | [MP4](../renders/unit-5-ep01-rainy-plans-black-v11.mp4) |
| EP02 有风就不能玩？ | 15.000秒 | 有风时选风筝还是雪人→英语揭晓→切到雪天再选择→归纳对应关系 | [MP4](../renders/unit-5-ep02-windy-snowy-black-v11.mp4) |
| EP03 想出门，先看天 | 15.458秒 | 雨天待在家→“换成晴天会怎样？”→运动玩耍→提问后给答案 | [MP4](../renders/unit-5-ep03-rainy-sunny-black-v11.mp4) |

三集为1080×1920、24fps、H.264/AAC，使用黑底v2和双语烧录字幕。首镜有2秒问题标题叠字，英语从约0.1秒开始；不单独播放栏目片头与关注片尾。EP01沿用既有1.2倍保音高语速；EP02/03为自然语速，问题卡各停留约1秒。无新TTS/视频供应商请求，无新增背景音乐，无平台提交。

![三集首帧](../storyboards/short-series-v11/three-openings.jpg)

## 教材与编辑边界

- 本地第三方扫描PDF，封面2024审定、人教版PEP四年级上册；版次/出版年/印次仍未核实。2026-10-25再次目视核对印刷p.51与p.55，对应PDF第57/61页；不把扫描件说成官方电子原件。详细来源和原文件SHA见`references/source-v1.md`。
- EP01采用原line-013–018，EP02采用line-007–010，EP03按line-011/012/005/006对照组织，共14条互不重复的教材选编台词。line-013沿用删除John姓名的改编，其余英语与v7核实稿一致、仅替换角色；中文沿用原项目翻译。
- 未选入标题朗读、单元核心问题、p.52北京天气问答，亦未覆盖全单元其它活动。p.51普通朗读不是原版旋律。
- 六张问题/答案卡及三个开场标题为本项目编辑提示，无语音，不冒充教材原句。EP03明确为雨天/晴天的情境对照，不宣称同一天立即变天。EP02雪景沿用原动画，原镜头小新略贴左边缘的限制保持记录。

## 文件与重建

- 剪辑清单：[short-series-v11.json](../short-series-v11.json)。无字幕源母版为黑底v9，逐句源时间轴和教材脚本为v7；原始动画、WAV、源母版未改。
- [逐集脚本](../script/dialogue-short-series-v11.md)、[剪辑分镜](../storyboards/storyboard-short-series-v11.md)、[声音清单](../audio/manifest-short-series-v11.md)。角色继续引用`characters/character-bible-v2.md`和全局voice library：小新Milo、风间Dean、妮妮Mia。
- 每集在`edit/short-series-v11/ep01..ep03/`保留`master.mp4`、`subtitles.srt`、`assembly.json`；后者记录原行号、说话人、输入/输出SHA、源区间、静音裁剪、实际速度、编辑卡和最终时间轴。每条竖屏视频旁保留布局JSON。
- [EP01 SRT](short-series-v11/ep01/subtitles.srt)、[EP02 SRT](short-series-v11/ep02/subtitles.srt)、[EP03 SRT](short-series-v11/ep03/subtitles.srt)。6/7/7个cue中，教材对白分别6/4/4条，其余为无声编辑卡。

```bash
python3 scripts/compose_short_series.py --config projects/grade-4-english-term-1/unit-5-the-weather-and-us/short-series-v11.json --dry-run
python3 scripts/compose_short_series.py --config projects/grade-4-english-term-1/unit-5-the-weather-and-us/short-series-v11.json
```

输出存在时拒绝覆盖，重新渲染需复制新版本清单并更换`id`与输出版本。局部制作可加`--episode ep01`。脚本复用现有竖屏合成器，不涉及供应商API；素材未变化的EP02/03与v10输出SHA完全相同。

## 返修与复核

v10整片ASR在EP01的line-014台词后识别出“Ha ha ha”。多模型分别检查v10整片、该句片段和原WAV，原WAV也有同样尾声；原句后静音区间为相对4.603–7.184秒，末尾另有声音。v11按源母版56.56秒收尾，保留完整park及约0.14秒缓冲，去掉后面的独立尾声。line-017在完整句子后也有2.617秒长停顿和短尾声，v11按源母版71.04秒收尾，保留film后的约0.19秒缓冲。原WAV、v10预览和机器筛查全部保留；不是重新配音，也不是把教材词句删短。

- 三个v11文件FFmpeg完整解码通过；格式/流/视频实长、逐句匹配、SRT有序无重叠且不超出视频、PCM峰值和样本见[媒体QA](short-series-v11/media-qa.json)。14条英语/中文与源脚本一致。三条AAC解码后均0削波样本，PCM峰值27444/27686/27489。
- 实际v11 MP4使用本机faster-whisper/small.en、CPU int8、beam5、无VAD反向转写；三集选定教材台词归一化词序全部匹配，OK/okay和标点作为书写差异。最后词idea/play/play都完整转写；[实际成片ASR](../audio/export-asr-short-series-v11.json)保留逐词时间戳。
- 从实际成片按帧号抽查首帧、开头、中间、所有编辑卡、末尾和最后视频帧，已目视检查文字/换行/字幕卡边距与人物内容。[EP01代表帧](../storyboards/short-series-v11/ep01-review.jpg)、[EP02代表帧](../storyboards/short-series-v11/ep02-review.jpg)、[EP03代表帧](../storyboards/short-series-v11/ep03-review.jpg)。图像源仍为原512×320动画，导出1080×1920不等于新增高清动画，独立TTS不保证逐词口型同步。
- 三集v11在BrowserOS Neo的原生video元素按1倍、静音播放到ended，0丢帧、无媒体错误；[浏览器证据](short-series-v11/browser-playback.json)。计数是浏览器累计显示帧，不作为文件帧数校验。
- **完整人工听检和用户验收：待完成。** 机器转写、解码、抽帧及静音播放不替代发音/自然度/音量/音画同步的完整听检；交付状态为预览。此次未发布，尚无新短集留存/流量结果，不宣称效果已经提高。

## 发布文案草稿

| 集 | 标题草稿 | 简介草稿 |
| --- | --- | --- |
| EP01 | 小新想打球，却连碰两次壁｜四年级英语Unit 5① | 下雨打不了球，图书馆也关门了，还能去哪？15秒看完小新的解决办法。PEP四上Unit 5选编，中英双语。 |
| EP02 | 刮风就不能玩？风间第一个不同意｜Unit 5② | 有风放风筝，下雪堆雪人。先替风间和妮妮选一个，再听英语揭晓。PEP四年级上册天气与活动选编。 |
| EP03 | 小新能不能出门，天气说了算｜Unit 5③ | 雨天在家等待，换成晴天又能做什么？看完回答最后一题。PEP四年级上册Unit 5选编，中英双语。 |

可考虑四年级英语/小学英语/人教版英语/英语启蒙/亲子英语方向；真实话题须获得当前发布授权后从平台建议选择。首帧是本地预览/封面参考，并不代表已经通过平台封面设置或发布检查。发布后按相同观察窗口记录各集跳出、平均观看、完播和收藏；这轮先比较开头与节奏，数据足够再推广到其它单元。

## SHA-256

| 视频 | SHA-256 |
| --- | --- |
| EP01 v11 | `7cf7c691d180b71b1451d03aa6fb08bb9bb4aa105548158a081cd8766094353e` |
| EP02 v11 | `458cc51e8a5129f6fba833be11899848d6c75a3776af89d6b65acc80bd421f45` |
| EP03 v11 | `c15ec332e29d95f31cb86792496ece1ac3343e01c0bad62b23235126126050a8` |
