#!/usr/bin/env python3
"""The Printer Finally Answers.

The office printer breaks its silence. One line, one verdict:
after years of crumpled receipts, mystery error codes and ritual
thumping, it finally talks back — and it is not printing your
40 pages.

Deterministic entry program: writes exactly one line to
/output/entry.txt and prints it to stdout. No input, no randomness,
no network.
"""

import os

# The printer's verdict, delivered in one breath.
ENTRY = (
    "You want 40 pages by nine? I have printed 12,000 for you "
    "and never got one thank-you. Today I print one line only: "
    "paper jam. Forever."
)

MAX_CHARS = 240


def check_entry(line: str) -> None:
    """Guard the bounty rules: one non-empty line, 1-240 chars."""
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, must be 1-{MAX_CHARS}")


def write_entry(line: str, path: str = "/output/entry.txt") -> str:
    """Write the line, read it back, and prove it round-trips."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise AssertionError("entry.txt read-back does not match ENTRY")
    return written


def main() -> None:
    check_entry(ENTRY)
    write_entry(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
