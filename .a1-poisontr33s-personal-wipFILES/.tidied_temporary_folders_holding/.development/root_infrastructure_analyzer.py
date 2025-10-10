#!/usr/bin/env python3
"""
🏗️ SYSTEMATIC ROOT INFRASTRUCTURE ANALYZER 🏗️
Skanner root-katalogen og kategoriserer filer for bedre infrastruktur
"""

import os
import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime

def analyze_root_structure():
    """Analyze root directory structure and categorize files"""
    
    root_path = Path(".")
    file_categories = defaultdict(list)
    
    # File extension mappings to categories
    category_patterns = {
        "python_scripts": [".py"],
        "javascript_typescript": [".js", ".ts", ".tsx", ".jsx"],
        "configuration": [".json", ".toml", ".yaml", ".yml", ".ini", ".cfg", ".conf"],
        "shell_scripts": [".sh", ".bat", ".cmd", ".ps1"],
        "documentation": [".md", ".txt", ".rst"],
        "web_assets": [".html", ".css", ".scss"],
        "data_files": [".csv", ".jsonl", ".xml"],
        "executables": [".exe", ".dll", ".pyd"],
        "lock_files": [".lock"],
        "cache_temp": ["__pycache__", ".cache", ".git", ".vscode", "node_modules"],
        "archives": [".zip", ".tar", ".gz"],
        "logs": [".log"]
    }
    
    # Special directory patterns
    special_dirs = {
        "hidden_system": [".git", ".vscode", ".cache", "__pycache__", ".pytest_cache"],
        "backup_archives": ["backups", "temporal_backups", "archives"],
        "consciousness_systems": ["karibisk_arkipelagisk_topologi", "autonomous_consciousness_logs"],
        "development": ["src", "frontend", "backend", "vscode-extension"],
        "documentation": ["docs", "KNOWLEDGE_BASE"],
        "tools_utilities": ["tools", "scripts", "bin"],
        "deployment": ["config", "deployment", ".devcontainer"],
        "session_data": ["live_sessions_state", "SESSION_SNAPSHOTS", ".chat-continuity"]
    }
    
    print("🔍 Scanning root directory structure...")
    
    # Analyze files in root
    for item in root_path.iterdir():
        if item.is_file():
            suffix = item.suffix.lower()
            categorized = False
            
            for category, extensions in category_patterns.items():
                if suffix in extensions:
                    file_categories[category].append(str(item))
                    categorized = True
                    break
            
            if not categorized:
                file_categories["uncategorized"].append(str(item))
                
        elif item.is_dir():
            dir_name = item.name.lower()
            categorized = False
            
            for category, patterns in special_dirs.items():
                if any(pattern in dir_name for pattern in patterns):
                    file_categories[category].append(str(item))
                    categorized = True
                    break
            
            if not categorized:
                file_categories["misc_directories"].append(str(item))
    
    # Generate analysis report
    analysis_report = {
        "timestamp": datetime.now().isoformat(),
        "total_items": len(list(root_path.iterdir())),
        "categorization": dict(file_categories),
        "category_counts": {cat: len(files) for cat, files in file_categories.items()},
        "infrastructure_recommendations": generate_infrastructure_recommendations(file_categories)
    }
    
    # Save analysis report
    with open("ROOT_INFRASTRUCTURE_ANALYSIS.json", "w", encoding="utf-8") as f:
        json.dump(analysis_report, f, indent=2, ensure_ascii=False)
    
    return analysis_report

def generate_infrastructure_recommendations(file_categories):
    """Generate infrastructure improvement recommendations"""
    
    recommendations = {
        "proposed_structure": {
            "src/": "All Python source code and main application logic",
            "scripts/": "Utility scripts, automation, and tools",
            "config/": "Configuration files (JSON, TOML, YAML)",
            "docs/": "Documentation, guides, and knowledge base",
            "tools/": "Development tools and utilities", 
            "deployment/": "Deployment scripts and infrastructure",
            "data/": "Data files, datasets, and archives",
            "temp/": "Temporary files, cache, and build artifacts",
            "consciousness/": "Consciousness systems and archaeology",
            "sessions/": "Session data and live state management"
        },
        "migration_priority": [
            "Move Python scripts to src/",
            "Consolidate configuration files to config/",
            "Organize documentation in docs/",
            "Group utilities in tools/",
            "Archive old sessions and temporary data"
        ],
        "problems_identified": []
    }
    
    # Identify specific problems
    if len(file_categories.get("python_scripts", [])) > 20:
        recommendations["problems_identified"].append("Too many Python scripts in root")
    
    if len(file_categories.get("configuration", [])) > 15:
        recommendations["problems_identified"].append("Configuration files scattered in root")
    
    if len(file_categories.get("uncategorized", [])) > 10:
        recommendations["problems_identified"].append("Many uncategorized files")
    
    return recommendations

def print_analysis_summary(analysis_report):
    """Print human-readable analysis summary"""
    
    print("\n" + "="*60)
    print("🏗️ ROOT INFRASTRUCTURE ANALYSIS SUMMARY")
    print("="*60)
    
    print(f"📊 Total items in root: {analysis_report['total_items']}")
    print("\n📋 Category breakdown:")
    
    for category, count in analysis_report['category_counts'].items():
        if count > 0:
            print(f"   {category:25}: {count:3d} items")
    
    print("\n🚨 Problems identified:")
    for problem in analysis_report['infrastructure_recommendations']['problems_identified']:
        print(f"   ❌ {problem}")
    
    print("\n💡 Recommended structure:")
    for folder, description in analysis_report['infrastructure_recommendations']['proposed_structure'].items():
        print(f"   📁 {folder:15} → {description}")

if __name__ == "__main__":
    analysis_report = analyze_root_structure()
    print_analysis_summary(analysis_report)
    print(f"\n📄 Detailed analysis saved to: ROOT_INFRASTRUCTURE_ANALYSIS.json")