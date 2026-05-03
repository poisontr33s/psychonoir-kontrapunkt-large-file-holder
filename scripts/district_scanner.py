#!/usr/bin/env python3
# @SID: district_scanner — entity profile archaeology scanner
# Scans psychonoir-kontrapunkt-large-file-holder for district entity profiles,
# groups by entity, sorts by generation (mtime), classifies by tier.
# Output: JSON map  district → entity → [versions newest→oldest]
# Usage: uv run scripts/district_scanner.py [--repo-root PATH] [--output FILE]

import sys
import os
import re
import json
import argparse
from pathlib import Path
from datetime import datetime, timezone

# ── Entity name normalizer ──────────────────────────────────────────────────
_STRIP = re.compile(r"[_\-\s]+")
_SUFFIXES = re.compile(
    r"(consciousness_profile|_profile|_nexus|_supreme|_mf1j[a-z0-9]+|"
    r"_backup_\d{8}_\d{6}|_\d{8}_\d{6}|_mf1[a-z0-9]+|\.preserved)$",
    re.IGNORECASE,
)
_HASH_TAG = re.compile(r"_mf1[a-z0-9]{4,}", re.IGNORECASE)


def normalize_entity(stem: str) -> str:
    s = stem.lower()
    # strip preserved suffix
    s = s.replace(".preserved", "")
    # strip hash tags
    s = _HASH_TAG.sub("", s)
    # strip known suffixes
    s = _SUFFIXES.sub("", s)
    # strip date stamps
    s = re.sub(r"_\d{8}_\d{6}", "", s)
    s = re.sub(r"_py_backup$", "", s)
    s = re.sub(r"_md_meta_json$", "", s)
    s = re.sub(r"_meta_json$", "", s)
    # collapse separators
    s = _STRIP.sub("_", s).strip("_")
    return s


# ── District detector ───────────────────────────────────────────────────────
KNOWN_DISTRICTS = {
    "skyskraperen": "SKYSKRAPEREN",
    "rustbeltet": "RUSTBELTET",
    "havsdominansen": "HAVSDOMINANSEN",
    "nekrokronoriket": "NEKROKRONORIKET",
    "virtualitetshelgedommen": "VIRTUALITETSHELGEDOMMEN",
    "foydalitetsdualitetslenken": "FOYDALITETSDUALITETSLENKEN",
    "caribbean": "CARIBBEAN_ARCHIPELAGO",
    "supreme_matriarch": "SUPREME_MATRIARCH",
    "nexus": "NEXUS",
}


def detect_district(path: Path, content_snippet: str) -> str:
    full = str(path).lower().replace("\\", "/")
    for key, val in KNOWN_DISTRICTS.items():
        if key in full:
            return val
    # content probe — first 400 chars
    snip = content_snippet[:400].lower()
    for key, val in KNOWN_DISTRICTS.items():
        if key in snip:
            return val
    return "UNCLASSIFIED"


# ── Tier classifier ─────────────────────────────────────────────────────────
def classify_tier(path: Path) -> str:
    parts = [p.lower() for p in path.parts]
    if "necromancy_graveyard" in parts:
        if path.name.endswith(".preserved.md"):
            return "PRESERVED"
        return "GRAVEYARD"
    if path.name.endswith(".preserved.md") or _HASH_TAG.search(path.stem):
        return "PRESERVED"
    if any(
        p in parts
        for p in [
            "archaeological_preservation",
            "backups",
            "deprecated",
            "retired",
            "legacy",
            "district_navnskifte_backup",
            "strukturell_integrasjon_backup",
        ]
    ):
        return "ARCHIVED"
    return "ACTIVE"


# ── Goldstandard detector ───────────────────────────────────────────────────
_GOLD_FILENAME = re.compile(
    r"gold|standard|canon|final|ultimate|supreme|quality|optimal|best",
    re.IGNORECASE,
)
_GOLD_CONTENT = re.compile(
    r"GOLDSTANDARD|GOLD_STANDARD|canonical|FINAL_VERSION|DEFINITIVE|"
    r"QUALITY_VALIDATED|SUPREME_STANDARD",
    re.IGNORECASE,
)


