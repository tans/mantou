# 镜头生成 manifest v1 — Unit 2 “A great picture” Fun Time

## 本次任务

- 供应商/模型：xiaoguai / MiniMax H3（`minimax-h3`）。
- 画幅与规格：16:9，864×480，供应商视频约 5.167 秒（请求时长 5 秒）。
- 参考图：无；镜头外观依据本课角色 Bible 和五格 Storyboard，以文字提示词保持服装、颜色和场景一致。
- 音频请求：`generate_audio_requested=false`。但供应商返回的 5 个原稿实际都含 AAC 音轨。原稿完整保留；下表列出的 `-silent.mp4` 是用 FFmpeg 仅复制视频流、移除音轨的派生稿，`-silent.json` 记录来源和 SHA-256。
- 抽帧复核：对每个静音派生稿抽取 0.5 秒与 4.5 秒画面检查构图、角色服装和对应动作；五条均为 H.264、864×480、约 5.167 秒，静音派生版确认没有音频流。尚未逐条完整播放，故仍为待全片复核的初稿。
- 任务提交时 Python TLS 校验失败；使用本机安装的 `certifi` CA 文件恢复正常 TLS 验证后成功提交。没有关闭证书校验。
- 已按 Storyboard 目标时长将 5 条静音派生稿裁为 3、3、3、4、3 秒，并合并出 16 秒静音预览：[`unit-2-a-great-picture-fun-time-silent-preview-v1.mp4`](unit-2-a-great-picture-fun-time-silent-preview-v1.mp4)，[元数据](unit-2-a-great-picture-fun-time-silent-preview-v1.json)。该预览尚未完成全片播放复核，也不含对白、字幕或配乐。

## 产物

| 镜头 / 脚本行 | 提示词 | 供应商原稿 | 静音派生稿 | 任务 ID | 抽帧结果 |
| --- | --- | --- | --- | --- | --- |
| shot-01 / line-001–002 | [`prompt-v1.txt`](../shots/shot-01/prompt-v1.txt) | [`MP4`](unit-2-a-great-picture-fun-time-shot-01-xiaoguai-minimax-h3-480p-5s-v1.mp4) · [JSON](unit-2-a-great-picture-fun-time-shot-01-xiaoguai-minimax-h3-480p-5s-v1.json) | [MP4](unit-2-a-great-picture-fun-time-shot-01-xiaoguai-minimax-h3-480p-5s-v1-silent.mp4) · [JSON](unit-2-a-great-picture-fun-time-shot-01-xiaoguai-minimax-h3-480p-5s-v1-silent.json) | `xg_8xQ139bCy5aSJlcVpTKp0` | 桌边双人邀请画树；衣着符合 Bible |
| shot-02 / line-003–004 | [`prompt-v1.txt`](../shots/shot-02/prompt-v1.txt) | [MP4](unit-2-a-great-picture-fun-time-shot-02-xiaoguai-minimax-h3-480p-5s-v1.mp4) · [JSON](unit-2-a-great-picture-fun-time-shot-02-xiaoguai-minimax-h3-480p-5s-v1.json) | [MP4](unit-2-a-great-picture-fun-time-shot-02-xiaoguai-minimax-h3-480p-5s-v1-silent.mp4) · [JSON](unit-2-a-great-picture-fun-time-shot-02-xiaoguai-minimax-h3-480p-5s-v1-silent.json) | `xg_fV5fwm2-znyVwzs8csXf8` | 手掌和颜料特写清楚；无伤害表现 |
| shot-03 / line-005 | [`prompt-v1.txt`](../shots/shot-03/prompt-v1.txt) | [MP4](unit-2-a-great-picture-fun-time-shot-03-xiaoguai-minimax-h3-480p-5s-v1.mp4) · [JSON](unit-2-a-great-picture-fun-time-shot-03-xiaoguai-minimax-h3-480p-5s-v1.json) | [MP4](unit-2-a-great-picture-fun-time-shot-03-xiaoguai-minimax-h3-480p-5s-v1-silent.mp4) · [JSON](unit-2-a-great-picture-fun-time-shot-03-xiaoguai-minimax-h3-480p-5s-v1-silent.json) | `xg_Movo-dWgIjVFoPVhh5ye8` | 男孩安慰并示意一起画画 |
| shot-04 / line-006–007 | [`prompt-v1.txt`](../shots/shot-04/prompt-v1.txt) | [MP4](unit-2-a-great-picture-fun-time-shot-04-xiaoguai-minimax-h3-480p-5s-v1.mp4) · [JSON](unit-2-a-great-picture-fun-time-shot-04-xiaoguai-minimax-h3-480p-5s-v1.json) | [MP4](unit-2-a-great-picture-fun-time-shot-04-xiaoguai-minimax-h3-480p-5s-v1-silent.mp4) · [JSON](unit-2-a-great-picture-fun-time-shot-04-xiaoguai-minimax-h3-480p-5s-v1-silent.json) | `xg_CxX8t8CEJOeBGqOkCGGRO` | 俯拍四种颜色手印组成树；未指定朗读者 |
| shot-05 / line-008 | [`prompt-v1.txt`](../shots/shot-05/prompt-v1.txt) | [MP4](unit-2-a-great-picture-fun-time-shot-05-xiaoguai-minimax-h3-480p-5s-v1.mp4) · [JSON](unit-2-a-great-picture-fun-time-shot-05-xiaoguai-minimax-h3-480p-5s-v1.json) | [MP4](unit-2-a-great-picture-fun-time-shot-05-xiaoguai-minimax-h3-480p-5s-v1-silent.mp4) · [JSON](unit-2-a-great-picture-fun-time-shot-05-xiaoguai-minimax-h3-480p-5s-v1-silent.json) | `xg_F40lbA9AwTdSe_7k08EyE` | 两名孩子展示手印树；暂不作台词人判定 |

## 剪辑备注

- Storyboard 目标总长 16 秒；当前供应商输出总长约 25.83 秒。组装时需选用静音派生稿并按镜头表裁剪，配音确认后再映射 TTS 与字幕。
- 角色总体连续；shot-02 以手部特写为主，shot-03/05 保留稳定服装识别。画面动作与教材页大意一致，但镜头仍需完整播放检查并按表现修订。

## 带对白预览

- 已使用五个静音派生镜头、line-001–008 的 MiMo TTS 和烧录英文字幕合成 [`unit-2-a-great-picture-fun-time-audio-preview-v1.mp4`](unit-2-a-great-picture-fun-time-audio-preview-v1.mp4)。H.264/AAC，864×480，24 fps，26.03 秒；SHA-256 `fa2229c65549125485b1a1bf6a27042297a92d227d665724708a5deb2df9ac97`。
- 对白段落时长按音频实际时长排布，shot-02 和 shot-04 的画面在源片末帧停留以覆盖较长台词；段间和镜头结束留短停顿。合成音轨与字幕源文件位于课次 `audio/preview-mix-v1.wav`、`edit/subtitles-preview-v1.srt`。
- FFprobe 流检查通过，抽查字幕画面可见；尚未逐条听音或完整播放验收。line-006–008 仍是 Mia 旁白试配。
