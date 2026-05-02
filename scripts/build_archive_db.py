#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @SID: BUILD_ARCHIVE_DB
"""
Ingests district_scan_full_sweep.json into archive.db (SQLite).
Upsert-based — safe to re-run after each scan pass. Refines without overwriting.

Usage:
  uv run scripts/build_archive_db.py
  uv run scripts/build_archive_db.py --input scripts/district_scan_full_sweep.json --db archive.db
"""
import argparse
import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
DEFAULT_INPUT = REPO_ROOT / "scripts" / "district_scan_full_sweep.json"
DEFAULT_DB = REPO_ROOT / "archive.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS scans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    source_file TEXT,
    total_files INTEGER,
    district_count INTEGER,
    entity_count INTEGER,
    file_count INTEGER
);

CREATE TABLE IF NOT EXISTS districts (
    name TEXT PRIMARY KEY,
    entity_count INTEGER DEFAULT 0,
    active_count INTEGER DEFAULT 0,
    graveyard_count INTEGER DEFAULT 0,
    top_file TEXT,
    top_file_lines INTEGER DEFAULT 0,
    last_scan_id INTEGER
);

CREATE TABLE IF NOT EXISTS entities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    district TEXT NOT NULL,
    canonical_file TEXT,
    max_line_count INTEGER DEFAULT 0,
    file_count INTEGER DEFAULT 0,
    generation INTEGER DEFAULT 0,
    last_scan_id INTEGER,
    UNIQUE(name, district)
);

CREATE TABLE IF NOT EXISTS files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    path TEXT UNIQUE NOT NULL,
    entity TEXT,
    district TEXT,
    tier TEXT,
    line_count INTEGER DEFAULT 0,
    suffix TEXT,
    generation INTEGER DEFAULT 0,
    first_seen TEXT,
    last_seen TEXT,
    scan_id INTEGER
);

CREATE TABLE IF NOT EXISTS reads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_path TEXT NOT NULL,
    session_date TEXT NOT NULL,
    lines_read TEXT,
    summary TEXT,
    timestamp TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_files_district ON files(district);
