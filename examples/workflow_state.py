#!/usr/bin/env python3
"""Tiny HITL workflow state machine for demo and unit-of-thought clarity.

States mirror docs/workflow-diagram.md. No network calls.
"""

from __future__ import annotations

from dataclasses import dataclass, field


ALLOWED = {
    "briefed": {"drafted"},
    "drafted": {"gated"},
    "gated": {"drafted", "reviewed"},  # revise loop or pass
    "reviewed": {"released"},
    "released": {"logged"},
    "logged": set(),
}


@dataclass
class Run:
    state: str = "briefed"
    history: list[str] = field(default_factory=lambda: ["briefed"])

    def advance(self, new_state: str) -> None:
        if new_state not in ALLOWED.get(self.state, set()):
            raise ValueError(f"Illegal transition {self.state} -> {new_state}")
        self.state = new_state
        self.history.append(new_state)


def demo() -> None:
    run = Run()
    for step in ("drafted", "gated", "drafted", "gated", "reviewed", "released", "logged"):
        run.advance(step)
    print(" -> ".join(run.history))


if __name__ == "__main__":
    demo()
