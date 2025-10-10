#!/usr/bin/env python3
"""Quick test to see what detect_changes() actually returns"""

import sys
from pathlib import Path

sys.path.insert(
    0,
    str(
        Path(__file__).parent
        / "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS"
        / "18_ACTIVE_SCRIPTS_SUPREME"
        / "consciousness_archaeology"
    ),
)

from md_consciousness_intelligent_sync import MDConsciousnessIntelligentSync

workspace_root = Path(__file__).parent
db_path = workspace_root / "claudine_md_consciousness.db"

sync = MDConsciousnessIntelligentSync(workspace_root, db_path)
sync.connect()

print("🔍 Testing detect_changes()...\n")
changes, workspace_files = sync.detect_changes()

print(f"\n📊 Results:")
print(f"   New: {len(changes['new'])}")
print(f"   Modified: {len(changes['modified'])}")
print(f"   Deleted: {len(changes['deleted'])}")
print(f"   Workspace files scanned: {len(workspace_files)}")

if changes["deleted"]:
    print(f"\n🗑️  First 5 deleted files:")
    for path in changes["deleted"][:5]:
        print(f"      • {path}")

sync.disconnect()
