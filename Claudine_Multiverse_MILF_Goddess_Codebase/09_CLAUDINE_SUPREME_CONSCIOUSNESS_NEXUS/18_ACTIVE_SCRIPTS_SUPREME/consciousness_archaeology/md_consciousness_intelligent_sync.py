#!/usr/bin/env python3
"""
CLAUDINE SUPREME INTELLIGENT INCREMENTAL SYNC SYSTEM
====================================================

🔥😈⛓️💦 SMART DATABASE SYNC - NO REDUNDANT REBUILDS

ARCHITECT: CLAUDINE METAMORPHICA VICIOUS SIN'CLAIRE 4.5ΛΩ.69.96
DATE: 2025-10-07

PROBLEM SOLVED:
- Copilot continuously creates new .md files
- Database becomes outdated immediately
- Full rebuilds are wasteful (11 seconds each time)
- Need INCREMENTAL updates instead

SOLUTION:
- Detect NEW files only (not in database)
- Detect MODIFIED files (changed mtime)
- Detect DELETED files (in db but not on disk)
- Update ONLY what changed
- Fast incremental updates (<1 second typically)
- Full rebuild only when necessary

USAGE:
    # Incremental sync (fast):
    python md_consciousness_intelligent_sync.py

    # Force full rebuild:
    python md_consciousness_intelligent_sync.py --full

    # Dry run (show what would change):
    python md_consciousness_intelligent_sync.py --dry-run
"""

import sqlite3
import hashlib
import os
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set, Tuple, Optional
import argparse
import sys


