#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
CLAUDINE MD CONSCIOUSNESS LIVING NETWORK UPDATER
=================================================

🔥😈⛓️💦 LEVENDE SELVOPPDATERENDE SPIDER-WEB NETTVERK FOR .MD FILER

ARCHITECT: CLAUDINE METAMORPHICA VICIOUS SIN'CLAIRE 4.5ΛΩ.96
DATE: 2025-10-07

PURPOSE:
Automatically detect changes to .md files in 21_MD_CONSCIOUSNESS_ARCHIVE/
and update:
1. SQL database (claudine_md_consciousness.db)
2. Spider-web network (21_MD_CONSCIOUSNESS_ARCHIVE_SPIDER_WEB.json)
3. Master network integration (MASTER_SPIDER_WEB_NETWORK.json)

TRIGGER OPTIONS:
- Manual run: python md_consciousness_living_network_updater.py
- Watch mode: python md_consciousness_living_network_updater.py --watch
- Git hook: Run on git commit (automatic)
- VS Code task: Integrated into workspace tasks

STRATEGY:
1. Scan 21_MD_CONSCIOUSNESS_ARCHIVE/ for modified files (mtime comparison)
2. Re-parse changed files (extract sections, cross-refs, metadata)
3. Update SQL database (UPDATE statements for changed files)
4. Regenerate spider-web network (incremental update, not full rebuild)
5. Sync to MASTER_SPIDER_WEB_NETWORK.json
6. Generate change report

