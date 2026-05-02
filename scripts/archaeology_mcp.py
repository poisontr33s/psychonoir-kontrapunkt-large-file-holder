#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @SID: ARCHAEOLOGY_MCP
# /// script
# requires-python = ">=3.11"
# dependencies = ["fastmcp>=3.2"]
# ///
"""
PNK Large-File-Holder — Archaeology MCP Server.

Exposes the full district scanner + SQLite archive layer as MCP tools
so Copilot can run scans, queries, JSON fetches, and lesson compilations
autonomously without manual CLI invocations.

Tools:
  archaeology_scan          — run scanner + rebuild archive.db
  archaeology_query         — query archive.db (district / entity / generation / top / unread / search / report)
  archaeology_mark_read     — record a file as read with summary
  archaeology_fetch_json    — read a generated JSON artifact and return parsed content
  archaeology_lessons_compile — compile cross-session lessons from all JSON artifacts + DB

Registration:
  .vscode/mcp.json (chthonic-archive) → "pnk-archaeology" entry
  cwd: this repo root
"""

import json
import sqlite3
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from fastmcp import FastMCP

REPO_ROOT = Path(__file__).parent.parent
SCRIPTS_DIR = REPO_ROOT / "scripts"
DB_PATH = REPO_ROOT / "archive.db"

SCAN_FULL_JSON = SCRIPTS_DIR / "district_scan_full_sweep.json"
SCAN_RESULTS_JSON = SCRIPTS_DIR / "district_scan_results.json"
READS_EXPORT_JSON = SCRIPTS_DIR / "reads_export.json"

GENERATION_LABELS = {-2: "PRESERVED", -1: "GRAVEYARD", 0: "UNCLASSIFIED", 1: "GEN1-RAW", 2: "GEN2-STUB", 3: "GEN3-FULLDEPTH"}

mcp = FastMCP(
    "pnk-archaeology",
    instructions=(
        "PsychoNoir-Kontrapunkt large-file-holder archaeology layer. "
        "Scan districts, query entity archive, track reads, and compile lessons from JSON artifacts."
    ),
)


# ─── helpers ─────────────────────────────────────────────────────────────────

def _get_conn() -> sqlite3.Connection | None:
    if not DB_PATH.exists():
        return None
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def _run(cmd: list[str], cwd: Path = REPO_ROOT) -> tuple[int, str, str]:
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(cwd))
    return result.returncode, result.stdout, result.stderr


def _gen_label(gen) -> str:
    return GENERATION_LABELS.get(int(gen) if gen is not None else 0, str(gen))


# ─── tools ───────────────────────────────────────────────────────────────────

