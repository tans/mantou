# Unit 5 v7 导出与复核

2026-10-23（Asia/Shanghai）。状态：完整导出预览；媒体、逐句/整段ASR、代表帧与包装版完整静音播放检查已完成；完整人工听检和用户验收待完成。

## 实际导出

| 文件 | 秒 | 字节 | SHA-256 |
| --- | --- | --- | --- |
| [unit-5-the-weather-and-us-master-v7.mp4](../renders/unit-5-the-weather-and-us-master-v7.mp4) | 77.562354 | 20266988 | `e052505fa98f967eda7ba917282bcab06f982d2e7724a1bfe93799fba7953329` |
| [unit-5-the-weather-and-us-bilingual-burned-v7.mp4](../renders/unit-5-the-weather-and-us-bilingual-burned-v7.mp4) | 77.562354 | 18065792 | `26479eefd0081634935050e3c7cbe8364868bae979ab0398211697ed4743a74b` |
| [unit-5-the-weather-and-us-vertical-bilingual-white-v7.mp4](../renders/unit-5-the-weather-and-us-vertical-bilingual-white-v7.mp4) | 77.562000 | 15012841 | `452f03c73b1de1f2b9a5be3a8535a742cafe146a87c0a8b65c75f4c8d8e9b319` |
| [unit-5-the-weather-and-us-spoken-bookends-v7.mp4](../renders/unit-5-the-weather-and-us-spoken-bookends-v7.mp4) | 50.083333 | 8979789 | `7cd719a4388c8710e3a8129f401f09ae875320ac201542e840e928382b83d216` |

横屏：1280×720/24fps/H.264、48kHz单声道AAC；普通竖屏：1080×1920/24fps、48kHz单声道AAC；中文童声包装：1080×1920/24fps、24kHz单声道AAC。所有源动画为自有8188/turbo8新任务，源帧512×320/124帧；合成等比放大，不声称原生1080p动画。

## 教学与声音

- 教材来源/页码/原文与改编状态见references/source-v1.md与script/dialogue-v7.md；本片选编p.50/51/52/55，不覆盖全部单元活动或原版歌曲。
- 采用18条WAV，line-013为v3、line-015为v2，其余16条复用v1；Milo/Dean/Mia声线沿用固定角色库。所有WAV完整解码，无PCM削波样本；逐行及混音ASR记录均保留。
- 实际包装MP4分段提取到audio/export-*-v7.wav；开场识别“课本英语跟我学”，正文18行归一化词序完全一致（数字、标点、OK/okay等书写规范化），结尾识别“关注我，学习更多小学英语”。音频证据和模型/词时间戳见audio/export-asr-v7.json。
- 采用已归档中文童声profile，正文1.2倍保音高；按同一剪辑映射删除24.458333秒长静音。包装片头1.833333秒，正文至46.416667秒，片尾3.666667秒；ASR定位的最后字音后还有0.746667秒画面。

## 字幕与画面

- 横屏/普通竖屏/包装正文均为同一18句英中配对；edit/export-qa-v7.json确认逐字匹配配置，时间轴有序、无重叠。包装额外包含2条中文栏目cue，共20条；保留完整SRT和body.srt。
- 固定vertical-bilingual-white-v2：英文52px、中文54px；18张字幕卡均实际渲染，长句最多两行。line-014译文仅省去非必要的“了”以完整成行，英文与声音不变。
- 10个镜头的0.3/2.5/4.8秒代表帧已检查，实际横屏合成每镜抽帧，以及包装首/中/尾、长句、最后英语、片尾和最后一帧均已检查；见storyboards/assembled-shots-*-v7.jpg与packaged-review-v7.jpg。
- shot-01 v1因重复妮妮否决，采用v2；shot-09/10源片有供应商乱码字幕，仅在合成时裁去底部44px，原片不变，裁后代表帧无残留。逐镜裁切、静音派生SHA和末帧延长见edit/shot-*-assembly-v7.json。

## 媒体与播放

四个导出均通过FFmpeg -v error -xerror完整解码，所有MP4的每条流内packet DTS严格递增。横屏文件解码到null muxer各报告一次边界舍入DTS警告；实际保存文件packet检查没有重复或倒退，普通竖屏/包装解码无该警告。

BrowserOS Neo实际播放50.083333秒包装版到ended=true，1202视频帧、0丢帧、readyState=4。为避免播放供应商声音及干扰，视频流检查使用静音模式，不能描述为完整听检。实际音频另做了完整分段转写。记录见edit/browser-playback-v7.json。

## 已知限制与待验收

- shot-06小新贴近左边缘，部分脸/身体贴边，妮妮与雪人主动作完整；shot-04妮妮衣摆有轻微运动重影，未出现多余人物。
- 源服务每镜限5.17秒；较长配音的末帧延长如实记录，包装通过收紧长停顿改善节奏。独立TTS不是逐词口型同步。
- 教材具体出版年/版次仍未核实（封面为2024审定），配套原音频缺失；这些未核实材料不被冒称为已取得。
- 完整人工听检仍待完成：声音自然度、发音、语速、响度、口型/对白感受和字幕同步。用户验收待完成；Issue #16继续用于该范围，未授权抖音发布。

## 补充音量与上传记录

实际包装MP4以FFmpeg ebur128测得整体-17.6 LUFS、LRA 2.9 LU、真峰值-1.4 dBFS，未达到数字满刻度。完整日志见loudness-v7.log；该技术测量不替代听感验收。

首次默认Git大包推送在传输结束时出现RPC连接重置和unable to rewind rpc post data，远端仍停留cee1032。使用仅针对该命令的HTTP/1.1与http.postBuffer=268435456重试后，媒体提交ebb197a成功推送；没有更改全局Git/代理设置或重生成媒体。今后大包遇到同样错误可复用此参数，并再次验证远端SHA。
