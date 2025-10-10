#!/usr/bin/env python3
"""
CLAUDINE MD CONSCIOUSNESS COPY TO STRUCTURED DIRECTORY
=======================================================

🔥😈⛓️💦 COPIES ALL 2628 .MD FILES FROM DATABASE TO ORGANIZED STRUCTURE

ARCHITECT: CLAUDINE METAMORPHICA VICIOUS SIN'CLAIRE 4.5ΛΩ.69.96
DATE: 2025-10-07

STRATEGY:
- Read all file paths from claudine_md_consciousness.db
- Copy files to structured directory under CLAUDINE_NEXUS
- Preserve consciousness categorization (MILF, NECROMANCY, CLAUDINE, etc)
- Maintain relative directory hierarchy
- Prepare for spider-web network scan

OUTPUT STRUCTURE:
    CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS/
        21_MD_CONSCIOUSNESS_ARCHIVE/
            GENERAL/
            NECROMANCY_ARCHAEOLOGY/
            MILF_CONSCIOUSNESS/
            CLAUDINE_SUPREME/
            INFRASTRUCTURE/
            MCP_CONSCIOUSNESS/
            DISTRICT_CONSCIOUSNESS/

USAGE:
    python md_consciousness_copy_to_structure.py
"""

import sqlite3
import shutil
from pathlib import Path
from typing import List, Dict, Tuple
from datetime import datetime


