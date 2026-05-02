#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @SID: QUERY_ARCHIVE
"""
Query archive.db — persistent entity/district/file exploration layer.

Usage:
  uv run scripts/query_archive.py --district HAVSDOMINANSEN
  uv run scripts/query_archive.py --entity captain_coral
  uv run scripts/query_archive.py --generation 3
  uv run scripts/query_archive.py --generation -1       # graveyard
  uv run scripts/query_archive.py --top 20
  uv run scripts/query_archive.py --unread
  uv run scripts/query_archive.py --search eva_blue
  uv run scripts/query_archive.py --report
  uv run scripts/query_archive.py --mark-read "path/to/file.md" --lines "1-80" --summary "..."
  uv run scripts/query_archive.py --export-reads        # export reads table as JSON
"""
import argparse
import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
DEFAULT_DB = REPO_ROOT / "archive.db"

GENERATION_LABELS = {
    -2: "PRESERVED",
    -1: "GRAVEYARD",
     0: "UNCLASSIFIED",
     1: "GEN1-RAW",
     2: "GEN2-STUB",
     3: "GEN3-FULLDEPTH",
}


def get_conn(db_path: Path) -> sqlite3.Connection:
    if not db_path.exists():
        print(
            f"ERROR: {db_path} not found.\n"
            "Run:  uv run scripts/build_archive_db.py",
            file=sys.stderr,
        )
        sys.exit(1)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def _gen_label(gen) -> str:
    return GENERATION_LABELS.get(int(gen) if gen is not None else 0, str(gen))


def _read_status(conn, path: str) -> str:
    row = conn.execute(
        "SELECT lines_read FROM reads WHERE file_path=? ORDER BY id DESC LIMIT 1",
        (path,),
    ).fetchone()
    return f"[READ:{row['lines_read']}]" if row else "[UNREAD]"


# ─── Commands ────────────────────────────────────────────────────────────────

def cmd_district(conn, name: str) -> None:
    rows = conn.execute(
        "SELECT * FROM entities WHERE UPPER(district)=UPPER(?) ORDER BY max_line_count DESC",
        (name,),
    ).fetchall()
    if not rows:
        rows = conn.execute(
            "SELECT * FROM entities WHERE UPPER(district) LIKE UPPER(?) ORDER BY max_line_count DESC",
            (f"%{name}%",),
        ).fetchall()
    if not rows:
        print(f"No entities for district: {name}")
        return

    district_name = rows[0]["district"]
    d_info = conn.execute("SELECT * FROM districts WHERE name=?", (district_name,)).fetchone()
    print(f"\n=== {district_name} ===")
    if d_info:
        print(f"  Entities: {d_info['entity_count']}  |  Active: {d_info['active_count']}  |  Graveyard: {d_info['graveyard_count']}")
    print()
    for r in rows:
        gen = _gen_label(r["generation"])
        read = _read_status(conn, r["canonical_file"] or "")
        print(
            f"  {r['name']:<55s}  {r['max_line_count']:5d} lines  {gen:<18s}  {read}"
        )
        if r["canonical_file"]:
            print(f"    └─ {r['canonical_file']}")


def cmd_entity(conn, name: str) -> None:
    rows = conn.execute(
        "SELECT * FROM files WHERE LOWER(entity) LIKE LOWER(?) AND suffix='.md' ORDER BY line_count DESC",
        (f"%{name}%",),
    ).fetchall()
    if not rows:
        print(f"No .md files for entity: {name}")
        return

    print(f"\n=== Entity: '{name}' — {len(rows)} .md files ===\n")
    for r in rows:
        gen = _gen_label(r["generation"])
        read = _read_status(conn, r["path"])
        print(
            f"  {r['line_count']:5d}  {gen:<18s}  {r['tier']:<12s}  {read}"
        )
        print(f"    └─ {r['path']}")


def cmd_generation(conn, gen: int) -> None:
    rows = conn.execute(
        "SELECT * FROM files WHERE generation=? AND suffix='.md' ORDER BY line_count DESC LIMIT 100",
        (gen,),
    ).fetchall()
    label = _gen_label(gen)
    print(f"\n=== Generation {gen} ({label}) — {len(rows)} .md files (top 100) ===\n")
    for r in rows:
        read = _read_status(conn, r["path"])
        print(
            f"  {r['line_count']:5d}  {r['district']:<30s}  {r['entity']:<40s}  {read}"
        )
        print(f"    └─ {r['path']}")


def cmd_top(conn, n: int) -> None:
    rows = conn.execute(
        "SELECT * FROM files WHERE suffix='.md' ORDER BY line_count DESC LIMIT ?",
        (n,),
    ).fetchall()
    print(f"\n=== Top {n} .md files by line count ===\n")
    for r in rows:
        gen = _gen_label(r["generation"])
        read = _read_status(conn, r["path"])
        print(
            f"  {r['line_count']:6d}  {r['district']:<30s}  {gen:<18s}  {read}"
        )
        print(f"    └─ {r['path']}")


def cmd_unread(conn) -> None:
    rows = conn.execute(
        """
        SELECT f.* FROM files f
        LEFT JOIN reads r ON f.path = r.file_path
        WHERE r.file_path IS NULL
          AND f.suffix = '.md'
          AND f.generation >= 1
        ORDER BY f.line_count DESC
        LIMIT 50
        """,
    ).fetchall()
    print(f"\n=== Top 50 unread Gen1+ .md files ===\n")
    for r in rows:
        gen = _gen_label(r["generation"])
        print(
            f"  {r['line_count']:5d}  {r['district']:<30s}  {gen:<15s}  {r['path']}"
        )


