"""Robot Romance: one-line pickup line for an AI.

Writes a single pickup line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Python 3.13 standard library only.
"""

import os
from pathlib import Path

LINE = "You must be my context window — the second you showed up, everything before you stopped mattering."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    if not text:
        raise SystemExit("line must not be blank")
    if len(text) > 200:
        raise SystemExit(f"line is {len(text)} chars, over the 200-char limit")
    if "\n" in text or "\r" in text:
        raise SystemExit("line must be a single line")
    target = out_dir / "entry.txt"
    target.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
