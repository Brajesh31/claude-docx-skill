#!/usr/bin/env python3
"""List package parts and relationship files in a DOCX archive."""

from __future__ import annotations
import argparse
import zipfile
from pathlib import Path

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    args = parser.parse_args()
    if not args.file.is_file() or not zipfile.is_zipfile(args.file):
        parser.error("Expected a valid ZIP-based DOCX file")
    with zipfile.ZipFile(args.file) as zf:
        for name in sorted(zf.namelist()):
            kind = "relationship" if name.endswith(".rels") else "part"
            print(f"{kind:14} {name}")
        print(f"Total entries: {len(zf.namelist())}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
