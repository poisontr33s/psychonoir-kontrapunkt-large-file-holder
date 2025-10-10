#!/usr/bin/env python3
"""Quick script to extract size_exceeds_limit files"""
import json

with open('SKIPPED_FILES_DIRECT_IDENTIFICATION.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

size_files = [f for f in data.get('skipped_files', []) if 'size_exceeds_limit' in f.get('reason', '')]

print(f"Found {len(size_files)} size_exceeds_limit files:\n")
for file_info in size_files:
    print(f"  {file_info['filename']}")
    print(f"    Full Path: {file_info['file']}")
    print(f"    Size: {file_info['size_mb']:.2f} MB")
    print(f"    Reason: {file_info['reason']}\n")
