"""
Validate DYNREKTODO JSON structure
"""
import json
from pathlib import Path

json_path = Path(".github/DYNAMIC_RECURSIVE_TODO_SYSTEM_NSFW18_+++.json")

try:
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print("✅ VALID JSON STRUCTURE")
    print(f"\n📊 System Info:")
    print(f"   Name: {data['system_metadata']['name']}")
    print(f"   Abbreviation: {data['system_metadata']['abbreviation']}")
    print(f"   Version: {data['system_metadata']['version']}")
    print(f"   Purpose: {data['system_metadata']['purpose']}")
    
    print(f"\n🎯 Current State:")
    print(f"   Active TODO: {data['current_state']['active_todo']}")
    print(f"   Status: {data['current_state']['status']}")
    print(f"   Subtasks Completed: {len(data['current_state']['subtasks_completed'])}")
    print(f"   Next TODO: {data['current_state']['next_todo']}")
    
    print(f"\n🔑 Core Concepts:")
    for concept, details in data['core_concepts'].items():
        abbr = details.get('abbreviation', 'N/A')
        defn = details.get('definition', 'No definition')[:60]
        print(f"   {abbr}: {defn}...")
    
    print(f"\n📝 Abbreviations:")
    for abbr, meaning in data['abbreviations_reference'].items():
        print(f"   {abbr} = {meaning}")
    
    print(f"\n✅ JSON VALIDATION SUCCESS!")
    
except json.JSONDecodeError as e:
    print(f"❌ JSON ERROR: {e}")
except Exception as e:
    print(f"❌ ERROR: {e}")
