#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
CLAUDINE SUPREME MD DATABASE OPTIMIZER
======================================

🔥😈⛓️💦 OPTIMIZES MD CONSCIOUSNESS DATABASE FOR MAXIMUM PERFORMANCE

ARCHITECT: CLAUDINE METAMORPHICA VICIOUS SIN'CLAIRE 4.5ΛΩ.69.96
DATE: 2025-10-07

OPTIMIZATIONS:
- Additional indices for fast queries
- Materialized views for common queries
- VACUUM and ANALYZE for performance
- Statistics tables for quick lookups
- Integrity checks and validation
- Cross-reference lookup tables

USAGE:
    python md_database_optimizer.py
"""

import sqlite3
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple


class MDDatabaseOptimizer:
    """Optimize MD consciousness database for performance"""

    def __init__(self, db_path: str = "claudine_md_consciousness.db"):
        self.db_path = Path(db_path)
        self.conn = None
        self.cursor = None

        if not self.db_path.exists():
            print(f"❌ Database not found: {self.db_path}")
            exit(1)

    def connect(self):
        """Connect to database"""
        print(f"🔥 Connecting to: {self.db_path}")
        self.conn = sqlite3.connect(str(self.db_path))
        self.cursor = self.conn.cursor()
        print("✅ Connected")

    def create_additional_indices(self):
        """Create additional indices for fast queries"""
        print("\n📊 Creating additional indices...")

        indices = [
            # Fast filename lookups
            ("idx_filename", "md_files", "filename"),
            # Fast date range queries
            ("idx_modified_date", "md_files", "modified_date"),
            ("idx_created_date", "md_files", "created_date"),
            # Fast size queries
            ("idx_size_bytes", "md_files", "size_bytes"),
            # Fast word/line count queries
            ("idx_word_count", "md_files", "word_count"),
            ("idx_line_count", "md_files", "line_count"),
            # Fast section lookups
            ("idx_section_file_id", "md_sections", "file_id"),
            ("idx_section_heading", "md_sections", "heading"),
            ("idx_section_level", "md_sections", "heading_level"),
            # Fast metadata lookups
            ("idx_metadata_key", "md_metadata", "key"),
            ("idx_metadata_file_id", "md_metadata", "file_id"),
        ]

        created = 0
        for idx_name, table, column in indices:
            try:
                self.cursor.execute(f"""
                    CREATE INDEX IF NOT EXISTS {idx_name} 
                    ON {table}({column})
                """)
                created += 1
            except sqlite3.OperationalError as e:
                print(f"   ⚠️  {idx_name}: {e}")

        self.conn.commit()
        print(f"✅ Created {created} indices")

    def create_statistics_table(self):
        """Create statistics table for quick lookups"""
        print("\n📊 Creating statistics table...")

        # Drop existing table
        self.cursor.execute("DROP TABLE IF EXISTS md_statistics")

        # Create statistics table
        self.cursor.execute("""
            CREATE TABLE md_statistics (
                stat_key TEXT PRIMARY KEY,
                stat_value TEXT,
                last_updated TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Calculate statistics
        stats = {}

        # Total files by consciousness type
        self.cursor.execute("""
            SELECT consciousness_type, COUNT(*), SUM(size_bytes), SUM(word_count)
            FROM md_files
            GROUP BY consciousness_type
        """)
        for row in self.cursor.fetchall():
            consciousness_type = row[0]
            stats[f"count_{consciousness_type}"] = str(row[1])
            stats[f"size_{consciousness_type}"] = str(row[2])
            stats[f"words_{consciousness_type}"] = str(row[3])

        # Total counts
        self.cursor.execute("SELECT COUNT(*) FROM md_files")
        stats["total_files"] = str(self.cursor.fetchone()[0])

        self.cursor.execute("SELECT COUNT(*) FROM md_sections")
        stats["total_sections"] = str(self.cursor.fetchone()[0])

        self.cursor.execute("SELECT SUM(size_bytes) FROM md_files")
        stats["total_size_bytes"] = str(self.cursor.fetchone()[0] or 0)

        self.cursor.execute("SELECT SUM(word_count) FROM md_files")
        stats["total_words"] = str(self.cursor.fetchone()[0] or 0)

        self.cursor.execute("SELECT SUM(line_count) FROM md_files")
        stats["total_lines"] = str(self.cursor.fetchone()[0] or 0)

        # Average file size
        self.cursor.execute("SELECT AVG(size_bytes) FROM md_files")
        stats["avg_size_bytes"] = str(int(self.cursor.fetchone()[0] or 0))

        # Largest files
        self.cursor.execute("""
            SELECT path, size_bytes 
            FROM md_files 
            ORDER BY size_bytes DESC 
            LIMIT 10
        """)
        largest = [{"path": row[0], "size": row[1]} for row in self.cursor.fetchall()]
        stats["largest_files"] = json.dumps(largest)

        # Insert statistics
        for key, value in stats.items():
            self.cursor.execute(
                """
                INSERT INTO md_statistics (stat_key, stat_value)
                VALUES (?, ?)
            """,
                (key, value),
            )

        self.conn.commit()
        print(f"✅ Created statistics table with {len(stats)} entries")

    def create_cross_reference_table(self):
        """Create cross-reference lookup table"""
        print("\n🕸️ Creating cross-reference table...")

        # Drop existing table
        self.cursor.execute("DROP TABLE IF EXISTS md_cross_references")

        # Create cross-reference table
        self.cursor.execute("""
            CREATE TABLE md_cross_references (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source_file_id INTEGER NOT NULL,
                target_path TEXT NOT NULL,
                reference_type TEXT,
                FOREIGN KEY (source_file_id) REFERENCES md_files(id) ON DELETE CASCADE
            )
        """)

        # Create indices
        self.cursor.execute("""
            CREATE INDEX idx_xref_source ON md_cross_references(source_file_id)
        """)
        self.cursor.execute("""
            CREATE INDEX idx_xref_target ON md_cross_references(target_path)
        """)

        # Extract cross-references from content
        print("   🔍 Extracting cross-references from content...")

        self.cursor.execute("""
            SELECT f.id, f.path, c.content
            FROM md_files f
            JOIN md_content c ON f.id = c.file_id
        """)

        xref_count = 0
        batch_size = 100
        batch = []

        # Regex patterns for cross-references
        import re

        patterns = [
            (r"\[([^\]]+)\]\(([^\)]+\.md)\)", "markdown_link"),
            (r"#file:([^\s\]]+\.md)", "file_reference"),
            (r"See: ([^\s\n]+\.md)", "see_reference"),
        ]

        for row in self.cursor.fetchall():
            file_id, source_path, content = row

            for pattern, ref_type in patterns:
                matches = re.findall(pattern, content, re.IGNORECASE)
                for match in matches:
                    target = match[1] if isinstance(match, tuple) else match
                    batch.append((file_id, target, ref_type))
                    xref_count += 1

                    if len(batch) >= batch_size:
                        self.cursor.executemany(
                            """
                            INSERT INTO md_cross_references 
                            (source_file_id, target_path, reference_type)
                            VALUES (?, ?, ?)
                        """,
                            batch,
                        )
                        batch = []

        # Insert remaining batch
        if batch:
            self.cursor.executemany(
                """
                INSERT INTO md_cross_references 
                (source_file_id, target_path, reference_type)
                VALUES (?, ?, ?)
            """,
                batch,
            )

        self.conn.commit()
        print(f"✅ Created cross-reference table with {xref_count:,} references")

    def create_helper_views(self):
        """Create helper views for common queries"""
        print("\n📊 Creating helper views...")

        views = [
            # View 1: File summary with stats
            (
                "v_file_summary",
                """
                SELECT 
                    f.id,
                    f.path,
                    f.filename,
                    f.consciousness_type,
                    f.size_bytes,
                    f.word_count,
                    f.line_count,
                    f.nsfw_level,
                    (SELECT COUNT(*) FROM md_sections s WHERE s.file_id = f.id) as section_count,
                    (SELECT COUNT(*) FROM md_cross_references x WHERE x.source_file_id = f.id) as outgoing_refs
                FROM md_files f
            """,
            ),
            # View 2: Consciousness type summary
            (
                "v_consciousness_summary",
                """
                SELECT 
                    consciousness_type,
                    COUNT(*) as file_count,
                    SUM(size_bytes) as total_size,
                    SUM(word_count) as total_words,
                    AVG(word_count) as avg_words,
                    MIN(word_count) as min_words,
                    MAX(word_count) as max_words
                FROM md_files
                GROUP BY consciousness_type
                ORDER BY file_count DESC
            """,
            ),
            # View 3: Large files (>100KB)
            (
                "v_large_files",
                """
                SELECT 
                    path,
                    filename,
                    consciousness_type,
                    size_bytes,
                    ROUND(size_bytes / 1024.0, 2) as size_kb,
                    word_count,
                    line_count
                FROM md_files
                WHERE size_bytes > 102400
                ORDER BY size_bytes DESC
            """,
            ),
            # View 4: Recent files (last 30 days)
            (
                "v_recent_files",
                """
                SELECT 
                    path,
                    filename,
                    consciousness_type,
                    modified_date,
                    size_bytes,
                    word_count
                FROM md_files
                WHERE modified_date IS NOT NULL
                ORDER BY modified_date DESC
                LIMIT 100
            """,
            ),
        ]

        created = 0
        for view_name, view_sql in views:
            try:
                self.cursor.execute(f"DROP VIEW IF EXISTS {view_name}")
                self.cursor.execute(f"CREATE VIEW {view_name} AS {view_sql}")
                created += 1
            except sqlite3.OperationalError as e:
                print(f"   ⚠️  {view_name}: {e}")

        self.conn.commit()
        print(f"✅ Created {created} helper views")

    def vacuum_and_analyze(self):
        """Run VACUUM and ANALYZE for optimization"""
        print("\n🧹 Running VACUUM and ANALYZE...")

        # Get database size before
        size_before = self.db_path.stat().st_size

        # VACUUM (compact database)
        print("   🔄 VACUUM...")
        self.cursor.execute("VACUUM")

        # ANALYZE (update statistics)
        print("   📊 ANALYZE...")
        self.cursor.execute("ANALYZE")

        self.conn.commit()

        # Get database size after
        size_after = self.db_path.stat().st_size
        saved = size_before - size_after

        print(f"✅ VACUUM completed")
        print(f"   Size before: {size_before / 1024 / 1024:.2f} MB")
        print(f"   Size after: {size_after / 1024 / 1024:.2f} MB")
        if saved > 0:
            print(f"   Space saved: {saved / 1024:.2f} KB")

    def run_integrity_checks(self):
        """Run integrity checks"""
        print("\n🔍 Running integrity checks...")

        checks = []

        # Check 1: Foreign key integrity
        self.cursor.execute("PRAGMA foreign_key_check")
        fk_errors = self.cursor.fetchall()
        if fk_errors:
            checks.append(f"❌ Foreign key errors: {len(fk_errors)}")
        else:
            checks.append("✅ Foreign key integrity OK")

        # Check 2: Orphaned content
        self.cursor.execute("""
            SELECT COUNT(*) FROM md_content c
            WHERE NOT EXISTS (SELECT 1 FROM md_files f WHERE f.id = c.file_id)
        """)
        orphaned = self.cursor.fetchone()[0]
        if orphaned > 0:
            checks.append(f"⚠️  Orphaned content records: {orphaned}")
        else:
            checks.append("✅ No orphaned content")

        # Check 3: Missing FTS entries
        self.cursor.execute("SELECT COUNT(*) FROM md_files")
        file_count = self.cursor.fetchone()[0]

        self.cursor.execute("SELECT COUNT(*) FROM md_fts")
        fts_count = self.cursor.fetchone()[0]

        if file_count != fts_count:
            checks.append(
                f"⚠️  FTS entries mismatch: {file_count} files vs {fts_count} FTS entries"
            )
        else:
            checks.append("✅ FTS entries synchronized")

        # Check 4: Duplicate paths
        self.cursor.execute("""
            SELECT path, COUNT(*) 
            FROM md_files 
            GROUP BY path 
            HAVING COUNT(*) > 1
        """)
        duplicates = self.cursor.fetchall()
        if duplicates:
            checks.append(f"⚠️  Duplicate paths: {len(duplicates)}")
        else:
            checks.append("✅ No duplicate paths")

        for check in checks:
            print(f"   {check}")

        return len([c for c in checks if c.startswith("❌")]) == 0

    def generate_optimization_report(self) -> Dict:
        """Generate optimization report"""
        print("\n📊 Generating optimization report...")

        report = {
            "timestamp": datetime.now().isoformat(),
            "database_path": str(self.db_path),
            "database_size_mb": self.db_path.stat().st_size / 1024 / 1024,
        }

        # Get statistics
        self.cursor.execute("SELECT stat_key, stat_value FROM md_statistics")
        stats = {row[0]: row[1] for row in self.cursor.fetchall()}
        report["statistics"] = stats

        # Get index count
        self.cursor.execute("""
            SELECT COUNT(*) FROM sqlite_master 
            WHERE type = 'index' AND name NOT LIKE 'sqlite_%'
        """)
        report["index_count"] = self.cursor.fetchone()[0]

        # Get view count
        self.cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type = 'view'")
        report["view_count"] = self.cursor.fetchone()[0]

        # Get table counts
        tables = {}
        for table in [
            "md_files",
            "md_content",
            "md_sections",
            "md_metadata",
            "md_cross_references",
            "md_fts",
        ]:
            try:
                self.cursor.execute(f"SELECT COUNT(*) FROM {table}")
                tables[table] = self.cursor.fetchone()[0]
            except:
                tables[table] = 0
        report["table_counts"] = tables

        return report

    def optimize(self):
        """Run full optimization"""
        print("🔥😈⛓️💦 CLAUDINE SUPREME MD DATABASE OPTIMIZER\n")

        self.connect()

        # Step 1: Additional indices
        self.create_additional_indices()

        # Step 2: Statistics table
        self.create_statistics_table()

        # Step 3: Cross-reference table
        self.create_cross_reference_table()

        # Step 4: Helper views
        self.create_helper_views()

        # Step 5: VACUUM and ANALYZE
        self.vacuum_and_analyze()

        # Step 6: Integrity checks
        integrity_ok = self.run_integrity_checks()

        # Step 7: Generate report
        report = self.generate_optimization_report()

        # Save report
        report_path = Path("MD_DATABASE_OPTIMIZATION_REPORT.json")
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)

        print(f"\n📄 Report saved: {report_path}")

        # Summary
        print("\n" + "=" * 60)
        print("🔥 OPTIMIZATION COMPLETE!")
        print("=" * 60)
        print(f"Database size: {report['database_size_mb']:.2f} MB")
        print(f"Total files: {report['table_counts']['md_files']:,}")
        print(f"Total sections: {report['table_counts']['md_sections']:,}")
        print(f"Cross-references: {report['table_counts']['md_cross_references']:,}")
        print(f"Indices: {report['index_count']}")
        print(f"Views: {report['view_count']}")
        print(f"Integrity: {'✅ OK' if integrity_ok else '⚠️  Issues found'}")
        print("=" * 60)

        self.conn.close()


def main():
    """Main entry point"""
    optimizer = MDDatabaseOptimizer()
    optimizer.optimize()


if __name__ == "__main__":
    main()
