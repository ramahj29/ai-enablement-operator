# Example HITL workflow (research summary)

Fictional internal workflow: turn a short brief plus allowed source notes into a first-pass summary for human review.

```mermaid
flowchart TD
  A[Human: write brief and attach allowed sources] --> B[Agent: draft outline]
  B --> C{Quality gate: checklist}
  C -->|Fail| D[Agent: revise with failure notes]
  D --> C
  C -->|Pass| E[Human: review and edit]
  E --> F{Irreversible?}
  F -->|Yes: send externally| G[Human: approve and send]
  F -->|No: file internally| H[Human: file to shared folder]
  G --> I[Log outcome and metrics]
  H --> I
  I --> J[Update failure-mode log if needed]
```

## State labels (for a simple runbook)
| State | Owner | Exit condition |
|---|---|---|
| `briefed` | Human | Brief and sources attached |
| `drafted` | Agent | Draft written |
| `gated` | Agent + checklist | Checklist pass or revise loop |
| `reviewed` | Human | Edits complete |
| `released` | Human | Filed or sent |
| `logged` | Either | Metrics and failures recorded |

A tiny state-machine sketch is in `examples/workflow_state.py`.
