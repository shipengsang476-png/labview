#!/usr/bin/env python3
"""Verify file sizes and SHA-256 hashes listed in ../manifest.csv."""

from __future__ import annotations

import csv
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "manifest.csv"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    failures: list[str] = []
    checked = 0
    with MANIFEST.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            rel = row["relative_path"]
            path = ROOT / rel
            if not path.is_file():
                failures.append(f"MISSING  {rel}")
                continue
            actual_size = path.stat().st_size
            actual_hash = sha256(path)
            if actual_size != int(row["size_bytes"]):
                failures.append(f"SIZE     {rel}: {actual_size} != {row['size_bytes']}")
            if actual_hash.lower() != row["sha256"].lower():
                failures.append(f"SHA256   {rel}: {actual_hash} != {row['sha256']}")
            checked += 1

    if failures:
        print("Manifest verification failed:")
        for failure in failures:
            print(f"  {failure}")
        return 1

    print(f"Verified {checked} files successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
