#!/usr/bin/env python3
"""Import authorized observation CSVs and produce reproducible weekly reviews."""
import argparse
import csv
from datetime import datetime, timedelta
import json
import math
from pathlib import Path

from review_short_series import sha

METRICS = {'exposures': '曝光', 'plays': '播放', 'bounce_2s_pct': '2秒跳出%',
           'retention_5s_pct': '5秒留存%', 'avg_watch_seconds': '平均观看秒',
           'completion_pct': '完播%', 'favorites': '收藏', 'comments': '评论',
           'shares': '分享', 'follows': '关注转化人数'}
WINDOWS = {'24h': (24, 3), '72h': (72, 6), '7d': (168, 12)}


def moment(value):
    result = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if result.tzinfo is None:
        raise ValueError('Timestamp must include timezone')
    return result


def metric(key, value):
    if value is None or value.strip() in ('', 'N/A', '-'):
        return None
    number = float(value)
    if not math.isfinite(number) or number < 0 or (key.endswith('_pct') and number > 100):
        raise ValueError(f'Invalid {key}: {value}')
    if key.endswith('_pct') or key == 'avg_watch_seconds':
        return number
    if not number.is_integer():
        raise ValueError(f'{key} must be an integer')
    return int(number)


def import_csv(ledger, path, source_kind):
    if source_kind not in ('official_export', 'author_provided'):
        raise ValueError('Only official exports or author-provided data may be imported')
    works = {work['key']: work for work in ledger['works']}
    seen = {(o['work_key'], o['window']) for o in ledger['observations']}
    with path.open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        required = {'work_key', 'window', 'observed_at', 'data_source'} | set(METRICS)
        if not required.issubset(reader.fieldnames or []):
            raise ValueError('Missing required CSV columns: ' + ', '.join(sorted(required - set(reader.fieldnames or []))))
        for row in reader:
            key, window = row['work_key'], row['window']
            if key not in works or window not in WINDOWS or (key, window) in seen:
                raise ValueError('Unknown work/window or duplicate observation')
            work = works[key]
            if not work.get('published_at') or work['status'] != 'published':
                raise ValueError('Observations require a documented publication time and published status')
            if not row['data_source'].strip():
                raise ValueError('Each observation needs a source locator')
            hours = (moment(row['observed_at']) - moment(work['published_at'])).total_seconds() / 3600
            target, tolerance = WINDOWS[window]
            if abs(hours - target) > tolerance:
                raise ValueError(f'Observed age {hours:.2f}h outside {window} tolerance ±{tolerance}h')
            values = {key: metric(key, row[key]) for key in METRICS}
            if all(value is None for value in values.values()):
                raise ValueError('Observation has no metrics; keep missing windows as N/A')
            ledger['observations'].append({'work_key': key, 'window': window, 'observed_at': row['observed_at'],
                                           'elapsed_hours': round(hours, 3), 'source_kind': source_kind,
                                           'data_source': row['data_source'], 'import_file': str(path),
                                           'import_sha256': sha(path), 'metrics': values})
            seen.add((key, window))
    return ledger


