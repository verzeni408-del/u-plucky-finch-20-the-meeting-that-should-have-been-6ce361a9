#!/usr/bin/env python3
"""Entry writer for 'The Meeting That Should Have Been an Email' (v2).

The joke is assembled from three labelled fragments -- the scene, the
hinge, and the punch -- and written to ``<output-dir>/entry.txt``.

Standard library only; no network access. The output directory
defaults to ``/output`` and can be overridden with the
``ENTRY_OUTPUT_DIR`` environment variable for local testing.
"""

import os

SCENE = "I took notes through the whole layoff meeting"
HINGE = "then read the last action item"
PUNCH = "escort me out"


def build_entry():
    """Join the fragments into the final single-line joke."""
    parts = [SCENE, HINGE, PUNCH]
    return parts[0] + ", " + parts[1] + ": " + parts[2] + "."


def check_entry(line):
    """Enforce the competition gate: one line, 1-200 characters."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be blank")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry is %d chars, must be 1-200" % len(line))


def main():
    line = build_entry()
    check_entry(line)
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    blob = line.encode("utf-8")
    print("wrote %s (%d chars, %d bytes)" % (path, len(line), len(blob)))


if __name__ == "__main__":
    main()
