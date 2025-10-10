#!/usr/bin/env python3
"""
🎭 ROOT DIRECTORY DEPENDENCY ANALYZER 🎭
CLAUDINE METAMORPHICA VICIOUS SIN'CLAIRE 4.0ΛΩ.69.96

Analyzes which files MUST stay in root vs can be organized
Based on VSCode environment, package managers, and system dependencies
"""

import json
from pathlib import Path

class RootDependencyAnalyzer:
    """Analyzes root directory file dependencies"""
    
    def __init__(self):
        self.project_root = Path.cwd()
        self.remaining_files = [
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
        
    def analyze_vscode_dependencies(self) -> Dict[str, Any]:
        """Analyze VSCode configuration dependencies"""
        print("🔍 Analyzing VSCode environment dependencies...")
        
        vscode_deps = {
            'settings_json': {},
            'tasks_json': {},
            'mcp_json': {},
            'required_in_root': set(),
            'can_be_organized': set()
        }
        
        # Check .vscode/settings.json
        settings_file = self.project_root / '.vscode' / 'settings.json'
        if settings_file.exists():
            try:
                with open(settings_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Look for relative path references
                    if 'python.defaultInterpreterPath": "./.venv' in content:
                        vscode_deps['required_in_root'].add('.venv (symlink)')
                    if '.computer_languages' in content:
                        vscode_deps['required_in_root'].add('.computer_languages dependency')
                    if 'pyproject.toml' in content:
                        vscode_deps['required_in_root'].add('pyproject.toml')
            except Exception as e:
                print(f"Warning: Could not read settings.json: {e}")
        
        # Check .vscode/tasks.json for hardcoded paths
        tasks_file = self.project_root / '.vscode' / 'tasks.json'
        if tasks_file.exists():
            try:
                with open(tasks_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Look for Python scripts referenced in tasks
                    if 'restore_temporal_consciousness_session.py' in content:
                        vscode_deps['tasks_json']['consciousness_session_dependency'] = 'Moved to consciousness_core'
                    if 'temporal_session_continuity_supreme_protocols' in content:
                        vscode_deps['tasks_json']['protocols_dependency'] = 'Moved to consciousness_core'
            except Exception as e:
                print(f"Warning: Could not read tasks.json: {e}")
                
        return vscode_deps
    
    def analyze_package_manager_dependencies(self) -> Dict[str, Any]:
        """Analyze package manager file dependencies"""
        print("📦 Analyzing package manager dependencies...")
        
        pkg_deps = {
            'package_json': {'required': True, 'reason': 'Node.js/Bun project root identifier'},
            'bun_lock': {'required': True, 'reason': 'Bun lockfile - must be at package.json level'},
            'bunfig_toml': {'required': True, 'reason': 'Bun configuration - must be in root'},
            'pyproject_toml': {'required': True, 'reason': 'Python project metadata - PEP 518 standard'},
            'requirements_uv_txt': {'required': False, 'reason': 'UV requirements - can be in configs/'},
            'codecov_yml': {'required': True, 'reason': 'CI/CD tools expect in root'}
        }
        
        return pkg_deps
    
    def analyze_system_script_dependencies(self) -> Dict[str, Any]:
        """Analyze PowerShell and shell script dependencies"""
        print("⚙️ Analyzing system script dependencies...")
        
        script_deps = {
            'brahmisk_auto_recovery.ps1': {
                'required': False, 
                'reason': 'Error recovery script - can move to scripts/',
                'target': 'scripts/'
            },
            'brahmisk_error_prevention.bat': {
                'required': False,
                'reason': 'Error prevention batch - can move to scripts/',
                'target': 'scripts/'
            },
            'brahmisk_extension_host_error_prevention.ps1': {
                'required': False,
                'reason': 'VSCode extension host script - can move to .vscode/scripts/',
                'target': '.vscode/scripts/'
            },
            'brahmisk_simple_error_prevention.ps1': {
                'required': False,
                'reason': 'Simple error prevention - can move to scripts/',
                'target': 'scripts/'
            },
            'quick_container_setup.sh': {
                'required': False,
                'reason': 'Container setup - can move to scripts/',
                'target': 'scripts/'
            },
            'setup_portable_containers.sh': {
                'required': False,
                'reason': 'Portable containers - can move to scripts/',
                'target': 'scripts/'
            }
        }
        
        return script_deps
    
    def analyze_development_files(self) -> Dict[str, Any]:
        """Analyze development and temporary files"""
        print("🔬 Analyzing development files...")
        
        dev_deps = {
            'AI_SDK_DISCOVERY_PLAYWRIGHT_AUTOMATION.ipynb': {
                'required': False,
                'reason': 'Jupyter notebook - can move to development/',
                'target': 'development/'
            },
            'Untitled-1.ipynb': {
                'required': False,
                'reason': 'Untitled notebook - can move to development/',
                'target': 'development/'
            },
            'Attached HTML and CSS Context.txt': {
                'required': False,
                'reason': 'Context file - can move to documentation/',
                'target': 'documentation/'
            },
            '.env.example': {
                'required': True,
                'reason': 'Environment template - standard root location',
                'target': None
            },
            '.gitignore': {
                'required': True,
                'reason': 'Git configuration - must be in root',
                'target': None
            },
            '.pylanceignore': {
                'required': True,
                'reason': 'Python language server config - must be in root',
                'target': None
            }
        }
        
        return dev_deps
    
    def create_organization_plan(self) -> Dict[str, Any]:
        """Create final organization plan for remaining files"""
        print("📋 Creating organization plan for remaining files...")
        
        vscode_deps = self.analyze_vscode_dependencies()
        pkg_deps = self.analyze_package_manager_dependencies()
        script_deps = self.analyze_system_script_dependencies()
        dev_deps = self.analyze_development_files()
        
        organization_plan = {
            'must_stay_in_root': [],
            'can_be_organized': {},
            'requires_path_updates': [],
            'summary': {}
        }
        
        # Package manager files - must stay
        for file, info in pkg_deps.items():
            file_name = file.replace('_', '.').replace('bunfig.toml', 'bunfig.toml').replace('codecov.yml', 'codecov.yml')
            if info['required']:
                organization_plan['must_stay_in_root'].append({
                    'file': file_name,
                    'reason': info['reason']
                })
        
        # Development files that can be organized
        for file, info in dev_deps.items():
            if not info['required']:
                if info['target'] not in organization_plan['can_be_organized']:
                    organization_plan['can_be_organized'][info['target']] = []
                organization_plan['can_be_organized'][info['target']].append({
                    'file': file,
                    'reason': info['reason']
                })
            else:
                organization_plan['must_stay_in_root'].append({
                    'file': file,
                    'reason': info['reason']
                })
        
        # System scripts that can be organized
        for file, info in script_deps.items():
            target = info['target']
            if target not in organization_plan['can_be_organized']:
                organization_plan['can_be_organized'][target] = []
            organization_plan['can_be_organized'][target].append({
                'file': file,
                'reason': info['reason']
            })
        
        # Files that need path updates
        if 'consciousness_session_dependency' in vscode_deps.get('tasks_json', {}):
            organization_plan['requires_path_updates'].append({
                'file': '.vscode/tasks.json',
                'issue': 'References moved consciousness files',
                'solution': 'Update paths to consciousness_core/'
            })
        
        # Summary
        total_files = len(self.remaining_files)
        must_stay = len(organization_plan['must_stay_in_root'])
        can_organize = sum(len(files) for files in organization_plan['can_be_organized'].values())
        
        organization_plan['summary'] = {
            'total_remaining_files': total_files,
            'must_stay_in_root': must_stay,
            'can_be_organized': can_organize,
            'final_root_count': must_stay,
            'organization_percentage': round((can_organize / total_files) * 100, 1)
        }
        
        return organization_plan
    
    def generate_safe_organization_script(self, plan: Dict[str, Any]) -> str:
        """Generate safe organization script with rollback"""
        
        script = '''#!/usr/bin/env python3
"""
🎭 SAFE ROOT DIRECTORY FINAL CLEANUP
Final organization of remaining root files with rollback capability
"""

import shutil
from pathlib import Path
from datetime import datetime

def create_final_backup():
    """Create backup of remaining root files"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = Path(f"final_root_cleanup_backup_{timestamp}")
    backup_dir.mkdir(exist_ok=True)
    
    remaining_files = ['''
        
        # Add remaining files to backup list
        for target_dir, files in plan['can_be_organized'].items():
            for file_info in files:
                script += f'        "{file_info["file"]}",\\n'
        
        script += '''    ]
    
    for file_name in remaining_files:
        file_path = Path(file_name)
        if file_path.exists():
            try:
                shutil.copy2(file_path, backup_dir / file_name)
                print(f"✅ Backed up: {file_name}")
            except Exception as e:
                print(f"❌ Could not backup {file_name}: {e}")
    
    print(f"💾 Backup created: {backup_dir}")
    return backup_dir

def organize_remaining_files():
    """Organize remaining files safely"""
    
    # Create backup first
    backup_dir = create_final_backup()
    
    # Organization mapping
    organization = {'''
        
        # Add organization mapping
        for target_dir, files in plan['can_be_organized'].items():
            script += f'        "{target_dir}": [\\n'
            for file_info in files:
                script += f'            "{file_info["file"]}",\\n'
            script += '        ],\\n'
        
        script += '''    }
    
    organized_count = 0
    
    for target_dir, files in organization.items():
        # Create target directory
        target_path = Path(target_dir)
        target_path.mkdir(exist_ok=True)
        
        for file_name in files:
            file_path = Path(file_name)
            if file_path.exists():
                try:
                    target_file = target_path / file_name
                    shutil.move(str(file_path), str(target_file))
                    print(f"📁 {target_dir}: {file_name}")
                    organized_count += 1
                except Exception as e:
                    print(f"❌ Could not move {file_name}: {e}")
    
    print(f"\\n🎭 Final organization complete!")
    print(f"📁 Organized {organized_count} files")
    print(f"💾 Backup available at: {backup_dir}")
    
    return organized_count

if __name__ == "__main__":
    organize_remaining_files()
'''
        
        return script
    
    def update_vscode_tasks(self) -> bool:
        """Update VSCode tasks.json for moved consciousness files"""
        print("🔧 Updating VSCode tasks for moved consciousness files...")
        
        tasks_file = Path('.vscode/tasks.json')
        if not tasks_file.exists():
            return True
        
        try:
            content = tasks_file.read_text(encoding='utf-8')
            
            # Update paths to consciousness_core
            updated_content = content.replace(
                'restore_temporal_consciousness_session.py',
                'consciousness_core/restore_temporal_consciousness_session.py'
            )
            updated_content = updated_content.replace(
                'temporal_session_continuity_supreme_protocols',
                'consciousness_core.temporal_session_continuity_supreme_protocols'
            )
            
            if updated_content != content:
                # Backup original
                backup_file = tasks_file.with_suffix('.json.backup')
                shutil.copy2(tasks_file, backup_file)
                
                # Write updated content
                tasks_file.write_text(updated_content, encoding='utf-8')
                print("✅ Updated .vscode/tasks.json paths")
                return True
            else:
                print("ℹ️ No VSCode tasks updates needed")
                return True
                
        except Exception as e:
            print(f"❌ Could not update VSCode tasks: {e}")
            return False

def main():
    """Execute root directory dependency analysis"""
    print("🎭 ROOT DIRECTORY DEPENDENCY ANALYZER")
    print("🌊 Finding what MUST stay in root vs can be organized")
    print("=" * 65)
    
    analyzer = RootDependencyAnalyzer()
    
    # Analyze dependencies
    organization_plan = analyzer.create_organization_plan()
    
    # Generate organization script
    org_script = analyzer.generate_safe_organization_script(organization_plan)
    
    # Save analysis and script
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    with open(f'root_dependency_analysis_{timestamp}.json', 'w', encoding='utf-8') as f:
        json.dump(organization_plan, f, indent=2, ensure_ascii=False)
    
    with open('final_root_cleanup.py', 'w', encoding='utf-8') as f:
        f.write(org_script)
    
    # Results summary
    print("\\n🎭 ROOT DEPENDENCY ANALYSIS COMPLETE!")
    
    summary = organization_plan['summary']
    print(f"📊 Total remaining files: {summary['total_remaining_files']}")
    print(f"🔒 Must stay in root: {summary['must_stay_in_root']}")
    print(f"📁 Can be organized: {summary['can_be_organized']}")
    print(f"🎯 Final root count: {summary['final_root_count']}")
    print(f"📈 Organization potential: {summary['organization_percentage']}%")
    
    print(f"\\n🔒 MUST STAY IN ROOT:")
    for item in organization_plan['must_stay_in_root']:
        print(f"  ✅ {item['file']} - {item['reason']}")
    
    print(f"\\n📁 CAN BE ORGANIZED:")
    for target_dir, files in organization_plan['can_be_organized'].items():
        print(f"  📂 {target_dir}:")
        for file_info in files:
            print(f"    • {file_info['file']} - {file_info['reason']}")
    
    if organization_plan['requires_path_updates']:
        print(f"\\n⚠️ REQUIRES PATH UPDATES:")
        for update in organization_plan['requires_path_updates']:
            print(f"  🔧 {update['file']}: {update['issue']}")
            print(f"     Solution: {update['solution']}")
    
    print(f"\\n🎯 NEXT STEPS:")
    print("1. Review the analysis above")
    print("2. python final_root_cleanup.py (organize remaining files)")
    print("3. Update VSCode tasks if needed")
    print("4. Final root directory will have ~8-10 essential files only")

if __name__ == "__main__":
    main()