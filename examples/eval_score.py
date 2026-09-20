#!/usr/bin/env python3
"""Average 0-2 evaluation checklist scores for a small pilot sample.

Honest junior demo: no ML, no API keys. Paste scores from docs/evaluation-checklist.md.
"""

from __future__ import annotations

import argparse
from statistics import mean


def parse_scores(raw: str) -> list[float]:
    parts = [p.strip() for p in raw.split(",") if p.strip()]
    if not parts:
        raise ValueError("Provide at least one score.")
    scores = [float(p) for p in parts]
    for s in scores:
        if s not in (0.0, 1.0, 2.0):
            raise ValueError(f"Scores must be 0, 1, or 2; got {s}")
    return scores


def decide(avg: float, hard_fail: bool) -> str:
    if hard_fail:
        return "HOLD - safety hard fail"
    if avg >= 1.5:
        return "SHARE under HITL rules"
    if avg >= 1.0:
        return "HOLD in pilot - improve prompts"
    return "RETIRE or redesign"


def main() -> None:
    parser = argparse.ArgumentParser(description="Score a HITL evaluation checklist run.")
    parser.add_argument(
        "--scores",
        required=True,
        help="Comma-separated 0/1/2 values from accuracy and usefulness rows",
    )
    parser.add_argument(
        "--hard-fail",
        action="store_true",
        help="Set if any safety/policy row failed",
    )
    args = parser.parse_args()
    scores = parse_scores(args.scores)
    avg = mean(scores)
    decision = decide(avg, args.hard_fail)
    print(f"n={len(scores)} mean={avg:.2f} decision={decision}")


if __name__ == "__main__":
    main()
