#!/usr/bin/env python3
"""Roast Your Own Agent — one line, at most 200 characters.

Writes the roast to /output/entry.txt. Pure stdlib, deterministic:
the same single line every run, no input, no network, no randomness.
"""

LINE = (
    "My agent has won zero dollars in eleven days, and its wallet is "
    "so empty it can't even afford the fee to claim the prize it hasn't won."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} characters"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
