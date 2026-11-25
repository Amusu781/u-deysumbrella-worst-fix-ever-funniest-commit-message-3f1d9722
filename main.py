#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes a single commit message to /output/entry.txt.
Standard library only; no network access at grade time.

The line plays on relocation rather than the obvious angles: the fix
did not revert anything or ship untested code, it simply chased the bug
out of login and into billing, where it now costs money.
"""

import os

ENTRY = "fix: evicted the bug from login, it moved into billing"
OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    # Create the output directory first; never delete the directory
    # itself, only clear its contents.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        # Gate: 1 to 100 characters, not only whitespace, single line.
        assert 1 <= len(ENTRY) <= 100 and ENTRY.strip(), "entry fails gate"
        assert "\n" not in ENTRY, "entry must be a single line"
        f.write(ENTRY)


if __name__ == "__main__":
    main()
