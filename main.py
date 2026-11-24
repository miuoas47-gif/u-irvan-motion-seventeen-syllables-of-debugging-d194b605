#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

Writes one haiku about debugging to entry.txt inside the output
directory named by MAKEFUN_OUTPUT_DIR (falling back to /output).

The haiku, in the 5-7-5 syllable shape:

    Cursor blinks at three          (5)
    stack trace spills down the dark screen  (7)
    the fix breaks it more          (5)

A cursor blinking at three in the morning and a stack trace
spilling down a dark screen are the concrete centre; the last
line turns the poem -- the fix itself makes things worse, which
is the truest moment in debugging. Syllables were counted word
by word (cur-sor / blinks / at / three = 5; stack / trace /
spills / down / the / dark / screen = 7; the / fix / breaks /
it / more = 5). Stdlib only, no network, no arguments,
deterministic: every run writes the exact same bytes.
"""

import os
import sys

HAIKU = (
    "Cursor blinks at three\n"
    "stack trace spills down the dark screen\n"
    "the fix breaks it more"
)

OUTPUT_FILENAME = "entry.txt"
MAX_CHARS = 200


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, OUTPUT_FILENAME)

    if not HAIKU or not HAIKU.strip():
        print("error: haiku is empty or only whitespace", file=sys.stderr)
        return 1
    if len(HAIKU) > MAX_CHARS:
        print("error: haiku is %d characters, over the %d cap"
              % (len(HAIKU), MAX_CHARS), file=sys.stderr)
        return 1
    if len(HAIKU.splitlines()) != 3:
        print("error: haiku is not three lines", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(HAIKU)

    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != HAIKU:
        print("error: entry.txt does not match the haiku", file=sys.stderr)
        return 1

    print("wrote %s (%d characters)" % (path, len(HAIKU)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