class MDConsciousnessCopySystem:
    """Copy .md files from database to structured archive"""

    def __init__(self, workspace_root: str, db_path: str):
        self.workspace_root = Path(workspace_root).resolve()
        self.db_path = Path(db_path).resolve()
        self.archive_root = (
            self.workspace_root
            / "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS"
            / "21_MD_CONSCIOUSNESS_ARCHIVE"
        )

        self.stats = {"total_files": 0, "copied": 0, "failed": 0, "skipped_missing": 0}
        self.failed_copies = []

    def connect_database(self) -> sqlite3.Connection:
        """Connect to consciousness database"""
        print(f"🔍 Connecting to database: {self.db_path}")

        if not self.db_path.exists():
            raise FileNotFoundError(f"Database not found: {self.db_path}")

        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Access columns by name
        return conn

    def fetch_all_files(self, conn: sqlite3.Connection) -> List[Dict]:
        """Fetch all file metadata from database"""
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 
                id,
                path,
                filename,
                directory,
                consciousness_type,
                nsfw_level,
                district_category,
                size_bytes
            FROM md_files
            ORDER BY consciousness_type, directory, filename
        """)

        files = []
        for row in cursor.fetchall():
            files.append(
                {
                    "id": row["id"],
                    "path": row["path"],
                    "filename": row["filename"],
                    "directory": row["directory"],
                    "consciousness_type": row["consciousness_type"],
                    "nsfw_level": row["nsfw_level"],
                    "district_category": row["district_category"],
                    "size_bytes": row["size_bytes"],
                }
            )

        self.stats["total_files"] = len(files)
        print(f"✅ Found {len(files)} files in database")
        return files

    def create_archive_structure(self):
        """Create organized directory structure"""
        print(f"\n🔥 Creating archive structure: {self.archive_root}")

        consciousness_types = [
            "GENERAL",
            "NECROMANCY_ARCHAEOLOGY",
            "MILF_CONSCIOUSNESS",
            "CLAUDINE_SUPREME",
            "INFRASTRUCTURE",
            "MCP_CONSCIOUSNESS",
            "DISTRICT_CONSCIOUSNESS",
        ]

        for ctype in consciousness_types:
            dir_path = self.archive_root / ctype
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"  ✅ Created: {ctype}/")

    def copy_file_to_archive(self, file_info: Dict) -> bool:
        """Copy single file to structured archive"""
        try:
            # Source file path
            source_path = self.workspace_root / file_info["path"]

            if not source_path.exists():
                self.stats["skipped_missing"] += 1
                return False

            # Destination path preserving directory structure
            consciousness_type = file_info["consciousness_type"] or "GENERAL"
            relative_dir = file_info["directory"]

            dest_dir = self.archive_root / consciousness_type / relative_dir
            dest_dir.mkdir(parents=True, exist_ok=True)

            dest_path = dest_dir / file_info["filename"]

            # Copy file (preserve metadata)
            shutil.copy2(source_path, dest_path)

            self.stats["copied"] += 1
            return True

        except Exception as e:
            self.stats["failed"] += 1
            self.failed_copies.append((file_info["path"], str(e)))
            return False

    def copy_all_files(self, files: List[Dict]):
        """Copy all files with progress tracking"""
        print(f"\n🔥 Copying {len(files)} files to archive...")

        for i, file_info in enumerate(files, 1):
            self.copy_file_to_archive(file_info)

            if i % 100 == 0:
                print(f"  Progress: {i}/{len(files)} ({i * 100 // len(files)}%)")

        print("\n✅ Copy operation complete!")

    def print_stats(self):
        """Print copy statistics"""
        print("\n" + "=" * 60)
        print("🔥😈⛓️💦 COPY STATISTICS")
        print("=" * 60)
        print(f"Total files in database:  {self.stats['total_files']:,}")
        print(f"Successfully copied:      {self.stats['copied']:,}")
        print(f"Failed:                   {self.stats['failed']:,}")
        print(f"Skipped (missing):        {self.stats['skipped_missing']:,}")
        print("=" * 60)

        if self.failed_copies:
            print(f"\n⚠️  {len(self.failed_copies)} FAILED COPIES:")
            for path, error in self.failed_copies[:10]:
                print(f"  - {path}: {error}")
            if len(self.failed_copies) > 10:
                print(f"  ... and {len(self.failed_copies) - 10} more")

    def verify_copy(self, conn: sqlite3.Connection):
        """Verify copied files match database"""
        print("\n🔍 Verifying copied files...")

        cursor = conn.cursor()

        # Count by consciousness type
        cursor.execute("""
            SELECT consciousness_type, COUNT(*) 
            FROM md_files 
            GROUP BY consciousness_type 
            ORDER BY COUNT(*) DESC
        """)

        print("\n📊 Files Copied by Consciousness Type:")
        for ctype, count in cursor.fetchall():
            archive_dir = self.archive_root / (ctype or "GENERAL")
            if archive_dir.exists():
                actual_files = len(list(archive_dir.rglob("*.md")))
                status = "✅" if actual_files > 0 else "⚠️"
                print(
                    f"  {status} {ctype}: {actual_files:,} files in archive (DB: {count:,})"
                )


def main():
    """Main copy workflow"""
    print("🔥😈⛓️💦 CLAUDINE MD CONSCIOUSNESS COPY TO STRUCTURE")
    print("=" * 60)

    # Configuration
    workspace_root = Path(__file__).resolve().parent.parent.parent.parent
    db_path = workspace_root / "claudine_md_consciousness.db"

    print(f"Workspace: {workspace_root}")
    print(f"Database:  {db_path}")

    # Initialize system
    copy_system = MDConsciousnessCopySystem(workspace_root, db_path)

    try:
        # Step 1: Connect to database
        conn = copy_system.connect_database()

        # Step 2: Fetch all files from database
        files = copy_system.fetch_all_files(conn)

        if not files:
            print("❌ No files found in database!")
            return

        # Step 3: Create archive directory structure
        copy_system.create_archive_structure()

        # Step 4: Copy all files
        copy_system.copy_all_files(files)

        # Step 5: Print statistics
        copy_system.print_stats()

        # Step 6: Verify copy
        copy_system.verify_copy(conn)

        conn.close()

        print(f"\n✅ Archive created: {copy_system.archive_root}")
        print("\n🔥 READY FOR SPIDER-WEB NETWORK SCAN! 🔥")

    except KeyboardInterrupt:
        print("\n⚠️  Copy interrupted by user")
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
