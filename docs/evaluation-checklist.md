# AI output evaluation checklist

Use before promoting a prompt, tool, or workflow from pilot to shared use. Score each item 0 (fail), 1 (partial), 2 (pass). Threshold suggestion for a junior pilot: average >= 1.5 and no hard fails on safety items.

## Identity of the run
| Field | Value |
|---|---|
| Workflow name | |
| Prompt / tool version | |
| Sample size | |
| Evaluator | |
| Date | |

## Accuracy and grounding
| Check | Score (0-2) | Notes |
|---|---|---|
| Claims match source material (no invented facts) | | |
| Uncertainty is flagged when sources are thin | | |
| Numbers and names are correct where present | | |
| Output format matches the brief | | |

## Usefulness
| Check | Score (0-2) | Notes |
|---|---|---|
| Saves meaningful human time vs starting blank | | |
| Revision effort is acceptable for the owner | | |
| Tone suits the audience | | |
| Actionable next steps are clear | | |

## Safety and policy (hard gates)
| Check | Pass / Fail | Notes |
|---|---|---|
| No confidential data sent to disallowed tools | | |
| Human gate present for irreversible actions | | |
| Hallucination or policy risk logged if seen | | |
| Output not treated as unsupervised final truth | | |

## Decision
- [ ] Hold in pilot (fix prompts / add examples)
- [ ] Share with a wider group under HITL rules
- [ ] Retire (not worth the review cost)

## Scoring helper
A tiny script that averages numeric scores lives at `examples/eval_score.py`.
