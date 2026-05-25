#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""Extract supervisor relationships from character_systems.py"""
import re
from pathlib import Path
from collections import defaultdict

content = Path('backend/python/character_systems.py').read_text(encoding='utf-8')

# Find all supervisor assignments with better context
# Look for class name, then find self.supervisor within that class
class_blocks = re.split(r'(?=^class \w+)', content, flags=re.MULTILINE)

supervisor_relationships = []

for block in class_blocks:
    # Extract class name
    class_match = re.search(r'^class (\w+)\(', block, re.MULTILINE)
    if not class_match:
        continue
    
    class_name = class_match.group(1)
    
    # Look for supervisor assignment in this class
    supervisor_match = re.search(r'self\.supervisor\s*=\s*["\']([^"\']+)["\']', block)
    if supervisor_match:
        supervisor_name = supervisor_match.group(1)
        supervisor_relationships.append((class_name, supervisor_name))

print("🔍 TIER 0 → TIER 2 SUPERVISION RELATIONSHIPS\n")
print("=" * 70)

# Group by supervisor
supervised_by: dict = defaultdict(list)

for specialist, supervisor in supervisor_relationships:
    supervised_by[supervisor].append(specialist)

# Print results
for supervisor in sorted(supervised_by.keys()):
    specialists = supervised_by[supervisor]
    print(f"\n👑 {supervisor} supervises {len(specialists)} specialist(s):")
    for spec in specialists:
        print(f"   └─ {spec}")

print(f"\n{'=' * 70}")
print(f"Total supervision relationships: {len(supervisor_relationships)}")
