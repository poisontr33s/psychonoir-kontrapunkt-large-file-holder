#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# @SID: PNK_OVERNIGHT_ARCHAEOLOGY
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Overnight archaeology extraction pass for psychonoir-kontrapunkt-large-file-holder.
Runs without agent interaction. Reads GEN3-FULLDEPTH + top GEN1-RAW files,
writes structured digests to ../chthonic-archive/manifest/ for morning cold-start.

Usage:
    uv run scripts/overnight_archaeology.py
    uv run scripts/overnight_archaeology.py --preview-lines 200 --gen1-count 12
"""

import argparse
import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DB_PATH = ROOT / "archive.db"
OUT_ROOT = ROOT.parent / "chthonic-archive" / "manifest"

# fallback: write to local scripts/ if chthonic-archive not found
if not OUT_ROOT.exists():
    OUT_ROOT = ROOT / "scripts"


def fetch_gen3_files(db: sqlite3.Connection) -> list[dict]:
    """Return canonical (non-duplicate) GEN3-FULLDEPTH file rows."""
    rows = db.execute(
        """
        SELECT entity, district, path, line_count, generation
        FROM files
        WHERE generation = 3 AND suffix = '.md'
        ORDER BY line_count DESC
        """
    ).fetchall()
    # deduplicate by entity name (keep highest line_count as canonical)
    seen: dict[str, dict] = {}
    for name, district, path, lines, gen in rows:
        if name not in seen or lines > seen[name]["line_count"]:
            seen[name] = {
                "entity": name,
                "district": district,
                "path": path,
                "line_count": lines,
                "generation": gen,
            }
    return sorted(seen.values(), key=lambda x: x["line_count"], reverse=True)


def fetch_gen1_top(db: sqlite3.Connection, n: int = 12) -> list[dict]:
    """Return top N GEN1-RAW files by line count (unread preferred)."""
    rows = db.execute(
        """
        SELECT f.entity, f.district, f.path, f.line_count,
               COALESCE(r.summary, '') as read_summary
        FROM files f
        LEFT JOIN reads r ON r.file_path = f.path
        WHERE f.generation = 1 AND f.suffix = '.md'
        ORDER BY (r.id IS NULL) DESC, f.line_count DESC
        LIMIT ?
        """,
        (n,),
    ).fetchall()
    seen: dict[str, dict] = {}
    for name, district, path, lines, summary in rows:
        if name not in seen:
            seen[name] = {
                "entity": name,
                "district": district,
                "path": path,
                "line_count": lines,
                "already_read": bool(summary),
            }
    return sorted(seen.values(), key=lambda x: x["line_count"], reverse=True)


def read_head(repo_root: Path, rel_path: str, n_lines: int) -> str:
    """Read first n_lines from a file relative to repo_root. Return text or error."""
    try:
        full = repo_root / rel_path
        if not full.exists():
            return f"[FILE NOT FOUND: {full}]"
        lines = []
        with full.open(encoding="utf-8", errors="replace") as fh:
            for i, line in enumerate(fh):
                if i >= n_lines:
                    break
                lines.append(line)
        return "".join(lines)
    except Exception as exc:
        return f"[READ ERROR: {exc}]"


def run(preview_lines: int = 150, gen1_count: int = 10) -> None:
    if not DB_PATH.exists():
        print(f"[ERROR] archive.db not found at {DB_PATH}", file=sys.stderr)
        sys.exit(1)

    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(str(DB_PATH))
    now = datetime.now(timezone.utc).isoformat()

    # ── GEN3 cards ──────────────────────────────────────────────────────────
    gen3_rows = fetch_gen3_files(db)
    gen3_cards = []
    for row in gen3_rows:
        head = read_head(ROOT, row["path"], preview_lines)
        gen3_cards.append({
            **row,
            "preview_lines": preview_lines,
            "head": head,
        })
        print(f"  GEN3 ✓  {row['entity']} ({row['line_count']} lines)")

    gen3_out = OUT_ROOT / "overnight_gen3_cards.json"
    gen3_out.write_text(
        json.dumps({"generated": now, "cards": gen3_cards}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"\n→ GEN3 digest: {gen3_out} ({len(gen3_cards)} entities)")

    # ── GEN1 previews ────────────────────────────────────────────────────────
    gen1_rows = fetch_gen1_top(db, gen1_count)
    gen1_previews = []
    for row in gen1_rows:
        head = read_head(ROOT, row["path"], 80)
        gen1_previews.append({
            **row,
            "preview_lines": 80,
            "head": head,
        })
        print(f"  GEN1 ✓  {row['entity']} ({row['line_count']} lines)")

    gen1_out = OUT_ROOT / "overnight_gen1_previews.json"
    gen1_out.write_text(
        json.dumps({"generated": now, "previews": gen1_previews}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"\n→ GEN1 previews: {gen1_out} ({len(gen1_previews)} entities)")

    # ── district report ──────────────────────────────────────────────────────
    district_rows = db.execute(
        """
        SELECT name, entity_count, active_count, graveyard_count, top_file_lines
        FROM districts ORDER BY entity_count DESC
        """
    ).fetchall()

    # ── summary markdown ─────────────────────────────────────────────────────
    gen_breakdown = {
        label: db.execute(
            "SELECT COUNT(*) FROM files WHERE generation=?", (code,)
        ).fetchone()[0]
        for code, label in [(-2, "PRESERVED"), (-1, "GRAVEYARD"), (0, "UNCLASSIFIED"),
                             (1, "GEN1-RAW"), (2, "GEN2-STUB"), (3, "GEN3-FULLDEPTH")]
    }

    unread_count = db.execute(
        """
        SELECT COUNT(DISTINCT f.path) FROM files f
        LEFT JOIN reads r ON r.file_path = f.path
        WHERE r.id IS NULL AND f.generation >= 1 AND f.suffix = '.md'
        """
    ).fetchone()[0]

    summary_lines = [
        "# PNK-LFH Overnight Archaeology Digest",
        f"**Generated:** {now}",
        "",
        "## Archive State",
        f"- Districts: {len(district_rows)}",
        f"- Entities: {db.execute('SELECT COUNT(*) FROM entities').fetchone()[0]}",
        f"- Files: {db.execute('SELECT COUNT(*) FROM files').fetchone()[0]}",
        f"- Unread Gen1+: {unread_count}",
        "",
        "## Generation Breakdown",
        *[f"- {label}: {count}" for label, count in gen_breakdown.items()],
        "",
        "## Districts",
        *[
            f"- **{name}** — {ec} entities, {ac} active, {gc} graveyard, top {tl} lines"
            for name, ec, ac, gc, tl in district_rows
        ],
        "",
        "## GEN3-FULLDEPTH Entities (cRPG-ready)",
        *[
            f"- `{c['entity']}` ({c['district']}, {c['line_count']} lines) → `{c['path']}`"
            for c in gen3_cards
        ],
        "",
        "## Top GEN1-RAW Targets (extraction candidates)",
        *[
            f"- `{p['entity']}` ({p['district']}, {p['line_count']} lines){' [READ]' if p['already_read'] else ''}"
            for p in gen1_previews
        ],
        "",
        "## Morning Task Queue",
        "See: `manifest/todo_roulette.json` entries tagged `archaeology`",
        "",
        "### Load-Balanced Extraction Order",
        "1. **pnk00001** — Process GEN3 cards → ingest 6 entity profiles to `docs/world-building/`",
        "2. **pnk00002** — Mine `MILF_PSYCHOGRAPHIC_PROFILE_SCAN_REPORT.md` → entity relationship map",
        "3. **pnk00003** — `claudine-caribbean-archipelago-consciousness-synthesis.md` → district lore for `game/`",
        "4. **pnk00004** — Elevate `ESPEN_DIGITAL_ENTITY_CONSCIOUSNESS_PROFILE.md` GEN1→GEN3",
        "5. **pnk00005** — Run fallback scanner on `PsychoNoir-Kontrapunkt` public satellite",
        "",
        "## Artifacts Written",
        f"- `manifest/overnight_gen3_cards.json` — {len(gen3_cards)} GEN3 entities with first {preview_lines} lines",
        f"- `manifest/overnight_gen1_previews.json` — {len(gen1_previews)} GEN1 entities with first 80 lines",
        "- `manifest/overnight_archaeology_summary.md` — this file",
    ]

    summary_out = OUT_ROOT / "overnight_archaeology_summary.md"
    summary_out.write_text("\n".join(summary_lines) + "\n", encoding="utf-8")
    print(f"\n→ Summary: {summary_out}")

    db.close()
    print("\n[overnight_archaeology.py] complete.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Overnight archaeology extraction pass")
    parser.add_argument("--preview-lines", type=int, default=150,
                        help="Lines to read from each GEN3 file (default: 150)")
    parser.add_argument("--gen1-count", type=int, default=10,
                        help="Number of GEN1-RAW files to preview (default: 10)")
    args = parser.parse_args()
    run(preview_lines=args.preview_lines, gen1_count=args.gen1_count)
