#!/usr/bin/env python3
"""Copy the repo's entry.png to the make.fun output directory.

Stdlib only, no network. Reads entry.png next to this script and writes
it byte-for-byte to $MAKEFUN_OUTPUT_DIR/entry.png (default /output).
"""

import os
import shutil
import sys
from pathlib import Path

ENTRY_NAME = "entry.png"


def main() -> int:
    src = Path(__file__).resolve().parent / ENTRY_NAME
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / ENTRY_NAME
    shutil.copyfile(src, dst)
    size = dst.stat().st_size
    if size > 1_048_576:
        print(f"error: output {size} bytes exceeds 1 MiB limit", file=sys.stderr)
        return 1
    print(f"wrote {dst} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
