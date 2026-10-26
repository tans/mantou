# Unit 5 发布基线与观察入口

`publication-ledger-v1.json`有四条历史发布记录及两个未发布候选。v9仅记录截至2026-10-24的审核中；v11三集记录2026-10-25已发布/公开页证据。每条保留原观察时间、作品ID、版本、视频与音轨SHA、模板、封面、hook、标题及话题。台账未重新访问平台，历史证据不等于当前实时状态。

当前没有24h/72h/7d官方导出或作者提供的数据，所有正式窗口指标为null/N/A；发布后数分钟0/1播放的后台片段不纳入比较。2026-10-26的[周报](weekly-review-2026-10-26-v1.md)只建立基线和补数行动，不宣称流量提升。

将平台官方导出或作者提供数据按`observation-template.csv`表头整理。一个work/window只能有一条记录；时间带时区；`data_source`写文件/页码/导出批次等可核对位置，原数据另行归档。没有的指标写N/A，明确观测到的0可填0。百分比为0–100，关注转化列记录人数。此CSV标准化是人工/作者数据入口，不是平台抓取器。

```bash
python3 scripts/publication_ledger.py import \
  --ledger projects/grade-4-english-term-1/unit-5-the-weather-and-us/analytics/publication-ledger-v1.json \
  --csv /path/to/official-or-author-observations.csv --source-kind author_provided \
  --output projects/grade-4-english-term-1/unit-5-the-weather-and-us/analytics/publication-ledger-v2.json

python3 scripts/publication_ledger.py report \
  --ledger projects/grade-4-english-term-1/unit-5-the-weather-and-us/analytics/publication-ledger-v1.json \
  --as-of 2026-10-26T09:37:00+08:00 \
  --output /path/to/weekly-review.md
```

容差为24h±3h、72h±6h、7d±12h，保留实际发布后小时数；不能把当前累计值倒填进已错过窗口。周报列出过去7天的同窗口数据、样本量、来源与SHA、对照限制及继续/修改行动；不自动作因果判断或发布。已有输出须换版本，不覆盖历史。

当前行动：v11三集的24h目标是2026-10-26 12:07/12:10/12:12（Asia/Shanghai），截至本次09:37尚未到目标时间，已进入约定容差。若作者有该窗口的官方数据，可按CSV录入；没有则保持N/A。不自动安排监测。候选A/B先完成创意与全片带声音人工复核，再另获发布授权。
