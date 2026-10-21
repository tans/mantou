# AIserver 8189 / MiniMax H3 manifest v1

## 运行信息

- 服务：`http://minixm.minapp.xin:8189`；本次提交前 `/health` 返回 HTTP 200，`/v1/models` 返回 `minimax-h3` 状态 `experimental`。
- 模型：`minimax-h3`，任务：`text_to_video`。
- 参数：每镜头 5.1666667 秒（124 帧），864×480，20 steps；无参考图。沿用与 xiaoguai 相同的五个 prompt v1 文件，以固定 seed 做记录。
- 同一服务的 H3 单 GPU 队列顺序执行。每个任务成功后下载原始 MP4 与脚本 JSON sidecar。
- 服务返回的五个原稿均含 H.264 视频和 AAC 音轨。保留原稿不变，再生成 `-silent.mp4`，仅复制视频流、移除模型音轨；最终预览复用既有 `audio/preview-mix-v1.wav`，没有重新生成 TTS。

## 镜头和产物

| 镜头 | 提示词 | 8189 原始稿 / job ID | 静音派生稿 | Seed | 原稿 SHA-256 · 静音稿 SHA-256 |
| --- | --- | --- | --- | --- | --- |
| shot-01 | [`prompt-v1.txt`](../../shots/shot-01/prompt-v1.txt) · `d6bcd8eac1ac0c1ef789265777561be6ff119e1b73c82e884468d03e322e88ff` | [`shot-01-v1.mp4`](shot-01-v1.mp4) · `job_bcf8da5ca4c74d35a1b11a7d71c33cae` | [`shot-01-v1-silent.mp4`](shot-01-v1-silent.mp4) | `2026102101` | 453b6a2b5f4754772f578af17b64a067bbca450bf55a87a3dbfc1c2b7a376cbf · 23bf884e82526b3f98aac692ef0450b663caacd4b1ea6f3862d55871f52d6d5b |
| shot-02 | [`prompt-v1.txt`](../../shots/shot-02/prompt-v1.txt) · `0b80ef0cf39d70169dc8dd07ca98795536b941dc44fab60604e5c2cb986f8d01` | [`shot-02-v1.mp4`](shot-02-v1.mp4) · `job_41656bcf5cbe4fc79485db47b906cf49` | [`shot-02-v1-silent.mp4`](shot-02-v1-silent.mp4) | `2026102102` | b509e293e9294f93507a09567f71f3e96a2e6c6bffb371f5c9fc00844a3cee3c · 9bd5f2920131336049eae94eb6b37f4de9fb7014ce353176cd6cfaccd794d472 |
| shot-03 | [`prompt-v1.txt`](../../shots/shot-03/prompt-v1.txt) · `4c28f673bd595e8e3ccea8d038e13298eea68b6ecb171dbb6590373d7a7194cc` | [`shot-03-v1.mp4`](shot-03-v1.mp4) · `job_6a98c779820d4b6086e21dd9a256c736` | [`shot-03-v1-silent.mp4`](shot-03-v1-silent.mp4) | `2026102103` | 32f073cbd90f09b733b6fb1159dc28fbb98889b00bd57ed7cba7895e4facb411 · f6a82473870aecbef21f3c0add1b01c2e11fe55542e52ec39d4f23c3dfcedf45 |
| shot-04 | [`prompt-v1.txt`](../../shots/shot-04/prompt-v1.txt) · `97407e29c714ea2e653a505f2a9d887e78dde35d4e258d26797edcbe2f9d0a0a` | [`shot-04-v1.mp4`](shot-04-v1.mp4) · `job_b7a3f044d2b74be2b6d96e8e56bc0119` | [`shot-04-v1-silent.mp4`](shot-04-v1-silent.mp4) | `2026102104` | dfc52fdc82b170ee3f438a37a7122cf8c2152ba5a814a616c5408a5e5b7b0b93 · 77cc7d1b80c405b0b6c4c85eb8eea6812b4ef086eeb7dbb84d93226a1004e291 |
| shot-05 | [`prompt-v1.txt`](../../shots/shot-05/prompt-v1.txt) · `a7f5fb0049e3e268cb52a11361fec81837c32bb188a9585bb100ef3b1b065601` | [`shot-05-v1.mp4`](shot-05-v1.mp4) · `job_68c6e7a6328b4f5d808760a80e714b46` | [`shot-05-v1-silent.mp4`](shot-05-v1-silent.mp4) | `2026102105` | 17e1a0c6d57ac95b7404a4eef47681f3c6d4b40ed6a9e345123c32c536a279d8 · 5c789a91e5f91bcd221a5cd3af484c633e9fe48cecdeda247982290fc8ecea48 |

## 合成对比预览

- 文件：[`../unit-2-a-great-picture-fun-time-aiserver-8189-preview-v1.mp4`](../unit-2-a-great-picture-fun-time-aiserver-8189-preview-v1.mp4)。H.264/AAC，864×480，24 fps，26.03 秒。
- 复用相同 MiMo 配音混音、字幕文件、镜头顺序和镜头时长，与 xiaoguai 预览保持相同时间轴以便对比；shot-02/04 的额外时长延续镜头末帧。
- FFprobe 确认视频与音频流；五镜头中点抽帧检查及预览多处字幕画面检查通过。完整播放和听音验收仍待完成。
- 本结果为实验模型生成的比较稿，不替代原 xiaoguai 版本。