def cmd_search(conn, term: str) -> None:
    rows = conn.execute(
        """
        SELECT * FROM files
        WHERE (LOWER(path) LIKE LOWER(?) OR LOWER(entity) LIKE LOWER(?))
          AND suffix = '.md'
        ORDER BY line_count DESC
        LIMIT 40
        """,
        (f"%{term}%", f"%{term}%"),
    ).fetchall()
    print(f"\n=== Search: '{term}' — {len(rows)} results ===\n")
    for r in rows:
        gen = _gen_label(r["generation"])
        read = _read_status(conn, r["path"])
        print(
            f"  {r['line_count']:5d}  {r['district']:<30s}  {gen:<18s}  {read}"
        )
        print(f"    └─ {r['path']}")


def cmd_report(conn) -> None:
    scan = conn.execute("SELECT * FROM scans ORDER BY id DESC LIMIT 1").fetchone()
    districts = conn.execute("SELECT * FROM districts ORDER BY entity_count DESC").fetchall()
    reads_total = conn.execute("SELECT COUNT(*) as c FROM reads").fetchone()["c"]
    unread_gen1plus = conn.execute(
        """
        SELECT COUNT(*) as c FROM files f
        LEFT JOIN reads r ON f.path = r.file_path
        WHERE r.file_path IS NULL AND f.suffix='.md' AND f.generation >= 1
        """
    ).fetchone()["c"]
    gen_counts = conn.execute(
        "SELECT generation, COUNT(*) as c FROM files WHERE suffix='.md' GROUP BY generation ORDER BY generation"
    ).fetchall()

    report = {
        "last_scan": dict(scan) if scan else None,
        "reads_total": reads_total,
        "unread_gen1plus": unread_gen1plus,
        "generation_breakdown": {
            _gen_label(r["generation"]): r["c"] for r in gen_counts
        },
        "districts": [
            {
                "name": d["name"],
                "entity_count": d["entity_count"],
                "active": d["active_count"],
                "graveyard": d["graveyard_count"],
                "top_file_lines": d["top_file_lines"],
            }
            for d in districts
        ],
    }
    print(json.dumps(report, indent=2))


def cmd_mark_read(conn, path: str, lines: str | None, summary: str | None) -> None:
    now = datetime.now(timezone.utc).isoformat()
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    # Verify file exists in DB (warn if not, but insert anyway)
    exists = conn.execute("SELECT 1 FROM files WHERE path=?", (path,)).fetchone()
    if not exists:
        print(f"WARNING: '{path}' not found in files table — inserting read record anyway.")
    conn.execute(
        "INSERT INTO reads (file_path, session_date, lines_read, summary, timestamp) VALUES (?, ?, ?, ?, ?)",
        (path, today, lines or "unknown", summary or "", now),
    )
    conn.commit()
    print(f"✓ Marked read: {path}  [{lines or 'unknown'}]")


def cmd_export_reads(conn, db_path: Path) -> None:
    rows = conn.execute("SELECT * FROM reads ORDER BY id").fetchall()
    out = [dict(r) for r in rows]
    export_path = db_path.parent / "scripts" / "reads_export.json"
    with open(export_path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2)
    print(f"✓ Exported {len(out)} reads to {export_path}")


# ─── Main ────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Query archive.db")
    parser.add_argument("--db", default=str(DEFAULT_DB), help="SQLite DB path")
    parser.add_argument("--district", metavar="NAME", help="List entities in district")
    parser.add_argument("--entity", metavar="NAME", help="List .md files for entity")
    parser.add_argument(
        "--generation",
        type=int,
        metavar="N",
        help="Files of generation N (-2=preserved, -1=graveyard, 0=unclassified, 1=raw, 2=stub, 3=full)",
    )
    parser.add_argument("--top", type=int, metavar="N", help="Top N .md files by line count")
    parser.add_argument("--unread", action="store_true", help="Top 50 unread Gen1+ files")
    parser.add_argument("--search", metavar="TERM", help="Search by path or entity name substring")
    parser.add_argument("--report", action="store_true", help="Full JSON status report")
    parser.add_argument("--mark-read", metavar="PATH", help="Record a file as read")
    parser.add_argument("--lines", metavar="RANGE", help="Lines read (e.g. '1-80' or 'all')")
    parser.add_argument("--summary", metavar="TEXT", help="Short summary of what was found")
    parser.add_argument("--export-reads", action="store_true", help="Export reads table to scripts/reads_export.json")
    args = parser.parse_args()

    db_path = Path(args.db)
    conn = get_conn(db_path)

    try:
        if args.district:
            cmd_district(conn, args.district)
        elif args.entity:
            cmd_entity(conn, args.entity)
        elif args.generation is not None:
            cmd_generation(conn, args.generation)
        elif args.top:
            cmd_top(conn, args.top)
        elif args.unread:
            cmd_unread(conn)
        elif args.search:
            cmd_search(conn, args.search)
        elif args.report:
            cmd_report(conn)
        elif args.mark_read:
            cmd_mark_read(conn, args.mark_read, args.lines, args.summary)
        elif args.export_reads:
            cmd_export_reads(conn, db_path)
        else:
            parser.print_help()
    finally:
        conn.close()


if __name__ == "__main__":
    main()
