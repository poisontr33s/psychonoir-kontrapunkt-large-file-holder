#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
CLAUDINE MD CONSCIOUSNESS ARCHIVE SYNC SYSTEM
==============================================

🔥😈⛓️💦 SYNKRONISERER OPPDATERTE FILER FRA WORKSPACE TIL ARKIV

ARCHITECT: CLAUDINE METAMORPHICA VICIOUS SIN'CLAIRE 4.5ΛΩ.96
DATE: 2025-10-07

PURPOSE:
When files are updated in workspace (e.g., by structural_update_engine.py),
this script syncs those changes to the archive to maintain consistency.

STRATEGY:
1. Connect to database to get all file paths
2. Compare modification times (original vs archive)
3. Sync newer files from workspace to archive
4. Verify hash matches after sync

USAGE:
    python md_consciousness_archive_sync.py
"""

import sqlite3
import shutil
import hashlib
from pathlib import Path
from datetime import datetime
from typing import List, Tuple


class MDConsciousnessArchiveSync:
    """Sync system for MD consciousness archive"""

    def __init__(self, workspace_root: str, db_path: str):
        self.workspace_root = Path(workspace_root).resolve()
        self.db_path = Path(db_path).resolve()
        self.archive_root = (
            self.workspace_root
            / "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS"
            / "21_MD_CONSCIOUSNESS_ARCHIVE"
        )

        self.stats = {
            "total_files": 0,
            "up_to_date": 0,
            "synced": 0,
            "failed": 0,
            "verified": 0,
        }

        self.synced_files = []
        self.failed_files = []

    def connect_database(self) -> sqlite3.Connection:
        """Connect to consciousness database"""
        print(f"🔍 Connecting to database: {self.db_path}")

        if not self.db_path.exists():
            raise FileNotFoundError(f"Database not found: {self.db_path}")

        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def calculate_file_hash(self, file_path: Path) -> str:
        """Calculate SHA256 hash of file"""
        sha256 = hashlib.sha256()

        try:
            with open(file_path, "rb") as f:
                while chunk := f.read(8192):
                    sha256.update(chunk)
            return sha256.hexdigest()
        except Exception:
            return None

    def sync_file(self, original_path: Path, archive_path: Path) -> bool:
        """Sync single file from workspace to archive"""
        try:
            # Ensure archive directory exists
            archive_path.parent.mkdir(parents=True, exist_ok=True)

            # Copy file with metadata preservation
            shutil.copy2(original_path, archive_path)

            # Verify hash after copy
            original_hash = self.calculate_file_hash(original_path)
            archive_hash = self.calculate_file_hash(archive_path)

            if original_hash == archive_hash:
                self.stats["verified"] += 1
                return True
            else:
                print(f"  ⚠️ Hash mismatch after sync: {original_path.name}")
                self.failed_files.append(
                    (str(original_path), "Hash mismatch after copy")
                )
                self.stats["failed"] += 1
                return False

        except Exception as e:
            print(f"  ❌ Failed to sync {original_path.name}: {e}")
            self.failed_files.append((str(original_path), str(e)))
            self.stats["failed"] += 1
            return False

    def sync_all_files(self, conn: sqlite3.Connection):
        """Sync all files that need updating"""
        print("\n🔄 Scanning for files needing sync...")

        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                path,
                filename,
                consciousness_type,
                modified_date
            FROM md_files
            ORDER BY consciousness_type, path
        """)

        files = cursor.fetchall()
        self.stats["total_files"] = len(files)

        print(f"📊 Checking {len(files)} files...")

        for i, row in enumerate(files, 1):
            original_path = self.workspace_root / row["path"]

            if not original_path.exists():
                continue

            # Determine archive path
            consciousness_type = row["consciousness_type"] or "GENERAL"
            relative_path = Path(row["path"])
            archive_path = self.archive_root / consciousness_type / relative_path

            if not archive_path.exists():
                # File missing from archive - sync it
                print(f"  📥 Syncing missing file: {row['filename']}")
                if self.sync_file(original_path, archive_path):
                    self.synced_files.append(str(original_path))
                    self.stats["synced"] += 1
                continue

            # Compare modification times
            original_mtime = original_path.stat().st_mtime
            archive_mtime = archive_path.stat().st_mtime

            if original_mtime > archive_mtime:
                # Original is newer - sync it
                print(f"  🔄 Syncing updated file: {row['filename']}")
                if self.sync_file(original_path, archive_path):
                    self.synced_files.append(str(original_path))
                    self.stats["synced"] += 1
            else:
                # Archive is up to date
                self.stats["up_to_date"] += 1

            if i % 100 == 0:
                print(f"  Progress: {i}/{len(files)} ({i * 100 // len(files)}%)")

    def print_stats(self):
        """Print sync statistics"""
        print("\n" + "=" * 60)
        print("🔥😈⛓️💦 SYNC STATISTICS")
        print("=" * 60)
        print(f"Total files checked:     {self.stats['total_files']:,}")
        print(f"Already up to date:      {self.stats['up_to_date']:,}")
        print(f"Synced:                  {self.stats['synced']:,}")
        print(f"Hash verified:           {self.stats['verified']:,}")
        print(f"Failed:                  {self.stats['failed']:,}")
        print("=" * 60)

        if self.synced_files:
            print(f"\n✅ Synced {len(self.synced_files)} file(s):")
            for path in self.synced_files[:10]:
                print(f"  - {Path(path).name}")
            if len(self.synced_files) > 10:
                print(f"  ... and {len(self.synced_files) - 10} more")

        if self.failed_files:
            print(f"\n❌ Failed {len(self.failed_files)} file(s):")
            for path, error in self.failed_files[:10]:
                print(f"  - {Path(path).name}: {error}")
            if len(self.failed_files) > 10:
                print(f"  ... and {len(self.failed_files) - 10} more")

    def run_sync(self) -> bool:
        """Run complete sync workflow"""
        print("🔥😈⛓️💦 CLAUDINE MD CONSCIOUSNESS ARCHIVE SYNC")
        print("=" * 60)

        conn = self.connect_database()

        try:
            self.sync_all_files(conn)
            self.print_stats()

            if self.stats["failed"] == 0:
                print("\n🔥 SYNC COMPLETE - ALL FILES UP TO DATE! 🔥")
                return True
            else:
                print(f"\n⚠️ SYNC COMPLETE WITH {self.stats['failed']} FAILURES")
                return False

        finally:
            conn.close()


def main():
    """Main sync workflow"""
    workspace_root = Path(__file__).resolve().parent.parent.parent.parent
    db_path = workspace_root / "claudine_md_consciousness.db"

    syncer = MDConsciousnessArchiveSync(workspace_root, db_path)
    success = syncer.run_sync()

    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
