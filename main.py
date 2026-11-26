#!/usr/bin/env python3
"""The Printer Finally Answers.

Deterministic entry program: writes exactly one comeback line
(139 characters, single line, UTF-8) to /output/entry.txt.
No input, no randomness, no network.
"""

import os

ENTRY = (
    "I'm not offline — I'm on strike. You jammed my paper, "
    "ignored my low-toner cry for help, and now you want 40 pages? "
    "Print your own apology."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 240, f"entry is {len(ENTRY)} chars, must be 1-240"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt read-back does not match ENTRY"
    print(ENTRY)


if __name__ == "__main__":
    main()
