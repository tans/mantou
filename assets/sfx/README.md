# 全局音频资源库

存放跨课次复用的音乐与音效，不放课程对白/TTS 或某一课的专属混音。每个素材都应登记用途、来源、创作者、许可、媒体属性、校验值和使用限制；来源不允许独立再分发时，不把音频文件提交到 Git。

## 目录

- `openings/`：片头、开场提示音和短开场音乐。
- 后续可按需要增加 `transitions/`、`foley/`、`ambience/` 等子目录。

## 资源索引

| ID | 用途 | 本地文件 | 来源与作者 | 媒体属性 | 授权与状态 |
| --- | --- | --- | --- | --- | --- |
| `opening-cartoon-kids-playtime-v1` | 轻快儿童/卡通开场音乐；可作为蜡笔小新风格课程片头的通用备选，不是《蜡笔小新》原声 | `openings/cartoon-kids-intro-playtime-v1.mp3` | [Pixabay 素材页](https://pixabay.com/sound-effects/musical-cartoon-kids-intro-music-playtime-door-open-500912/)，OpenMindAudio | MP3，48 kHz，立体声，256 kb/s，9.816 秒；SHA-256 `f15e7b7b2e684364f1f9e0fd7c188c1c7023022512ae09618f1bdfe098da53bc` | Pixabay Content License；本地副本已取得，音频文件因禁止独立再分发而由本地 `.gitignore` 排除 |
| `opening-cartoon-music-v4-v1` | 卡通开场音乐备选 | `openings/cartoon-music-v4-v1.mp3` | [Pixabay 素材页](https://pixabay.com/sound-effects/musical-cartoon-cartoon-music-version-4-537857/)，BombinSound | MP3，44.1 kHz，立体声，256 kb/s，9.979 秒；SHA-256 `177f86e90462a6c4fb52deb2c1af15f699d2ce83e9743a91e5efc89c313f718c` | Pixabay Content License；本地副本已取得，音频文件因禁止独立再分发而由本地 `.gitignore` 排除 |

## 授权与取用

- 两个素材均从 Pixabay 对应素材详情页下载；许可摘要见 [Pixabay Content License](https://pixabay.com/service/license-summary/)，查阅日期：2026-10-22。许可允许在更大的创作项目中使用，但不允许把素材本身作为独立文件再分发/转售；使用前应重新查看当时适用的许可及素材页状态。
- MP3 留在 `openings/` 供当前工作区使用，由同目录 `.gitignore` 排除，不会推送到 GitHub。新克隆仓库的使用者须访问上表素材页并自行下载到对应路径。
- 以上是卡通风格的可替代开场音乐，不是蜡笔小新原版开场曲或动画中的原始音效；不得以官方原声、已获角色/音乐授权等名义使用或宣传。
- 如需精确使用原版音效/主题曲，应取得权利方或正规授权平台提供的许可文件，并在此记录授权范围与期限；不要从视频站抓取音轨归档。

## 新增规则

1. 先检查素材页和许可，确认可下载及目标用途；避免未授权抓取影视/动画原声。
2. 文件采用稳定、可读、带版本号的名称；原始下载文件不覆盖，转换/裁剪版本另存并记录与源文件关系。
3. 对会提交到公开仓库的二进制素材，确认许可明确允许再分发；若许可不允许，使用本地忽略文件并记录可复现的下载地址。
4. 下载后用 `file`/`ffprobe` 检查格式、编码、采样率、声道、时长，并记录 SHA-256。
