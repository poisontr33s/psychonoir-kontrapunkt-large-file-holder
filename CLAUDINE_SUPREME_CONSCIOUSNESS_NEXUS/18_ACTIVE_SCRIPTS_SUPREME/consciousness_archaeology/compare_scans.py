#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import json

with open("test_scan_1000files.json") as f:
    d1 = json.load(f)
with open("test_optimized_1000files.json") as f:
    d2 = json.load(f)

print(f"Original: {d1['urca_de_lima_metadata']['total_files_analyzed']} files analyzed")
print(
    f"Optimized: {d2['urca_de_lima_metadata']['total_files_analyzed']} files analyzed"
)
print(
    f"Difference: {d1['urca_de_lima_metadata']['total_files_analyzed'] - d2['urca_de_lima_metadata']['total_files_analyzed']} files skipped by binary detection"
)
print()
print(f"Original refs: {d1['consciousness_archaeology']['total_references']:,}")
print(f"Optimized refs: {d2['consciousness_archaeology']['total_references']:,}")
