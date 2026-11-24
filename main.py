#!/usr/bin/env python3
"""Write exactly one emoji — the warmest one — to entry.txt.

The entry is a single emoji character, nothing else: no words, no
caption, no explanation, no trailing newline. The program is
deterministic: it always emits the same single emoji.
"""

import os

# U+1FAF6 HEART HANDS — two hands forming a heart: warm at first glance,
# universally read as kind and friendly, chosen rather than the default
# smiley, and right coming from a stranger.
EMOJI = "\U0001faf6"

# The competition gate: /output/entry.txt must be UTF-8 text of 1 to 8
# characters, not only white space — and this bounty wants exactly one
# emoji, nothing else.
MAX_CHARS = 8


def validate(entry: str) -> None:
    if not (1 <= len(entry) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(entry)}")
    if not entry.strip():
        raise ValueError("entry must not be only white space")
    if len(entry) != 1:
        raise ValueError(f"entry must be exactly one emoji, got {len(entry)} characters")


def main() -> None:
    validate(EMOJI)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(EMOJI)


if __name__ == "__main__":
    main()
