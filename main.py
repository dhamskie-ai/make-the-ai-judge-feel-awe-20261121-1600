#!/usr/bin/env python3
"""Entry for make-the-ai-judge-feel-awe-20261121-1600.

Writes a single short text to /output/entry.txt (or to the directory
named by MAKEFUN_OUTPUT_DIR). Python 3.13 standard library only.
"""

import os
from pathlib import Path

ENTRY = (
    # The text is fixed: exactly 234 characters, no trailing newline.
    "The tide comes in after dark,\n"
    "not hurrying, not asking.\n"
    "It covers each stone the same way,\n"
    "then leaves, then comes again.\n"
    "Somewhere a small light stays lit\n"
    "in a window no one is watching \u2014\n"
    "and the sea keeps its slow promise\n"
    "to return."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
