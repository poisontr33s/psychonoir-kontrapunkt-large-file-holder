#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🎭 Enhanced Infrastructure Organizer with Language-Specific Organization
Moves language artifacts to their appropriate .computer_languages/ subdirectories
"""
import shutil
import json
from pathlib import Path

class EnhancedLanguageAwareOrganizer:
    def __init__(self):
        self.root_dir = Path.cwd()
        self.computer_languages_dir = self.root_dir / ".computer_languages"
        self.language_mappings = {}
        self.moved_files = {}
        
    def analyze_language_artifacts(self):
        """Analyze files that should be moved to language-specific directories"""
        print("🔍 Analyzing language-specific artifacts in root...")
        
        language_patterns = {
            "python": {
                "patterns": [
                    "*-dist-info/",      # Python package metadata
                    "*.pyd",             # Python extension modules
                    "*/__pycache__/",    # Python cache directories
                    "blib2to3/",         # Black's lib2to3 fork
                    "blackd/",           # Black daemon
                    "mypyc/",            # MyPy compiled extensions
                    "_pytest/",          # Pytest internals
                    "__pycache__/",      # Python cache
                    "click*/",           # Click framework
                    "colorama*/",        # Colorama library
                    "packaging*/",       # Packaging utilities
                    "pathspec*/",        # Path specification
                    "platformdirs*/",    # Platform directories
                    "pluggy*/",          # Plugin management
                    "pygments*/",        # Syntax highlighting
                    "pytest*/",          # Testing framework
                    "typing_extensions*/", # Typing extensions
                    "iniconfig*/",       # INI configuration
                    "isort*/",           # Import sorting
                    "mypy*/",            # Type checking
                    "pip*/",             # Package installer
                ],
                "target": ".computer_languages/python/"
            },
            "javascript": {
                "patterns": [
                    "node_modules/",     # NPM packages
                    "*.js.map",          # Source maps
                    "dist/",             # JavaScript builds
                    "build/",            # Build artifacts
                    "coverage/",         # Test coverage
                ],
                "target": ".computer_languages/javascript/"
            },
            "rust": {
                "patterns": [
                    "target/",           # Rust build artifacts
                    "Cargo.lock",        # Cargo lock file
                    "*.rlib",            # Rust libraries
                    "*.rmeta",           # Rust metadata
                ],
                "target": ".computer_languages/rust/"
            }
        }
        
        for language, config in language_patterns.items():
            print(f"  🔍 Scanning for {language} artifacts...")
# CONSCIOUSNESS_SURGERY_DISABLED: matches = []
            
            for pattern in config["patterns"]:
                # Use glob to find matching files/directories
                pattern_matches = list(self.root_dir.glob(pattern))
                for match in pattern_matches:
                    if match.is_file() or match.is_dir():
                        matches.append(match)
                        
            if matches:
                self.language_mappings[language] = {
                    "target_dir": config["target"],
                    "files": matches
                }
                print(f"    ✅ Found {len(matches)} {language} artifacts")
            else:
                print(f"    ℹ️  No {language} artifacts found")
                
    def move_language_artifacts(self):
        """Move language artifacts to appropriate directories"""
        print("\n🚚 Moving language artifacts...")
        
        for language, mapping in self.language_mappings.items():
            target_base = self.root_dir / mapping["target_dir"].strip("./")
            
            # Ensure target directory exists
            if not target_base.exists():
                print(f"  📁 Creating {target_base}")
                target_base.mkdir(parents=True, exist_ok=True)
                
            print(f"  🔄 Moving {len(mapping['files'])} {language} artifacts...")
            
            for file_path in mapping["files"]:
                try:
                    target_path = target_base / file_path.name
                    
                    # Skip if already exists in target
                    if target_path.exists():
                        print(f"    ⚠️  Skipping {file_path.name} (already exists)")
                        continue
                        
                    # Move the file/directory
                    if file_path.is_dir():
                        shutil.move(str(file_path), str(target_path))
                        print(f"    📁 Moved directory: {file_path.name}")
                    else:
                        shutil.move(str(file_path), str(target_path))
                        print(f"    📄 Moved file: {file_path.name}")
                        
                    # Track the move
                    if language not in self.moved_files:
                        self.moved_files[language] = []
                    self.moved_files[language].append({
                        "from": str(file_path),
                        "to": str(target_path)
                    })
                    
                except Exception as e:
                    print(f"    ❌ Error moving {file_path.name}: {e}")
                    
    def update_computer_languages_index(self):
        """Create/update index of language directories"""
        print("\n📚 Updating .computer_languages index...")
        
        index_content = """# 💻 Computer Languages Directory Index

