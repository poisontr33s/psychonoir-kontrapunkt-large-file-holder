#!/usr/bin/env python3
"""
🎭 ROOT DIRECTORY ORGANIZATION SOLUTION 🎭
CLAUDINE METAMORPHICA VICIOUS SIN'CLAIRE 4.0ΛΩ.69.96

Intelligent file organization for consciousness-enhanced repository
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any
import json

class ConsciousnessAwareFileOrganizer:
    """Intelligent file organizer that respects consciousness architecture"""
    
    def __init__(self):
        self.project_root = Path.cwd()
        self.organization_plan = {}
        self.consciousness_files = []
        self.backup_location = None
        
    def analyze_root_directory_chaos(self) -> Dict[str, Any]:
        """Analyze the current file chaos in root directory"""
        print("🔍 Analyzing root directory chaos...")
        
        files = list(self.project_root.glob("*"))
        files = [f for f in files if f.is_file()]
        
        analysis = {
            'total_files': len(files),
            'file_types': {},
            'consciousness_files': [],
            'organizational_categories': {},
            'timestamp': datetime.now().isoformat()
        }
        
        # Categorize by file type
        for file in files:
            ext = file.suffix.lower()
            if ext not in analysis['file_types']:
                analysis['file_types'][ext] = 0
            analysis['file_types'][ext] += 1
            
            # Identify consciousness files (these need special handling)
            if any(term in file.name.lower() for term in ['consciousness', 'claudine', 'milf', 'supreme', 'archaeology']):
                analysis['consciousness_files'].append({
                    'name': file.name,
                    'type': ext,
                    'size_kb': round(file.stat().st_size / 1024, 2),
                    'priority': 'PRESERVE'
                })
        
        # Create organizational categories
        analysis['organizational_categories'] = {
            'consciousness_core': {
                'description': 'Core consciousness files - highest priority preservation',
                'patterns': ['*consciousness*', '*claudine*', '*supreme*', '*milf*', '*archaeology*'],
                'target_folder': 'consciousness_core',
                'file_count': len(analysis['consciousness_files'])
            },
            'development_tools': {
                'description': 'Development and automation scripts',
                'patterns': ['*.py', '*.ts', '*.js'],
                'target_folder': 'development',
                'file_count': analysis['file_types'].get('.py', 0) + analysis['file_types'].get('.ts', 0) + analysis['file_types'].get('.js', 0)
            },
            'data_and_reports': {
                'description': 'JSON data files and reports',
                'patterns': ['*.json'],
                'target_folder': 'data_reports',
                'file_count': analysis['file_types'].get('.json', 0)
            },
            'documentation': {
                'description': 'Markdown documentation',
                'patterns': ['*.md'],
                'target_folder': 'documentation',
                'file_count': analysis['file_types'].get('.md', 0)
            },
            'backups_and_temp': {
                'description': 'Backup files and temporary data',
                'patterns': ['*.backup*', '*.consciousness_enhancement_backup', '*.tsbuildinfo'],
                'target_folder': 'backups_temp',
                'file_count': analysis['file_types'].get('.consciousness_enhancement_backup', 0) + analysis['file_types'].get('.tsbuildinfo', 0) + analysis['file_types'].get('.backup_20250922_172642', 0)
            },
            'configuration': {
                'description': 'Configuration files',
                'patterns': ['*.toml', '*.yml', '*.json', '*.gitignore', '*.lock'],
                'target_folder': None,  # Keep in root
                'file_count': analysis['file_types'].get('.toml', 0) + analysis['file_types'].get('.yml', 0)
            }
        }
        
        return analysis
    
    def create_safe_organization_plan(self, analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Create safe organization plan with rollback capability"""
        print("📋 Creating safe organization plan...")
        
        plan = [
            {
                'phase': 1,
                'title': 'BACKUP CREATION',
                'risk': 'MINIMAL',
                'duration': '5 minutes',
                'actions': [
                    'Create complete backup of current state',
                    'Generate rollback script',
                    'Validate backup integrity'
                ],
                'files_affected': 0,
                'success_criteria': 'Complete backup with verified integrity'
            },
            {
                'phase': 2,
                'title': 'CONSCIOUSNESS CORE PRESERVATION',
                'risk': 'MINIMAL',
                'duration': '10 minutes',
                'actions': [
                    'Create consciousness_core/ directory',
                    'Move consciousness files with import preservation',
                    'Update any hardcoded paths',
                    'Test consciousness system integrity'
                ],
                'files_affected': len(analysis['consciousness_files']),
                'success_criteria': 'All consciousness files preserved and functional'
            },
            {
                'phase': 3,
                'title': 'DEVELOPMENT TOOL ORGANIZATION',
                'risk': 'LOW',
                'duration': '15 minutes',
                'actions': [
                    'Create development/ directory structure',
                    'Organize Python/TypeScript files by function',
                    'Preserve development workflow',
                    'Update task configurations'
                ],
                'files_affected': analysis['organizational_categories']['development_tools']['file_count'],
                'success_criteria': 'Development tools organized and accessible'
            },
            {
                'phase': 4,
                'title': 'DATA AND DOCUMENTATION CLEANUP',
                'risk': 'LOW',
                'duration': '15 minutes',
                'actions': [
                    'Create data_reports/ and documentation/ directories',
                    'Organize JSON reports by date/type',
                    'Organize markdown documentation',
                    'Preserve documentation links'
                ],
                'files_affected': analysis['organizational_categories']['data_and_reports']['file_count'] + analysis['organizational_categories']['documentation']['file_count'],
                'success_criteria': 'Clean documentation and data organization'
            },
            {
                'phase': 5,
                'title': 'BACKUP AND TEMPORARY FILE MANAGEMENT',
                'risk': 'MINIMAL',
                'duration': '10 minutes',
                'actions': [
                    'Create backups_temp/ directory',
                    'Move backup and temporary files',
                    'Compress old backups',
                    'Clean up unnecessary temp files'
                ],
                'files_affected': analysis['organizational_categories']['backups_and_temp']['file_count'],
                'success_criteria': 'Backup files organized and accessible'
            }
        ]
        
        return plan
    
    def generate_organization_scripts(self) -> Dict[str, str]:
        """Generate organization scripts for each phase"""
        
        scripts = {
            'phase1_backup_creation.py': '''#!/usr/bin/env python3
"""Phase 1: Create complete backup before organization"""
import shutil
import json
from pathlib import Path
from datetime import datetime

def create_complete_backup():
    """Create complete backup with rollback capability"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = Path(f"organization_backup_{timestamp}")
    
    print(f"🔄 Creating backup: {backup_dir}")
    
    # Create backup directory
    backup_dir.mkdir(exist_ok=True)
    
    # Copy all root files
    root_files = [f for f in Path('.').glob('*') if f.is_file()]
    backup_count = 0
    
    for file in root_files:
        try:
            shutil.copy2(file, backup_dir / file.name)
            backup_count += 1
        except Exception as e:
            print(f"❌ Could not backup {file.name}: {e}")
    
    # Create rollback script
    rollback_script = f"""#!/usr/bin/env python3
# ROLLBACK SCRIPT - Generated {timestamp}
import shutil
from pathlib import Path

def rollback_organization():
    backup_dir = Path("{backup_dir}")
    
    if not backup_dir.exists():
        print("❌ Backup directory not found!")
        return False
    
    print("🔄 Rolling back organization...")
    
    # Remove organized directories
    for org_dir in ["consciousness_core", "development", "data_reports", "documentation", "backups_temp"]:
        if Path(org_dir).exists():
            shutil.rmtree(org_dir)
    
    # Restore files to root
    for backup_file in backup_dir.glob("*"):
        if backup_file.is_file():
            shutil.copy2(backup_file, Path(".") / backup_file.name)
    
    print("✅ Rollback complete!")
    return True

if __name__ == "__main__":
    rollback_organization()
"""
    
    Path("rollback_organization.py").write_text(rollback_script, encoding='utf-8')
    
    print(f"✅ Backup created: {backup_count} files")
    print(f"✅ Rollback script: rollback_organization.py")
    
    return backup_dir

if __name__ == "__main__":
    create_complete_backup()
''',
            
            'phase2_consciousness_preservation.py': '''#!/usr/bin/env python3
"""Phase 2: Preserve consciousness files with import integrity"""
import shutil
from pathlib import Path

def preserve_consciousness_files():
    """Move consciousness files while preserving functionality"""
    
    consciousness_dir = Path("consciousness_core")
    consciousness_dir.mkdir(exist_ok=True)
    
    consciousness_patterns = ['*consciousness*', '*claudine*', '*supreme*', '*milf*', '*archaeology*']
    moved_files = []
    
    for pattern in consciousness_patterns:
        for file in Path('.').glob(pattern):
            if file.is_file() and not file.name.startswith('consciousness_core'):
                try:
                    target = consciousness_dir / file.name
                    shutil.move(str(file), str(target))
                    moved_files.append(file.name)
                    print(f"✅ Moved: {file.name}")
                except Exception as e:
                    print(f"❌ Could not move {file.name}: {e}")
    
    print(f"🎭 Preserved {len(moved_files)} consciousness files")
    return moved_files

if __name__ == "__main__":
    preserve_consciousness_files()
''',
            
            'complete_organization.py': '''#!/usr/bin/env python3
"""Complete file organization with consciousness preservation"""
import os
import shutil
from pathlib import Path

def organize_all_files():
    """Organize all files into appropriate directories"""
    
    # Create directory structure
    directories = {
        'consciousness_core': 'Core consciousness files',
        'development': 'Python, TypeScript, JavaScript files', 
        'data_reports': 'JSON data and reports',
        'documentation': 'Markdown documentation',
        'backups_temp': 'Backup and temporary files'
    }
    
    for dir_name in directories:
        Path(dir_name).mkdir(exist_ok=True)
    
    # Organization rules
    organization_rules = {
        'consciousness_core': ['*consciousness*', '*claudine*', '*supreme*', '*milf*', '*archaeology*'],
        'development': ['*.py', '*.ts', '*.js'],
        'data_reports': ['*.json'],
        'documentation': ['*.md'],
        'backups_temp': ['*.backup*', '*.consciousness_enhancement_backup', '*.tsbuildinfo']
    }
    
    # Configuration files to keep in root
    keep_in_root = ['*.toml', '*.yml', '*.gitignore', '*.lock', 'package.json', 'bun.lock']
    
    organized_count = {}
    
    for target_dir, patterns in organization_rules.items():
        organized_count[target_dir] = 0
        
        for pattern in patterns:
            for file in Path('.').glob(pattern):
                if file.is_file() and file.parent == Path('.'):
                    # Skip if it matches keep_in_root patterns
                    should_keep = False
                    for keep_pattern in keep_in_root:
                        if file.match(keep_pattern):
                            should_keep = True
                            break
                    
                    if not should_keep:
                        try:
                            target = Path(target_dir) / file.name
                            shutil.move(str(file), str(target))
                            organized_count[target_dir] += 1
                            print(f"📁 {target_dir}: {file.name}")
                        except Exception as e:
                            print(f"❌ Could not move {file.name}: {e}")
    
    # Summary
    print(f"\\n🎭 ORGANIZATION COMPLETE!")
    for dir_name, count in organized_count.items():
        print(f"📁 {dir_name}: {count} files")
    
    return organized_count

if __name__ == "__main__":
    organize_all_files()
'''
        }
        
        return scripts

