#!/usr/bin/env python3
"""Entry generator for the make.fun one-liner competition."""

from pathlib import Path

ENTRY = "I declined the recurring meeting once, and it rescheduled itself as my performance review."
OUTPUT_PATH = Path("/output/entry.txt")


def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY + "\n", encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
