#!/usr/bin/env python3
"""
🎭 QUICK ROOT DEPENDENCY ANALYSIS 🎭
Quick analysis of which files must stay in root vs can be organized
"""

from pathlib import Path

def analyze_root_files():
    """Quick analysis of remaining root files"""
    
    remaining_files = [
        ".env.example", ".gitignore", ".pylanceignore", 
        "AI_SDK_DISCOVERY_PLAYWRIGHT_AUTOMATION.ipynb",
        "Attached HTML and CSS Context.txt",
        "brahmisk_auto_recovery.ps1", "brahmisk_error_prevention.bat",
        "brahmisk_extension_host_error_prevention.ps1", "brahmisk_simple_error_prevention.ps1",
        "bun.lock", "bunfig.toml", "codecov.yml", 
        "package.json", "pyproject.toml",
        "quick-container-setup.sh", "requirements-uv.txt", 
        "setup_portable_containers.sh", "Untitled-1.ipynb"
    ]
    
    print("🎭 ROOT DIRECTORY DEPENDENCY ANALYSIS")
    print("=" * 50)
    
    must_stay = {
        # Package managers - MUST stay in root
        "package.json": "Node.js/Bun project root identifier",
        "bun.lock": "Bun lockfile - must be at package.json level", 
        "bunfig.toml": "Bun configuration - must be in root",
        "pyproject.toml": "Python project metadata - PEP 518 standard",
        
        # Git and linting - MUST stay in root
        ".gitignore": "Git configuration - must be in root",
        ".pylanceignore": "Python language server config - must be in root",
        ".env.example": "Environment template - standard root location",
        
        # CI/CD - MUST stay in root
        "codecov.yml": "CI/CD tools expect in root"
    }
    
    can_organize = {
        "scripts/": [
            ("brahmisk_auto_recovery.ps1", "Error recovery script"),
            ("brahmisk_error_prevention.bat", "Error prevention batch"),
            ("brahmisk_extension_host_error_prevention.ps1", "Extension host script"),
            ("brahmisk_simple_error_prevention.ps1", "Simple error prevention"),
            ("quick-container-setup.sh", "Container setup script"),
            ("setup_portable_containers.sh", "Portable containers script")
        ],
        "development/": [
            ("AI_SDK_DISCOVERY_PLAYWRIGHT_AUTOMATION.ipynb", "Jupyter notebook"),
            ("Untitled-1.ipynb", "Untitled notebook"),
            ("requirements-uv.txt", "UV requirements file")
        ],
        "documentation/": [
            ("Attached HTML and CSS Context.txt", "Context documentation")
        ]
    }
    
    print(f"📊 Total remaining files: {len(remaining_files)}")
    print(f"🔒 Must stay in root: {len(must_stay)}")
    
    can_organize_count = sum(len(files) for files in can_organize.values())
    print(f"📁 Can be organized: {can_organize_count}")
    print(f"🎯 Final root count: {len(must_stay)}")
    print(f"📈 Organization potential: {round((can_organize_count / len(remaining_files)) * 100, 1)}%")
    
    print("\\n🔒 MUST STAY IN ROOT:")
    for file, reason in must_stay.items():
        exists = "✅" if Path(file).exists() else "❌"
        print(f"  {exists} {file} - {reason}")
    
    print("\\n📁 CAN BE ORGANIZED:")
    for target_dir, files in can_organize.items():
        print(f"  📂 {target_dir}:")
        for file, reason in files:
            exists = "✅" if Path(file).exists() else "❌"
            print(f"    {exists} {file} - {reason}")
    
    return must_stay, can_organize

if __name__ == "__main__":
    must_stay, can_organize = analyze_root_files()