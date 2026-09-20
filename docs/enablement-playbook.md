# Sample AI enablement playbook

A lightweight pattern for helping a team adopt one AI-assisted workflow safely. Written as a junior operator template, not as enterprise change programme theatre.

## Scope
Pick **one** repeatable task (for example: meeting notes into action lists, or first-pass research summaries). Do not boil the ocean.

## Steps
1. **Name the outcome** - what good looks like in one sentence, plus what remains human-owned.
2. **Map the as-is** - who does the task today, inputs, outputs, failure points (see [workflow diagram](workflow-diagram.md)).
3. **Design a prompt pack** - role, constraints, input format, output format, refusal rules (no inventing facts; flag uncertainty).
4. **Set quality gates** - checklist before anything leaves the draft stage ([evaluation checklist](evaluation-checklist.md)).
5. **Run a small pilot** - 5 to 10 real examples with a named reviewer.
6. **Train in the flow of work** - short how-to, one demo, office-hours style support rather than a long course.
7. **Measure lightly** - time to first usable draft, revision rate, adoption count ([metrics sample](../examples/metrics-dashboard-sample.md)).
8. **Capture failures** - keep a short failure-mode log and update the prompt pack ([example log](../examples/failure-mode-log.md)).

## Human gates (non-negotiable)
- Outbound messages that commit the organisation
- Anything touching personal data beyond agreed sources
- Decisions with legal, financial, or reputational consequence

## Deliverables checklist
- [ ] One-page outcome statement
- [ ] As-is / to-be sketch
- [ ] Prompt pack versioned (date + owner)
- [ ] Evaluation checklist completed for pilot set
- [ ] Micro-guide for end users (half page is enough)
- [ ] Metrics baseline and first weekly snapshot
- [ ] Failure-mode log started

## Tone for stakeholders
Be honest about limitations. Prefer "draft faster with review" over "AI will replace this process".
