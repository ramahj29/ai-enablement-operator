# Agent runbook template

Copy this page for each workflow. Keep it short enough that a tired human can still follow it.

## Metadata
| Field | Value |
|---|---|
| Workflow name | |
| Owner (human) | |
| Agent role | Draft / prepare only |
| Last updated | |
| Prompt pack version | |

## Purpose
One sentence: what the agent is allowed to accelerate.

## Inputs
- Required fields:
- Allowed data sources:
- Explicitly forbidden sources:

## Steps the agent may take
1.
2.
3.

## Steps reserved for humans
-
-
-

## Quality gate
Link or paste the evaluation checklist items that must pass before handoff.

## Failure handling
| Symptom | First action | Escalate when |
|---|---|---|
| Empty or truncated draft | Re-run once with same inputs | Second empty result |
| Invented citations | Discard draft; log failure mode | Recurs across samples |
| Tool / API timeout | Retry with backoff; note time | Three failures in a session |
| Captcha / identity challenge | Stop; human takes over | Always |

## Observability
- Where runs are logged:
- Where metrics are updated:
- Where failure modes are recorded:

## Roll-back
How to disable the agent path and return to the manual process:
