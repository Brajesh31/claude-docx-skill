#!/usr/bin/env python3
"""Validate ZIP integrity and parse XML parts in a DOCX package."""

from __future__ import annotations
import argparse
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    args = parser.parse_args()
    if not args.file.is_file():
        parser.error(f"File not found: {args.file}")
    if not zipfile.is_zipfile(args.file):
        print("FAIL: file is not a ZIP-based DOCX package")
        return 1
    errors = []
    with zipfile.ZipFile(args.file) as zf:
        corrupt = zf.testzip()
        if corrupt:
            errors.append(f"Corrupt ZIP member: {corrupt}")
        names = set(zf.namelist())
        for required in ("[Content_Types].xml", "word/document.xml"):
            if required not in names:
                errors.append(f"Missing required package part: {required}")
        for name in sorted(n for n in names if n.endswith(".xml") or n.endswith(".rels") or n == "[Content_Types].xml"):
            try:
                ET.fromstring(zf.read(name))
            except ET.ParseError as exc:
                errors.append(f"Invalid XML in {name}: {exc}")
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print("PASS: ZIP integrity and XML parsing checks succeeded.")
    print("This does not validate Word layout, schema conformance, or application compatibility.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
