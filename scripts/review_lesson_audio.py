#!/usr/bin/env python3
"""Transcribe every selected lesson WAV locally and flag wording differences."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
from run_lesson import load, sha


NUMBER_WORDS = {
    word: str(value)
    for value, word in enumerate(
        'zero one two three four five six seven eight nine ten eleven twelve '
        'thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty'.split()
    )
}


def words(text):
    # Normalize spelling, number formatting, and punctuation before comparing ASR.
    text = re.sub(
        r"\bneighbours?\b",
        lambda match: 'neighbor' + ('s' if match.group(0).endswith('s') else ''),
        text.lower(),
    )
    tokens = re.findall(r"[a-z0-9']+", text)
    return [NUMBER_WORDS.get(token, token) for token in tokens]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--config',required=True,type=Path)
    p.add_argument('--output',required=True,type=Path)
    p.add_argument('--model',default='small.en')
    p.add_argument('--line',action='append',help='Review only these line IDs; repeat as needed')
    args=p.parse_args()
    if args.output.exists():p.error('Output exists; use a new review version')
    cfg,lesson=load(args.config)
    lines=[l for l in cfg['lines'] if not args.line or l['id'] in args.line]
    if not lines or (args.line and set(args.line)-{l['id'] for l in lines}):p.error('Unknown line IDs')
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        p.error('Install optional local ASR dependencies: faster-whisper and av==16.1.0')
    model=WhisperModel(args.model,device='cpu',compute_type='int8',cpu_threads=4)
    rows=[]
    for l in lines:
        audio=lesson/l.get('audio',f"audio/tts/{l['id']}-{cfg['version']}.wav")
        segments,_=model.transcribe(str(audio),language='en',beam_size=5,vad_filter=False)
        recognized=' '.join(s.text.strip() for s in segments)
        row={'line':l['id'],'audio':str(audio),'audio_sha256':sha(audio),'expected':l['text'],'recognized':recognized,'wording_match':words(l['text'])==words(recognized)}
        rows.append(row)
        print(json.dumps(row,ensure_ascii=False),flush=True)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps({'reviewed_at':datetime.now(timezone.utc).isoformat(),'config':str(args.config),'config_sha256':sha(args.config),'model':'faster-whisper/'+args.model,'method':'local CPU int8, English, beam_size 5; not a substitute for full listening','lines':rows,'flagged_lines':[r['line'] for r in rows if not r['wording_match']]},ensure_ascii=False,indent=2)+'\n')


if __name__=='__main__':main()
