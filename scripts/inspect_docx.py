#!/usr/bin/env python3
"""Print DOCX package parts and basic document counts."""

from __future__ import annotations
import argparse
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    args = parser.parse_args()
    if not args.file.is_file():
        parser.error(f"File not found: {args.file}")
    if not zipfile.is_zipfile(args.file):
        print("Invalid DOCX package: not a ZIP archive.")
        return 1
    with zipfile.ZipFile(args.file) as zf:
        bad = zf.testzip()
        if bad:
            print(f"Corrupt ZIP member: {bad}")
            return 1
        names = zf.namelist()
        print("Package parts:")
        for name in names:
            print(f"- {name}")
        if "word/document.xml" not in names:
            print("Missing word/document.xml")
            return 1
        root = ET.fromstring(zf.read("word/document.xml"))
        print(f"Paragraphs: {len(root.findall('.//w:p', NS))}")
        print(f"Tables: {len(root.findall('.//w:tbl', NS))}")
        print(f"Tracked insertions: {len(root.findall('.//w:ins', NS))}")
        print(f"Tracked deletions: {len(root.findall('.//w:del', NS))}")
        print(f"Comment range starts: {len(root.findall('.//w:commentRangeStart', NS))}")
        print(f"Inline drawings: {len(root.findall('.//w:drawing', NS))}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
