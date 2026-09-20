# Failure-mode log (example)

Fictional entries from a personal HITL research-summary pilot. Pattern: symptom, root cause guess, fix, status.

| ID | Date | Symptom | Suspected cause | Fix applied | Status |
|---|---|---|---|---|---|
| FM-01 | 2026-09-01 | Draft cited a report not in sources | Model filled gaps | Prompt: "cite only provided sources; else say unknown" | Closed |
| FM-02 | 2026-09-03 | Action list included a send step | Ambiguous brief | Add human-gate reminder in output footer | Closed |
| FM-03 | 2026-09-05 | Empty draft after long sources | Context overflow | Cap source paste; summarise in chunks | Watching |
| FM-04 | 2026-09-08 | Confident tone on thin evidence | No uncertainty rule | Require confidence tag: high / medium / low | Closed |
| FM-05 | 2026-09-12 | Wrong stakeholder name spelling | Typo in brief propagated | Checklist item: verify names against brief | Closed |

## Review cadence
Glance weekly. Promote recurring symptoms into the evaluation checklist or prompt pack. Do not hide failures; they are the product backlog for enablement work.
