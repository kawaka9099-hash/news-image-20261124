#!/usr/bin/env python3
"""Entry point for the make.fun news-image-20261124 submission.

Standard library only. Copies the pre-rendered front page (entry.png,
bundled next to this file) to the output path the grader asks for:

  1. argv[1] when given,
  2. else $MAKEFUN_OUTPUT_DIR/entry.png,
  3. else /output/entry.png.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def output_path():
    if len(sys.argv) > 1:
        return sys.argv[1]
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.png")
    return "/output/entry.png"


def main():
    dest = output_path()
    parent = os.path.dirname(dest)
    if parent:
        os.makedirs(parent, exist_ok=True)
    shutil.copyfile(SRC, dest)
    print("wrote", dest)


if __name__ == "__main__":
    main()
