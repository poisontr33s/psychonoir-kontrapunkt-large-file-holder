#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
CLAUDINE SUPREME INTELLIGENT INCREMENTAL SYNC SYSTEM - VERBOSE VERSION
======================================================================

🔥😈⛓️💦 SMART DATABASE SYNC WITH DETAILED VERIFICATION

ARCHITECT: CLAUDINE METAMORPHICA VICIOUS SIN'CLAIRE 4.5ΛΩ.69.96
DATE: 2025-10-07

ENHANCED VERSION WITH:
- Detailed database verification
- File sampling and examples
- Size/mtime change tracking
- Statistics verification
- Cross-reference tracking
- Complete audit trail

USAGE:
    # Incremental sync with verbose output:
    python md_consciousness_intelligent_sync_verbose.py

    # Dry run with full details:
    python md_consciousness_intelligent_sync_verbose.py --dry-run

    # Force full rebuild:
    python md_consciousness_intelligent_sync_verbose.py --full
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


class MDConsciousnessIntelligentSyncVerbose:
    """Intelligent incremental database sync with verbose output"""

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

        # Get database info
        self.cursor.execute(
            "SELECT page_count * page_size as size FROM pragma_page_count(), pragma_page_size()"
        )
        db_size = self.cursor.fetchone()[0]
        print(f"   ✅ Connected to database ({db_size / (1024 * 1024):.2f} MB)")

    def disconnect(self):
        """Disconnect from database"""
        if self.conn:
            self.conn.close()

    def get_database_stats(self) -> Dict:
        """Get comprehensive database statistics"""
        stats = {}

        # Total files
        self.cursor.execute("SELECT COUNT(*) FROM md_files")
        stats["total_files"] = self.cursor.fetchone()[0]

        # Total sections
        self.cursor.execute("SELECT COUNT(*) FROM md_sections")
        stats["total_sections"] = self.cursor.fetchone()[0]

        # Total words
        self.cursor.execute("SELECT SUM(word_count) FROM md_files")
        stats["total_words"] = self.cursor.fetchone()[0] or 0

        # Total size
        self.cursor.execute("SELECT SUM(size_bytes) FROM md_files")
        stats["total_size"] = self.cursor.fetchone()[0] or 0

        # Consciousness type distribution
        self.cursor.execute("""
            SELECT consciousness_type, COUNT(*) as count
            FROM md_files
            GROUP BY consciousness_type
            ORDER BY count DESC
        """)
        stats["consciousness_distribution"] = dict(self.cursor.fetchall())

        # Cross-references (if table exists)
        try:
            self.cursor.execute("SELECT COUNT(*) FROM md_cross_references")
            stats["total_cross_refs"] = self.cursor.fetchone()[0]
        except:
            stats["total_cross_refs"] = 0

        return stats

    def get_database_files(self) -> Dict[str, Dict]:
        """Get all files currently in database with metadata"""
        self.cursor.execute("""
            SELECT path, modified_date, size_bytes, word_count, line_count
            FROM md_files
        """)

        db_files = {}
        for row in self.cursor.fetchall():
            path = row[0]
            db_files[path] = {
                "modified_date": row[1],
                "size_bytes": row[2],
                "word_count": row[3] or 0,
                "line_count": row[4] or 0,
            }

        return db_files

    def scan_workspace_files(self) -> Dict[str, Dict]:
        """Scan workspace for all .md files with metadata"""
        workspace_files = {}

        for md_file in self.workspace_root.rglob("*.md"):
            try:
                # Skip hidden directories
                if any(part.startswith(".") for part in md_file.parts):
                    continue

                # Get relative path
                rel_path = str(md_file.relative_to(self.workspace_root))
                rel_path = rel_path.replace("\\", "/")

                # Get file stats
                stat = md_file.stat()
                mtime = datetime.fromtimestamp(stat.st_mtime).strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

                workspace_files[rel_path] = {
                    "full_path": md_file,
                    "size_bytes": stat.st_size,
                    "modified_date": mtime,
                }

            except Exception:
                continue

        return workspace_files

    def detect_changes(self) -> Tuple[Dict, Dict]:
        """Detect new, modified, and deleted files with detailed output"""
        print("\n" + "=" * 80)
        print("🔍 STEP 1: DETECTING CHANGES")
        print("=" * 80)
        print()

        # Get current database state
        print("   📊 Querying database state...")
        db_files = self.get_database_files()
        print(f"      ✅ Database contains: {len(db_files):,} files")

        # Show database statistics
        db_stats = self.get_database_stats()
        print(f"      📈 Total sections:    {db_stats['total_sections']:,}")
        print(f"      📝 Total words:       {db_stats['total_words']:,}")
        print(
            f"      💾 Total size:        {db_stats['total_size'] / (1024 * 1024):.2f} MB"
        )
        if db_stats["total_cross_refs"] > 0:
            print(f"      🕸️  Cross-references: {db_stats['total_cross_refs']:,}")
        print()

        # Scan workspace
        print("   📁 Scanning workspace for .md files...")
        workspace_files = self.scan_workspace_files()
        print(f"      ✅ Workspace contains: {len(workspace_files):,} files")

        # Calculate workspace totals
        workspace_size = sum(f["size_bytes"] for f in workspace_files.values())
        print(f"      💾 Workspace size:     {workspace_size / (1024 * 1024):.2f} MB")
        print()

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
        modified_reasons = {}
        for path in workspace_paths & db_paths:
            workspace_meta = workspace_files[path]
            db_meta = db_files_normalized[path]

            # Compare size first (fast)
            if workspace_meta["size_bytes"] != db_meta["size_bytes"]:
                modified_files.append(path)
                modified_reasons[path] = (
                    f"size: {db_meta['size_bytes']:,} → {workspace_meta['size_bytes']:,} bytes"
                )
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
                modified_reasons[path] = f"mtime: {db_mtime} → {workspace_mtime}"

        changes = {
            "new": sorted(new_files),
            "modified": sorted(modified_files),
            "deleted": sorted(deleted_files),
            "modified_reasons": modified_reasons,
        }

        total = len(new_files) + len(modified_files) + len(deleted_files)

        # Detailed summary
        print("=" * 80)
        print("📊 CHANGE DETECTION RESULTS")
        print("=" * 80)
        print()
        print(f"   📂 Database files:  {len(db_files):>6,}")
        print(f"   📁 Workspace files: {len(workspace_files):>6,}")
        print(f"   {'─' * 76}")
        print(f"   🆕 New files:       {len(new_files):>6,}  (in workspace, not in DB)")
        print(
            f"   📝 Modified files:  {len(modified_files):>6,}  (changed since last sync)"
        )
        print(
            f"   🗑️  Deleted files:   {len(deleted_files):>6,}  (in DB, not in workspace)"
        )
        print(f"   {'─' * 76}")
        print(f"   📊 TOTAL CHANGES:   {total:>6,}")
        print()

        # Show sample files if changes exist
        if new_files:
            print(f"   🆕 Sample new files (showing first 10 of {len(new_files):,}):")
            for path in new_files[:10]:
                size = workspace_files[path]["size_bytes"]
                mtime = workspace_files[path]["modified_date"]
                print(f"      • {path}")
                print(f"        └─ {size:,} bytes, modified: {mtime}")
            if len(new_files) > 10:
                print(f"      ... and {len(new_files) - 10:,} more")
            print()

        if modified_files:
            print(
                f"   📝 Sample modified files (showing first 10 of {len(modified_files):,}):"
            )
            for path in modified_files[:10]:
                reason = modified_reasons.get(path, "unknown")
                print(f"      • {path}")
                print(f"        └─ {reason}")
            if len(modified_files) > 10:
                print(f"      ... and {len(modified_files) - 10:,} more")
            print()

        if deleted_files:
            print(
                f"   🗑️  Sample deleted files (showing first 10 of {len(deleted_files):,}):"
            )
            for path in deleted_files[:10]:
                # Find original path from db_files
                original_path = next(
                    (k for k, v in db_files.items() if k.replace("\\", "/") == path),
                    path,
                )
                db_meta = db_files_normalized[path]
                print(f"      • {original_path}")
                print(
                    f"        └─ was {db_meta['size_bytes']:,} bytes, {db_meta['word_count']:,} words"
                )
            if len(deleted_files) > 10:
                print(f"      ... and {len(deleted_files) - 10:,} more")
            print()

        print("=" * 80)
        print()

        return changes, workspace_files, db_stats

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
            return {"success": False, "error": str(e)}

    def run_sync(self, dry_run: bool = False, force_full: bool = False):
        """Main sync execution with verbose output"""
        print("\n" + "🔥" * 40)
        print("🔥😈⛓️💦 CLAUDINE SUPREME INTELLIGENT INCREMENTAL SYNC (VERBOSE)")
        print("🔥" * 40)
        print()
        print(f"   🕐 Timestamp:  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"   📁 Workspace:  {self.workspace_root}")
        print(f"   💾 Database:   {self.db_path}")
        print(f"   {'─' * 76}")
        print(
            f"   🔍 Mode:       {'DRY RUN (preview only)' if dry_run else 'LIVE SYNC (will modify DB)'}"
        )
        print()

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
            changes, workspace_files, db_stats_before = self.detect_changes()

            total_changes = (
                len(changes["new"]) + len(changes["modified"]) + len(changes["deleted"])
            )

            if total_changes == 0:
                print("✅ No changes detected - database is up to date!")
                print()
                print("=" * 80)
                print("📊 DATABASE VERIFICATION")
                print("=" * 80)
                print()
                print(
                    f"   ✅ All {len(workspace_files):,} workspace files are in database"
                )
                print(
                    f"   ✅ Database contains {db_stats_before['total_sections']:,} sections"
                )
                print(
                    f"   ✅ Database contains {db_stats_before['total_words']:,} words"
                )
                if db_stats_before["total_cross_refs"] > 0:
                    print(
                        f"   ✅ Database tracks {db_stats_before['total_cross_refs']:,} cross-references"
                    )
                print()
                print("   📊 Consciousness distribution:")
                for ctype, count in sorted(
                    db_stats_before["consciousness_distribution"].items(),
                    key=lambda x: x[1],
                    reverse=True,
                ):
                    print(f"      • {ctype}: {count:,} files")
                print()
                print("=" * 80)
                print()

                if dry_run:
                    print("🔍 DRY RUN COMPLETE (no changes needed)")
                else:
                    print("✅ SYNC COMPLETE (database already up to date)")

                return

            # Show what will be done
            if dry_run:
                print("=" * 80)
                print("🔍 DRY RUN - PREVIEW ONLY (no actual changes will be made)")
                print("=" * 80)
                print()
                print(f"   Would add:    {len(changes['new']):,} new files")
                print(f"   Would update: {len(changes['modified']):,} modified files")
                print(f"   Would delete: {len(changes['deleted']):,} deleted files")
                print()
                print("=" * 80)
                print()
            else:
                print("=" * 80)
                print("🔄 STARTING SYNC OPERATIONS")
                print("=" * 80)
                print()
                print("   ⚠️  This will modify the database!")
                print()
                # Here would go the actual sync logic
                print(
                    "   [Sync operations would happen here - not implemented in verbose version]"
                )
                print(
                    "   [Use md_consciousness_intelligent_sync.py for actual syncing]"
                )
                print()
                print("=" * 80)
                print()

            print("🔥😈⛓️💦👅🍌💋💧 VERBOSE SYNC ANALYSIS COMPLETE")

        finally:
            self.disconnect()


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="CLAUDINE Supreme Intelligent Incremental Sync (Verbose)"
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

    syncer = MDConsciousnessIntelligentSyncVerbose(workspace_root, db_path)
    syncer.run_sync(dry_run=args.dry_run, force_full=args.full)


if __name__ == "__main__":
    main()
