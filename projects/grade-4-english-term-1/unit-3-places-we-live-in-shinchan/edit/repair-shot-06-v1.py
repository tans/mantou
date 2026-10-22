#!/usr/bin/env python3
"""Rebuild the facilities shot from reviewed, teaching-correct video extracts."""
from pathlib import Path
import json
import math
import sys
import wave
sys.path.insert(0,str(Path(__file__).resolve().parents[4]/'scripts'))
from run_lesson import run,save,sha,probe

lesson=Path(__file__).resolve().parents[1]
cfg=json.loads((lesson/'lesson-v7.json').read_text())
lines={l['id']:l for l in cfg['lines']}
boundaries=[];position=cfg['lead']
for lid in ['line-016','line-017','line-018']:
    with wave.open(str(lesson/lines[lid]['audio'])) as w:
        position+=w.getnframes()/w.getframerate()+lines[lid]['pause_after']
    boundaries.append(round(position*24))
boundaries[-1]=math.ceil((position+cfg['tail'])*24)
parts=[
 {'source':'renders/shot-06-xiaoguai-h3-v3.mp4','start':4.0,'crop':'1088:512:0:0','purpose':'Bus stop and WC symbols; omit erroneous medical cross and avoid cutting visible people'},
 {'source':'renders/shot-12-hospital-corrected-v4.mp4','start':0.5,'crop':None,'purpose':'Independent hospital exterior for There is a hospital.'},
 {'source':'renders/shot-03-xiaoguai-h3-v3.mp4','start':0.5,'crop':None,'purpose':'Playground for There is also a playground.'},
]
output=lesson/'renders/shot-06-teaching-corrected-silent-v1.mp4'
if output.exists():raise SystemExit('Retain existing derivative; use a new repair version')
for p in parts:
    src=lesson/p['source']
    if not src.exists():raise SystemExit('Waiting for source: '+str(src))
    if json.loads(src.with_suffix('.json').read_text())['output_sha256']!=sha(src):raise SystemExit('Source hash differs')
last=0;segments=[]
for i,p in enumerate(parts):
    frames=boundaries[i]-last;last=boundaries[i]
    target=lesson/f'edit/shot-06-repair-part-{i+1}-v1.mp4'
    vf=(f"crop={p['crop']}," if p['crop'] else '')+'scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2:color=white,setsar=1,fps=24'
    run(['ffmpeg','-v','error','-n','-ss',p['start'],'-i',lesson/p['source'],'-map','0:v:0','-an','-vf',vf,'-frames:v',frames,'-c:v','libx264','-preset','fast','-crf','19','-pix_fmt','yuv420p',target])
    p.update(source_sha256=sha(lesson/p['source']),frames=frames,derived_segment=str(target.relative_to(lesson)),segment_sha256=sha(target));segments.append(target)
listing=lesson/'edit/shot-06-repair-concat-v1.txt'
listing.write_text(''.join("file '"+str(p.resolve()).replace("'","'\\''")+"'\n" for p in segments))
run(['ffmpeg','-v','error','-n','-f','concat','-safe','0','-i',listing,'-map','0:v:0','-an','-c:v','copy','-movflags','+faststart',output])
save(output.with_suffix('.json'),{'provider':'local-edit','model':None,'task_id':None,'recipe':'edit/repair-shot-06-v1.py','parts':parts,'output_sha256':sha(output),'reason':'Original source merged medical cross with public toilet symbols; separate facilities to match verified teaching text','media':probe(output)})
print(output)
