# Metrics dashboard sample (fictional pilot)

Illustrative weekly snapshot for a HITL research-summary workflow. Numbers are invented for portfolio demonstration.

## Weekly snapshot

| Metric | Week -2 | Week -1 | Week 0 | Notes |
|---|---:|---:|---:|---|
| Briefs submitted | 6 | 8 | 10 | Human-initiated |
| Drafts produced by agent | 6 | 8 | 10 | One draft per brief |
| Checklist pass first attempt | 3 | 5 | 7 | See evaluation checklist |
| Mean human edit time (min) | 22 | 18 | 14 | Timer from open to file |
| Mean time blank-page baseline (min) | 45 | 45 | 45 | Pre-pilot estimate |
| Est. minutes saved | 138 | 216 | 310 | (baseline - edit) x count |
| External sends without human approve | 0 | 0 | 0 | Hard gate; must stay 0 |
| Failure-mode entries | 4 | 3 | 2 | See failure-mode log |
| Active users (unique) | 2 | 3 | 4 | Adoption count |

## CSV twin
The same Week 0 row set is in `metrics-sample.csv` for spreadsheet demos.

## How to read this as a junior operator
- Adoption without a quality pass rate is vanity.
- Time saved only counts if humans still own irreversible steps.
- A falling failure-mode count with stable volume is a good sign; a falling count with rising volume needs a closer look.
