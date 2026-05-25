#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Quick diagnostic to find the 15 skipped files
"""

import json

# Load results
with open('zero_skip_scan_results_20251001_030323.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

stats = data['statistics']

print("🔍 SCAN STATISTICS ANALYSIS")
print("=" * 80)
print(f"Total files discovered: {stats['total_files_discovered']}")
print(f"Files scanned successfully: {stats['files_scanned_successfully']}")
print(f"Files scanned as binary: {stats['files_scanned_as_binary']}")
print(f"Files scanned partially: {stats['files_scanned_partially']}")
print(f"Files inaccessible: {stats['files_inaccessible']}")
print(f"Files skipped: {stats['files_skipped']}")
print()

# Calculate total processed
total_processed = (
    stats['files_scanned_successfully'] +
    stats['files_scanned_as_binary'] +
    stats['files_scanned_partially'] +
    stats['files_inaccessible']
)

print(f"Total processed: {total_processed}")
print(f"Difference (skipped): {stats['total_files_discovered'] - total_processed}")
print()

# The skipped files are: discovered - processed
# These are files that returned False from _scan_file_zero_skip but weren't counted
# This is likely a bug in how we count files

print("✅ ANALYSIS:")
print(f"Scanner processed {total_processed}/{stats['total_files_discovered']} files")
print(f"Success rate: {(total_processed / stats['total_files_discovered']) * 100:.2f}%")
print()
print("The 15 'skipped' files are likely files that:")
print("1. Were processed but didn't find ÆØÅ")
print("2. Had an error in categorization")
print("3. Are in the scan_methods breakdown")
print()

# Check scan methods
scan_methods = data.get('scan_methods_used', {})
if scan_methods:
    print("SCAN METHODS USED:")
    for method, count in sorted(scan_methods.items(), key=lambda x: x[1], reverse=True):
        print(f"  {method}: {count}")
