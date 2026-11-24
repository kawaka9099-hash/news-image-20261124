"""Hand the finished front-page image to the grader.

This script does no drawing. The picture (entry.png) is already rendered
and lives next to this file; the only job here is to place a copy of it
where the grader collects outputs.

The destination directory comes from the MAKEFUN_OUTPUT_DIR environment
variable and falls back to /output when that variable is not set. The
directory is created if it does not exist yet, and nothing else in it is
touched.
"""

import os
import shutil
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, out_dir / "entry.png")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
