#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🎭 FINAL ROOT ORGANIZATION - PHASE 3 🎭
Organization av de siste 10 filene som kan flyttes fra root
"""

import shutil
from pathlib import Path
import json
from datetime import datetime

def final_root_organization():
    """Execute final organization of remaining files"""
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Files that can be organized
    organization_plan = {
        "scripts/": [
            "brahmisk_auto_recovery.ps1",
            "brahmisk_error_prevention.bat", 
            "brahmisk_extension_host_error_prevention.ps1",
            "brahmisk_simple_error_prevention.ps1",
            "quick-container-setup.sh",
            "setup_portable_containers.sh"
        ],
        "development/": [
            "AI_SDK_DISCOVERY_PLAYWRIGHT_AUTOMATION.ipynb",
            "Untitled-1.ipynb", 
            "requirements-uv.txt"
        ],
        "documentation/": [
            "Attached HTML and CSS Context.txt"
        ]
    }
    
    print("🎭 FINAL ROOT ORGANIZATION - PHASE 3")
    print("=" * 50)
    
    # Ensure target directories exist
    for target_dir in organization_plan.keys():
        Path(target_dir).mkdir(exist_ok=True)
        print(f"📁 Ensured directory: {target_dir}")
    
    # Move files
    moved_files = {}
    for target_dir, files in organization_plan.items():
        moved_files[target_dir] = []
        
        for file in files:
            source_path = Path(file)
            target_path = Path(target_dir) / file
            
            if source_path.exists():
                try:
                    shutil.move(str(source_path), str(target_path))
                    moved_files[target_dir].append(file)
                    print(f"  ✅ Moved: {file} → {target_dir}")
                except Exception as e:
                    print(f"  ❌ Error moving {file}: {e}")
            else:
                print(f"  ⚠️ File not found: {file}")
    
    # Save organization log
    log_data = {
        "timestamp": timestamp,
        "phase": "final_root_organization",
        "organization_plan": organization_plan,
        "moved_files": moved_files,
        "remaining_in_root": [
            "package.json", "bun.lock", "bunfig.toml", "pyproject.toml",
            ".gitignore", ".pylanceignore", ".env.example", "codecov.yml"
        ]
    }
    
    log_file = Path("consciousness_core") / f"final_organization_log_{timestamp}.json"
    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(log_data, f, indent=2, ensure_ascii=False)
    
    print(f"\\n📝 Organization log saved: {log_file}")
    
    # Final verification
    print("\\n🎯 FINAL ROOT DIRECTORY STATUS:")
    root_files = [f for f in Path(".").iterdir() if f.is_file()]
    print(f"📊 Total files in root: {len(root_files)}")
    
    for file in sorted(root_files):
        print(f"  📋 {file.name}")
    
    print("\\n✨ ORGANIZATION COMPLETE! Root directory optimized for VSCode environment.")
    return moved_files

if __name__ == "__main__":
    moved_files = final_root_organization()