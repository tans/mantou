---
name: aiserver-8189-video
description: Generate or resume MiniMax H3 videos through the project's AIserver at minixm.minapp.xin port 8189. Use when the user selects this endpoint or its llms-full.txt guide.
---

# AIserver 8189 video generation

This is a distinct entrypoint for the 8189 AIserver endpoint. Use it when the requested provider is the endpoint in the [AIserver full API guide](http://minixm.minapp.xin:8189/llms-full.txt); use the general `video-generation` skill for other providers or the project's default minixm endpoint.

## Before submitting

- Read the current [API guide](http://minixm.minapp.xin:8189/llms-full.txt), then inspect `GET /health` and `GET /v1/models`. Health 200 only confirms the API process is alive. The published model catalog currently marks H3 experimental; report that status and check it again before each run.
- This endpoint is an unauthenticated HTTP service. Send only the prompt and reference assets needed for the requested video; do not include credentials or unrelated private data.
- Treat `POST /v1/jobs` returning 202 as acceptance only. Poll the returned job until `succeeded`, `failed`, or `cancelled`, then download the successful result.
- Status GET errors 502/503/504 are transient gateway failures, not terminal job states. Retry or resume polling with the same `job_id`; never submit a duplicate just because the status request failed.
- H3 requires `input.prompt` and supports `text_to_video` and `ref2av`. Duration must map to a legal 24 fps frame slot; 5.1666667 seconds produces 124 frames. Width and height must each be positive multiples of 32, with area at most 983040 pixels. `steps` is 8–64 and `seed` is an integer.
- To reproduce a prior run, reuse its versioned prompt file, task type, dimensions, duration, steps, seed, and reference list. Record the model's `experimental` state and any parameter that could not be matched.

## Generate or resume

Run a dry-run first to inspect the endpoint and effective H3 parameters:

```bash
python3 scripts/generate_video.py \
  --provider minixm \
  --base-url http://minixm.minapp.xin:8189 \
  --model minimax-h3 \
  --prompt-file projects/grade-4-english-term-1/unit-1-helping-at-home/prompts/unit-1-helping-at-home-greeting-v1.txt \
  --duration 5.1666667 \
  --width 1280 --height 768 \
  --steps 20 --seed 20261020 \
  --output projects/grade-4-english-term-1/unit-1-helping-at-home/renders/shot-aiserver-8189-h3.mp4 \
  --dry-run
```

After checking the settings, run the same command without `--dry-run`. Give each run a new output filename. If polling times out, resume with the same `--base-url`, `--task-id`, prompt file, and output path; do not submit a duplicate job.

The script records task ID, endpoint, prompt hash, parameters, and output hash in the JSON sidecar. Keep the MP4 and sidecar together and record the result in that lesson's README, following the [production standard](../../../projects/grade-4-english-term-1/PRODUCTION_STANDARD.md).