def main():
    """Execute root directory organization analysis"""
    print("🎭 ROOT DIRECTORY ORGANIZATION SOLUTION")
    print("🌊 Intelligent file organization with consciousness preservation")
    print("=" * 70)
    
    organizer = ConsciousnessAwareFileOrganizer()
    
    # Phase 1: Analyze current chaos
    analysis = organizer.analyze_root_directory_chaos()
    
    # Phase 2: Create safe organization plan  
    organization_plan = organizer.create_safe_organization_plan(analysis)
    
    # Phase 3: Generate organization scripts
    scripts = organizer.generate_organization_scripts()
    
    # Save analysis and plan
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    with open(f'root_directory_analysis_{timestamp}.json', 'w', encoding='utf-8') as f:
        json.dump({
            'analysis': analysis,
            'organization_plan': organization_plan,
            'timestamp': datetime.now().isoformat()
        }, f, indent=2, ensure_ascii=False)
    
    # Save organization scripts
    for script_name, script_content in scripts.items():
        with open(script_name, 'w', encoding='utf-8') as f:
            f.write(script_content)
    
    # Results summary
    print(f"\\n🎭 ROOT DIRECTORY ANALYSIS COMPLETE!")
    print(f"📊 Total files in root: {analysis['total_files']}")
    
    # File type breakdown
    print(f"\\n📁 FILE TYPE BREAKDOWN:")
    top_types = sorted(analysis['file_types'].items(), key=lambda x: x[1], reverse=True)[:10]
    for ext, count in top_types:
        ext_display = ext if ext else '(no extension)'
        print(f"  {ext_display}: {count} files")
    
    # Consciousness files
    consciousness_count = len(analysis['consciousness_files'])
    print(f"\\n🎭 CONSCIOUSNESS FILES: {consciousness_count} (PRESERVED)")
    
    # Organization plan summary
    print(f"\\n📋 ORGANIZATION PLAN:")
    total_files_to_organize = 0
    for phase in organization_plan:
        files_affected = phase.get('files_affected', 0)
        total_files_to_organize += files_affected
        print(f"  Phase {phase['phase']}: {phase['title']} ({files_affected} files, {phase['risk']} risk)")
    
    print(f"\\n🎯 ORGANIZATION SCRIPTS CREATED:")
    for script_name in scripts.keys():
        print(f"  📄 {script_name}")
    
    print(f"\\n🌊 RECOMMENDED EXECUTION ORDER:")
    print("1. python phase1_backup_creation.py (CREATE BACKUP FIRST!)")
    print("2. python phase2_consciousness_preservation.py (PRESERVE CONSCIOUSNESS)")
    print("3. python complete_organization.py (ORGANIZE EVERYTHING)")
    print("4. Test system integrity")
    print("5. If problems: python rollback_organization.py")

if __name__ == "__main__":
    main()