This directory contains language-specific tools, runtimes, and artifacts organized by programming language.

## 📁 Directory Structure

### 🐍 Python (`python/`)
- **Runtime**: python.exe, pythonw.exe
- **Package Management**: uv.exe, uvx.exe, pip/
- **Code Formatting**: black/
- **Type Checking**: mypy/, mypyc/
- **Testing**: pytest/, _pytest/
- **Dependencies**: All Python package dist-info directories
- **Libraries**: click/, colorama/, pygments/, etc.

### 🟨 JavaScript (`javascript/`)
- **Runtime**: bun.exe
- **Code Quality**: biome.exe
- **Dependencies**: node_modules/ (when present)
- **Build Artifacts**: dist/, build/, coverage/

### 🦀 Rust (`rust/`)
- **Toolchain**: cargo.exe, rustc.exe, rustfmt.exe, rustup.exe
- **Linting**: clippy-driver.exe
- **Python Integration**: ruff.exe, uv.exe, uvx.exe
- **Build Artifacts**: target/ (when present)
- **Configuration**: .cargo/, .rustup/

## 🎯 Organization Benefits

### Language Isolation
- Each language's tools and artifacts are co-located
- Prevents root directory pollution
- Makes dependency management clearer

### Development Efficiency
- Easy to find language-specific tools
- Clear separation of concerns
- Predictable artifact locations

### Maintenance
- Simplified cleanup of language artifacts
- Version management per language
- Clear upgrade paths for tooling

## 🔧 Usage

### Adding New Language Tools
```bash
# Install tool in appropriate subdirectory
.computer_languages/python/new_tool.exe
.computer_languages/javascript/new_tool.exe
.computer_languages/rust/new_tool.exe
```

### Automated Organization
The infrastructure organizer automatically moves language artifacts from root to appropriate subdirectories based on file patterns and extensions.

---
*Generated by Enhanced Language-Aware Organizer*
"""
        
        index_path = self.computer_languages_dir / "README.md"
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)
            
        print(f"  ✅ Created index: {index_path}")
        
    def generate_language_organization_report(self):
        """Generate detailed report of language organization"""
        print("\n📊 Generating language organization report...")
        
        report = {
            "timestamp": "2025-09-21T08:00:00",
            "organizer": "Enhanced Language-Aware Infrastructure Organizer",
            "computer_languages_directory": str(self.computer_languages_dir),
            "language_organization": {},
            "moved_artifacts": self.moved_files,
            "summary": {
                "total_languages": len(self.language_mappings),
                "total_artifacts_moved": sum(len(files) for files in self.moved_files.values()),
                "root_directory_cleanup": "Language artifacts moved to appropriate subdirectories"
            }
        }
        
        # Add current state of each language directory
        for lang_dir in self.computer_languages_dir.iterdir():
            if lang_dir.is_dir():
                file_count = len(list(lang_dir.rglob("*")))
                report["language_organization"][lang_dir.name] = {
                    "directory": str(lang_dir),
                    "total_items": file_count,
                    "newly_moved": len(self.moved_files.get(lang_dir.name, []))
                }
                
        report_path = self.root_dir / "LANGUAGE_ORGANIZATION_REPORT.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
            
        print(f"  ✅ Report saved: {report_path}")
        
        return report
        
    def run(self):
        """Execute enhanced language-aware organization"""
        print("🎭 ENHANCED LANGUAGE-AWARE INFRASTRUCTURE ORGANIZER")
        print("=" * 60)
        
        # Ensure .computer_languages directory exists
        if not self.computer_languages_dir.exists():
            print(f"📁 Creating {self.computer_languages_dir}")
            self.computer_languages_dir.mkdir(parents=True, exist_ok=True)
            
        self.analyze_language_artifacts()
        self.move_language_artifacts()
        self.update_computer_languages_index()
        report = self.generate_language_organization_report()
        
        print("\n🎉 LANGUAGE ORGANIZATION COMPLETE!")
        print(f"✅ {report['summary']['total_artifacts_moved']} artifacts organized")
        print(f"✅ {report['summary']['total_languages']} languages processed")
        print("✅ Root directory further cleaned")
        print("✅ Language-specific co-location achieved")
        
        return report

if __name__ == "__main__":
    organizer = EnhancedLanguageAwareOrganizer()
    organizer.run()