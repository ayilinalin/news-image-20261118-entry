#!/usr/bin/env python3
"""news-image-20261118 entry.

Copies the bundled front-page image (entry.png, in this repository) to
$MAKEFUN_OUTPUT_DIR/entry.png. Standard library only, no network, fully
deterministic: the same bytes are written on every run.
"""

import os
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"
OUTPUT_NAME = "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576
MAX_DIMENSION = 1024


def check_image(data: bytes) -> str | None:
    """Return an error message if the bundled image breaks the gate, else None."""
    if not data.startswith(PNG_MAGIC):
        return "bundled image is not a PNG"
    if len(data) > MAX_BYTES:
        return f"bundled image is {len(data)} bytes, over the 1 MiB limit"
    return None


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    here = Path(__file__).resolve().parent
    source = here / SOURCE_NAME
    if not source.is_file():
        print(f"error: bundled image not found: {source}", file=sys.stderr)
        return 1

    data = source.read_bytes()
    problem = check_image(data)
    if problem is not None:
        print(f"error: {problem}", file=sys.stderr)
        return 1

    dest_dir = Path(out_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / OUTPUT_NAME

    dest.write_bytes(data)
    os.chmod(dest, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
