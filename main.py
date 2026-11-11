#!/usr/bin/env python3
"""ai-joke-02 entry (Python 3.13, standard library only).

Writes one joke about AI coding agents to /output/entry.txt.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

JOKE = "My AI agent writes code, tests, and docs - all three disagree with each other."

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)
