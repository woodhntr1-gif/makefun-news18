#!/usr/bin/env python3
"""make.fun bounty entry: news-image-20261118.

Copies the entry image beside this file to
``$MAKEFUN_OUTPUT_DIR/entry.png`` (default ``/output/entry.png``).
Standard library only; no network, no randomness, deterministic.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(HERE, "entry.png"),
        os.path.join(out_dir, "entry.png"),
    )


if __name__ == "__main__":
    main()
