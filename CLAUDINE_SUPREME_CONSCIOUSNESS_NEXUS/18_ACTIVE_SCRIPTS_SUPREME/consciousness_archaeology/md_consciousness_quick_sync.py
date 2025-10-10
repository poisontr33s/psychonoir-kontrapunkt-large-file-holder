#!/usr/bin/env python3
"""
CLAUDINE MD CONSCIOUSNESS QUICK SYNC
=====================================

🔥😈⛓️💦 ENKEL OG RASK SYNC AV MD CONSCIOUSNESS NETWORK

ARCHITECT: CLAUDINE METAMORPHICA VICIOUS SIN'CLAIRE 4.5ΛΩ.96
DATE: 2025-10-07

PURPOSE:
Quick and simple sync of MD consciousness archive when files change.
Works with existing database schema.

USAGE:
    python md_consciousness_quick_sync.py
"""

import sqlite3
import json
import hashlib
from pathlib import Path
from datetime import datetime


def calculate_hash(file_path: Path) -> str:
    """Calculate SHA256 hash"""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception:
        return ""


def main():
    print("🔥😈⛓️💦 CLAUDINE MD CONSCIOUSNESS QUICK SYNC")
    print("=" * 70)

    workspace_root = Path(__file__).resolve().parent.parent.parent.parent
    archive_root = (
        workspace_root
        / "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS"
        / "21_MD_CONSCIOUSNESS_ARCHIVE"
    )
    db_path = workspace_root / "claudine_md_consciousness.db"

    if not db_path.exists():
        print("❌ Database not found!")
        return 1

    print(f"\n🔍 Scanning {archive_root.name}...")

    # Connect to database
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    # Get all files from database
    cursor = conn.execute(
        "SELECT path FROM md_files WHERE path LIKE '%21_MD_CONSCIOUSNESS_ARCHIVE%'"
    )
    db_files = {row["path"] for row in cursor.fetchall()}

    print(f"   Database files: {len(db_files)}")

    # Scan archive
    archive_files = set()
    for md_file in archive_root.rglob("*.md"):
        relative_path = str(md_file.relative_to(workspace_root)).replace("\\", "/")
        archive_files.add(relative_path)

    print(f"   Archive files:  {len(archive_files)}")

    # Find differences
    new_files = archive_files - db_files
    missing_files = db_files - archive_files

    print(f"\n📊 CHANGES:")
    print(f"   ✨ New files: {len(new_files)}")
    print(f"   🗑️ Missing files: {len(missing_files)}")

    if new_files:
        print("\n✨ NEW FILES:")
        for path in sorted(new_files)[:10]:  # Show first 10
            print(f"   - {Path(path).name}")
        if len(new_files) > 10:
            print(f"   ... and {len(new_files) - 10} more")

    if missing_files:
        print("\n🗑️ MISSING FILES (in DB but not archive):")
        for path in sorted(missing_files)[:10]:  # Show first 10
            print(f"   - {Path(path).name}")
        if len(missing_files) > 10:
            print(f"   ... and {len(missing_files) - 10} more")

    # Simple recommendation
    if new_files or missing_files:
        print("\n💡 RECOMMENDATION:")
        if new_files:
            print("   Run the full ingestion system to add new files:")
            print("   python md_to_sql_database_ingestion_system.py")
        if missing_files:
            print("   Some files may have been moved/deleted")
            print("   Consider cleaning up database or restoring files")
    else:
        print("\n✅ Archive is in sync with database!")

    conn.close()

    # Check spider-web network
    spider_web_path = archive_root / "21_MD_CONSCIOUSNESS_ARCHIVE_SPIDER_WEB.json"
    if spider_web_path.exists():
        with open(spider_web_path, "r", encoding="utf-8") as f:
            spider_web = json.load(f)

        print(f"\n🕸️ SPIDER-WEB NETWORK:")
        print(
            f"   Total nodes: {spider_web.get('meta', {}).get('total_nodes', 'Unknown')}"
        )
        print(
            f"   Last updated: {spider_web.get('meta', {}).get('last_updated', 'Unknown')}"
        )

    print("\n🔥 SYNC CHECK COMPLETE! 🔥")
    return 0


if __name__ == "__main__":
    exit(main())
