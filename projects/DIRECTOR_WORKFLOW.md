# 短视频导演流程与发布门禁

路线图：[Issue #24](https://github.com/tans/mantou/issues/24)。本流程扩展既有 lesson、短集配置、SRT 与 assembly。

## 先绑定，再合成

每课在 `characters/speaker-bindings-vN.json` 按 line ID 声明 `speaker`、`voice_profile`、`shot_id`、`shot_type`、`active_character`、`other_characters`、`on_screen_speaker`、`voiceover`、`focus_method` 与 `staging_reason`。角色、声线和镜头引用以所选 lesson 为准。画外音明确标记，旁白不强制口型。

短集配置增加可选 `speaker_bindings` 相对路径，或合成命令传 `--bindings`。有绑定时，合成前校验引用、台词输入、实际 WAV/声线参数和镜头哈希；错误停止导出。多人同框须声明焦点方法。旧配置仍可导出预览，但缺少绑定不能通过发布检查。声明描述创作意图，实际人物是否在正确时刻发言由人工听看核实。

## 复核实际导出

```bash
python3 scripts/review_short_series.py \
  --config <课次>/short-series-vN.json \
  --bindings <课次>/characters/speaker-bindings-vN.json \
  --episode ep01 --report <课次>/edit/speaker-qa-vN/ep01.json
```

命令输出逐句秒数、音轨 SHA、声线、人物和镜头，并核对 assembly、配置、源素材、实际导出、字幕文字/时间和区间覆盖。JSON 与 Markdown 同时归档；报告存在时换版本。无人工记录时 `human_status=pending`、`publishable=false`。静态通过不证明听感或实际声画归属。

复核人完整带声音播放指定 SHA 的视频，逐句填写 `checks` 中 `speaker_voice`、`intelligibility`、`subtitle_timing`、`tail`、`lip_mismatch` 为 `pending/pass/fail`，问题在该行 `notes` 记录。显著口型错位导致误认说话人时记 fail；旁白按画外音约定复核。另填 `reviewer`、带时区的 `reviewed_at`、`full_playback_with_sound=true`、`visual_safety` 与 `hook_payoff`，后两项也使用 `pending/pass/fail`。使用报告的四项 SHA 绑定文件；素材或剪辑变化后重新复核。

```bash
python3 scripts/review_short_series.py \
  --config <课次>/short-series-vN.json \
  --bindings <课次>/characters/speaker-bindings-vN.json \
  --episode ep01 --review <课次>/edit/human-review-ep01-vN.json \
  --require-publishable
```

发布前命令必须返回0；缺失、pending、fail、过期SHA均返回2。允许对 `active_character` / `speaker_focus` 的特殊调度写明 `waivers`（rule、line、reason、reviewer、带时区reviewed_at），豁免随报告保留；源指纹、缺映射及人工未复核不能豁免。

门禁是仓库发布工作流的前置命令，不控制已发布平台作品。通过后仍须取得当前请求的发布授权，并核对账号、文案、真实话题、封面及AI声明。

## 创意、版式和数据

先记录目标受众、学习点、首帧、0–2秒hook、冲突、兑现与互动，再审稿，最后生成。角色聚焦和hook实验各自只改变一个主要变量；候选片保持未发布，人工创意审稿和声画复核分别记录。旧黑底教材版继续可用。

`social-story-v1` 用完整前景保留横屏人物，背景铺满9:16画布，逐句角色标签指向当前发言人。旧512×320源的清晰度限制随清单记录，放大与模糊背景不代表新增高清动画或原生竖屏镜头。以后确有预算的局部生成优先单人/双人竖屏构图。

运营使用发布台账及24h/72h/7d同口径窗口。仅采纳官方导出或作者提供数据，每个观测保存来源和时间；缺失为N/A。样本不足时给出补数/修改建议，不下流量改善结论。P0人工声画基线通过后才启动#23口型同步样片。

数据录入及一命令周报入口：`scripts/publication_ledger.py`；[Unit 5台账说明/CSV模板](grade-4-english-term-1/unit-5-the-weather-and-us/analytics/README.md)。数据不足时只形成基线，不将#22标为完成，也不通过自动化抓取补造窗口。

Unit 5首批逐句清单：`grade-4-english-term-1/unit-5-the-weather-and-us/edit/speaker-qa-v1/`。

## 生成剧情对照预览

`social-story-vN.json`保留源母版/时间轴/lesson字段，增加`template=social-story-v1`、`source_series`、`speaker_bindings`及每个候选的`source_episode`。候选items和speech_speed与源assembly一致，避免再次剪辑或提速。发言者方向位置按shot/character归一化登记；字幕、标签放在人物前景之外。

```bash
python3 scripts/compose_social_story.py --config <课次>/social-story-vN.json --dry-run
python3 scripts/compose_social_story.py --config <课次>/social-story-vN.json
```

输出新视频、独立设计封面、SRT副本和assembly；已有输出时换版本。源短集静态检查必须通过，人工pending允许生成待验收候选。导出后仍用同一`review_short_series.py`逐集生成清单，完整带声音验收后才能进入发布流程。
