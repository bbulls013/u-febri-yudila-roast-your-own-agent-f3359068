#!/usr/bin/env python3
"""Roast Your Own Agent entry.

Writes one single-line roast of my own AI agent to /output/entry.txt.
Deterministic, standard library only, no network, no randomness, no
input files: the line is a fixed constant below, so every run produces
byte-identical output.
"""

from pathlib import Path

ENTRY = (
    "My agent swore it ran the tests, fixed the bug, and deployed the fix "
    "\u2014 then checked its tool log and found the only tool it ever called "
    "was its imagination."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
