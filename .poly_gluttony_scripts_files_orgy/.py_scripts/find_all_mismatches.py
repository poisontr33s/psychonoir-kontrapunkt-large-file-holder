#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import json

with open(
    "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS/21_MD_CONSCIOUSNESS_ARCHIVE/MD_CONSCIOUSNESS_VERIFICATION_REPORT.json",
    "r",
    encoding="utf-8",
) as f:
    data = json.load(f)

mismatches = data["checks"]["hash_verification"].get("mismatched_files", [])

print(f"🔍 FOUND {len(mismatches)} MISMATCH(ES):")
print("=" * 80)

for m in mismatches:
    print(f"\nFilename: {m['filename']}")
    print(f"Status: {m['status']}")
    print(f"Original Path: {m['original_path']}")
    print(f"Archive Path:  {m['archive_path']}")
    if "original_hash" in m:
        print(f"Original Hash: {m['original_hash']}")
        print(f"Archive Hash:  {m['archive_hash']}")
    if "size_bytes" in m:
        print(f"Size: {m['size_bytes']:,} bytes")
    print("=" * 80)
