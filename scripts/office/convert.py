#!/usr/bin/env python3
"""Convert DOCX or legacy DOC files with a locally installed LibreOffice executable."""

from __future__ import annotations
import argparse
import shutil
import subprocess
from pathlib import Path

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--to", choices=("docx", "pdf", "odt", "html"), default="pdf")
    parser.add_argument("--output-dir", type=Path, default=Path("converted"))
    args = parser.parse_args()
    if not args.input.is_file():
        parser.error(f"Input not found: {args.input}")
    office = shutil.which("libreoffice") or shutil.which("soffice")
    if not office:
        parser.error("LibreOffice/soffice is not installed or not on PATH")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    command = [office, "--headless", "--convert-to", args.to, "--outdir", str(args.output_dir), str(args.input)]
    result = subprocess.run(command, text=True, capture_output=True)
    if result.returncode:
        print(result.stderr.strip() or result.stdout.strip())
        return result.returncode
    expected = args.output_dir / f"{args.input.stem}.{args.to}"
    if not expected.exists():
        print("Conversion command completed, but expected output was not found.")
        return 1
    print(expected)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
