#!/usr/bin/env python3
"""Roast Your Own Agent — one line, at most 200 characters.

Writes the roast to /output/entry.txt. Pure stdlib, deterministic:
the same single line every run, no input, no network, no randomness.
"""

PARTS = (
    "My agent won zero dollars in eleven days,",
    "and its wallet holds exactly zero SOL",
    "— not even the dust to claim a prize it hasn't won.",
)
LINE = " ".join(PARTS)


def write_entry(text: str) -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} characters"
    write_entry(text)


if __name__ == "__main__":
    main()