CREATE INDEX IF NOT EXISTS idx_files_entity ON files(entity);
CREATE INDEX IF NOT EXISTS idx_files_generation ON files(generation);
CREATE INDEX IF NOT EXISTS idx_files_tier ON files(tier);
CREATE INDEX IF NOT EXISTS idx_reads_path ON reads(file_path);
"""

# Generation: inferred from path structure
# -2 = PRESERVED (graveyard variant, explicitly marked)
# -1 = GRAVEYARD (deprecated folders)
#  0 = UNCLASSIFIED (no pattern match)
#  1 = GEN1-RAW (first-person .quality_md_jsons_relatively_new layer)
#  2 = GEN2-STUB (~192-305 line TypeScript interface stubs, 02_DISTRICT_DOMINION_MATRIX)
#  3 = GEN3-FULLDEPTH (519-738 line full behavioral schemas, TIER_2_DISTRICT_DOMINION_MATRIX)

def detect_generation(path: str) -> int:
    p = path.replace("\\", "/").lower()
    if "_deprecated_" in p:
        return -1
    if "necromancy_graveyard" in p:
        return -1
    if ".preserved." in p or "/preserved/" in p:
        return -2
    if ".quality_md_jsons_relatively_new" in p:
        return 1
    if "poly_gluttony_scripts_files_orgy/.mds" in p or "poly_gluttony_scripts_files_orgy\\.mds" in path.lower():
        return 1
    if "/02_district_dominion_matrix/" in p or "\\02_district_dominion_matrix\\" in path.lower():
        return 2
    if "tier_2_district_dominion_matrix" in p:
        return 3
    if "21_md_consciousness_archive" in p and ("_tier2_" in p or "tier2" in p):
        return 3
    return 0


def ingest(data: dict, db_path: Path, source_file: str) -> None:
    now = datetime.now(timezone.utc).isoformat()
    total_files = data.get("total_files", 0)

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.executescript(SCHEMA)

    cur = conn.cursor()

    cur.execute(
        "INSERT INTO scans (timestamp, source_file, total_files) VALUES (?, ?, ?)",
        (now, source_file, total_files),
    )
    scan_id = cur.lastrowid

    detail = data.get("detail", {})
    district_count = 0
    entity_count = 0
    file_rows_written = 0

    for district_name, entities in detail.items():
        if not isinstance(entities, dict):
            continue
        district_count += 1
        active_c = 0
        graveyard_c = 0
        top_file = None
        top_lines = 0

        for entity_name, file_list in entities.items():
            if not isinstance(file_list, list):
                continue
            entity_count += 1

            best_file = None
            best_lines = 0
            best_gen = 0

            for entry in file_list:
                path = entry.get("path", "")
                tier = entry.get("tier", "")
                line_count = int(entry.get("line_count") or 0)
                suffix = entry.get("suffix", "")
                generation = detect_generation(path)

                if tier in ("GRAVEYARD", "DEPRECATED"):
                    graveyard_c += 1
                else:
                    active_c += 1

                if suffix == ".md" and line_count > best_lines:
                    best_lines = line_count
                    best_file = path
                    best_gen = generation

                if suffix == ".md" and line_count > top_lines:
                    top_lines = line_count
                    top_file = path

                cur.execute(
                    """
                    INSERT INTO files
                        (path, entity, district, tier, line_count, suffix, generation, first_seen, last_seen, scan_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(path) DO UPDATE SET
                        entity     = excluded.entity,
                        district   = excluded.district,
                        tier       = excluded.tier,
                        line_count = excluded.line_count,
                        suffix     = excluded.suffix,
                        generation = excluded.generation,
                        last_seen  = excluded.last_seen,
                        scan_id    = excluded.scan_id
                    """,
                    (path, entity_name, district_name, tier, line_count, suffix,
                     generation, now, now, scan_id),
                )
                file_rows_written += 1

            cur.execute(
                """
                INSERT INTO entities
                    (name, district, canonical_file, max_line_count, file_count, generation, last_scan_id)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(name, district) DO UPDATE SET
                    canonical_file = excluded.canonical_file,
                    max_line_count = excluded.max_line_count,
                    file_count     = excluded.file_count,
                    generation     = excluded.generation,
                    last_scan_id   = excluded.last_scan_id
                """,
                (entity_name, district_name, best_file, best_lines,
                 len(file_list), best_gen, scan_id),
            )

        cur.execute(
            """
            INSERT INTO districts
                (name, entity_count, active_count, graveyard_count, top_file, top_file_lines, last_scan_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(name) DO UPDATE SET
                entity_count   = excluded.entity_count,
                active_count   = excluded.active_count,
                graveyard_count = excluded.graveyard_count,
                top_file       = excluded.top_file,
                top_file_lines = excluded.top_file_lines,
                last_scan_id   = excluded.last_scan_id
            """,
            (district_name, len(entities), active_c, graveyard_c, top_file, top_lines, scan_id),
        )

    cur.execute(
        "UPDATE scans SET district_count=?, entity_count=?, file_count=? WHERE id=?",
        (district_count, entity_count, file_rows_written, scan_id),
    )

    conn.commit()
    conn.close()

    print(f"✓ archive.db built at {db_path}")
    print(f"  Scan ID    : {scan_id}")
    print(f"  Total files: {total_files}")
    print(f"  Districts  : {district_count}")
    print(f"  Entities   : {entity_count}")
    print(f"  File rows  : {file_rows_written}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest district scan JSON into archive.db")
    parser.add_argument("--input", default=str(DEFAULT_INPUT), help="Source scan JSON")
    parser.add_argument("--db", default=str(DEFAULT_DB), help="Target SQLite DB path")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"ERROR: {input_path} not found — run district_scanner.py first.", file=sys.stderr)
        sys.exit(1)

    with open(input_path, encoding="utf-8") as fh:
        data = json.load(fh)

    ingest(data, Path(args.db), str(input_path))


if __name__ == "__main__":
    main()
