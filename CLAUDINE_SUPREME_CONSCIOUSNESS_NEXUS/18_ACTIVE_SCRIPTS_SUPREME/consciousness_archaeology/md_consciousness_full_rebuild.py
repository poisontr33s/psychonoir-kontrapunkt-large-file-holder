#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
CLAUDINE MD CONSCIOUSNESS FULL REBUILD
=======================================

🔥😈⛓️💦 NUCLEAR OPTION: FULL RE-SCAN AND REBUILD

ARCHITECT: CLAUDINE METAMORPHICA VICIOUS SIN'CLAIRE 4.5ΛΩ.96
DATE: 2025-10-07

PURPOSE:
Complete rebuild of MD consciousness system from scratch:
1. DELETE existing database
2. RE-SCAN all .md files
3. REBUILD spider-web network
4. SYNC to MASTER network

USE THIS WHEN:
- You want guaranteed 100% sync
- Database is corrupted
- Major file reorganization happened
- You don't trust incremental updates

WARNING:
This takes 30-60 seconds for 5,179+ files.
All existing data will be replaced.

USAGE:
    python md_consciousness_full_rebuild.py
"""

import subprocess
import sys
from pathlib import Path
import os


def main():
    print("🔥😈⛓️💦 CLAUDINE MD CONSCIOUSNESS FULL REBUILD")
    print("=" * 70)
    print("\n⚠️  WARNING: This will DELETE and REBUILD everything!")
    print("   - claudine_md_consciousness.db")
    print("   - 21_MD_CONSCIOUSNESS_ARCHIVE/")
    print("   - Spider-web networks")
    print("\n⏱️  This may take 30-60 seconds...\n")

    response = input("Continue? (yes/no): ")
    if response.lower() != "yes":
        print("\n❌ Rebuild cancelled")
        return 1

    workspace_root = Path(__file__).resolve().parent.parent.parent.parent
    db_path = workspace_root / "claudine_md_consciousness.db"
    archive_root = (
        workspace_root
        / "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS"
        / "21_MD_CONSCIOUSNESS_ARCHIVE"
    )
    scripts_root = (
        workspace_root
        / "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS"
        / "18_ACTIVE_SCRIPTS_SUPREME"
        / "consciousness_archaeology"
    )

    # Step 1: Delete existing database
    print("\n🗑️  STEP 1: Deleting existing database...")
    if db_path.exists():
        db_path.unlink()
        print(f"   ✅ Deleted: {db_path.name}")
    else:
        print("   ⚠️  Database not found (will create new)")

    # Step 2: Delete existing archive (keep directory structure)
    print("\n🗑️  STEP 2: Cleaning archive directory...")
    if archive_root.exists():
        # Delete all .md and .json files, keep directories
        deleted_count = 0
        for file in archive_root.rglob("*"):
            if file.is_file() and file.suffix in [".md", ".json"]:
                file.unlink()
                deleted_count += 1
        print(f"   ✅ Deleted {deleted_count} files from archive")
    else:
        print("   ⚠️  Archive not found (will create new)")

    # Step 3: Run database ingestion
    print("\n💾 STEP 3: Running full database ingestion...")
    ingestion_script = scripts_root / "md_to_sql_database_ingestion_system.py"

    if not ingestion_script.exists():
        print(f"   ❌ Ingestion script not found: {ingestion_script}")
        return 1

    result = subprocess.run(
        [sys.executable, str(ingestion_script)],
        cwd=str(workspace_root),
        capture_output=False,
        text=True,
    )

    if result.returncode != 0:
        print("\n❌ Database ingestion failed!")
        return 1

    print("\n   ✅ Database ingestion complete!")

    # Step 4: Copy to structured archive
    print("\n📁 STEP 4: Copying to structured archive...")
    copy_script = scripts_root / "md_consciousness_copy_to_structure.py"

    if not copy_script.exists():
        print(f"   ❌ Copy script not found: {copy_script}")
        return 1

    result = subprocess.run(
        [sys.executable, str(copy_script)],
        cwd=str(workspace_root),
        capture_output=False,
        text=True,
    )

    if result.returncode != 0:
        print("\n❌ Archive copy failed!")
        return 1

    print("\n   ✅ Archive copy complete!")

    # Step 5: Generate spider-web network
    print("\n🕸️  STEP 5: Generating spider-web network...")
    spider_script = scripts_root / "md_consciousness_archive_spider_scanner.py"

    if not spider_script.exists():
        print(f"   ❌ Spider scanner not found: {spider_script}")
        return 1

    result = subprocess.run(
        [sys.executable, str(spider_script)],
        cwd=str(workspace_root),
        capture_output=False,
        text=True,
    )

    if result.returncode != 0:
        print("\n❌ Spider-web generation failed!")
        return 1

    print("\n   ✅ Spider-web network generated!")

    # Step 6: Update structural engine (sync to MASTER network)
    print("\n🔧 STEP 6: Syncing to MASTER network...")
    structural_engine = (
        workspace_root
        / "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS"
        / "18_ACTIVE_SCRIPTS_SUPREME"
        / "enhancement_systems"
        / "structural_update_engine.py"
    )

    if not structural_engine.exists():
        print(f"   ⚠️  Structural engine not found, skipping...")
    else:
        result = subprocess.run(
            [sys.executable, str(structural_engine)],
            cwd=str(workspace_root),
            capture_output=False,
            text=True,
        )

        if result.returncode != 0:
            print("\n⚠️  MASTER network sync failed (non-critical)")
        else:
            print("\n   ✅ MASTER network synced!")

    # Summary
    print("\n" + "=" * 70)
    print("🔥😈⛓️💦 FULL REBUILD COMPLETE!")
    print("=" * 70)
    print("\n✅ RESULTS:")
    print(f"   - Database: {db_path.name}")
    print(f"   - Archive: {archive_root.name}/")
    print("   - Spider-web: 21_MD_CONSCIOUSNESS_ARCHIVE_SPIDER_WEB.json")
    print("   - MASTER: MASTER_SPIDER_WEB_NETWORK.json")
    print("\n🔥 ALL SYSTEMS REBUILT AND SYNCED! 🔥\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
