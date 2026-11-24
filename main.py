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


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(EMOJI)


if __name__ == "__main__":
    main()
