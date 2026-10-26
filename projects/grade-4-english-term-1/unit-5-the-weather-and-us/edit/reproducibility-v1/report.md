# 新旧模板隔离重建记录

日期：2026-10-26T09:57:22.779580+08:00；代码：3c94d0a13841bfd424701b96ce6df6cc8dd837c8。

原配置逐字节复制到隔离课次目录，源素材链接既有归档，仅省略原输出和目标assembly目录。使用现有生产命令完整重建原三集及两个剧情候选，无供应商任务。实际环境、命令、配置/脚本SHA及输出SHA见report.json。

| 版本 | MP4相同 | 母版相同 | SRT相同 | 封面相同 | 完整解码 | 静态 | 人工 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ep01 | True | True | True | N/A | pass | pass | pending |
| ep02 | True | True | True | N/A | pass | pass | pending |
| ep03 | True | True | True | N/A | pass | pass | pending |
| ep01-focus | True | True | True | True | pass | pass | pending |
| ep01-hook | True | True | True | True | pass | pass | pending |

原输出保持不变：True。配置字节一致：True。五条MP4与归档SHA逐一完全一致；两个剧情候选的独立封面也逐字节一致。

这证明当前记录环境下black-v2旧短集和social-story-v1候选均可由现有配置重建；不推广为所有机器/编码器版本下均字节相同，也不代表人工有声视听已通过。隔离产物不重复提交，原视频/封面/旧报告不覆盖。

未完成关口：三集及候选的完整有声人工复核、创意/手机视觉与封面人工检查；正式窗口数据和真实效果复盘；P0通过后才启动#23口型样片评估。
