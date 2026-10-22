# 完整导出检查记录 v9

2026-10-22。状态：**完整导出预览，待人工全片视听与用户验收**。

## 已完成的检查

- 教材脚本/课程配置：`run_lesson.py plan --config lesson-v8.json`通过；49行、20镜头。
- 49条SRT英文/中文/时间与最终脚本和timeline完全一致；顺序非重叠，末条在片尾前结束。
- 49条实际采用WAV的SHA与small.en复核报告一致，49/49逐词匹配；机器转写不代替听检。
- 横屏双语与竖屏双语完整解码通过，错误日志为空；所有三份导出各4614个视频帧，源时间戳严格递增。
- 初次横屏默认null输出将一处拼接边界四舍五入到同一24fps tick；保留demux时间基后完整解码干净。原视频PTS无重复/倒退；竖屏为固定24fps。
- 横屏母版响度-17.9 LUFS，LRA5.3 LU，AAC真峰值-1.4dBFS。源WAV未改动；最终混音48kHz单声道AAC。
- 已目视20个源镜头首中尾帧、最终横屏代表帧、竖屏开场/中段/长句/结尾和字幕切换（35.0、35.2、35.5秒）。
- shot-06教学物件修复、shot-12医院返修、shot-08/17源字幕裁去；中文句尾标点换行修复保留版本关系。

## 导出文件

| 版本 | 分辨率/音频 | 时长 | 字节 | SHA-256 |
| --- | --- | --- | --- | --- |
| [master](../renders/unit-3-places-we-live-in-shinchan-master-v8.mp4) | 1280×720/H264；48000Hz mono AAC | 192.270688s | 48324019 | `cf3c362c2429c0413fa1c4a45c8fe22ba0000a57b1c6f31a0c39d2eae5016fae` |
| [landscape_bilingual](../renders/unit-3-places-we-live-in-shinchan-bilingual-burned-v8.mp4) | 1280×720/H264；48000Hz mono AAC | 192.270354s | 44026882 | `3086313bfbec6153160dc708ea12f9e91d3c5aabb909198f08c520688acbb55b` |
| [portrait_bilingual](../renders/unit-3-shinchan-vertical-bilingual-v9.mp4) | 1080×1920/H264；48000Hz mono AAC | 192.250000s | 35048512 | `da3bb6aa5af07f16c141e41b0c5b4939d2471fca0673a829609205b93942f178` |

## 尚未完成

完整连续播放、人工听感及用户教学验收仍待完成。未做逐字音素口型匹配；角色为合成英语声音，不是原动画演员。教材出版年份/版次仍UNRESOLVED，不影响本次已核对的单元正文，但换版本必须重新核对。

检查JSON保存完整ffprobe流、源配置/SRT哈希及验收边界。Issue #12保持开放到人工视听/用户验收完成。
