#!/usr/bin/env python3
"""
🏗️ SYSTEMATIC FILE ORGANIZER 🏗️
Organiserer filer i root til den nye infrastrukturelle strukturen
"""

import os
import shutil
import json
from pathlib import Path
from datetime import datetime

def organize_root_files():
    """Organize root files into systematic infrastructure"""
    
    print("🏗️ Starting systematic file organization...")
    
    # Load analysis data
    with open("ROOT_INFRASTRUCTURE_ANALYSIS.json", "r", encoding="utf-8") as f:
        analysis = json.load(f)
    
    # Migration mapping based on file patterns and purpose
    migration_rules = {
        # Core consciousness systems
        "consciousness": {
            "target": "infrastructure/src/consciousness/",
            "patterns": [
                "*consciousness*",
                "*uv_autonomous*", 
                "*norwegian*",
                "*claudine*",
                "*milf*",
                "*necromancy*",
                "*quantum*"
            ]
        },
        
        # Automation and orchestration
        "automation": {
            "target": "infrastructure/src/automation/",
            "patterns": [
                "*autonomous*",
                "*orchestrat*",
                "*workflow*",
                "*automation*",
                "*ecosystem*"
            ]
        },
        
        # Analysis and reporting
        "analysis": {
            "target": "infrastructure/src/analysis/", 
            "patterns": [
                "*analyz*",
                "*report*",
                "*scan*",
                "*detect*",
                "*index*",
                "*cross_validation*"
            ]
        },
        
        # Deployment and infrastructure
        "deployment": {
            "target": "infrastructure/src/deployment/",
            "patterns": [
                "*deploy*",
                "*launch*",
                "*production*",
                "*railway*",
                "*setup*"
            ]
        },
        
        # Utilities and tools
        "utilities": {
            "target": "infrastructure/src/utilities/",
            "patterns": [
                "*util*",
                "*tool*",
                "*helper*",
                "*bridge*",
                "*fix*",
                "*clean*"
            ]
        },
        
        # Configuration files
        "config": {
            "target": "infrastructure/config/development/",
            "patterns": ["*.json", "*.toml", "*.yaml", "*.yml", "*.ini", "*.cfg"]
        },
        
        # Shell scripts  
        "scripts": {
            "target": "infrastructure/scripts/utilities/",
            "patterns": ["*.sh", "*.bat", "*.cmd", "*.ps1"]
        },
        
        # Documentation
        "docs": {
            "target": "infrastructure/docs/",
            "patterns": ["*.md", "*.txt", "*.rst"]
        },
        
        # Session and temporary data
        "sessions": {
            "target": "archives/sessions/historical/",
            "patterns": [
                "*session*",
                "*log*",
                "*backup*",
                "*restore*",
                "*cache*"
            ]
        }
    }
    
    # Track migration results
    migration_results = {
        "timestamp": datetime.now().isoformat(),
        "files_moved": {},
        "errors": [],
        "summary": {}
    }
    
    # Get all files in root (excluding directories for now)
    root_files = [f for f in Path(".").iterdir() if f.is_file() and f.name not in [
        "ROOT_INFRASTRUCTURE_ANALYSIS.json",
        "SYSTEMATIC_INFRASTRUCTURE_DESIGN.md", 
        "systematic_file_organizer.py",
        "root_infrastructure_analyzer.py"
    ]]
    
    print(f"📁 Found {len(root_files)} files to organize...")
    
    for file_path in root_files:
        try:
            moved = False
            file_name = file_path.name.lower()
            
            # Try to match file to migration rules
            for category, rules in migration_rules.items():
                target_dir = Path(rules["target"])
                
                # Check if file matches any pattern
                for pattern in rules["patterns"]:
                    if pattern.startswith("*") and pattern.endswith("*"):
                        # Contains pattern
                        if pattern[1:-1] in file_name:
                            target_dir.mkdir(parents=True, exist_ok=True)
                            target_path = target_dir / file_path.name
                            
                            if not target_path.exists():
                                shutil.move(str(file_path), str(target_path))
                                migration_results["files_moved"][str(file_path)] = str(target_path)
                                print(f"   ✅ {file_path.name} → {category}")
                                moved = True
                                break
                    elif pattern.startswith("*."):
                        # Extension pattern
                        if file_path.suffix.lower() == pattern[1:]:
                            target_dir.mkdir(parents=True, exist_ok=True)
                            target_path = target_dir / file_path.name
                            
                            if not target_path.exists():
                                shutil.move(str(file_path), str(target_path))
                                migration_results["files_moved"][str(file_path)] = str(target_path)
                                print(f"   ✅ {file_path.name} → {category}")
                                moved = True
                                break
                
                if moved:
                    break
            
            # If no specific rule matched, move to legacy
            if not moved:
                legacy_dir = Path("archives/legacy/old_scripts")
                legacy_dir.mkdir(parents=True, exist_ok=True)
                target_path = legacy_dir / file_path.name
                
                if not target_path.exists():
                    shutil.move(str(file_path), str(target_path))
                    migration_results["files_moved"][str(file_path)] = str(target_path)
                    print(f"   📦 {file_path.name} → legacy")
        
        except Exception as e:
            error_msg = f"Error moving {file_path}: {str(e)}"
            migration_results["errors"].append(error_msg)
            print(f"   ❌ {error_msg}")
    
    # Generate summary
    migration_results["summary"] = {
        "total_files_processed": len(root_files),
        "files_successfully_moved": len(migration_results["files_moved"]),
        "errors_encountered": len(migration_results["errors"])
    }
    
    # Save migration report
    with open("SYSTEMATIC_MIGRATION_REPORT.json", "w", encoding="utf-8") as f:
        json.dump(migration_results, f, indent=2, ensure_ascii=False)
    
    print(f"\n🎯 Migration completed:")
    print(f"   ✅ {migration_results['summary']['files_successfully_moved']} files organized")
    print(f"   ❌ {migration_results['summary']['errors_encountered']} errors")
    print(f"   📄 Report saved: SYSTEMATIC_MIGRATION_REPORT.json")
    
    return migration_results

if __name__ == "__main__":
    organize_root_files()