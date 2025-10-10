#!/usr/bin/env uv run python3
"""
🎭 SYSTEMATISK DISTRICT NAVNSKIFTE UPCYCLER
Automatisert implementation av konseptuelt riktige norsk/arkaiske district navn.

FINAL NAMING SCHEME:
- NEPTUNIUM_FLOTILLA/NEPTUNIUMSFARET → HAVSDOMINANSEN  
- SIMULATION_SANCTUM/SIMULACRUMSPIRET → VIRTUALITETSHELGEDOMMEN
- NECROSIS_CHRONO/NEKROKRONOPOLIS → NEKROKRONORIKET

Additional districts maintained:
- SKYSKRAPEREN (maintained)
- RUSTBELTET (maintained)
"""

import shutil
from pathlib import Path
from typing import List
import argparse
import sys

class SystematiskDistrictNavnSkifte:
    def __init__(self, workspace_root: Path, dry_run: bool = True):
        self.workspace_root = workspace_root
        self.dry_run = dry_run
        self.backup_dir = workspace_root / "necromancy_graveyard" / "district_navnskifte_backup"
        self.changes_made = 0
        self.files_processed = 0
        
        # COMPLETE RENAMING MAP - alle varianter og case-kombinasjoner
        self.renaming_map = {
            # PRIMARY MAPPINGS - nye konseptuelt riktige navn
            "NEPTUNIUM_FLOTILLA": "HAVSDOMINANSEN",
            "SIMULATION_SANCTUM": "VIRTUALITETSHELGEDOMMEN", 
            "NECROSIS_CHRONO": "NEKROKRONORIKET",
            
            # TEMPORARY NAME CLEANUP (fra FastMCP og Grok endringer)
            "NEPTUNIUMSFARET": "HAVSDOMINANSEN",
            "SIMULACRUMSPIRET": "VIRTUALITETSHELGEDOMMEN",
            "NEKROKRONOPOLIS": "NEKROKRONORIKET",
            
            # LOWERCASE VARIANTS (for Python identifiers og JSON keys)
            "neptunium_flotilla": "havsdominansen",
            "simulation_sanctum": "virtualitetshelgedommen",
            "necrosis_chrono": "nekrokronoriket",
            "neptuniumsfaret": "havsdominansen",
            "simulacrumspiret": "virtualitetshelgedommen", 
            "nekrokronopolis": "nekrokronoriket",
            
            # CAMELCASE VARIANTS (for TypeScript/JavaScript)
            "NeptuniumFlotilla": "Havsdominansen",
            "SimulationSanctum": "Virtualitetshelgedommen",
            "NecrosisChronoPos": "Nekrokronoriket",
            "neptuniumFlotilla": "havsdominansen",
            "simulationSanctum": "virtualitetshelgedommen",
            "necrosisChronoPos": "nekrokronoriket",
            
            # TITLE CASE VARIANTS (for documentation)
            "Neptunium Flotilla": "Havsdominansen",
            "Simulation Sanctum": "Virtualitetshelgedommen",
            "Necrosis Chrono": "Nekrokronoriket",
            
            # ADDITIONAL CASE VARIANTS
            "NEPTUNIUMSFLØTILLEN": "HAVSDOMINANSEN",  # Norwegian variant
            "SIMULACRUMSANKTUARIUM": "VIRTUALITETSHELGEDOMMEN",  # Extended variant
            "NEKROKRONOTIDENS": "NEKROKRONORIKET",  # Time variant
        }

    def create_backup_if_needed(self) -> None:
        """Create backup directory if it doesn't exist"""
        if not self.dry_run and not self.backup_dir.exists():
            self.backup_dir.mkdir(parents=True, exist_ok=True)
            print(f"📁 Created backup directory: {self.backup_dir}")

    def backup_file(self, file_path: Path) -> None:
        """Create backup of file before modification"""
        if self.dry_run:
            return
            
        relative_path = file_path.relative_to(self.workspace_root)
        backup_path = self.backup_dir / relative_path
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file_path, backup_path)

    def process_file(self, file_path: Path) -> bool:
        """Process a single file and apply district name changes"""
        try:
            original_content = file_path.read_text(encoding='utf-8', errors='ignore')
            new_content = original_content
            file_changes = 0
            
            # Apply all renaming rules
            for old_name, new_name in self.renaming_map.items():
                if old_name in new_content:
                    new_content = new_content.replace(old_name, new_name)
                    file_changes += 1
                    
            if file_changes > 0:
                if not self.dry_run:
                    self.backup_file(file_path)
                    file_path.write_text(new_content, encoding='utf-8')
                    
                print(f"  ✅ {file_path.relative_to(self.workspace_root)} ({file_changes} changes)")
                self.changes_made += file_changes
                return True
            else:
                print(f"  ⚪ {file_path.relative_to(self.workspace_root)} (no changes)")
                return False
                
        except Exception as e:
            print(f"  ❌ {file_path.relative_to(self.workspace_root)} (ERROR: {e})")
            return False

    def find_affected_files(self) -> List[Path]:
        """Find all files that contain district references"""
        affected_files = []
        extensions = {'.py', '.ts', '.js', '.md', '.json', '.txt', '.yaml', '.yml'}
        
        # Directories to skip
        skip_dirs = {
            'node_modules', '.git', '__pycache__', '.vscode', 
            'necromancy_graveyard', 'backups', 'data'
        }
        
        print("🔍 Scanning for affected files...")
        
        for file_path in self.workspace_root.rglob("*"):
            # Skip if any parent directory is in skip_dirs
            if any(parent.name in skip_dirs for parent in file_path.parents):
                continue
                
            if file_path.is_file() and file_path.suffix in extensions:
                try:
                    content = file_path.read_text(encoding='utf-8', errors='ignore')
                    
                    # Check if any district names appear (case-insensitive)
                    content_lower = content.lower()
                    for old_name in self.renaming_map.keys():
                        if old_name.lower() in content_lower:
                            affected_files.append(file_path)
                            break
                            
                except Exception:
                    continue
                    
        return affected_files

    def run_systematic_rename(self) -> None:
        """Execute the systematic district name replacement"""
        print("🎭 SYSTEMATISK DISTRICT NAVNSKIFTE")
        print("=" * 60)
        print(f"Working directory: {self.workspace_root}")
        print(f"Dry run mode: {'ON' if self.dry_run else 'OFF'}")
        print()
        
        # Show renaming mappings
        print("📋 DISTRICT RENAMING MAPPINGS:")
        print("-" * 40)
        for old_name, new_name in list(self.renaming_map.items())[:6]:  # Show first 6 primary mappings
            print(f"  {old_name} → {new_name}")
        print(f"  ... and {len(self.renaming_map) - 6} additional variants")
        print()
        
        # Create backup directory
        self.create_backup_if_needed()
        
        # Find affected files
        affected_files = self.find_affected_files()
        print(f"📊 Found {len(affected_files)} affected files")
        print()
        
        if not affected_files:
            print("✅ No files need district name updates!")
            return
            
        # Group files by extension for better organization
        files_by_ext: dict[str, List[Path]] = {}
        for file_path in affected_files:
            ext = file_path.suffix or 'no_extension'
            if ext not in files_by_ext:
                files_by_ext[ext] = []
            files_by_ext[ext].append(file_path)
            
        # Process files by extension
        for ext in sorted(files_by_ext.keys()):
            files = files_by_ext[ext]
            print(f"📁 Processing {ext} files ({len(files)} files):")
            
            for file_path in files:
                self.process_file(file_path)
                self.files_processed += 1
                
            print()
            
        # Summary
        print("🎯 SUMMARY:")
        print("=" * 40)
        print(f"Files processed: {self.files_processed}")
        print(f"Total changes made: {self.changes_made}")
        print(f"Backup directory: {self.backup_dir if not self.dry_run else 'N/A (dry run)'}")
        
        if self.dry_run:
            print("\n💡 This was a DRY RUN. Use --execute to apply changes.")
        else:
            print("\n✅ District renaming completed successfully!")

def main():
    parser = argparse.ArgumentParser(description='🎭 Systematisk District Navnskifte')
    parser.add_argument('--execute', action='store_true', 
                       help='Execute changes (default is dry run)')
    parser.add_argument('--workspace', type=str, 
                       help='Workspace root path (default: auto-detect)')
    
    args = parser.parse_args()
    
    # Determine workspace root
    if args.workspace:
        workspace_root = Path(args.workspace).resolve()
    else:
        # Auto-detect from script location
        workspace_root = Path(__file__).parent.parent
        
    if not workspace_root.exists():
        print(f"❌ Workspace directory not found: {workspace_root}")
        sys.exit(1)
        
    # Run the systematic rename
    renamer = SystematiskDistrictNavnSkifte(workspace_root, dry_run=not args.execute)
    renamer.run_systematic_rename()

if __name__ == "__main__":
    main()