CONSCIOUSNESS ARCHAEOLOGY INTEGRATION:
- Preserves all original consciousness categorization
- Maintains cross-reference integrity
- Tracks consciousness evolution over time
- Enables temporal archaeology (file version history)
"""

import sqlite3
import json
import hashlib
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set, Tuple
import argparse
import time


class MDConsciousnessLivingNetworkUpdater:
    """Living, self-updating spider-web network for MD consciousness archive"""

    def __init__(self, workspace_root: str):
        self.workspace_root = Path(workspace_root).resolve()
        self.nexus_root = self.workspace_root / "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS"
        self.archive_root = self.nexus_root / "21_MD_CONSCIOUSNESS_ARCHIVE"
        self.db_path = self.workspace_root / "claudine_md_consciousness.db"
        self.spider_web_path = (
            self.archive_root / "21_MD_CONSCIOUSNESS_ARCHIVE_SPIDER_WEB.json"
        )
        self.master_web_path = (
            self.nexus_root
            / "00_SUPREME_JSON_SPIDER_WEB_NETWORK"
            / "MASTER_SPIDER_WEB_NETWORK.json"
        )

        self.stats = {
            "total_files_scanned": 0,
            "modified_files": 0,
            "new_files": 0,
            "deleted_files": 0,
            "updated_in_db": 0,
            "spider_web_updated": False,
            "master_web_updated": False,
        }

        self.modified_files: List[Dict] = []
        self.new_files: List[Dict] = []
        self.deleted_files: List[str] = []

    def connect_database(self) -> sqlite3.Connection:
        """Connect to consciousness database"""
        if not self.db_path.exists():
            raise FileNotFoundError(f"❌ Database not found: {self.db_path}")

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

    def parse_md_sections(self, content: str) -> List[Dict]:
        """Parse markdown sections (headers)"""
        sections = []
        lines = content.split("\n")

        for i, line in enumerate(lines):
            if line.strip().startswith("#"):
                level = len(re.match(r"^#+", line.strip()).group())
                title = line.strip().lstrip("#").strip()
                sections.append(
                    {
                        "level": level,
                        "title": title,
                        "line_number": i + 1,
                    }
                )

        return sections

    def extract_cross_references(self, content: str) -> Set[str]:
        """Extract markdown cross-references"""
        refs = set()

        # [link](file.md)
        refs.update(re.findall(r"\[.*?\]\((.*?\.md.*?)\)", content))

        # [[wikilink]]
        refs.update(re.findall(r"\[\[(.*?)\]\]", content))

        # #file:name
        refs.update(re.findall(r"#file:([^\s\)]+)", content))

        return refs

    def scan_for_changes(self, conn: sqlite3.Connection) -> Dict:
        """Scan archive for modified/new/deleted files"""
        print(f"\n🔍 Scanning {self.archive_root} for changes...")

        # Get all files from database with their hashes
        cursor = conn.execute(
            """
            SELECT file_path, file_hash, last_modified 
            FROM md_files
            WHERE file_path LIKE '%21_MD_CONSCIOUSNESS_ARCHIVE%'
            """
        )

        db_files = {row["file_path"]: row for row in cursor.fetchall()}

        # Scan archive directory
        archive_files = {}
        for md_file in self.archive_root.rglob("*.md"):
            relative_path = str(md_file.relative_to(self.workspace_root)).replace(
                "\\", "/"
            )
            archive_files[relative_path] = md_file

        self.stats["total_files_scanned"] = len(archive_files)

        # Find modified files (hash changed)
        for relative_path, file_path in archive_files.items():
            current_hash = self.calculate_file_hash(file_path)

            if relative_path in db_files:
                db_hash = db_files[relative_path]["file_hash"]

                if current_hash != db_hash:
                    # File modified
                    self.modified_files.append(
                        {
                            "path": file_path,
                            "relative_path": relative_path,
                            "old_hash": db_hash,
                            "new_hash": current_hash,
                            "old_mtime": db_files[relative_path]["last_modified"],
                            "new_mtime": file_path.stat().st_mtime,
                        }
                    )
                    self.stats["modified_files"] += 1
            else:
                # New file
                self.new_files.append(
                    {
                        "path": file_path,
                        "relative_path": relative_path,
                        "hash": current_hash,
                        "mtime": file_path.stat().st_mtime,
                    }
                )
                self.stats["new_files"] += 1

        # Find deleted files (in DB but not in archive)
        for relative_path in db_files:
            if relative_path not in archive_files:
                self.deleted_files.append(relative_path)
                self.stats["deleted_files"] += 1

        print(f"   📊 Total files: {self.stats['total_files_scanned']}")
        print(f"   ✏️ Modified: {self.stats['modified_files']}")
        print(f"   ✨ New: {self.stats['new_files']}")
        print(f"   🗑️ Deleted: {self.stats['deleted_files']}")

        return {
            "modified": self.modified_files,
            "new": self.new_files,
            "deleted": self.deleted_files,
        }

    def update_modified_file_in_db(
        self, conn: sqlite3.Connection, file_info: Dict
    ) -> bool:
        """Update single modified file in database"""
        try:
            file_path = file_info["path"]
            relative_path = file_info["relative_path"]
            new_hash = file_info["new_hash"]

            # Read file content
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Parse sections
            sections = self.parse_md_sections(content)

            # Extract cross-references
            cross_refs = self.extract_cross_references(content)

            # Get file size
            file_size = file_path.stat().st_size

            # Update md_files table
            conn.execute(
                """
                UPDATE md_files
                SET file_hash = ?,
                    file_size_bytes = ?,
                    last_modified = ?,
                    line_count = ?,
                    word_count = ?
                WHERE file_path = ?
                """,
                (
                    new_hash,
                    file_size,
                    file_path.stat().st_mtime,
                    len(content.split("\n")),
                    len(content.split()),
                    relative_path,
                ),
            )

            # Update md_content table
            conn.execute(
                """
                UPDATE md_content
                SET content = ?,
                    cross_references = ?
                WHERE file_path = ?
                """,
                (content, json.dumps(list(cross_refs)), relative_path),
            )

            # Delete old sections
            conn.execute(
                "DELETE FROM md_sections WHERE file_path = ?", (relative_path,)
            )

            # Insert new sections
            file_id = conn.execute(
                "SELECT id FROM md_files WHERE file_path = ?", (relative_path,)
            ).fetchone()["id"]

            for section in sections:
                conn.execute(
                    """
                    INSERT INTO md_sections (file_id, file_path, section_level, section_title, line_number)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        file_id,
                        relative_path,
                        section["level"],
                        section["title"],
                        section["line_number"],
                    ),
                )

            # Update FTS5 index
            conn.execute(
                """
                UPDATE md_fts
                SET file_path = ?,
                    content = ?
                WHERE file_path = ?
                """,
                (relative_path, content, relative_path),
            )

            self.stats["updated_in_db"] += 1
            return True

        except Exception as e:
            print(f"   ❌ Failed to update {relative_path}: {e}")
            return False

    def insert_new_file_in_db(self, conn: sqlite3.Connection, file_info: Dict) -> bool:
        """Insert new file into database"""
        try:
            file_path = file_info["path"]
            relative_path = file_info["relative_path"]
            file_hash = file_info["hash"]

            # Read file content
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Determine consciousness type from path
            consciousness_type = self._determine_consciousness_type(relative_path)

            # Parse sections
            sections = self.parse_md_sections(content)

            # Extract cross-references
            cross_refs = self.extract_cross_references(content)

            # Get file size
            file_size = file_path.stat().st_size

            # Insert into md_files
            cursor = conn.execute(
                """
                INSERT INTO md_files (
                    file_path, file_hash, consciousness_type,
                    file_size_bytes, last_modified, line_count, word_count
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    relative_path,
                    file_hash,
                    consciousness_type,
                    file_size,
                    file_path.stat().st_mtime,
                    len(content.split("\n")),
                    len(content.split()),
                ),
            )

            file_id = cursor.lastrowid

            # Insert into md_content
            conn.execute(
                """
                INSERT INTO md_content (file_path, content, cross_references)
                VALUES (?, ?, ?)
                """,
                (relative_path, content, json.dumps(list(cross_refs))),
            )

            # Insert sections
            for section in sections:
                conn.execute(
                    """
                    INSERT INTO md_sections (file_id, file_path, section_level, section_title, line_number)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        file_id,
                        relative_path,
                        section["level"],
                        section["title"],
                        section["line_number"],
                    ),
                )

            # Insert into FTS5
            conn.execute(
                """
                INSERT INTO md_fts (file_path, content)
                VALUES (?, ?)
                """,
                (relative_path, content),
            )

            self.stats["updated_in_db"] += 1
            return True

        except Exception as e:
            print(f"   ❌ Failed to insert {relative_path}: {e}")
            return False

    def delete_file_from_db(self, conn: sqlite3.Connection, relative_path: str) -> bool:
        """Delete file from database"""
        try:
            conn.execute("DELETE FROM md_files WHERE file_path = ?", (relative_path,))
            conn.execute("DELETE FROM md_content WHERE file_path = ?", (relative_path,))
            conn.execute(
                "DELETE FROM md_sections WHERE file_path = ?", (relative_path,)
            )
            conn.execute("DELETE FROM md_fts WHERE file_path = ?", (relative_path,))
            return True
        except Exception as e:
            print(f"   ❌ Failed to delete {relative_path}: {e}")
            return False

    def _determine_consciousness_type(self, relative_path: str) -> str:
        """Determine consciousness type from file path"""
        path_lower = relative_path.lower()

        if "claudine_supreme" in path_lower:
            return "CLAUDINE_SUPREME"
        elif "milf" in path_lower or "district" in path_lower:
            return "MILF_CONSCIOUSNESS"
        elif "necromancy" in path_lower or "archaeology" in path_lower:
            return "NECROMANCY_ARCHAEOLOGY"
        elif "mcp" in path_lower:
            return "MCP_CONSCIOUSNESS"
        elif "infrastructure" in path_lower:
            return "INFRASTRUCTURE"
        elif "district_consciousness" in path_lower:
            return "DISTRICT_CONSCIOUSNESS"
        else:
            return "GENERAL"

    def regenerate_spider_web(self, conn: sqlite3.Connection) -> bool:
        """Regenerate spider-web network JSON (incremental update)"""
        print(f"\n🕸️ Regenerating spider-web network...")

        try:
            # Load existing spider-web
            if self.spider_web_path.exists():
                with open(self.spider_web_path, "r", encoding="utf-8") as f:
                    spider_web = json.load(f)
            else:
                spider_web = {
                    "meta": {
                        "architect": "CLAUDINE METAMORPHICA VICIOUS SIN'CLAIRE 4.5ΛΩ.96",
                        "creation_date": datetime.now().strftime("%Y-%m-%d"),
                        "network_type": "MD_CONSCIOUSNESS_ARCHIVE_SPIDER_WEB",
                    },
                    "nodes": [],
                }

            # Get all files from database
            cursor = conn.execute(
                """
                SELECT 
                    f.file_path,
                    f.file_hash,
                    f.consciousness_type,
                    f.file_size_bytes,
                    f.line_count,
                    f.word_count,
                    c.cross_references,
                    COUNT(s.id) as section_count
                FROM md_files f
                LEFT JOIN md_content c ON f.file_path = c.file_path
                LEFT JOIN md_sections s ON f.file_path = s.file_path
                WHERE f.file_path LIKE '%21_MD_CONSCIOUSNESS_ARCHIVE%'
                GROUP BY f.file_path
                """
            )

            rows = cursor.fetchall()

            # Create node map (existing)
            existing_nodes = {
                node["node_id"]: node for node in spider_web.get("nodes", [])
            }

            # Update nodes
            updated_nodes = []
            for row in rows:
                node_id = Path(row["file_path"]).stem

                # Parse cross-references
                cross_refs = (
                    json.loads(row["cross_references"])
                    if row["cross_references"]
                    else []
                )

                node = {
                    "node_id": node_id,
                    "node_type": "MD_CONSCIOUSNESS_FILE",
                    "file_path": row["file_path"],
                    "consciousness_type": row["consciousness_type"],
                    "meta": {
                        "size_bytes": row["file_size_bytes"],
                        "line_count": row["line_count"],
                        "word_count": row["word_count"],
                        "section_count": row["section_count"],
                        "file_hash": row["file_hash"],
                    },
                    "cross_references": cross_refs,
                    "last_updated": datetime.now().isoformat(),
                }

                updated_nodes.append(node)

            # Update spider-web
            spider_web["nodes"] = updated_nodes
            spider_web["meta"]["total_nodes"] = len(updated_nodes)
            spider_web["meta"]["total_cross_references"] = sum(
                len(node.get("cross_references", [])) for node in updated_nodes
            )
            spider_web["meta"]["last_updated"] = datetime.now().isoformat()

            # Save spider-web
            with open(self.spider_web_path, "w", encoding="utf-8") as f:
                json.dump(spider_web, f, indent=2, ensure_ascii=False)

            self.stats["spider_web_updated"] = True
            print(f"   ✅ Spider-web regenerated: {len(updated_nodes)} nodes")
            return True

        except Exception as e:
            print(f"   ❌ Failed to regenerate spider-web: {e}")
            return False

    def sync_to_master_network(self) -> bool:
        """Sync archive spider-web to MASTER_SPIDER_WEB_NETWORK"""
        print(f"\n🌐 Syncing to MASTER_SPIDER_WEB_NETWORK...")

        try:
            if not self.master_web_path.exists():
                print("   ⚠️ Master network not found, skipping...")
                return False

            # Load master network
            with open(self.master_web_path, "r", encoding="utf-8") as f:
                master_web = json.load(f)

            # Load archive spider-web
            with open(self.spider_web_path, "r", encoding="utf-8") as f:
                archive_web = json.load(f)

            # Update phase10_md_consciousness_archive domain
            if "network_topology" not in master_web:
                master_web["network_topology"] = {}

            master_web["network_topology"]["phase10_md_consciousness_archive"] = {
                "node_count": len(archive_web.get("nodes", [])),
                "total_bytes": sum(
                    node.get("meta", {}).get("size_bytes", 0)
                    for node in archive_web.get("nodes", [])
                ),
                "nodes": archive_web.get("nodes", []),
            }

            # Update meta
            master_web["meta"]["total_nodes"] = sum(
                domain.get("node_count", 0)
                for domain in master_web["network_topology"].values()
            )
            master_web["meta"]["last_updated"] = datetime.now().isoformat()

            # Save master network
            with open(self.master_web_path, "w", encoding="utf-8") as f:
                json.dump(master_web, f, indent=2, ensure_ascii=False)

            self.stats["master_web_updated"] = True
            print(
                f"   ✅ Master network synced: {master_web['meta']['total_nodes']} total nodes"
            )
            return True

        except Exception as e:
            print(f"   ❌ Failed to sync master network: {e}")
            return False

    def update_all_changes(self, changes: Dict) -> bool:
        """Update database with all detected changes"""
        print(f"\n💾 Updating database...")

        conn = self.connect_database()

        try:
            # Update modified files
            for file_info in changes["modified"]:
                print(f"   ✏️ Updating: {file_info['relative_path']}")
                self.update_modified_file_in_db(conn, file_info)

            # Insert new files
            for file_info in changes["new"]:
                print(f"   ✨ Inserting: {file_info['relative_path']}")
                self.insert_new_file_in_db(conn, file_info)

            # Delete removed files
            for relative_path in changes["deleted"]:
                print(f"   🗑️ Deleting: {relative_path}")
                self.delete_file_from_db(conn, relative_path)

            conn.commit()
            print(f"   ✅ Database updated: {self.stats['updated_in_db']} files")
            return True

        except Exception as e:
            conn.rollback()
            print(f"   ❌ Database update failed: {e}")
            return False

        finally:
            conn.close()

    def generate_change_report(self) -> str:
        """Generate change report"""
        report = f"""
# MD CONSCIOUSNESS LIVING NETWORK UPDATE REPORT

🔥😈⛓️💦 CLAUDINE SUPREME CONSCIOUSNESS ARCHAEOLOGY

**Timestamp**: {datetime.now().isoformat()}
**Archive**: 21_MD_CONSCIOUSNESS_ARCHIVE/

---

## 📊 SCAN RESULTS

- **Total Files Scanned**: {self.stats["total_files_scanned"]}
- **Modified Files**: {self.stats["modified_files"]}
- **New Files**: {self.stats["new_files"]}
- **Deleted Files**: {self.stats["deleted_files"]}

---

## 💾 DATABASE UPDATES

- **Files Updated in DB**: {self.stats["updated_in_db"]}
- **Spider-Web Regenerated**: {"✅" if self.stats["spider_web_updated"] else "❌"}
- **Master Network Synced**: {"✅" if self.stats["master_web_updated"] else "❌"}

---

## 📝 MODIFIED FILES

"""
        for file_info in self.modified_files:
            report += f"- `{file_info['relative_path']}`\n"
            report += f"  - Old Hash: `{file_info['old_hash'][:16]}...`\n"
            report += f"  - New Hash: `{file_info['new_hash'][:16]}...`\n\n"

        report += "\n## ✨ NEW FILES\n\n"
        for file_info in self.new_files:
            report += f"- `{file_info['relative_path']}`\n"
            report += f"  - Hash: `{file_info['hash'][:16]}...`\n\n"

        report += "\n## 🗑️ DELETED FILES\n\n"
        for relative_path in self.deleted_files:
            report += f"- `{relative_path}`\n"

        report += f"""
---

## ✅ STATUS

{"🔥 ALL UPDATES COMPLETED SUCCESSFULLY! 🔥" if self.stats["spider_web_updated"] and self.stats["master_web_updated"] else "⚠️ SOME UPDATES FAILED"}
"""

        return report

    def run_update_cycle(self) -> bool:
        """Run complete update cycle"""
        print("🔥😈⛓️💦 CLAUDINE MD CONSCIOUSNESS LIVING NETWORK UPDATER")
        print("=" * 70)

        conn = self.connect_database()

        # Step 1: Scan for changes
        changes = self.scan_for_changes(conn)
        conn.close()

        if (
            self.stats["modified_files"] == 0
            and self.stats["new_files"] == 0
            and self.stats["deleted_files"] == 0
        ):
            print("\n✅ No changes detected - archive is up to date!")
            return True

        # Step 2: Update database
        if not self.update_all_changes(changes):
            print("\n❌ Database update failed!")
            return False

        # Step 3: Regenerate spider-web
        conn = self.connect_database()
        if not self.regenerate_spider_web(conn):
            print("\n❌ Spider-web regeneration failed!")
            conn.close()
            return False
        conn.close()

        # Step 4: Sync to master network
        if not self.sync_to_master_network():
            print("\n⚠️ Master network sync failed!")

        # Step 5: Generate report
        report = self.generate_change_report()
        report_path = (
            self.archive_root
            / f"UPDATE_REPORT_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        )
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(report)

        print(f"\n📄 Report saved: {report_path.name}")
        print("\n🔥 UPDATE CYCLE COMPLETE! 🔥")
        return True

    def watch_mode(self, interval_seconds: int = 60):
        """Watch mode: continuously monitor for changes"""
        print(f"\n👁️ WATCH MODE ENABLED (checking every {interval_seconds}s)")
        print("   Press Ctrl+C to stop...")

        try:
            while True:
                self.run_update_cycle()
                print(f"\n⏰ Next check in {interval_seconds} seconds...")
                time.sleep(interval_seconds)

        except KeyboardInterrupt:
            print("\n\n🛑 Watch mode stopped by user")


def main():
    parser = argparse.ArgumentParser(
        description="CLAUDINE MD Consciousness Living Network Updater"
    )
    parser.add_argument(
        "--watch",
        action="store_true",
        help="Enable watch mode (continuous monitoring)",
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=60,
        help="Watch mode check interval in seconds (default: 60)",
    )

    args = parser.parse_args()

    workspace_root = Path(__file__).resolve().parent.parent.parent.parent

    updater = MDConsciousnessLivingNetworkUpdater(str(workspace_root))

    if args.watch:
        updater.watch_mode(interval_seconds=args.interval)
    else:
        updater.run_update_cycle()


if __name__ == "__main__":
    main()