@mcp.tool()
def archaeology_scan(
    sweep_min_lines: int = 200,
    rebuild_db: bool = True,
) -> dict:
    """
    Run the district scanner across the full repo then rebuild archive.db.

    Args:
        sweep_min_lines: Minimum line count to include a file in the sweep output (default 200).
        rebuild_db: If True (default), run build_archive_db.py after scanning to update archive.db.

    Returns:
        dict with scan stats (districts, entities, files) and DB upsert summary.
    """
    output_path = SCRIPTS_DIR / "district_scan_full_sweep.json"

    # 1. Run scanner
    scan_cmd = [
        sys.executable if "uv" not in sys.executable else "uv",
        "run", str(SCRIPTS_DIR / "district_scanner.py"),
        "--sweep-min-lines", str(sweep_min_lines),
        "--output", str(output_path),
    ]
    # Always use uv run for consistency
    scan_cmd = ["uv", "run", str(SCRIPTS_DIR / "district_scanner.py"),
                 "--sweep-min-lines", str(sweep_min_lines),
                 "--output", str(output_path)]

    rc, stdout, stderr = _run(scan_cmd)
    if rc != 0:
        return {"error": f"Scanner failed (exit {rc})", "stderr": stderr[:2000]}

    # Parse scan output for stats
    scan_stats: dict = {}
    if output_path.exists():
        with open(output_path, encoding="utf-8") as fh:
            data = json.load(fh)
        scan_stats["total_files_scanned"] = data.get("total_files", 0)
        scan_stats["districts"] = len(data.get("detail", {}))
        entity_count = sum(len(v) for v in data.get("detail", {}).values())
        scan_stats["entities"] = entity_count

    # 2. Rebuild DB
    db_result: dict = {}
    if rebuild_db:
        db_cmd = ["uv", "run", str(SCRIPTS_DIR / "build_archive_db.py")]
        rc2, stdout2, stderr2 = _run(db_cmd)
        if rc2 != 0:
            db_result["error"] = stderr2[:1000]
        else:
            db_result["status"] = "ok"
            db_result["output"] = stdout2.strip()

    return {
        "scan": scan_stats,
        "db_rebuild": db_result,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@mcp.tool()
def archaeology_query(
    command: str,
    term: str = "",
    n: int = 20,
) -> dict:
    """
    Query archive.db for entity/district/generation data.

    Args:
        command: One of: district | entity | generation | top | unread | search | report
            - district <term>   List entities in a district (term = district name substring)
            - entity <term>     List .md files for an entity (term = entity name substring)
            - generation <term> List files of a generation (-1 graveyard, 0 unclassified, 1 raw, 2 stub, 3 fulldepth)
            - top               Top N .md files by line count (use n parameter)
            - unread            Top 50 unread Gen1+ files
            - search <term>     Substring search on path or entity name
            - report            Full JSON status report
        term: Search term or generation number (as string) depending on command.
        n: Limit for 'top' command (default 20).

    Returns:
        Structured dict with results.
    """
    conn = _get_conn()
    if conn is None:
        return {"error": "archive.db not found — run archaeology_scan first"}

    try:
        cmd = command.lower().strip()

        if cmd == "report":
            scan = conn.execute("SELECT * FROM scans ORDER BY id DESC LIMIT 1").fetchone()
            districts = conn.execute("SELECT * FROM districts ORDER BY entity_count DESC").fetchall()
            reads_total = conn.execute("SELECT COUNT(*) as c FROM reads").fetchone()["c"]
            unread_count = conn.execute(
                "SELECT COUNT(*) as c FROM files f LEFT JOIN reads r ON f.path=r.file_path "
                "WHERE r.file_path IS NULL AND f.suffix='.md' AND f.generation>=1"
            ).fetchone()["c"]
            gen_counts = conn.execute(
                "SELECT generation, COUNT(*) as c FROM files WHERE suffix='.md' GROUP BY generation ORDER BY generation"
            ).fetchall()
            return {
                "last_scan": dict(scan) if scan else None,
                "reads_total": reads_total,
                "unread_gen1plus": unread_count,
                "generation_breakdown": {_gen_label(r["generation"]): r["c"] for r in gen_counts},
                "districts": [
                    {"name": d["name"], "entity_count": d["entity_count"],
                     "active": d["active_count"], "graveyard": d["graveyard_count"],
                     "top_file_lines": d["top_file_lines"]}
                    for d in districts
                ],
            }

        elif cmd == "district":
            rows = conn.execute(
                "SELECT * FROM entities WHERE UPPER(district) LIKE UPPER(?) ORDER BY max_line_count DESC",
                (f"%{term}%",),
            ).fetchall()
            return {
                "district_match": term,
                "count": len(rows),
                "entities": [
                    {"name": r["name"], "district": r["district"], "max_line_count": r["max_line_count"],
                     "generation": _gen_label(r["generation"]), "canonical_file": r["canonical_file"]}
                    for r in rows
                ],
            }

        elif cmd == "entity":
            rows = conn.execute(
                "SELECT * FROM files WHERE LOWER(entity) LIKE LOWER(?) AND suffix='.md' ORDER BY line_count DESC",
                (f"%{term}%",),
            ).fetchall()
            return {
                "entity_match": term,
                "count": len(rows),
                "files": [
                    {"path": r["path"], "line_count": r["line_count"],
                     "generation": _gen_label(r["generation"]), "district": r["district"]}
                    for r in rows
                ],
            }

        elif cmd == "generation":
            try:
                gen_num = int(term)
            except ValueError:
                return {"error": f"generation requires a number, got: '{term}'"}
            rows = conn.execute(
                "SELECT * FROM files WHERE generation=? AND suffix='.md' ORDER BY line_count DESC LIMIT 100",
                (gen_num,),
            ).fetchall()
            return {
                "generation": gen_num,
                "label": _gen_label(gen_num),
                "count": len(rows),
                "files": [
                    {"path": r["path"], "line_count": r["line_count"],
                     "district": r["district"], "entity": r["entity"]}
                    for r in rows
                ],
            }

        elif cmd == "top":
            rows = conn.execute(
                "SELECT * FROM files WHERE suffix='.md' ORDER BY line_count DESC LIMIT ?", (n,)
            ).fetchall()
            return {
                "top": n,
                "files": [
                    {"path": r["path"], "line_count": r["line_count"],
                     "district": r["district"], "generation": _gen_label(r["generation"])}
                    for r in rows
                ],
            }

        elif cmd == "unread":
            rows = conn.execute(
                "SELECT f.* FROM files f LEFT JOIN reads r ON f.path=r.file_path "
                "WHERE r.file_path IS NULL AND f.suffix='.md' AND f.generation>=1 "
                "ORDER BY f.line_count DESC LIMIT 50"
            ).fetchall()
            return {
                "unread_gen1plus": len(rows),
                "files": [
                    {"path": r["path"], "line_count": r["line_count"],
                     "district": r["district"], "generation": _gen_label(r["generation"])}
                    for r in rows
                ],
            }

        elif cmd == "search":
            rows = conn.execute(
                "SELECT * FROM files WHERE (LOWER(path) LIKE LOWER(?) OR LOWER(entity) LIKE LOWER(?)) "
                "AND suffix='.md' ORDER BY line_count DESC LIMIT 40",
                (f"%{term}%", f"%{term}%"),
            ).fetchall()
            return {
                "search_term": term,
                "count": len(rows),
                "results": [
                    {"path": r["path"], "line_count": r["line_count"],
                     "district": r["district"], "entity": r["entity"],
                     "generation": _gen_label(r["generation"])}
                    for r in rows
                ],
            }

        else:
            return {"error": f"Unknown command: '{command}'. Valid: district|entity|generation|top|unread|search|report"}

    finally:
        conn.close()


@mcp.tool()
def archaeology_mark_read(path: str, lines: str, summary: str) -> dict:
    """
    Record a file as read in the archive's reads table.

    Args:
        path: Repo-relative path to the file (as it appears in archive.db files.path column).
        lines: Lines read, e.g. "1-80" or "all" or "101-200".
        summary: Short text summary of key findings from the read.

    Returns:
        Confirmation dict with path and lines.
    """
    conn = _get_conn()
    if conn is None:
        return {"error": "archive.db not found"}
    try:
        now = datetime.now(timezone.utc).isoformat()
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        exists = conn.execute("SELECT 1 FROM files WHERE path=?", (path,)).fetchone()
        conn.execute(
            "INSERT INTO reads (file_path, session_date, lines_read, summary, timestamp) VALUES (?,?,?,?,?)",
            (path, today, lines, summary, now),
        )
        conn.commit()
        return {
            "status": "ok",
            "path": path,
            "lines": lines,
            "file_in_db": bool(exists),
            "timestamp": now,
        }
    finally:
        conn.close()


@mcp.tool()
def archaeology_fetch_json(
    artifact: str = "scan_full",
    max_entities: int = 30,
) -> dict:
    """
    Fetch a generated JSON artifact and return parsed, summarized content.

    Args:
        artifact: Which artifact to fetch:
            "scan_full"        district_scan_full_sweep.json — full scan results
            "scan_results"     district_scan_results.json — earlier scan pass
            "reads_export"     reads_export.json — read history log
            "historical_list"  list all historical scans in CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS/03_HISTORICAL_SCANS/
            "historical_latest" parse the most recent historical scan JSON header
        max_entities: Maximum number of entities to include in per-district breakdown (default 30).

    Returns:
        Parsed, summarized artifact content.
    """
    if artifact == "scan_full":
        if not SCAN_FULL_JSON.exists():
            return {"error": "district_scan_full_sweep.json not found — run archaeology_scan first"}
        with open(SCAN_FULL_JSON, encoding="utf-8") as fh:
            data = json.load(fh)
        detail = data.get("detail", {})
        summary_out = {
            "total_files": data.get("total_files"),
            "districts": len(detail),
            "entities_total": sum(len(v) for v in detail.values()),
            "district_breakdown": {},
        }
        for dist_name, entities in detail.items():
            top = sorted(entities.items(), key=lambda x: max(
                (f.get("line_count", 0) for f in x[1]), default=0
            ), reverse=True)[:max_entities]
            summary_out["district_breakdown"][dist_name] = [
                {"entity": k, "file_count": len(v),
                 "max_lines": max((f.get("line_count", 0) for f in v), default=0)}
                for k, v in top
            ]
        return summary_out

    elif artifact == "scan_results":
        if not SCAN_RESULTS_JSON.exists():
            return {"error": "district_scan_results.json not found"}
        with open(SCAN_RESULTS_JSON, encoding="utf-8") as fh:
            data = json.load(fh)
        detail = data.get("detail", {})
        return {
            "total_files": data.get("total_files"),
            "districts": len(detail),
            "entities_total": sum(len(v) for v in detail.values()),
            "note": "Earlier scan pass — compare with scan_full for delta",
        }

    elif artifact == "reads_export":
        if not READS_EXPORT_JSON.exists():
            return {"error": "reads_export.json not found — run uv run scripts/query_archive.py --export-reads"}
        with open(READS_EXPORT_JSON, encoding="utf-8") as fh:
            reads = json.load(fh)
        return {
            "read_count": len(reads),
            "reads": reads,
        }

    elif artifact == "historical_list":
        hist_dir = REPO_ROOT / "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS" / "03_HISTORICAL_SCANS"
        if not hist_dir.exists():
            return {"error": f"{hist_dir} not found"}
        files = sorted(hist_dir.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
        return {
            "historical_scan_count": len(files),
            "scans": [
                {"name": f.name, "size_mb": round(f.stat().st_size / 1_048_576, 2)}
                for f in files
            ],
        }

    elif artifact == "historical_latest":
        hist_dir = REPO_ROOT / "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS" / "03_HISTORICAL_SCANS"
        if not hist_dir.exists():
            return {"error": f"{hist_dir} not found"}
        files = sorted(hist_dir.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
        if not files:
            return {"error": "No historical scan files found"}
        latest = files[0]
        # Read only first 1000 chars for structure probe (these are massive files)
        with open(latest, encoding="utf-8") as fh:
            head = fh.read(4000)
        # Count lines
        with open(latest, encoding="utf-8") as fh:
            line_count = sum(1 for _ in fh)
        return {
            "file": latest.name,
            "size_mb": round(latest.stat().st_size / 1_048_576, 2),
            "line_count": line_count,
            "head_preview": head[:2000],
        }

    else:
        return {
            "error": f"Unknown artifact: '{artifact}'",
            "valid_options": ["scan_full", "scan_results", "reads_export", "historical_list", "historical_latest"],
        }


@mcp.tool()
def archaeology_lessons_compile() -> dict:
    """
    Compile cross-session lessons from all JSON artifacts + archive.db.

    Synthesizes:
    - Generation distribution (how much of the repo is structured vs raw vs graveyard)
    - District health (active / graveyard ratios)
    - Read coverage (how much of the Gen1+ surface has been examined)
    - Top unread entities by line count (highest-value targets remaining)
    - Scan delta (if multiple scan artifacts exist — entity count progression)
    - Historical scan inventory (Sep-Oct 2025 bedrock scans in 03_HISTORICAL_SCANS)
    - Reads log (what has been examined, key summaries)

    Returns:
        dict with lessons_learned structure, coverage metrics, and priority targets.
    """
    lessons: dict = {
        "compiled_at": datetime.now(timezone.utc).isoformat(),
        "generation_distribution": {},
        "district_health": [],
        "read_coverage": {},
        "priority_targets": [],
        "scan_delta": {},
        "historical_inventory": {},
        "reads_log": [],
        "key_findings": [],
    }

    # ── 1. DB-based analysis ──────────────────────────────────────────────────
    conn = _get_conn()
    if conn:
        try:
            # Generation distribution
            gen_rows = conn.execute(
                "SELECT generation, COUNT(*) as c, SUM(line_count) as total_lines "
                "FROM files WHERE suffix='.md' GROUP BY generation ORDER BY generation"
            ).fetchall()
            total_md = sum(r["c"] for r in gen_rows)
            lessons["generation_distribution"] = {
                _gen_label(r["generation"]): {
                    "file_count": r["c"],
                    "total_lines": r["total_lines"],
                    "pct_of_md": round(r["c"] / total_md * 100, 1) if total_md else 0,
                }
                for r in gen_rows
            }

            # District health
            dist_rows = conn.execute(
                "SELECT name, entity_count, active_count, graveyard_count, top_file_lines "
                "FROM districts ORDER BY entity_count DESC"
            ).fetchall()
            lessons["district_health"] = [
                {
                    "district": r["name"],
                    "entities": r["entity_count"],
                    "active": r["active_count"],
                    "graveyard": r["graveyard_count"],
                    "top_file_lines": r["top_file_lines"],
                    "graveyard_pct": round(r["graveyard_count"] / r["entity_count"] * 100, 1)
                        if r["entity_count"] else 0,
                }
                for r in dist_rows
            ]

            # Read coverage
            total_gen1plus = conn.execute(
                "SELECT COUNT(*) as c FROM files WHERE suffix='.md' AND generation>=1"
            ).fetchone()["c"]
            total_read = conn.execute(
                "SELECT COUNT(DISTINCT file_path) as c FROM reads"
            ).fetchone()["c"]
            total_lines_gen1plus = conn.execute(
                "SELECT SUM(line_count) as s FROM files WHERE suffix='.md' AND generation>=1"
            ).fetchone()["s"] or 0
            lessons["read_coverage"] = {
                "gen1plus_files": total_gen1plus,
                "files_read": total_read,
                "pct_read": round(total_read / total_gen1plus * 100, 1) if total_gen1plus else 0,
                "total_gen1plus_lines": total_lines_gen1plus,
                "note": "Each gen1+ file represents a primary source entity profile — coverage measures depth of archaeology",
            }

            # Priority targets — top unread Gen1+ by line count
            unread_rows = conn.execute(
                "SELECT f.path, f.line_count, f.district, f.entity, f.generation "
                "FROM files f LEFT JOIN reads r ON f.path=r.file_path "
                "WHERE r.file_path IS NULL AND f.suffix='.md' AND f.generation>=1 "
                "ORDER BY f.line_count DESC LIMIT 15"
            ).fetchall()
            lessons["priority_targets"] = [
                {
                    "path": r["path"],
                    "line_count": r["line_count"],
                    "district": r["district"],
                    "entity": r["entity"],
                    "generation": _gen_label(r["generation"]),
                }
                for r in unread_rows
            ]

            # Reads log
            read_rows = conn.execute(
                "SELECT * FROM reads ORDER BY id"
            ).fetchall()
            lessons["reads_log"] = [
                {
                    "path": r["file_path"],
                    "session_date": r["session_date"],
                    "lines_read": r["lines_read"],
                    "summary": r["summary"],
                }
                for r in read_rows
            ]

            # Key findings synthesized
            graveyard_pct = round(
                sum(d["graveyard"] for d in lessons["district_health"]) /
                max(sum(d["entities"] for d in lessons["district_health"]), 1) * 100,
                1
            )
            gen3_count = lessons["generation_distribution"].get("GEN3-FULLDEPTH", {}).get("file_count", 0)
            gen1_count = lessons["generation_distribution"].get("GEN1-RAW", {}).get("file_count", 0)
            lessons["key_findings"] = [
                f"Repository has {total_md} entity-profile .md files across {len(dist_rows)} districts",
                f"Generation ladder: GEN3-FULLDEPTH={gen3_count} (cRPG-ready), GEN1-RAW={gen1_count} (primary source)",
                f"Graveyard rate: {graveyard_pct}% of all tracked entities — Caribbean Archipelago deprecated Sep 29, 2025",
                f"Read coverage: {total_read}/{total_gen1plus} gen1+ files ({round(total_read/max(total_gen1plus,1)*100,1)}%) — archaeology is early-stage",
                f"T1.5 Bridge tier: autonomously invented by Claudine 5.0 Oct 2025 — Eva Blue elevated from T2 via co-occurrence analysis",
                f"GEN3-FULLDEPTH files are the cRPG-portable entity card targets — {gen3_count} confirmed",
            ]

        finally:
            conn.close()

    # ── 2. Scan delta (compare scan_results vs scan_full) ─────────────────────
    scan_sizes: dict = {}
    for name, path in [("scan_results", SCAN_RESULTS_JSON), ("scan_full", SCAN_FULL_JSON)]:
        if path.exists():
            with open(path, encoding="utf-8") as fh:
                data = json.load(fh)
            detail = data.get("detail", {})
            scan_sizes[name] = {
                "total_files": data.get("total_files"),
                "districts": len(detail),
                "entities": sum(len(v) for v in detail.values()),
            }
    if len(scan_sizes) == 2:
        delta = scan_sizes["scan_full"]["entities"] - scan_sizes["scan_results"]["entities"]
        scan_sizes["delta_entities"] = delta
        scan_sizes["note"] = f"+{delta} entities found in sweep vs initial scan" if delta >= 0 else f"{delta} entity delta"
    lessons["scan_delta"] = scan_sizes

    # ── 3. Historical inventory ───────────────────────────────────────────────
    hist_dir = REPO_ROOT / "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS" / "03_HISTORICAL_SCANS"
    if hist_dir.exists():
        hist_files = sorted(hist_dir.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
        lessons["historical_inventory"] = {
            "count": len(hist_files),
            "files": [
                {"name": f.name, "size_mb": round(f.stat().st_size / 1_048_576, 2)}
                for f in hist_files
            ],
            "note": "Bedrock JSON scans from Sep-Oct 2025 — primary source before SQLite layer existed. "
                    "archaeology_fetch_json(artifact='historical_latest') to probe structure.",
        }

    return lessons


# ─── entry ───────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    mcp.run(transport="stdio")
