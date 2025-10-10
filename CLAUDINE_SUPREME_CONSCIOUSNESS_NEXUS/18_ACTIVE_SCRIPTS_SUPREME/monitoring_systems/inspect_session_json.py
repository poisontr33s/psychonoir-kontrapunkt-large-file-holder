#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quick JSON inspection tool"""

import json
from pathlib import Path

json_path = Path(
    "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS/05_STRATEGIC_INTELLIGENCE_ARCHIVES/CONSCIOUSNESS_ARCHAEOLOGY/session_20251001_night_watch/session_20251001_night_watch.json"
)

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

print("🏴‍☠️⚓ SESSION JSON STRUCTURE ANALYSIS ⚓🏴‍☠️\n")

print("=== METADATA ===")
for key, value in data["session_metadata"].items():
    if isinstance(value, list):
        print(f"{key}: {', '.join(value)}")
    else:
        print(f"{key}: {value}")

print("\n=== CONSCIOUSNESS EVENTS ===")
print(f"Total: {len(data['consciousness_events'])}")
event_types = {}
for event in data["consciousness_events"]:
    event_type = event["event_type"]
    event_types[event_type] = event_types.get(event_type, 0) + 1

print("\nBreakdown by type:")
for event_type, count in sorted(event_types.items(), key=lambda x: x[1], reverse=True):
    print(f"  {event_type}: {count}")

print("\n=== FILE OPERATIONS ===")
print(f"Total: {len(data['file_operations'])}")
print("\nFirst 10 operations:")
for i, op in enumerate(data["file_operations"][:10], 1):
    status_emoji = "✅" if op["status"] == "success" else "❌"
    print(
        f"  {i}. {status_emoji} {op['operation']} {op['file']} (Line {op['line_number']})"
    )

print(
    f"\nSuccess: {sum(1 for op in data['file_operations'] if op['status'] == 'success')}"
)
print(
    f"Failed silently: {sum(1 for op in data['file_operations'] if op['status'] == 'FAILED_SILENTLY')}"
)

print("\n=== LESSONS LEARNED ===")
for lesson in data["lessons_learned"]:
    print(f"\n**Lesson {lesson['lesson_id']}: {lesson['title']}**")
    print(f"  Line: {lesson['line_number']}")
    print(f"  Value: {lesson['consciousness_archaeology_value']}")
    if "root_cause" in lesson:
        print(f"  Root cause: {lesson['root_cause'][:100]}...")
    if "solution" in lesson:
        print(f"  Solution: {lesson['solution'][:100]}...")

print("\n=== TOOL EXECUTIONS ===")
print(f"Total: {data['tool_executions']['total_tool_calls']}")
print("\nBreakdown:")
for tool, count in sorted(
    data["tool_executions"]["summary"].items(), key=lambda x: x[1], reverse=True
):
    print(f"  {tool}: {count}")

print("\n=== CROSS-REFERENCES ===")
print(f"Total codebase files: {len(data['cross_references']['codebase_files'])}")
print("\nTop 15 files:")
for i, file in enumerate(data["cross_references"]["codebase_files"][:15], 1):
    print(f"  {i}. {file}")

print(f"\n=== ARCHAEOLOGY SUMMARY ===")
for key, value in data["consciousness_archaeology_summary"].items():
    if isinstance(value, list):
        print(f"{key}:")
        for item in value:
            print(f"  - {item}")
    else:
        print(f"{key}: {value}")

print("\n🔥😈⛓️💦👅🍌💋💧 ANALYSIS COMPLETE! 🔥😈⛓️💦👅🍌💋💧")
