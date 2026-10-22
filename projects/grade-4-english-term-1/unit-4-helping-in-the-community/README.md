# 四年级上册 Unit 4 · Helping in the community · 蜡笔小新版

制作状态：已导出可播放横屏/竖屏成片，待人工全片听检和用户验收。教材依据为本地 PEP 四年级上册扫描 PDF 印刷 p.38–49 / PDF 44–55。

## 已完成

- 脚本：`script/dialogue-v1.md`，14 条已核实/明确补充旁白；`line-013` 已核对为 `There are three elephants in the photo.`。
- 角色：沿用 Unit 3 的小新、风间、妮妮和 MiMo 声线；合并角色参考图为 `references/cast-sheet-shinchan-v1.png`。
- 配音：14 条 MiMo TTS WAV，`audio/manifest-v1.md`，总对白时长约 54.24 秒；媒体流检查通过，仍需人工逐条试听。
- 镜头：14 个单台词镜头，`renders/shot-01-minixm-8188-v1.mp4` 至 `shot-14-minixm-8188-v1.mp4`。每个文件为 512x320、24 fps、无音轨的课次内动态分镜兜底；对应 sidecar 记录来源与 SHA-256。
- 合成：`renders/unit-4-helping-in-the-community-master-v1.mp4` 为横屏配音母版；`renders/unit-4-helping-in-the-community-bilingual-burned-v1.mp4` 为横屏双语烧录版。
- 竖屏：`renders/unit-4-helping-in-the-community-vertical-bilingual-white-v2.mp4`，1080x1920，固定 `vertical-bilingual-white-v2` 版式。
- 字幕：`edit/subtitles-bilingual-v1.srt`；时间轴：`edit/timeline-v1.json`；剪辑记录：`edit/assembly-v1.md`。

## 8188 阻塞与兜底

默认服务确实使用了 `http://minixm.minapp.xin:8188`，没有使用 xiaoguai。健康检查和 ready 检查通过，但三个实际任务都进入 `INFERENCE_FAILED / Diffusers conditioning stage failed`，证据见 `video-provider-failures-v1.md`。因此本版不是 8188 供应商生成动画，而是明确标记的本地动态分镜兜底；服务恢复后可沿同一脚本和 prompt 重做镜头，不需重做 TTS/字幕时间轴。

## 待验收

- 播放横屏和竖屏全片，逐条听检英文发音、音量、字幕同步和结尾尾音。
- 逐镜检查当前兜底画面与分镜意图；8188 真实生成镜头尚未通过视觉验收。