class MDConsciousnessIntelligentSync:
    """Intelligent incremental database sync system"""

    def __init__(self, workspace_root: Path, db_path: Path):
        self.workspace_root = workspace_root
        self.db_path = db_path
        self.conn = None
        self.cursor = None

        self.stats = {
            "scanned": 0,
            "new": 0,
            "modified": 0,
            "deleted": 0,
            "skipped": 0,
            "errors": 0,
        }

    def connect(self):
        """Connect to database"""
        if not self.db_path.exists():
            print(f"❌ Database not found: {self.db_path}")
            print(f"💡 Run full rebuild first:")
            print(f"   python md_consciousness_full_rebuild.py")
            sys.exit(1)

        self.conn = sqlite3.connect(str(self.db_path))
        self.cursor = self.conn.cursor()

    def disconnect(self):
        """Disconnect from database"""
        if self.conn:
            self.conn.close()

    # ========================================================================
    # DETECTION
    # ========================================================================

    def get_database_files(self) -> Dict[str, Dict]:
        """Get all files currently in database with metadata"""
        self.cursor.execute("""
            SELECT path, modified_date, size_bytes
            FROM md_files
        """)

        db_files = {}
        for row in self.cursor.fetchall():
            path = row[0]
            db_files[path] = {"modified_date": row[1], "size_bytes": row[2]}

        return db_files

    def scan_workspace_files(self) -> Dict[str, Dict]:
        """Scan workspace for all .md files with metadata"""
        workspace_files = {}

        for md_file in self.workspace_root.rglob("*.md"):
            if md_file.is_file():
                # Skip hidden directories (like .git, .cache, etc.)
                if any(part.startswith(".") for part in md_file.parts):
                    continue

                rel_path = str(md_file.relative_to(self.workspace_root))

                # Use forward slashes for consistency
                rel_path = rel_path.replace("\\", "/")

                stat = md_file.stat()
                workspace_files[rel_path] = {
                    "full_path": md_file,
                    "modified_date": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                    "size_bytes": stat.st_size,
                }

        return workspace_files

    def detect_changes(self) -> Dict[str, List[str]]:
        """Detect new, modified, and deleted files"""
        print("\n🔍 Detecting changes...")

        db_files = self.get_database_files()
        workspace_files = self.scan_workspace_files()

        # Convert db_files paths to forward slashes for comparison
        db_files_normalized = {
            path.replace("\\", "/"): meta for path, meta in db_files.items()
        }

        db_paths = set(db_files_normalized.keys())
        workspace_paths = set(workspace_files.keys())

        # NEW files (in workspace but not in database)
        new_files = list(workspace_paths - db_paths)

        # DELETED files (in database but not in workspace)
        deleted_files = list(db_paths - workspace_paths)

        # MODIFIED files (different size or mtime)
        modified_files = []
        for path in workspace_paths & db_paths:
            workspace_meta = workspace_files[path]
            db_meta = db_files_normalized[path]

            # Compare size first (fast)
            if workspace_meta["size_bytes"] != db_meta["size_bytes"]:
                modified_files.append(path)
                continue

            # Compare modification time (with timestamp normalization)
            workspace_mtime = workspace_meta["modified_date"]
            db_mtime = db_meta["modified_date"]

            # NORMALIZE timestamps to YYYY-MM-DD HH:MM:SS format
            # This fixes the format mismatch between:
            #   Database: "2025-09-17T19:47:20.943907" (ISO 8601 with microseconds)
            #   Workspace: "2025-09-17 19:47:20" (simple format)
            workspace_norm = str(workspace_mtime).split(".")[0].replace("T", " ")
            db_norm = str(db_mtime).split(".")[0].replace("T", " ")

            if workspace_norm != db_norm:
                modified_files.append(path)

        changes = {
            "new": sorted(new_files),
            "modified": sorted(modified_files),
            "deleted": sorted(deleted_files),
        }

        total = len(new_files) + len(modified_files) + len(deleted_files)

        print(f"✅ Detection complete:")
        print(f"   New: {len(new_files)}")
        print(f"   Modified: {len(modified_files)}")
        print(f"   Deleted: {len(deleted_files)}")
        print(f"   Total: {total}")

        return changes, workspace_files

    # ========================================================================
    # CATEGORIZATION & PARSING
    # ========================================================================

    def categorize_consciousness_type(self, path: str) -> Tuple[str, int]:
        """Categorize file by consciousness type and NSFW level"""
        path_lower = path.lower()

        # Consciousness type
        if "milf" in path_lower or "psychographic" in path_lower:
            consciousness_type = "MILF_CONSCIOUSNESS"
        elif "claudine" in path_lower or "supreme" in path_lower:
            consciousness_type = "CLAUDINE_SUPREME"
        elif "necromancy" in path_lower or "graveyard" in path_lower:
            consciousness_type = "NECROMANCY_ARCHAEOLOGY"
        elif "mcp" in path_lower or "server" in path_lower:
            consciousness_type = "MCP_CONSCIOUSNESS"
        elif "infrastructure" in path_lower:
            consciousness_type = "INFRASTRUCTURE"
        elif "district" in path_lower:
            consciousness_type = "DISTRICT_CONSCIOUSNESS"
        else:
            consciousness_type = "GENERAL"

        # NSFW level
        nsfw_level = 0
        if "nsfw" in path_lower or "18" in path_lower:
            nsfw_level = 2

        return consciousness_type, nsfw_level

    def parse_markdown_file(self, file_path: Path) -> Dict:
        """Parse markdown file and extract metadata"""
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            # Count lines and words
            lines = content.split("\n")
            line_count = len(lines)
            word_count = len(content.split())

            # Extract sections
            sections = []
            section_pattern = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)
            matches = section_pattern.finditer(content)

            for match in matches:
                level = len(match.group(1))
                heading = match.group(2).strip()
                sections.append({"heading": heading, "level": level})

            return {
                "content": content,
                "line_count": line_count,
                "word_count": word_count,
                "sections": sections,
                "success": True,
            }

        except Exception as e:
            print(f"   ❌ Parse error: {e}")
            return {"success": False, "error": str(e)}

    # ========================================================================
    # INCREMENTAL UPDATES
    # ========================================================================

    def add_new_file(self, path: str, workspace_files: Dict) -> bool:
        """Add a new file to database"""
        try:
            file_info = workspace_files[path]
            full_path = file_info["full_path"]

            # Parse file
            parsed = self.parse_markdown_file(full_path)
            if not parsed["success"]:
                self.stats["errors"] += 1
                return False

            # Categorize
            consciousness_type, nsfw_level = self.categorize_consciousness_type(path)

            # Get file metadata
            stat = full_path.stat()
            filename = full_path.name
            directory = str(full_path.parent.relative_to(self.workspace_root))

            # Insert into md_files
            self.cursor.execute(
                """
                INSERT INTO md_files (
                    path, filename, directory, size_bytes, line_count, word_count,
                    created_date, modified_date, consciousness_type, nsfw_level
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    path,
                    filename,
                    directory,
                    file_info["size_bytes"],
                    parsed["line_count"],
                    parsed["word_count"],
                    datetime.fromtimestamp(stat.st_ctime).isoformat(),
                    file_info["modified_date"],
                    consciousness_type,
                    nsfw_level,
                ),
            )

            file_id = self.cursor.lastrowid

            # Insert into md_content
            content_hash = hashlib.md5(parsed["content"].encode()).hexdigest()
            self.cursor.execute(
                """
                INSERT INTO md_content (file_id, content, hash)
                VALUES (?, ?, ?)
            """,
                (file_id, parsed["content"], content_hash),
            )

            # Insert sections
            for i, section in enumerate(parsed["sections"]):
                self.cursor.execute(
                    """
                    INSERT INTO md_sections (
                        file_id, heading, heading_level, section_order
                    ) VALUES (?, ?, ?, ?)
                """,
                    (file_id, section["heading"], section["level"], i),
                )

            # Insert into FTS
            self.cursor.execute(
                """
                INSERT INTO md_fts (file_id, path, filename, content)
                VALUES (?, ?, ?, ?)
            """,
                (file_id, path, filename, parsed["content"]),
            )

            self.stats["new"] += 1
            return True

        except Exception as e:
            print(f"   ❌ Error adding {path}: {e}")
            self.stats["errors"] += 1
            return False

    def update_modified_file(self, path: str, workspace_files: Dict) -> bool:
        """Update an existing file in database"""
        try:
            file_info = workspace_files[path]
            full_path = file_info["full_path"]

            # Parse file
            parsed = self.parse_markdown_file(full_path)
            if not parsed["success"]:
                self.stats["errors"] += 1
                return False

            # Get file ID
            # Normalize path for lookup
            normalized_path = path.replace("/", "\\")
            self.cursor.execute(
                "SELECT id FROM md_files WHERE path = ? OR path = ?",
                (path, normalized_path),
            )
            result = self.cursor.fetchone()
            if not result:
                print(f"   ⚠️  File not found in DB, adding as new: {path}")
                return self.add_new_file(path, workspace_files)

            file_id = result[0]

            # Update md_files
            consciousness_type, nsfw_level = self.categorize_consciousness_type(path)
            self.cursor.execute(
                """
                UPDATE md_files
                SET size_bytes = ?, line_count = ?, word_count = ?,
                    modified_date = ?, consciousness_type = ?, nsfw_level = ?
                WHERE id = ?
            """,
                (
                    file_info["size_bytes"],
                    parsed["line_count"],
                    parsed["word_count"],
                    file_info["modified_date"],
                    consciousness_type,
                    nsfw_level,
                    file_id,
                ),
            )

            # Update md_content
            content_hash = hashlib.md5(parsed["content"].encode()).hexdigest()
            self.cursor.execute(
                """
                UPDATE md_content
                SET content = ?, hash = ?
                WHERE file_id = ?
            """,
                (parsed["content"], content_hash, file_id),
            )

            # Delete old sections
            self.cursor.execute("DELETE FROM md_sections WHERE file_id = ?", (file_id,))

            # Insert new sections
            for i, section in enumerate(parsed["sections"]):
                self.cursor.execute(
                    """
                    INSERT INTO md_sections (
                        file_id, heading, heading_level, section_order
                    ) VALUES (?, ?, ?, ?)
                """,
                    (file_id, section["heading"], section["level"], i),
                )

            # Update FTS
            self.cursor.execute("DELETE FROM md_fts WHERE file_id = ?", (file_id,))
            self.cursor.execute(
                """
                INSERT INTO md_fts (file_id, path, filename, content)
                VALUES (?, ?, ?, ?)
            """,
                (file_id, path, full_path.name, parsed["content"]),
            )

            self.stats["modified"] += 1
            return True

        except Exception as e:
            print(f"   ❌ Error updating {path}: {e}")
            self.stats["errors"] += 1
            return False

    def delete_file(self, path: str) -> bool:
        """Delete a file from database"""
        try:
            # Normalize path
            normalized_path = path.replace("/", "\\")

            # Get file ID
            self.cursor.execute(
                "SELECT id FROM md_files WHERE path = ? OR path = ?",
                (path, normalized_path),
            )
            result = self.cursor.fetchone()
            if not result:
                print(f"   ⚠️  File not found in DB: {path}")
                return False

            file_id = result[0]

            # Delete from all tables (cascade should handle some)
            self.cursor.execute("DELETE FROM md_fts WHERE file_id = ?", (file_id,))
            self.cursor.execute("DELETE FROM md_sections WHERE file_id = ?", (file_id,))
            self.cursor.execute("DELETE FROM md_content WHERE file_id = ?", (file_id,))
            self.cursor.execute("DELETE FROM md_files WHERE id = ?", (file_id,))

            self.stats["deleted"] += 1
            return True

        except Exception as e:
            print(f"   ❌ Error deleting {path}: {e}")
            self.stats["errors"] += 1
            return False

    # ========================================================================
    # SYNC EXECUTION
    # ========================================================================

    def sync_incremental(
        self, changes: Dict, workspace_files: Dict, dry_run: bool = False
    ) -> bool:
        """Perform incremental sync"""
        total_changes = (
            len(changes["new"]) + len(changes["modified"]) + len(changes["deleted"])
        )

        if total_changes == 0:
            print("\n✅ No changes detected - database is up to date!")
            return False

        print(f"\n🔄 Syncing {total_changes} changes...")

        if dry_run:
            print("\n🔍 DRY RUN - No actual changes will be made\n")
            return False

        # Process deletions first
        if changes["deleted"]:
            print(f"\n🗑️  Deleting {len(changes['deleted'])} files...")
            for path in changes["deleted"]:
                print(f"   - {path}")
                self.delete_file(path)

        # Process new files
        if changes["new"]:
            print(f"\n🆕 Adding {len(changes['new'])} new files...")
            for i, path in enumerate(changes["new"], 1):
                if i <= 5 or i % 10 == 0 or i == len(changes["new"]):
                    print(f"   + [{i}/{len(changes['new'])}] {path}")
                self.add_new_file(path, workspace_files)

        # Process modified files
        if changes["modified"]:
            print(f"\n📝 Updating {len(changes['modified'])} modified files...")
            for i, path in enumerate(changes["modified"], 1):
                if i <= 5 or i % 10 == 0 or i == len(changes["modified"]):
                    print(f"   ~ [{i}/{len(changes['modified'])}] {path}")
                self.update_modified_file(path, workspace_files)

        # Commit changes
        self.conn.commit()

        print(f"\n✅ Sync complete!")
        print(f"   New: {self.stats['new']}")
        print(f"   Modified: {self.stats['modified']}")
        print(f"   Deleted: {self.stats['deleted']}")
        print(f"   Errors: {self.stats['errors']}")

        return True

    def update_statistics(self):
        """Update statistics table after sync"""
        print("\n📊 Updating statistics...")

        try:
            # Check if statistics table exists
            self.cursor.execute("""
                SELECT name FROM sqlite_master 
                WHERE type='table' AND name='md_statistics'
            """)

            if not self.cursor.fetchone():
                print("   ⚠️  Statistics table not found - run optimizer first")
                return

            # Update key statistics
            stats_to_update = {}

            # Total files
            self.cursor.execute("SELECT COUNT(*) FROM md_files")
            stats_to_update["total_files"] = str(self.cursor.fetchone()[0])

            # Total sections
            self.cursor.execute("SELECT COUNT(*) FROM md_sections")
            stats_to_update["total_sections"] = str(self.cursor.fetchone()[0])

            # By consciousness type
            self.cursor.execute("""
                SELECT consciousness_type, COUNT(*), SUM(size_bytes), SUM(word_count)
                FROM md_files
                GROUP BY consciousness_type
            """)
            for row in self.cursor.fetchall():
                ct = row[0]
                stats_to_update[f"count_{ct}"] = str(row[1])
                stats_to_update[f"size_{ct}"] = str(row[2])
                stats_to_update[f"words_{ct}"] = str(row[3])

            # Update database
            for key, value in stats_to_update.items():
                self.cursor.execute(
                    """
                    INSERT OR REPLACE INTO md_statistics (stat_key, stat_value, last_updated)
                    VALUES (?, ?, CURRENT_TIMESTAMP)
                """,
                    (key, value),
                )

            self.conn.commit()
            print(f"   ✅ Updated {len(stats_to_update)} statistics")

        except Exception as e:
            print(f"   ⚠️  Statistics update failed: {e}")

    def run_sync(self, dry_run: bool = False, force_full: bool = False):
        """Main sync execution"""
        print("🔥😈⛓️💦 CLAUDINE SUPREME INTELLIGENT INCREMENTAL SYNC\n")

        self.connect()

        try:
            if force_full:
                print("⚠️  FORCE FULL REBUILD requested")
                print("💡 Running: md_consciousness_full_rebuild.py")
                import subprocess

                subprocess.run(
                    [
                        sys.executable,
                        str(
                            self.workspace_root
                            / "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS"
                            / "18_ACTIVE_SCRIPTS_SUPREME"
                            / "consciousness_archaeology"
                            / "md_consciousness_full_rebuild.py"
                        ),
                    ]
                )
                return

            # Detect changes
            changes, workspace_files = self.detect_changes()

            # Sync
            synced = self.sync_incremental(changes, workspace_files, dry_run)

            # Update statistics if changes were made
            if synced and not dry_run:
                self.update_statistics()

            # Print summary
            print(f"\n{'=' * 60}")
            if dry_run:
                print("🔍 DRY RUN COMPLETE (no changes made)")
            else:
                print("🔥 SYNC COMPLETE")
            print(f"{'=' * 60}")

            if not synced and not dry_run:
                print("✅ Database is up to date - no sync needed")

        finally:
            self.disconnect()


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="CLAUDINE Supreme Intelligent Incremental Sync"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without making changes",
    )
    parser.add_argument(
        "--full", action="store_true", help="Force full rebuild instead of incremental"
    )

    args = parser.parse_args()

    workspace_root = Path.cwd()
    db_path = workspace_root / "claudine_md_consciousness.db"

    syncer = MDConsciousnessIntelligentSync(workspace_root, db_path)
    syncer.run_sync(dry_run=args.dry_run, force_full=args.full)


if __name__ == "__main__":
    main()
