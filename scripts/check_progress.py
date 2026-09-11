#!/usr/bin/env python3
"""Validate public progress metadata without requiring source PDFs."""
from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
progress = list(csv.DictReader((ROOT / "progress" / "progress.csv").open(encoding="utf-8")))
ranges = list(csv.DictReader((ROOT / "progress" / "page_status.csv").open(encoding="utf-8")))
covered = []
for r in ranges:
    a, b = int(r["pdf_start"]), int(r["pdf_end"])
    assert 1 <= a <= b <= 592, r
    covered.extend(range(a, b + 1))
assert covered == list(range(1, 593)), "page ranges must cover 1..592 exactly once and in order"
assert len({r["version"] for r in progress}) == len(progress), "duplicate version"
for r in progress:
    assert len(r["sha256"]) == 64 and all(c in "0123456789abcdef" for c in r["sha256"].lower()), r["version"]
    assert int(r["zero_ink"]) == 0, f"nonzero zero-ink count at {r['version']}"
print(f"OK: {len(progress)} checkpoints; {len(ranges)} ranges covering 592 pages")
