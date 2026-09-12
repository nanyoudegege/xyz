#!/usr/bin/env python3
"""Validate public progress metadata without requiring source PDFs."""
from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
progress = list(csv.DictReader((ROOT / "progress" / "progress.csv").open(encoding="utf-8")))
ranges = list(csv.DictReader((ROOT / "progress" / "page_status.csv").open(encoding="utf-8")))

covered = []
for row in ranges:
    start, end = int(row["pdf_start"]), int(row["pdf_end"])
    assert 1 <= start <= end <= 592, row
    covered.extend(range(start, end + 1))
assert covered == list(range(1, 593)), "page ranges must cover 1..592 exactly once and in order"

assert len({row["version"] for row in progress}) == len(progress), "duplicate version"
for row in progress:
    sha = row["sha256"].lower()
    assert len(sha) == 64 and all(c in "0123456789abcdef" for c in sha), row["version"]
    zero_ink = int(row["zero_ink"])
    assert zero_ink >= 0, row["version"]
    if zero_ink:
        assert "deferred" in row["status"], (
            f"{row['version']} has conservative-mask misses but is not marked deferred"
        )

latest = progress[-1]["version"] if progress else "none"
print(f"OK: {len(progress)} checkpoints; {len(ranges)} ranges covering 592 pages; latest={latest}")
