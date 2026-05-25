#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""Phase 1: Create complete backup before organization"""
import shutil
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