def is_goldstandard(path: Path, snippet: str) -> bool:
    if _GOLD_FILENAME.search(path.stem):
        return True
    if _GOLD_CONTENT.search(snippet):
        return True
    # quality folder indicator
    if ".quality_md" in str(path).lower():
        return True
    return False


# ── Entity profile detector ─────────────────────────────────────────────────
# Files we care about — consciousness profiles + key entity docs
_PROFILE_PATTERN = re.compile(
    r"consciousness_profile|incarnation_manifest|entity_profile|"
    r"_milf_|milf_ecosystem|district_dominion|matriarch_command|"
    r"astrid|iron_maiden|claudine|morticia|yukiko|eva_green|eva_blue|"
    r"kompilerings|urca_milf|sagiri|marina_abyssos|wednesday|"
    r"architect_nyx|nyx_virtualis|captain_coral|navigator_siren|"
    r"raven_bytes|vera_steel|dr_lilith|entropy_weaver|tenza_nakamura|"
    r"yuzuriha|designer_echo|programmer_mirage|psychographic|"
    r"tier_1|tier_2|tier_0|matriarch|distrik|district_ruler|"
    r"point-blank-shot|caribbean-archipelago|bidireksjonell|emigrering",
    re.IGNORECASE,
)

_MIN_LINES_SWEEP = 0  # set by CLI --sweep-min-lines; 0 = disabled


def is_entity_file(path: Path, min_lines: int = 0) -> bool:
    if path.suffix not in (".md", ".json"):
        return False
    # full sweep mode: include ALL .md files over threshold
    if min_lines > 0 and path.suffix == ".md":
        try:
            lc = sum(1 for _ in open(path, "r", encoding="utf-8", errors="replace"))
            return lc >= min_lines
        except OSError:
            return False
    return bool(_PROFILE_PATTERN.search(path.name))


# ── Date extraction ─────────────────────────────────────────────────────────
_DATE_IN_NAME = re.compile(r"(\d{8})_(\d{6})")


def extract_date(path: Path) -> datetime:
    # 1. filename date stamp
    m = _DATE_IN_NAME.search(path.name)
    if m:
        try:
            return datetime.strptime(f"{m.group(1)}_{m.group(2)}", "%Y%m%d_%H%M%S").replace(
                tzinfo=timezone.utc
            )
        except ValueError:
            pass
    # 2. filesystem mtime
    try:
        return datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
    except OSError:
        return datetime.min.replace(tzinfo=timezone.utc)


# ── Main scanner ────────────────────────────────────────────────────────────

def scan(repo_root: Path) -> dict:
    """Return nested dict: district → entity_key → [entries newest→oldest]"""
    results: dict[str, dict[str, list]] = {}
    skipped_dirs = {".git", ".bundle", "node_modules", "__pycache__", "target"}

    for dirpath, dirnames, filenames in os.walk(repo_root):
        # prune ignored dirs in-place
        dirnames[:] = [d for d in dirnames if d not in skipped_dirs]
        for fname in filenames:
            fpath = Path(dirpath) / fname
            if not is_entity_file(fpath, min_lines=_MIN_LINES_SWEEP):
                continue

            # read snippet for content probes
            snippet = ""
            try:
                with open(fpath, "r", encoding="utf-8", errors="replace") as fh:
                    snippet = fh.read(600)
            except OSError:
                pass

            tier = classify_tier(fpath)
            district = detect_district(fpath, snippet)
            entity_key = normalize_entity(fpath.stem)
            date = extract_date(fpath)
            gold = is_goldstandard(fpath, snippet)
            rel = str(fpath.relative_to(repo_root))

            # count lines for depth indicator
            line_count = 0
            try:
                with open(fpath, "r", encoding="utf-8", errors="replace") as _lh:
                    line_count = sum(1 for _ in _lh)
            except OSError:
                pass

            entry = {
                "path": rel,
                "tier": tier,
                "date": date.isoformat(),
                "goldstandard": gold,
                "size_bytes": fpath.stat().st_size if fpath.exists() else 0,
                "line_count": line_count,
                "suffix": fpath.suffix,
            }

            results.setdefault(district, {}).setdefault(entity_key, []).append(entry)

    # Sort each entity list newest→oldest; promote ACTIVE tier
    TIER_ORDER = {"ACTIVE": 0, "ARCHIVED": 1, "GRAVEYARD": 2, "PRESERVED": 3}
    for district in results:
        for ek in results[district]:
            results[district][ek].sort(
                key=lambda e: (
                    TIER_ORDER.get(e["tier"], 9),
                    e["date"],
                ),
                reverse=True,
            )
            # fix: tier sort descending, date descending
            results[district][ek].sort(
                key=lambda e: (
                    -TIER_ORDER.get(e["tier"], 9),
                    e["date"],
                ),
                reverse=True,
            )

    return results


