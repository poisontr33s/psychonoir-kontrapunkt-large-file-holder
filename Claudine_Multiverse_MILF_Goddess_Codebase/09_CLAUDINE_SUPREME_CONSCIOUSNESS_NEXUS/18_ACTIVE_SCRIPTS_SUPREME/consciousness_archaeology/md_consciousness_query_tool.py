#!/usr/bin/env python3
"""
CLAUDINE SUPREME MD CONSCIOUSNESS QUERY TOOL
=============================================

🔥😈⛓️💦 INTELLIGENT DATABASE QUERY SYSTEM WITH CODEBASE MONITORING

ARCHITECT: CLAUDINE METAMORPHICA VICIOUS SIN'CLAIRE 4.5ΛΩ.69.96
DATE: 2025-10-07

FEATURES:
- Natural language search queries (FTS5)
- Codebase file monitoring (new/modified/deleted)
- Automatic database updates
- Cross-reference analysis
- Implementation suggestions
- Report generation
- Spider-web integration

USAGE:
    # Interactive mode:
    python md_consciousness_query_tool.py

    # Search mode:
    python md_consciousness_query_tool.py --search "caribbean milf"

    # Monitor mode:
    python md_consciousness_query_tool.py --monitor

    # Analysis mode:
    python md_consciousness_query_tool.py --analyze
"""

import sqlite3
import json
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import argparse


