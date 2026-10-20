# Assembly v1 — Unit 2 “A great picture” Fun Time

## 当前状态

已产出 16 秒静音预览，供剪辑节奏和镜头顺序检查；五条教材已核实对白的 TTS 也已生成。预览仍不是带配音和字幕的最终成片，TTS 逐条试听和全片同步验收未完成。

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

## 阻塞和待办

- line-001–005 的 TTS WAV 已生成，文件属性与哈希见 [`audio/manifest-v1.md`](../audio/manifest-v1.md)；逐条试听验收待完成。
- line-006–008 的合读/说话人分配没有通过教材配套音频确认。当前预览只使用画面动作，不添加任何对白声线。
- 预览尚未完整播放验收；全片对白同步、字幕、音量和转场均未验收。完成 TTS 听检、确认 line-006–008 的朗读方式后，再产出最终版。