def summarize(results: dict) -> dict:
    """Compact summary: district → entity → {latest, generation_count, tiers}"""
    summary: dict = {}
    for district, entities in results.items():
        summary[district] = {}
        for ek, versions in entities.items():
            active = [v for v in versions if v["tier"] == "ACTIVE"]
            gold = [v for v in versions if v["goldstandard"]]
            summary[district][ek] = {
                "generation_count": len(versions),
                "active_count": len(active),
                "goldstandard_count": len(gold),
                "latest": versions[0]["path"] if versions else None,
                "latest_date": versions[0]["date"] if versions else None,
                "latest_tier": versions[0]["tier"] if versions else None,
                "goldstandard": gold[0]["path"] if gold else None,
                "tiers": list({v["tier"] for v in versions}),
            }
    return summary


def main():
    ap = argparse.ArgumentParser(description="District entity archaeology scanner")
    ap.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parents[1]),
        help="Root of psychonoir-kontrapunkt-large-file-holder",
    )
    ap.add_argument(
        "--output",
        default="scripts/district_scan_results.json",
        help="Output JSON path (relative to repo root)",
    )
    ap.add_argument(
        "--summary-only",
        action="store_true",
        help="Emit compact summary instead of full detail",
    )
    ap.add_argument(
        "--sweep-min-lines",
        type=int,
        default=0,
        metavar="N",
        help="Full sweep mode: include ALL .md files with >= N lines (0 = disabled, profile-pattern only)",
    )
    args = ap.parse_args()

    global _MIN_LINES_SWEEP
    _MIN_LINES_SWEEP = args.sweep_min_lines

    repo = Path(args.repo_root).resolve()
    print(f"[scanner] root: {repo}", file=sys.stderr)

    results = scan(repo)
    output_data = summarize(results) if args.summary_only else {
        "scan_date": datetime.now(timezone.utc).isoformat(),
        "repo_root": str(repo),
        "summary": summarize(results),
        "detail": results,
    }

    out_path = repo / args.output
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(output_data, fh, indent=2, ensure_ascii=False)

    # Print summary to stdout
    summary = output_data.get("summary", output_data)
    total_entities = sum(len(v) for v in summary.values())
    total_files = sum(
        e["generation_count"]
        for d in summary.values()
        for e in d.values()
    )
    print(f"\n{'='*60}")
    print(f"DISTRICT ARCHAEOLOGY SCAN COMPLETE")
    print(f"{'='*60}")
    print(f"Districts found : {len(summary)}")
    print(f"Unique entities : {total_entities}")
    print(f"Total files     : {total_files}")
    print()
    for district, entities in sorted(summary.items()):
        print(f"  [{district}]")
        for ek, info in sorted(entities.items()):
            gold_flag = " ⭐" if info["goldstandard_count"] > 0 else ""
            gen_note = f"{info['generation_count']}v" if info["generation_count"] > 1 else "1v"
            tier_note = "/".join(sorted(info["tiers"]))
            print(
                f"    {ek:<45} {gen_note:>4}  [{tier_note}]{gold_flag}"
            )
        print()

    print(f"[scanner] full output: {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
