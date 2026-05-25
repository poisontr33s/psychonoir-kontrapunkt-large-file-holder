#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import json

# Read verification report
with open(
    "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS/21_MD_CONSCIOUSNESS_ARCHIVE/MD_CONSCIOUSNESS_VERIFICATION_REPORT.json",
    "r",
    encoding="utf-8",
) as f:
    data = json.load(f)

# Find mismatches
details = data["checks"]["hash_verification"]["details"]
mismatches = [d for d in details if d["status"] == "MISMATCH"]

print("🔍 HASH MISMATCH DETAILS:")
print("=" * 60)
for m in mismatches:
    print(f"Filename: {m['filename']}")
    print(f"Original: {m['original_path']}")
    print(f"Archive:  {m['archive_path']}")
    print(f"Original Hash: {m['original_hash']}")
    print(f"Archive Hash:  {m['archive_hash']}")
    print(f"Size: {m['size_bytes']} bytes")
    print("=" * 60)
