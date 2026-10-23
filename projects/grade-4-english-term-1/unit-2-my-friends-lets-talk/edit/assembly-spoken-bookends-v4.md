# 中文童声片头片尾与提速预览 v4

2026-10-23；跟踪 [Issue #15](https://github.com/tans/mantou/issues/15)。用户要求中文小朋友声音读出片头，实际加快语速，完整收尾，并以“关注我，学习更多小学英语”作语音关注提示，形成可复用流程。

## 交付

- [24秒预览](../renders/unit-2-my-friends-spoken-bookends-v4.mp4)：H.264，1080×1920，24fps，AAC 24kHz单声道；音视频均为24秒。
- [完整时间轴SRT](../renders/unit-2-my-friends-spoken-bookends-v4.srt)：两条中文包装cue及六条双语正文cue。
- [纯正文对轴SRT](../renders/unit-2-my-friends-spoken-bookends-v4.body.srt)、[剪辑/语速/profile/哈希元数据](../renders/unit-2-my-friends-spoken-bookends-v4.json)。
- [媒体/字幕/画面QA](spoken-bookends-v4-qa.json)、[实际成片音频转写](spoken-bookends-v4-asr.json)、[代表帧](../references/spoken-bookends-v4/contact-sheet.jpg)。
- 输出SHA-256：`886814b40514d9f2b3bf1009b98e2fb6e04141e06a686ca281bed24ef86a2f23`。

| 段落 | 起点 | 终点 | 内容/处理 |
| --- | --- | --- | --- |
| 中文童声片头 | 0.000秒 | 1.833秒 | “课本英语跟我学！”；真实语音1.739秒，加整帧尾部余量 |
| 英语正文及尾部停留 | 1.833秒 | 20.333秒 | 六句教材正文，setpts/atempo=1.2，字幕同映射，正文尾部另留0.25秒 |
| 中文关注提示及收尾 | 20.333秒 | 24.000秒 | “关注我，学习更多小学英语！”；真实语音3.062秒，之后保留0.604秒画面 |

包装来源是用户指定补充旁白，唯一脚本与WAV位于 `assets/branding/primary-english-child-zh-v1/`。设计为清亮普通话合成童声；同次生成两句、保存原件并分开后跨课复用，不和英语对白叠放。具体童声质感仍待人工试听。

## 正文与首句返修

六句教材正文、中文翻译、角色voice ID与顺序保持；原始字幕源仍为 `edit/subtitles-bilingual-vertical-v1.srt`。原首句在普通速度也被ASR识别为Alma/faint；沿用Milo局部重配，保留原始候选的加词问题与所选完整句，见 [`audio/manifest-v2.md`](../audio/manifest-v2.md)和 [`line-001-revision-v2.json`](../audio/line-001-revision-v2.json)。只替换首句音轨槽位，line-002–006及源动画视频流复用，新的可编辑横屏输入是 `renders/unit-2-my-friends-corrected-master-v2.mp4`。

先收紧8处长静音，合计约3.958秒，再对正文音视频/字幕同步1.2倍提速。使用音视频较长流确定覆盖时长；不足画面由末帧延长、不足音轨由补静音对齐，完整保留最后一句音频。最后正文字幕覆盖至关注提示开始，关注文字保留到最后一帧。

## 复现与后续课程

```bash
python3 scripts/compose_vertical_lesson.py   --input projects/grade-4-english-term-1/unit-2-my-friends-lets-talk/renders/unit-2-my-friends-corrected-master-v2.mp4   --srt projects/grade-4-english-term-1/unit-2-my-friends-lets-talk/edit/subtitles-bilingual-vertical-v1.srt   --grade '小学英语 · 四年级上册' --unit 'Unit 2'   --title 'My friends' --lesson "A. Let's talk"   --tighten-pauses   --packaging-profile assets/branding/primary-english-child-zh-v1/profile.json   --output projects/grade-4-english-term-1/unit-2-my-friends-lets-talk/renders/unit-2-my-friends-spoken-bookends-v4.mp4
```

输出存在时拒绝覆盖；重做选择新版本名。下一课换横屏母版、字幕和课程标题，继续同一个profile即可；包装WAV不重新生成。完整流程和验收条件见 [`projects/SOCIAL_VIDEO_GUIDE.md`](../../../SOCIAL_VIDEO_GUIDE.md)，项目教材制作技能、TTS技能、生产标准和换课指南均已有入口。

## 历史与验收边界

- fast-opening-v1为此前只含文字的21.7秒版本，保留。
- spoken-bookends-v2为初次语音包装候选，保留其完整文件、机器转写和代表帧；首句源配音存在疑点后用本版替代。
- spoken-bookends-v3导出在抓取结束帧时发现音频长于视频导致取帧越界，只留下正文SRT，无成片；取帧现依据真实视频时长，画面尾部按完整音频长度延长。v4为修复后实际完成版本。
- v4已完整解码，六条双语正文字幕文本与源一致，开场/转场/中段/末句/关注提示/末帧已目视核对。
- 实际v4音频中中文开场与关注提示转写相符，英文最后一句完整。姓名在ASR中出现Zhang/Jiang拼写差异，原line-003未改变，字幕继续教材Zhang Peng，保留人工听检项。
- 完整人工播放、童声质感、提速后的可懂度、口型同步及用户验收仍待完成。机器检查不是人工听检；当前交付明确称预览。本次没有发布抖音。