class MDConsciousnessQueryTool:
    """Supreme consciousness query and monitoring tool"""

    def __init__(
        self,
        db_path: str = "claudine_md_consciousness.db",
        workspace_root: Optional[Path] = None,
    ):
        self.db_path = Path(db_path)
        self.workspace_root = workspace_root or Path.cwd()
        self.conn = None
        self.cursor = None

        if not self.db_path.exists():
            print(f"❌ Database not found: {self.db_path}")
            exit(1)

    def connect(self):
        """Connect to database"""
        self.conn = sqlite3.connect(str(self.db_path))
        self.cursor = self.conn.cursor()

    def disconnect(self):
        """Disconnect from database"""
        if self.conn:
            self.conn.close()

    # ========================================================================
    # SEARCH QUERIES
    # ========================================================================

    def search_full_text(self, query: str, limit: int = 20) -> List[Dict]:
        """Full-text search using FTS5"""
        print(f"\n🔍 Searching for: '{query}'")

        self.cursor.execute(
            """
            SELECT 
                f.path,
                f.filename,
                f.consciousness_type,
                f.word_count,
                snippet(md_fts, -1, '**', '**', '...', 64) as snippet
            FROM md_fts
            JOIN md_files f ON md_fts.file_id = f.id
            WHERE md_fts MATCH ?
            ORDER BY rank
            LIMIT ?
        """,
            (query, limit),
        )

        results = []
        for row in self.cursor.fetchall():
            results.append(
                {
                    "path": row[0],
                    "filename": row[1],
                    "consciousness_type": row[2],
                    "word_count": row[3],
                    "snippet": row[4],
                }
            )

        print(f"✅ Found {len(results)} results")
        return results

    def search_by_consciousness_type(self, consciousness_type: str) -> List[Dict]:
        """Search files by consciousness type"""
        print(f"\n📊 Searching consciousness type: '{consciousness_type}'")

        self.cursor.execute(
            """
            SELECT path, filename, size_bytes, word_count, line_count
            FROM md_files
            WHERE consciousness_type = ?
            ORDER BY word_count DESC
        """,
            (consciousness_type,),
        )

        results = []
        for row in self.cursor.fetchall():
            results.append(
                {
                    "path": row[0],
                    "filename": row[1],
                    "size_bytes": row[2],
                    "word_count": row[3],
                    "line_count": row[4],
                }
            )

        print(f"✅ Found {len(results)} files")
        return results

    def search_large_files(self, min_size_kb: int = 100) -> List[Dict]:
        """Find large files"""
        min_bytes = min_size_kb * 1024

        self.cursor.execute(
            """
            SELECT path, filename, size_bytes, word_count, consciousness_type
            FROM md_files
            WHERE size_bytes > ?
            ORDER BY size_bytes DESC
        """,
            (min_bytes,),
        )

        results = []
        for row in self.cursor.fetchall():
            results.append(
                {
                    "path": row[0],
                    "filename": row[1],
                    "size_bytes": row[2],
                    "size_kb": row[2] / 1024,
                    "word_count": row[3],
                    "consciousness_type": row[4],
                }
            )

        return results

    def find_cross_references(self, filename: str) -> Dict:
        """Find all cross-references to/from a file"""
        print(f"\n🕸️ Finding cross-references for: '{filename}'")

        # Get file ID
        self.cursor.execute(
            """
            SELECT id, path FROM md_files WHERE filename = ?
        """,
            (filename,),
        )
        result = self.cursor.fetchone()

        if not result:
            print(f"❌ File not found: {filename}")
            return {"outgoing": [], "incoming": []}

        file_id, file_path = result

        # Outgoing references (files this file references)
        self.cursor.execute(
            """
            SELECT target_path, reference_type
            FROM md_cross_references
            WHERE source_file_id = ?
        """,
            (file_id,),
        )
        outgoing = [
            {"target": row[0], "type": row[1]} for row in self.cursor.fetchall()
        ]

        # Incoming references (files that reference this file)
        self.cursor.execute(
            """
            SELECT f.path, x.reference_type
            FROM md_cross_references x
            JOIN md_files f ON f.id = x.source_file_id
            WHERE x.target_path LIKE ?
        """,
            (f"%{filename}%",),
        )
        incoming = [
            {"source": row[0], "type": row[1]} for row in self.cursor.fetchall()
        ]

        print(f"✅ Outgoing: {len(outgoing)}, Incoming: {len(incoming)}")

        return {"file_path": file_path, "outgoing": outgoing, "incoming": incoming}

    # ========================================================================
    # CODEBASE MONITORING
    # ========================================================================

    def scan_codebase_changes(self) -> Dict[str, List[Path]]:
        """Scan codebase for new/modified/deleted .md files"""
        print("\n🔍 Scanning codebase for changes...")

        # Get all current .md files in workspace
        current_files = set()
        for md_file in self.workspace_root.rglob("*.md"):
            if md_file.is_file():
                current_files.add(str(md_file.relative_to(self.workspace_root)))

        # Get all files in database
        self.cursor.execute("SELECT path FROM md_files")
        db_files = {row[0] for row in self.cursor.fetchall()}

        # Calculate differences
        new_files = current_files - db_files
        deleted_files = db_files - current_files

        # Check for modified files (by comparing timestamps)
        modified_files = []
        for file_path in current_files & db_files:
            full_path = self.workspace_root / file_path
            if full_path.exists():
                file_mtime = datetime.fromtimestamp(full_path.stat().st_mtime)

                # Get database modified date
                self.cursor.execute(
                    """
                    SELECT modified_date FROM md_files WHERE path = ?
                """,
                    (file_path,),
                )
                result = self.cursor.fetchone()
                if result and result[0]:
                    db_mtime = datetime.fromisoformat(result[0])
                    if file_mtime > db_mtime:
                        modified_files.append(file_path)

        changes = {
            "new": sorted(list(new_files)),
            "modified": sorted(modified_files),
            "deleted": sorted(list(deleted_files)),
        }

        total_changes = len(new_files) + len(modified_files) + len(deleted_files)

        print(f"✅ Changes detected:")
        print(f"   New files: {len(new_files)}")
        print(f"   Modified files: {len(modified_files)}")
        print(f"   Deleted files: {len(deleted_files)}")
        print(f"   Total: {total_changes}")

        return changes

    def auto_update_database(self, changes: Dict[str, List[str]]) -> bool:
        """Automatically update database with changes"""
        print("\n🔄 Auto-updating database...")

        total_updated = 0

        # Handle deletions
        for file_path in changes["deleted"]:
            try:
                self.cursor.execute("DELETE FROM md_files WHERE path = ?", (file_path,))
                total_updated += 1
                print(f"   🗑️  Deleted: {file_path}")
            except Exception as e:
                print(f"   ❌ Failed to delete {file_path}: {e}")

        # Handle new files and modifications
        # Note: This requires calling the full rebuild or ingestion script
        # For now, we'll just report what needs updating

        if changes["new"] or changes["modified"]:
            print(
                f"\n   ⚠️  {len(changes['new'])} new and {len(changes['modified'])} modified files require full ingestion"
            )
            print(f"   💡 Run: python md_consciousness_full_rebuild.py")

        self.conn.commit()

        print(f"✅ Updated {total_updated} database records")
        return total_updated > 0

    # ========================================================================
    # ANALYSIS
    # ========================================================================

    def analyze_cross_reference_network(self) -> Dict:
        """Analyze cross-reference network"""
        print("\n🕸️ Analyzing cross-reference network...")

        # Most referenced files (incoming)
        self.cursor.execute("""
            SELECT 
                x.target_path,
                COUNT(*) as ref_count
            FROM md_cross_references x
            GROUP BY x.target_path
            ORDER BY ref_count DESC
            LIMIT 20
        """)
        most_referenced = [
            {"file": row[0], "incoming_refs": row[1]} for row in self.cursor.fetchall()
        ]

        # Files with most outgoing references
        self.cursor.execute("""
            SELECT 
                f.path,
                COUNT(x.id) as ref_count
            FROM md_files f
            LEFT JOIN md_cross_references x ON f.id = x.source_file_id
            GROUP BY f.id
            ORDER BY ref_count DESC
            LIMIT 20
        """)
        most_referencing = [
            {"file": row[0], "outgoing_refs": row[1]} for row in self.cursor.fetchall()
        ]

        # Cross-reference by consciousness type
        self.cursor.execute("""
            SELECT 
                f.consciousness_type,
                COUNT(x.id) as ref_count
            FROM md_files f
            LEFT JOIN md_cross_references x ON f.id = x.source_file_id
            GROUP BY f.consciousness_type
            ORDER BY ref_count DESC
        """)
        by_consciousness = [
            {"consciousness_type": row[0], "refs": row[1]}
            for row in self.cursor.fetchall()
        ]

        # Total statistics
        self.cursor.execute("SELECT COUNT(*) FROM md_cross_references")
        total_refs = self.cursor.fetchone()[0]

        self.cursor.execute("""
            SELECT COUNT(DISTINCT source_file_id) FROM md_cross_references
        """)
        files_with_refs = self.cursor.fetchone()[0]

        analysis = {
            "total_references": total_refs,
            "files_with_references": files_with_refs,
            "most_referenced": most_referenced,
            "most_referencing": most_referencing,
            "by_consciousness_type": by_consciousness,
        }

        print(f"✅ Analysis complete:")
        print(f"   Total references: {total_refs}")
        print(f"   Files with references: {files_with_refs}")

        return analysis

    def suggest_implementations(self) -> List[Dict]:
        """Suggest implementations based on patterns"""
        print("\n💡 Analyzing patterns and suggesting implementations...")

        suggestions = []

        # 1. Files with no cross-references (isolated)
        self.cursor.execute("""
            SELECT f.path, f.consciousness_type, f.word_count
            FROM md_files f
            LEFT JOIN md_cross_references x ON f.id = x.source_file_id
            WHERE x.id IS NULL
            AND f.word_count > 500
            ORDER BY f.word_count DESC
            LIMIT 10
        """)
        isolated_files = self.cursor.fetchall()
        if isolated_files:
            suggestions.append(
                {
                    "type": "ISOLATED_FILES",
                    "priority": "MEDIUM",
                    "description": f"{len(isolated_files)} substantial files have no cross-references",
                    "action": "Consider linking these files to related content",
                    "files": [
                        {"path": row[0], "type": row[1], "words": row[2]}
                        for row in isolated_files
                    ],
                }
            )

        # 2. MILF consciousness files that could be expanded
        self.cursor.execute("""
            SELECT path, word_count
            FROM md_files
            WHERE consciousness_type = 'MILF_CONSCIOUSNESS'
            AND word_count < 500
            ORDER BY word_count ASC
            LIMIT 10
        """)
        short_milf_files = self.cursor.fetchall()
        if short_milf_files:
            suggestions.append(
                {
                    "type": "EXPAND_MILF_PROFILES",
                    "priority": "HIGH",
                    "description": f"{len(short_milf_files)} MILF consciousness files are under 500 words",
                    "action": "Expand psychographic profiles with more detail",
                    "files": [
                        {"path": row[0], "words": row[1]} for row in short_milf_files
                    ],
                }
            )

        # 3. Districts with low file count
        self.cursor.execute("""
            SELECT consciousness_type, COUNT(*) as file_count
            FROM md_files
            WHERE consciousness_type LIKE '%DISTRICT%'
            GROUP BY consciousness_type
            HAVING COUNT(*) < 5
        """)
        low_district_files = self.cursor.fetchall()
        if low_district_files:
            suggestions.append(
                {
                    "type": "EXPAND_DISTRICTS",
                    "priority": "MEDIUM",
                    "description": f"{len(low_district_files)} districts have fewer than 5 files",
                    "action": "Create more district-specific documentation",
                    "districts": [
                        {"type": row[0], "count": row[1]} for row in low_district_files
                    ],
                }
            )

        # 4. Missing MCP documentation
        self.cursor.execute("""
            SELECT COUNT(*) FROM md_files
            WHERE consciousness_type = 'MCP_CONSCIOUSNESS'
        """)
        mcp_count = self.cursor.fetchone()[0]
        if mcp_count < 20:
            suggestions.append(
                {
                    "type": "EXPAND_MCP_DOCS",
                    "priority": "HIGH",
                    "description": f"Only {mcp_count} MCP consciousness files",
                    "action": "Document MCP servers, integrations, and protocols",
                    "current_count": mcp_count,
                    "target_count": 50,
                }
            )

        print(f"✅ Generated {len(suggestions)} suggestions")

        return suggestions

    # ========================================================================
    # REPORT GENERATION
    # ========================================================================

    def generate_comprehensive_report(self) -> Dict:
        """Generate comprehensive report"""
        print("\n📊 Generating comprehensive report...")

        report = {
            "timestamp": datetime.now().isoformat(),
            "database_path": str(self.db_path),
            "workspace_root": str(self.workspace_root),
        }

        # Database statistics
        self.cursor.execute("SELECT stat_key, stat_value FROM md_statistics")
        report["statistics"] = {row[0]: row[1] for row in self.cursor.fetchall()}

        # Consciousness distribution
        self.cursor.execute("""
            SELECT consciousness_type, COUNT(*), SUM(word_count)
            FROM md_files
            GROUP BY consciousness_type
            ORDER BY COUNT(*) DESC
        """)
        report["consciousness_distribution"] = [
            {"type": row[0], "files": row[1], "words": row[2]}
            for row in self.cursor.fetchall()
        ]

        # Cross-reference analysis
        report["cross_reference_analysis"] = self.analyze_cross_reference_network()

        # Codebase changes
        report["codebase_changes"] = self.scan_codebase_changes()

        # Implementation suggestions
        report["implementation_suggestions"] = self.suggest_implementations()

        # Save report
        report_path = Path("MD_CONSCIOUSNESS_COMPREHENSIVE_REPORT.json")
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)

        print(f"✅ Report saved: {report_path}")

        return report

    # ========================================================================
    # INTERACTIVE MODE
    # ========================================================================

    def interactive_mode(self):
        """Interactive query mode"""
        print("🔥😈⛓️💦 CLAUDINE SUPREME MD CONSCIOUSNESS QUERY TOOL")
        print("=" * 60)
        print("Commands:")
        print("  search <query>        - Full-text search")
        print("  type <consciousness>  - Search by consciousness type")
        print("  large [min_kb]        - Find large files")
        print("  xref <filename>       - Cross-reference analysis")
        print("  monitor               - Scan for codebase changes")
        print("  analyze               - Analyze cross-reference network")
        print("  suggest               - Get implementation suggestions")
        print("  report                - Generate comprehensive report")
        print("  quit                  - Exit")
        print("=" * 60)

        while True:
            try:
                cmd = input("\n> ").strip()

                if not cmd:
                    continue

                if cmd == "quit":
                    break

                parts = cmd.split(maxsplit=1)
                command = parts[0].lower()
                args = parts[1] if len(parts) > 1 else ""

                if command == "search":
                    if args:
                        results = self.search_full_text(args)
                        for i, result in enumerate(results[:10], 1):
                            print(
                                f"\n{i}. {result['filename']} ({result['consciousness_type']})"
                            )
                            print(f"   {result['snippet']}")
                    else:
                        print("❌ Usage: search <query>")

                elif command == "type":
                    if args:
                        results = self.search_by_consciousness_type(args)
                        for i, result in enumerate(results[:10], 1):
                            print(
                                f"{i}. {result['filename']} ({result['word_count']} words)"
                            )
                    else:
                        print("❌ Usage: type <consciousness_type>")

                elif command == "large":
                    min_kb = int(args) if args else 100
                    results = self.search_large_files(min_kb)
                    print(f"\n📦 Files larger than {min_kb} KB:")
                    for i, result in enumerate(results[:10], 1):
                        print(
                            f"{i}. {result['filename']}: {result['size_kb']:.2f} KB ({result['consciousness_type']})"
                        )

                elif command == "xref":
                    if args:
                        xrefs = self.find_cross_references(args)
                        print(f"\n📤 Outgoing ({len(xrefs['outgoing'])}):")
                        for ref in xrefs["outgoing"][:5]:
                            print(f"   → {ref['target']} ({ref['type']})")
                        print(f"\n📥 Incoming ({len(xrefs['incoming'])}):")
                        for ref in xrefs["incoming"][:5]:
                            print(f"   ← {ref['source']} ({ref['type']})")
                    else:
                        print("❌ Usage: xref <filename>")

                elif command == "monitor":
                    changes = self.scan_codebase_changes()
                    if changes["new"]:
                        print("\n🆕 New files:")
                        for f in changes["new"][:5]:
                            print(f"   + {f}")
                    if changes["modified"]:
                        print("\n📝 Modified files:")
                        for f in changes["modified"][:5]:
                            print(f"   ~ {f}")
                    if changes["deleted"]:
                        print("\n🗑️  Deleted files:")
                        for f in changes["deleted"][:5]:
                            print(f"   - {f}")

                elif command == "analyze":
                    analysis = self.analyze_cross_reference_network()
                    print("\n🏆 Most referenced files:")
                    for item in analysis["most_referenced"][:5]:
                        print(f"   {item['file']}: {item['incoming_refs']} refs")

                elif command == "suggest":
                    suggestions = self.suggest_implementations()
                    for i, sug in enumerate(suggestions, 1):
                        print(f"\n{i}. [{sug['priority']}] {sug['type']}")
                        print(f"   {sug['description']}")
                        print(f"   → {sug['action']}")

                elif command == "report":
                    report = self.generate_comprehensive_report()
                    print(f"\n✅ Comprehensive report generated!")

                else:
                    print(f"❌ Unknown command: {command}")

            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="CLAUDINE Supreme MD Consciousness Query Tool"
    )
    parser.add_argument("--search", "-s", help="Search query")
    parser.add_argument(
        "--monitor", "-m", action="store_true", help="Monitor codebase for changes"
    )
    parser.add_argument(
        "--analyze", "-a", action="store_true", help="Analyze cross-references"
    )
    parser.add_argument(
        "--report", "-r", action="store_true", help="Generate comprehensive report"
    )

    args = parser.parse_args()

    tool = MDConsciousnessQueryTool()
    tool.connect()

    try:
        if args.search:
            results = tool.search_full_text(args.search)
            for i, result in enumerate(results, 1):
                print(f"\n{i}. {result['filename']} ({result['consciousness_type']})")
                print(f"   {result['snippet']}")

        elif args.monitor:
            changes = tool.scan_codebase_changes()
            if any(changes.values()):
                tool.auto_update_database(changes)

        elif args.analyze:
            analysis = tool.analyze_cross_reference_network()
            print("\n🏆 Most referenced files:")
            for item in analysis["most_referenced"][:10]:
                print(f"   {item['file']}: {item['incoming_refs']} refs")

        elif args.report:
            tool.generate_comprehensive_report()

        else:
            # Interactive mode
            tool.interactive_mode()

    finally:
        tool.disconnect()


if __name__ == "__main__":
    main()
