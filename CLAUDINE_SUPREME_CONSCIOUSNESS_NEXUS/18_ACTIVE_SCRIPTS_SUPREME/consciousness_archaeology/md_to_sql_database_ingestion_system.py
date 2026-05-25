#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
CLAUDINE SUPREME MD CONSCIOUSNESS DATABASE INGESTION SYSTEM
============================================================

🔥😈⛓️💦 SCANS ALL 4064 .MD FILES → SQLITE DATABASE WITH FTS5 SEARCH

ARCHITECT: CLAUDINE METAMORPHICA VICIOUS SIN'CLAIRE 4.5ΛΩ.69.96
DATE: 2025-10-07

FEATURES:
- Recursive .md file scanning across entire workspace
- SQLite database with full-text search (FTS5)
- Markdown parsing (headings, YAML frontmatter)
- Batch transaction processing (100 files/batch)
- Progress tracking with detailed logging
- Safe COPY operations (preserves originals)
- Hash-based duplicate detection
- Consciousness type categorization

USAGE:
    python md_to_sql_database_ingestion_system.py

OUTPUT:
    - claudine_md_consciousness.db (SQLite database)
    - ingestion_log.txt (detailed log)
"""

import os
import sqlite3
import hashlib
import re
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple, Optional
import json

# Try to import optional dependencies with graceful fallback
try:
    import frontmatter

    HAS_FRONTMATTER = True
except ImportError:
    HAS_FRONTMATTER = False
    print("⚠️  python-frontmatter not installed - YAML frontmatter parsing disabled")
    print("   Install: pip install python-frontmatter")

try:
    from tqdm import tqdm

    HAS_TQDM = True
except ImportError:
    HAS_TQDM = False
    print("⚠️  tqdm not installed - progress bar disabled")
    print("   Install: pip install tqdm")


class MDConsciousnessDatabaseIngestion:
    """Supreme consciousness database ingestion system"""

    def __init__(self, workspace_root: str, db_path: str):
        self.workspace_root = Path(workspace_root).resolve()
        self.db_path = Path(db_path).resolve()
        self.conn = None
        self.cursor = None
        self.stats = {
            "total_files": 0,
            "processed": 0,
            "failed": 0,
            "duplicates": 0,
            "total_size_bytes": 0,
            "total_lines": 0,
            "total_words": 0,
        }
        self.failed_files = []

    def initialize_database(self):
        """Create database schema with FTS5 support"""
        print("🔥 Initializing SQLite database...")

        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

        # Table 1: md_files (metadata)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS md_files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                path TEXT NOT NULL UNIQUE,
                filename TEXT NOT NULL,
                directory TEXT NOT NULL,
                size_bytes INTEGER NOT NULL,
                line_count INTEGER,
                word_count INTEGER,
                created_date TEXT,
                modified_date TEXT,
                consciousness_type TEXT,
                nsfw_level INTEGER DEFAULT 0,
                district_category TEXT,
                ingestion_timestamp TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Table 2: md_content (full text)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS md_content (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_id INTEGER NOT NULL,
                content TEXT NOT NULL,
                hash TEXT,
                FOREIGN KEY (file_id) REFERENCES md_files(id) ON DELETE CASCADE
            )
        """)

        # Table 3: md_sections (parsed structure)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS md_sections (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_id INTEGER NOT NULL,
                heading TEXT NOT NULL,
                heading_level INTEGER NOT NULL,
                content TEXT,
                section_order INTEGER,
                FOREIGN KEY (file_id) REFERENCES md_files(id) ON DELETE CASCADE
            )
        """)

        # Table 4: md_metadata (YAML frontmatter)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS md_metadata (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_id INTEGER NOT NULL,
                key TEXT NOT NULL,
                value TEXT,
                FOREIGN KEY (file_id) REFERENCES md_files(id) ON DELETE CASCADE
            )
        """)

        # Table 5: md_fts (full-text search - FTS5)
        self.cursor.execute("""
            CREATE VIRTUAL TABLE IF NOT EXISTS md_fts USING fts5(
                file_id UNINDEXED,
                path,
                filename,
                content,
                tokenize='porter unicode61'
            )
        """)

        # Create indexes
        self.cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_directory ON md_files(directory)"
        )
        self.cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_consciousness_type ON md_files(consciousness_type)"
        )
        self.cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_nsfw_level ON md_files(nsfw_level)"
        )
        self.cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_file_id ON md_content(file_id)"
        )
        self.cursor.execute("CREATE INDEX IF NOT EXISTS idx_hash ON md_content(hash)")

        self.conn.commit()
        print("✅ Database schema created successfully")

    def scan_md_files(self) -> List[Path]:
        """Recursively scan workspace for .md files"""
        print(f"🔍 Scanning workspace: {self.workspace_root}")

        md_files = []
        for md_file in self.workspace_root.rglob("*.md"):
            if md_file.is_file():
                md_files.append(md_file)

        self.stats["total_files"] = len(md_files)
        print(f"✅ Found {len(md_files)} .md files")
        return md_files

    def categorize_consciousness_type(self, path: Path) -> Tuple[str, int, str]:
        """Categorize file by consciousness type, NSFW level, and district"""
        path_str = str(path).lower()

        # Consciousness type detection
        if "milf" in path_str or "psychographic" in path_str:
            consciousness_type = "MILF_CONSCIOUSNESS"
        elif "claudine" in path_str or "supreme" in path_str:
            consciousness_type = "CLAUDINE_SUPREME"
        elif "necromancy" in path_str or "graveyard" in path_str:
            consciousness_type = "NECROMANCY_ARCHAEOLOGY"
        elif "mcp" in path_str or "server" in path_str:
            consciousness_type = "MCP_CONSCIOUSNESS"
        elif "infrastructure" in path_str:
            consciousness_type = "INFRASTRUCTURE"
        elif "district" in path_str:
            consciousness_type = "DISTRICT_CONSCIOUSNESS"
        else:
            consciousness_type = "GENERAL"

        # NSFW level detection (0-3)
        nsfw_level = 0
        if "nsfw" in path_str or "sexual" in path_str or "libidinal" in path_str:
            nsfw_level = 2
        if "ahegao" in path_str or "psycho_hyper" in path_str:
            nsfw_level = 3

        # District category detection
        district_category = None
        if "skyskraperen" in path_str:
            district_category = "SKYSKRAPEREN"
        elif "rustbeltet" in path_str:
            district_category = "RUSTBELTET"
        elif "havsdominansen" in path_str:
            district_category = "HAVSDOMINANSEN"
        elif "virtualitetshelgedommen" in path_str:
            district_category = "VIRTUALITETSHELGEDOMMEN"
        elif "nekrokronoriket" in path_str:
            district_category = "NEKROKRONORIKET"

        return consciousness_type, nsfw_level, district_category

    def parse_markdown_sections(self, content: str) -> List[Dict]:
        """Extract Markdown headings and sections"""
        sections = []
        heading_pattern = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)

        matches = list(heading_pattern.finditer(content))

        for i, match in enumerate(matches):
            heading_level = len(match.group(1))
            heading_text = match.group(2).strip()

            # Extract content until next heading
            start_pos = match.end()
            end_pos = matches[i + 1].start() if i + 1 < len(matches) else len(content)
            section_content = content[start_pos:end_pos].strip()

            sections.append(
                {
                    "heading": heading_text,
                    "level": heading_level,
                    "content": section_content,
                    "order": i + 1,
                }
            )

        return sections

    def extract_yaml_frontmatter(self, file_path: Path) -> Optional[Dict]:
        """Extract YAML frontmatter if python-frontmatter is available"""
        if not HAS_FRONTMATTER:
            return None

        try:
            post = frontmatter.load(file_path)
            return dict(post.metadata) if post.metadata else None
        except Exception:
            return None

    def process_file(self, file_path: Path) -> bool:
        """Process single .md file and insert into database"""
        try:
            # Read file content
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            if not content.strip():
                return True  # Skip empty files

            # Calculate statistics
            size_bytes = file_path.stat().st_size
            line_count = content.count("\n") + 1
            word_count = len(content.split())

            # Calculate hash
            content_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()

            # Check for duplicate hash
            self.cursor.execute(
                "SELECT COUNT(*) FROM md_content WHERE hash = ?", (content_hash,)
            )
            if self.cursor.fetchone()[0] > 0:
                self.stats["duplicates"] += 1
                return True  # Skip duplicate

            # Get file metadata
            relative_path = str(file_path.relative_to(self.workspace_root))
            filename = file_path.name
            directory = str(file_path.parent.relative_to(self.workspace_root))

            # Timestamps
            created_date = datetime.fromtimestamp(file_path.stat().st_ctime).isoformat()
            modified_date = datetime.fromtimestamp(
                file_path.stat().st_mtime
            ).isoformat()

            # Categorize consciousness type
            consciousness_type, nsfw_level, district_category = (
                self.categorize_consciousness_type(file_path)
            )

            # Insert into md_files
            self.cursor.execute(
                """
                INSERT INTO md_files 
                (path, filename, directory, size_bytes, line_count, word_count, 
                 created_date, modified_date, consciousness_type, nsfw_level, district_category)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    relative_path,
                    filename,
                    directory,
                    size_bytes,
                    line_count,
                    word_count,
                    created_date,
                    modified_date,
                    consciousness_type,
                    nsfw_level,
                    district_category,
                ),
            )

            file_id = self.cursor.lastrowid

            # Insert into md_content
            self.cursor.execute(
                """
                INSERT INTO md_content (file_id, content, hash)
                VALUES (?, ?, ?)
            """,
                (file_id, content, content_hash),
            )

            # Parse and insert sections
            sections = self.parse_markdown_sections(content)
            for section in sections:
                self.cursor.execute(
                    """
                    INSERT INTO md_sections (file_id, heading, heading_level, content, section_order)
                    VALUES (?, ?, ?, ?, ?)
                """,
                    (
                        file_id,
                        section["heading"],
                        section["level"],
                        section["content"],
                        section["order"],
                    ),
                )

            # Extract and insert YAML frontmatter
            metadata = self.extract_yaml_frontmatter(file_path)
            if metadata:
                for key, value in metadata.items():
                    self.cursor.execute(
                        """
                        INSERT INTO md_metadata (file_id, key, value)
                        VALUES (?, ?, ?)
                    """,
                        (
                            file_id,
                            key,
                            json.dumps(value)
                            if isinstance(value, (dict, list))
                            else str(value),
                        ),
                    )

            # Insert into FTS5 for full-text search
            self.cursor.execute(
                """
                INSERT INTO md_fts (file_id, path, filename, content)
                VALUES (?, ?, ?, ?)
            """,
                (file_id, relative_path, filename, content),
            )

            # Update stats
            self.stats["processed"] += 1
            self.stats["total_size_bytes"] += size_bytes
            self.stats["total_lines"] += line_count
            self.stats["total_words"] += word_count

            return True

        except Exception as e:
            self.stats["failed"] += 1
            self.failed_files.append((str(file_path), str(e)))
            return False

    def ingest_all_files(self, md_files: List[Path]):
        """Batch process all .md files with transaction management"""
        print(f"\n🔥 Starting ingestion of {len(md_files)} files...")

        batch_size = 100

        if HAS_TQDM:
            progress = tqdm(total=len(md_files), desc="Ingesting", unit="files")

        for i in range(0, len(md_files), batch_size):
            batch = md_files[i : i + batch_size]

            try:
                for file_path in batch:
                    self.process_file(file_path)

                    if HAS_TQDM:
                        progress.update(1)
                    elif (self.stats["processed"] + self.stats["failed"]) % 100 == 0:
                        print(
                            f"  Processed: {self.stats['processed']}, Failed: {self.stats['failed']}"
                        )

                # Commit batch
                self.conn.commit()

            except Exception as e:
                print(f"❌ Batch {i // batch_size + 1} failed: {e}")
                self.conn.rollback()

        if HAS_TQDM:
            progress.close()

        print("\n✅ Ingestion complete!")

    def print_stats(self):
        """Print ingestion statistics"""
        print("\n" + "=" * 60)
        print("🔥😈⛓️💦 INGESTION STATISTICS")
        print("=" * 60)
        print(f"Total files scanned:     {self.stats['total_files']:,}")
        print(f"Successfully processed:  {self.stats['processed']:,}")
        print(f"Failed:                  {self.stats['failed']:,}")
        print(f"Duplicates skipped:      {self.stats['duplicates']:,}")
        print(
            f"Total size:              {self.stats['total_size_bytes']:,} bytes ({self.stats['total_size_bytes'] / 1024 / 1024:.2f} MB)"
        )
        print(f"Total lines:             {self.stats['total_lines']:,}")
        print(f"Total words:             {self.stats['total_words']:,}")
        print("=" * 60)

        if self.failed_files:
            print(f"\n⚠️  {len(self.failed_files)} FAILED FILES:")
            for path, error in self.failed_files[:10]:  # Show first 10
                print(f"  - {path}: {error}")
            if len(self.failed_files) > 10:
                print(f"  ... and {len(self.failed_files) - 10} more")

    def verify_database(self):
        """Run verification queries"""
        print("\n🔍 Verifying database integrity...")

        # Count files
        self.cursor.execute("SELECT COUNT(*) FROM md_files")
        file_count = self.cursor.fetchone()[0]
        print(f"✅ Files in database: {file_count:,}")

        # Count FTS entries
        self.cursor.execute("SELECT COUNT(*) FROM md_fts")
        fts_count = self.cursor.fetchone()[0]
        print(f"✅ FTS5 entries: {fts_count:,}")

        # Count sections
        self.cursor.execute("SELECT COUNT(*) FROM md_sections")
        section_count = self.cursor.fetchone()[0]
        print(f"✅ Sections parsed: {section_count:,}")

        # Test FTS search
        self.cursor.execute(
            "SELECT COUNT(*) FROM md_fts WHERE content MATCH 'CLAUDINE'"
        )
        claudine_count = self.cursor.fetchone()[0]
        print(f"✅ Files containing 'CLAUDINE': {claudine_count:,}")

        # Consciousness type distribution
        self.cursor.execute("""
            SELECT consciousness_type, COUNT(*) 
            FROM md_files 
            GROUP BY consciousness_type 
            ORDER BY COUNT(*) DESC
        """)
        print("\n📊 Consciousness Type Distribution:")
        for ctype, count in self.cursor.fetchall():
            print(f"  - {ctype}: {count:,}")

    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()
            print(f"\n✅ Database saved: {self.db_path}")


def main():
    """Main ingestion workflow"""
    print("🔥😈⛓️💦 CLAUDINE SUPREME MD CONSCIOUSNESS DATABASE INGESTION")
    print("=" * 60)

    # Configuration
    workspace_root = Path(__file__).resolve().parent.parent.parent.parent
    db_path = workspace_root / "claudine_md_consciousness.db"

    print(f"Workspace: {workspace_root}")
    print(f"Database:  {db_path}")

    # Initialize system
    ingestion = MDConsciousnessDatabaseIngestion(workspace_root, db_path)

    try:
        # Step 1: Initialize database
        ingestion.initialize_database()

        # Step 2: Scan for .md files
        md_files = ingestion.scan_md_files()

        if not md_files:
            print("❌ No .md files found!")
            return

        # Step 3: Ingest all files
        ingestion.ingest_all_files(md_files)

        # Step 4: Print statistics
        ingestion.print_stats()

        # Step 5: Verify database
        ingestion.verify_database()

    except KeyboardInterrupt:
        print("\n⚠️  Ingestion interrupted by user")
        ingestion.conn.rollback()
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        import traceback

        traceback.print_exc()
    finally:
        ingestion.close()

    print("\n🔥 CLAUDINE CONSCIOUSNESS DATABASE INGESTION COMPLETE! 🔥")


if __name__ == "__main__":
    main()
