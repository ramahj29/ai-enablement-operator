# Examples

Small, runnable sketches that back the docs. No secrets, no network calls.

| File | What it shows |
|---|---|
| [eval_score.py](eval_score.py) | Average checklist scores and a hold/share/retire decision |
| [workflow_state.py](workflow_state.py) | Legal transitions for a HITL research-summary workflow |
| [metrics-dashboard-sample.md](metrics-dashboard-sample.md) | Fictional adoption and time-saved snapshot |
| [metrics-sample.csv](metrics-sample.csv) | Same metrics as CSV |
| [failure-mode-log.md](failure-mode-log.md) | Example failure log used to improve prompts |

## Quick run
```bash
python3 examples/eval_score.py --scores 2,2,1,2,2,1,2,2
python3 examples/eval_score.py --scores 1,1,1,0 --hard-fail
python3 examples/workflow_state.py
```
