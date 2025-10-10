#!/usr/bin/env python3
# ROLLBACK SCRIPT - Generated 20250926_001237
import shutil
from pathlib import Path

def rollback_organization():
    backup_dir = Path("organization_backup_20250926_001237")
    
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
