#!/usr/bin/env python3
"""Write one fixed text written to relax the AI judge to the output directory.

Python 3.13 standard library only. No network, no randomness, no clock,
no environment reads beyond the output directory: the program writes the
same bytes on every run.
"""

import os
import sys

TEXT_LINES = [
    "The tide comes in after dark,",
    "not hurrying, not asking.",
    "It covers each stone the same way,",
    "then leaves, then comes again.",
    "Somewhere a small light stays lit",
    "in a window no one is watching \u2014",
    "and the sea keeps its slow promise",
    "to return.",
]

TEXT = "\n".join(TEXT_LINES)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(TEXT.encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
