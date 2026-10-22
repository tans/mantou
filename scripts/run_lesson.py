#!/usr/bin/env python3
"""Run a single, verified lesson using the existing provider and layout tools."""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import math
import os
from pathlib import Path
import re
import subprocess
import sys
import wave

ROOT = Path(__file__).resolve().parents[1]

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    tmp.replace(path)

def run(command):
    subprocess.run([str(x) for x in command], check=True)

def probe(path):
    return json.loads(subprocess.check_output(['ffprobe', '-v', 'error', '-show_streams', '-show_format', '-of', 'json', str(path)], text=True))

def stamp(seconds):
    ms = round(seconds * 1000)
    return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'

def load(path):
    cfg = json.loads(path.read_text())
    lesson = path.parent
    version = cfg['version']
    source = lesson / f'script/dialogue-{version}.md'
    rows = {}
    for row in source.read_text().splitlines():
        cells = [x.strip() for x in row.strip('|').split('|')]
        if cells and re.fullmatch(r'line-\d{3}', cells[0]):
            if cells[0] in rows:
                raise ValueError('Duplicate canonical script line: ' + cells[0])
            rows[cells[0]] = cells
    ids = [l['id'] for l in cfg['lines']]
    if len(ids) != len(set(ids)) or set(ids) != set(rows):
        raise ValueError('Config and canonical script IDs differ')
    shot_ids = [s['id'] for s in cfg['shots']]
    if len(shot_ids) != len(set(shot_ids)):
        raise ValueError('Duplicate shot IDs')
    mapped = [lid for s in cfg['shots'] for lid in s['lines']]
    if mapped != ids:
        raise ValueError('Shot line order/coverage differs from canonical script')
    for line in cfg['lines']:
        row = rows[line['id']]
        if line['status'] != 'verified' or row[-1] != 'verified' or row[2:4] != [line['text'], line['zh']]:
            raise ValueError('Unverified or changed canonical text: ' + line['id'])
        if row[1] != cfg['voices'][line['speaker']]['name'] or row[-2] != line['shot']:
            raise ValueError('Speaker/shot mapping differs: ' + line['id'])
        textfile = lesson / line.get('input', f"script/tts-input/{line['id']}-{version}.txt")
        if textfile.read_text().strip() != line['text']:
            raise ValueError('TTS input differs: ' + str(textfile))
    return cfg, lesson

def audio_path(lesson, line, version):
    return lesson / line.get('audio', f"audio/tts/{line['id']}-{version}.wav")

def tts(cfg, lesson, args):
    def one(line):
        target = audio_path(lesson, line, cfg['version'])
        voice = cfg['voices'][line['speaker']]
        style = line.get('style', voice['style'])
        textfile = lesson / line.get('input', f"script/tts-input/{line['id']}-{cfg['version']}.txt")
        key = {'text_sha256': sha(textfile), 'voice': voice['voice'], 'style': style, 'model': 'mimo-v2.5-tts'}
        meta = target.with_suffix('.json')
        if target.exists():
            if not meta.exists() or json.loads(meta.read_text())['input'] != key or json.loads(meta.read_text())['sha256'] != sha(target):
                raise ValueError('Existing TTS has changed/unknown inputs; use a new version: ' + str(target))
            with wave.open(str(target)) as w:
                w.readframes(w.getnframes())
            print('Reused ' + target.name, flush=True)
            return
        command = [sys.executable, ROOT/'scripts/generate_tts.py', '--text-file', textfile, '--voice', voice['voice'], '--style', style, '--output', target]
        if args.dry_run:
            command.append('--dry-run')
        run(command)
        if not args.dry_run:
            save(meta, {'input': key, 'sha256': sha(target), 'qa': 'media probe only; full listening pending'})
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        list(pool.map(one, [l for l in cfg['lines'] if not args.line or l['id'] == args.line]))

