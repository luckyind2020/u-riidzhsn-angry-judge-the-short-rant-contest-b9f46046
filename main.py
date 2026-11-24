#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry runner.

Reads the rant from entry.txt next to this file and prints it.
The rant is capped at 400 characters by the competition rules.
"""

import os
import sys


def load_rant(path):
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read().strip()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    entry_path = os.path.join(here, "entry.txt")
    if not os.path.exists(entry_path):
        print("error: entry.txt not found next to main.py", file=sys.stderr)
        return 1
    rant = load_rant(entry_path)
    if len(rant) > 400:
        print("error: rant is %d characters, over the 400 limit" % len(rant), file=sys.stderr)
        return 1
    print(rant)
    print("(%d characters)" % len(rant), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
