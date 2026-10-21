# Assembly v1 — Unit 2 “A great picture” Fun Time

## 当前状态

已产出 16 秒静音预览及 26.03 秒带配音、烧录英文字幕的合成预览。八条教材文本均已进入预览，其中 line-006–008 是 Mia 旁白试配。合成预览仍是待验收版本，完整试听和全片同步检查未完成。

另已使用 AIserver 8189 / MiniMax H3 的第二组镜头生成同规格对比预览。两版复用同一份 TTS 混音与字幕文件，原 xiaoguai 版本保持独立保留。

## 镜头顺序与裁剪

| 顺序 | 镜头 | 脚本行 | 使用文件 | 取用时长 |
| --- | --- | --- | --- | --- |
| 1 | shot-01 | line-001–002 | [`renders/unit-2-a-great-picture-fun-time-shot-01-xiaoguai-minimax-h3-480p-5s-v1-silent.mp4`](../renders/unit-2-a-great-picture-fun-time-shot-01-xiaoguai-minimax-h3-480p-5s-v1-silent.mp4) | 3 秒 |
| 2 | shot-02 | line-003–004 | [`renders/unit-2-a-great-picture-fun-time-shot-02-xiaoguai-minimax-h3-480p-5s-v1-silent.mp4`](../renders/unit-2-a-great-picture-fun-time-shot-02-xiaoguai-minimax-h3-480p-5s-v1-silent.mp4) | 3 秒 |
| 3 | shot-03 | line-005 | [`renders/unit-2-a-great-picture-fun-time-shot-03-xiaoguai-minimax-h3-480p-5s-v1-silent.mp4`](../renders/unit-2-a-great-picture-fun-time-shot-03-xiaoguai-minimax-h3-480p-5s-v1-silent.mp4) | 3 秒 |
| 4 | shot-04 | line-006–007 | [`renders/unit-2-a-great-picture-fun-time-shot-04-xiaoguai-minimax-h3-480p-5s-v1-silent.mp4`](../renders/unit-2-a-great-picture-fun-time-shot-04-xiaoguai-minimax-h3-480p-5s-v1-silent.mp4) | 4 秒 |
| 5 | shot-05 | line-008 | [`renders/unit-2-a-great-picture-fun-time-shot-05-xiaoguai-minimax-h3-480p-5s-v1-silent.mp4`](../renders/unit-2-a-great-picture-fun-time-shot-05-xiaoguai-minimax-h3-480p-5s-v1-silent.mp4) | 3 秒 |

## 输出

- 静音预览：[`unit-2-a-great-picture-fun-time-silent-preview-v1.mp4`](../renders/unit-2-a-great-picture-fun-time-silent-preview-v1.mp4)。H.264，864×480，16:9，16.000 秒，无音频流。
- 元数据与 SHA-256：[`unit-2-a-great-picture-fun-time-silent-preview-v1.json`](../renders/unit-2-a-great-picture-fun-time-silent-preview-v1.json)。
- 处理：用 FFmpeg 按上表裁剪后顺序拼接，输出无音轨预览。原始供应商文件和音轨已保留在 `renders/` 中；使用的静音派生版本及哈希见 [`renders/manifest-v1.md`](../renders/manifest-v1.md)。
- 带配音字幕预览：[`unit-2-a-great-picture-fun-time-audio-preview-v1.mp4`](../renders/unit-2-a-great-picture-fun-time-audio-preview-v1.mp4)，H.264/AAC，864×480，24 fps，26.03 秒；SHA-256 `fa2229c65549125485b1a1bf6a27042297a92d227d665724708a5deb2df9ac97`。对白按脚本顺序串接，每句之间留 0.20 秒，镜头对白结束后留 0.35 秒；shot-02、shot-04 超出源长的部分使用末帧停留。字幕已烧录，SRT 与合成 WAV 分别保存在 [`subtitles-preview-v1.srt`](subtitles-preview-v1.srt) 和 [`preview-mix-v1.wav`](../audio/preview-mix-v1.wav)；更多参数见[预览元数据](../renders/unit-2-a-great-picture-fun-time-audio-preview-v1.json)。
- AIserver 8189 对比预览：[`unit-2-a-great-picture-fun-time-aiserver-8189-preview-v1.mp4`](../renders/unit-2-a-great-picture-fun-time-aiserver-8189-preview-v1.mp4)，镜头顺序、停留时长、TTS 混音与烧录字幕均与 xiaoguai 版一致。服务端生成模型音轨未用于成片；详细 job、seed、提示词哈希和原/静音稿哈希见 [`renders/aiserver-8189/manifest-v1.md`](../renders/aiserver-8189/manifest-v1.md)。生成时模型目录将 H3 标为 `experimental`。

## 阻塞和待办

- line-001–008 的 TTS WAV 已生成，文件属性与哈希见 [`audio/manifest-v1.md`](../audio/manifest-v1.md)；逐条试听验收待完成。
- line-006–008 暂为旁白试配，合读/说话人分配没有通过教材配套音频确认；取得原音后再决定是否替换。
- FFprobe 已确认预览含 H.264 视频与 AAC 音频，画面尺寸、帧率及总时长符合记录；抽查字幕画面正常。完整播放、音量和对白口型同步仍待人工验收。
- 两个预览均待完整播放对比；AIserver 镜头抽帧已检查构图、角色和颜色手印，非全时段动作质量验收。
- 完成 TTS 听检及 line-006–008 朗读方式复核后，再修订节奏并产出最终版。