def video(cfg, lesson, args):
    by_id = {l['id']: l for l in cfg['lines']}
    for shot in cfg['shots']:
        if args.shot and shot['id'] != args.shot:
            continue
        output = lesson / shot['output']
        refs = [lesson / x for x in cfg.get('character_references', [])]
        if shot.get('reference'):
            refs.append(lesson / shot['reference'])
        prompt = lesson / shot['prompt']
        for ref in refs:
            if not ref.is_file():
                raise ValueError('Reference missing: ' + str(ref))
        if not refs:
            raise ValueError('A character or scene reference is required')
        seconds = cfg['lead'] + cfg['tail']
        for lid in shot['lines']:
            with wave.open(str(audio_path(lesson, by_id[lid], cfg['version']))) as w:
                seconds += w.getnframes() / w.getframerate()
            seconds += by_id[lid].get('pause_after', cfg['gap'])
        duration = min(15, max(5, math.ceil(seconds)))
        key = {'prompt_sha256': sha(prompt), 'reference_sha256': [sha(ref) for ref in refs], 'duration': duration, 'resolution': shot['resolution'], 'provider': 'xiaoguai', 'model': 'minimax-h3', 'aspect_ratio': '16:9', 'generate_audio': False, 'adapter_sha256': sha(ROOT/'scripts/generate_video.py')}
        statefile = lesson / f"shots/{shot['id']}/task-{cfg['version']}.json"
        state = json.loads(statefile.read_text()) if statefile.exists() else None
        if state and state['input'] != key:
            raise ValueError('Shot inputs changed; retain old asset and create a new version: ' + shot['id'])
        if output.exists():
            probe(output)
            if not state or not output.with_suffix('.json').exists():
                raise ValueError('Untracked existing output: ' + str(output))
            if json.loads(output.with_suffix('.json').read_text())['output_sha256'] != sha(output):
                raise ValueError('Video output hash changed: ' + str(output))
            print('Reused ' + output.name, flush=True)
            continue
        command = [sys.executable, ROOT/'scripts/generate_video.py', '--provider', 'xiaoguai', '--prompt-file', prompt, '--duration', duration, '--resolution', shot['resolution'], '--aspect-ratio', '16:9', '--output', output, '--poll-interval', 15]
        for ref in refs:
            command += ['--reference-image', ref]
        if args.dry_run:
            run(command + ['--dry-run'])
            continue
        if state:
            if not state.get('task_id'):
                raise ValueError('Submission outcome unknown. Check provider account before retrying: ' + str(statefile))
            command += ['--task-id', state['task_id']]
        else:
            state = {'input': key, 'status': 'submitting', 'task_id': None}
            save(statefile, state)
        log = lesson / f"shots/{shot['id']}/generation-{cfg['version']}.log"
        with log.open('a') as out:
            process = subprocess.Popen([str(x) for x in command], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
            for message in process.stdout:
                out.write(message); out.flush()
                print(message, end='', flush=True)
                match = re.search(r'Submitted xiaoguai task (\S+)', message)
                if match:
                    state.update(task_id=match[1], status='running'); save(statefile, state)
            code = process.wait()
        state['status'] = 'downloaded' if code == 0 else 'resume_required'
        save(statefile, state)
        if code:
            raise RuntimeError('Resume the recorded task; do not resubmit: ' + shot['id'])

def assemble(cfg, lesson, args):
    version = cfg['version']
    edit = lesson / 'edit'
    renders = lesson / 'renders'
    master = renders / f"{cfg['lesson_id']}-master-{version}.mp4"
    horizontal = renders / f"{cfg['lesson_id']}-bilingual-burned-{version}.mp4"
    if master.exists() or horizontal.exists():
        raise ValueError('Output exists; export a new version instead of overwriting')
    if args.dry_run:
        print('Assembly will probe every source, remove provider audio, preserve speech timing, and save a master, SRT and bilingual video.')
        return
    from PIL import Image, ImageDraw, ImageFont
    import compose_vertical_lesson as layout
    enpaths = ['/System/Library/Fonts/Supplemental/Arial Bold.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf']
    zhpaths = ['/System/Library/Fonts/PingFang.ttc', '/System/Library/Fonts/STHeiti Medium.ttc', '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc']
    enfont = layout.font_from(enpaths, 36); zhfont = layout.font_from(zhpaths, 35)
    by_id = {l['id']: l for l in cfg['lines']}
    timeline=[]; clips=[]; captioned=[]; cursor=0.0
    audio_settings = None
    for shot in cfg['shots']:
        src = lesson / shot['output']
        media = probe(src)
        raw_duration = float(next(s for s in media['streams'] if s['codec_type']=='video')['duration'])
        silent = src.with_name(src.stem + '-silent.mp4')
        if not silent.exists():
            run(['ffmpeg','-v','error','-n','-i',src,'-map','0:v:0','-c:v','copy','-an',silent])
        if any(s['codec_type']=='audio' for s in probe(silent)['streams']):
            raise ValueError('Silent derivative contains audio')
        chunks=[]; local_cues=[]; position=cfg['lead']
        for lid in shot['lines']:
            line = by_id[lid]
            path=audio_path(lesson,line,version)
            with wave.open(str(path)) as w:
                params=(w.getnchannels(),w.getsampwidth(),w.getframerate())
                if params[0]!=1 or params[1]!=2:
                    raise ValueError('Assembly expects mono PCM16 WAV; convert a derivative explicitly')
                if audio_settings and params!=audio_settings:
                    raise ValueError('Mixed WAV formats; convert derivatives explicitly')
                audio_settings=params
                frames=w.readframes(w.getnframes()); dur=w.getnframes()/w.getframerate()
            if not chunks: chunks.append(bytes(round(cfg['lead']*params[2])*params[1]))
            cue={'line':lid,'shot':shot['id'],'speaker':line['speaker'],'start':round(cursor+position,3),'end':round(cursor+position+dur,3),'english':line['text'],'chinese':line['zh'],'audio':str(path),'audio_sha256':sha(path)}
            timeline.append(cue);local_cues.append({**cue,'start':position,'end':position+dur})
            chunks.append(frames)
            gap=line.get('pause_after',cfg['gap'])
            chunks.append(bytes(round(gap*params[2])*params[1]))
            position+=dur+gap
        duration=math.ceil((position+cfg['tail'])*cfg['fps'])/cfg['fps']
        chunks.append(bytes(round((duration-position)*params[2])*params[1]))
        wav=edit/f"{shot['id']}-mix-{version}.wav"
        with wave.open(str(wav),'wb') as w:
            w.setparams((*params,0,'NONE','not compressed'));w.writeframes(b''.join(chunks))
        clip=edit/f"{shot['id']}-picture-audio-{version}.mp4"
        vf=f"scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2:color=white,setsar=1,fps={cfg['fps']},tpad=stop_mode=clone:stop_duration={duration:.6f}"
        run(['ffmpeg','-v','error','-n','-i',silent,'-i',wav,'-map','0:v:0','-map','1:a:0','-vf',vf,'-t',f'{duration:.6f}','-c:v','libx264','-preset','fast','-crf','19','-pix_fmt','yuv420p','-c:a','aac','-b:a','128k','-movflags','+faststart',clip])
        clips.append(clip)
        command=['ffmpeg','-v','error','-n','-i',clip]
        filters=[];prev='0:v'
        for i,cue in enumerate(local_cues):
            card=edit/f"{cue['line']}-caption-{version}.png"
            img=Image.new('RGBA',(1280,720),(0,0,0,0));d=ImageDraw.Draw(img)
            en=layout.wrap_text(d,cue['english'],enfont,1170);zh=layout.wrap_text(d,cue['chinese'],zhfont,1170)
            h=24+len(en)*43+len(zh)*42;y=720-h-12
            d.rounded_rectangle((28,y,1252,708),radius=16,fill=(255,255,255,236))
            yy=y+10
            for text in en:d.text((640,yy),text,font=enfont,anchor='mt',fill='#183B5B');yy+=43
            for text in zh:d.text((640,yy),text,font=zhfont,anchor='mt',fill='#2D3748');yy+=42
            img.save(card)
            command+=['-i',card]
            name=f'cap{i}'
            filters.append(f"[{prev}][{i+1}:v]overlay=0:0:eof_action=repeat:enable='gte(t,{cue['start']:.6f})*lt(t,{cue['end']:.6f})'[{name}]")
            prev=name
        subclip=edit/f"{shot['id']}-bilingual-{version}.mp4"
        run(command+['-filter_complex',';'.join(filters),'-map',f'[{prev}]','-map','0:a:0','-t',f'{duration:.6f}','-c:v','libx264','-preset','fast','-crf','19','-pix_fmt','yuv420p','-c:a','copy',subclip])
        captioned.append(subclip)
        save(edit/f"{shot['id']}-assembly-{version}.json",{'source':str(src),'source_sha256':sha(src),'silent':str(silent),'silent_sha256':sha(silent),'source_duration':raw_duration,'timeline_duration':duration,'last_frame_extension':max(0,duration-raw_duration),'cues':local_cues})
        cursor+=duration
    for paths,target,label in ((clips,master,'master'),(captioned,horizontal,'bilingual')):
        listing=edit/f'concat-{label}-{version}.txt'
        listing.write_text(''.join("file '"+str(p.resolve()).replace("'","'\\''")+"'\n" for p in paths))
        run(['ffmpeg','-v','error','-n','-f','concat','-safe','0','-i',listing,'-c','copy','-movflags','+faststart',target])
    srt=edit/f'subtitles-bilingual-{version}.srt'
    srt.write_text('\n\n'.join(f"{i+1}\n{stamp(c['start'])} --> {stamp(c['end'])}\n{c['english']}\n{c['chinese']}" for i,c in enumerate(timeline))+'\n')
    save(edit/f'timeline-{version}.json',timeline)
    for target in (master,horizontal):
        save(target.with_suffix('.json'),{'config_sha256':sha(args.config),'script_sha256':sha(lesson/f'script/dialogue-{version}.md'),'output_sha256':sha(target),'duration':cursor,'media':probe(target),'qa':'generated; visual checks and full listening tracked in README'})
    (edit/f'assembly-{version}.md').write_text('# 剪辑时间轴 '+version+'\n\n按 TTS 实际 WAV 长度剪辑；不加速、不截断对白。每镜头前留 '+str(cfg['lead'])+' 秒，尾部至少 '+str(cfg['tail'])+' 秒；静音问答停顿见行配置。\n\n完整 cue 映射见 `timeline-'+version+'.json`；每镜头源 SHA、去音轨派生 SHA、实际时长与末帧延长见 `shot-*-assembly-'+version+'.json`。字幕源 `subtitles-bilingual-'+version+'.srt`。\n\n| cue | 行 | 角色 | 起点 | 终点 |\n| --- | --- | --- | --- | --- |\n'+'\n'.join(f"| {i+1} | {c['line']} | {c['speaker']} | {stamp(c['start'])} | {stamp(c['end'])} |" for i,c in enumerate(timeline))+'\n\n生成完成不是用户验收；视听状态见课次 README。\n')
    print(json.dumps({'master':str(master),'bilingual':str(horizontal),'srt':str(srt),'duration':cursor},ensure_ascii=False))

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('stage',choices=['plan','tts','video','assemble'])
    p.add_argument('--config',required=True,type=Path)
    p.add_argument('--dry-run',action='store_true')
    p.add_argument('--workers',type=int,choices=[1,2,3],default=1)
    p.add_argument('--line');p.add_argument('--shot')
    args=p.parse_args()
    cfg,lesson=load(args.config)
    if args.line and args.line not in {l['id'] for l in cfg['lines']}:p.error('Unknown --line')
    if args.shot and args.shot not in {s['id'] for s in cfg['shots']}:p.error('Unknown --shot')
    if args.stage=='plan':
        print(json.dumps({'lesson':cfg['lesson_id'],'lines':len(cfg['lines']),'shots':len(cfg['shots']),'text_verified':True,'paid_requests':'Only explicit tts/video stages contact providers; plan and assemble do not.'},ensure_ascii=False,indent=2))
    else:
        globals()[args.stage](cfg,lesson,args)

if __name__=='__main__':
    try:main()
    except (ValueError,RuntimeError,OSError,subprocess.CalledProcessError) as e:
        raise SystemExit(f'Lesson stopped: {e}')