def report(ledger, as_of, ledger_path):
    lines = ['# 视频发布与观察周报', '', f'截至：{as_of.isoformat()}；过去7天观察与待办。',
             f'台账：{ledger_path}；SHA-256：{sha(ledger_path)}。', '',
             '平台状态按原证据的观察时间列示，本命令不抓取平台。N/A表示缺失，不能视为0。', '',
             '| 版本 | 记录状态 | 状态观察时间 | 作品ID | 时长秒 |', '| --- | --- | --- | --- | --- |']
    works = {w['key']: w for w in ledger['works']}
    for work in ledger['works']:
        lines.append(f'| {work["key"]} | {work["status"]} | {work.get("status_observed_at") or "N/A"} | {work.get("work_id") or "N/A"} | {work["duration_seconds"]} |')
    lines += ['', '## 固定窗口', '', '窗口容差：24h±3h、72h±6h、7d±12h；保留实际elapsed_hours。不同时间窗口不混比。', '']
    recent = [o for o in ledger['observations'] if as_of - timedelta(days=7) <= moment(o['observed_at']) <= as_of]
    for window, (hours, tolerance) in WINDOWS.items():
        sources = []
        lines += [f'### {window}', '', '| 作品 | 观测时间 | ' + ' | '.join(METRICS.values()) + ' |',
                  '| --- | --- | ' + ' | '.join('---' for _ in METRICS) + ' |']
        for key, work in works.items():
            observation = next((o for o in recent if o['work_key'] == key and o['window'] == window), None)
            values = observation['metrics'] if observation else {}
            lines.append('| ' + ' | '.join([key, observation['observed_at'] if observation else 'N/A'] + [str(values[k]) if values.get(k) is not None else 'N/A' for k in METRICS]) + ' |')
            if observation:
                sources.append(f'- {key}来源：{observation["data_source"]}；导入SHA：{observation["import_sha256"]}；实际年龄{observation["elapsed_hours"]}h。')
        lines += [''] + sources + ['']
    lines += ['## 对照与行动', '']
    for experiment in ledger['experiments']:
        members = experiment['members']
        lines += [f'- {experiment["id"]}：{experiment["variable"]}。']
        usable = []
        for window in WINDOWS:
            observations = [next((o for o in recent if o['work_key'] == key and o['window'] == window), None) for key in members]
            if all(o and o['metrics'].get('plays') is not None for o in observations):
                usable.append(window)
        if not usable:
            lines.append('  决策：继续准备/补数；没有同窗口可比较的播放样本，暂停效果判断。先完成声画与创意人工审稿，获授权后再发布候选。')
        else:
            lines.append('  决策：修改比较记录；已有同窗口数据（' + ', '.join(usable) + '），先核对发布时间、受众、播放样本量和分发差异，再决定扩大实验。仅作描述，不能由单条样本推出因果。')
        lines.append('  可比性限制：' + experiment['limitations'])
    lines += ['', '## 缺项与下一步', '']
    for work in ledger['works']:
        if work.get('published_at'):
            for window, (hours, tolerance) in WINDOWS.items():
                due = moment(work['published_at']) + timedelta(hours=hours)
                exists = any(o['work_key'] == work['key'] and o['window'] == window for o in ledger['observations'])
                if not exists:
                    state = ('尚未进入容差' if as_of < due - timedelta(hours=tolerance) else
                             '容差内待采集' if as_of <= due + timedelta(hours=tolerance) else
                             '历史窗口已错过，保留N/A')
                    lines.append(f'- {work["key"]} {window}：{due.isoformat()}；{state}。')
        elif work['status'] == 'reviewing':
            lines.append(f'- {work["key"]}：原记录为审核中，缺作品ID/公开时间；需另行核验状态，不沿用为当前事实。')
    lines += ['', '数据入口：官方导出或作者提供的CSV。新片发布须单独授权；本命令只读/生成本地记录。', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('report', 'import'))
    parser.add_argument('--ledger', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path, help='New version; never overwrite an existing record')
    parser.add_argument('--as-of', help='Required for a reproducible report, ISO-8601 with timezone')
    parser.add_argument('--csv', type=Path)
    parser.add_argument('--source-kind', choices=('official_export', 'author_provided'))
    args = parser.parse_args()
    if args.output.exists():
        parser.error('Output exists; choose a new version')
    ledger = json.loads(args.ledger.read_text())
    if args.command == 'import':
        if not args.csv or not args.source_kind:
            parser.error('Import needs --csv and --source-kind')
        result = json.dumps(import_csv(ledger, args.csv, args.source_kind), ensure_ascii=False, indent=2) + '\n'
    else:
        if not args.as_of:
            parser.error('Report needs --as-of')
        result = report(ledger, moment(args.as_of), args.ledger)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(result)
    print(args.output)


if __name__ == '__main__':
    main()
