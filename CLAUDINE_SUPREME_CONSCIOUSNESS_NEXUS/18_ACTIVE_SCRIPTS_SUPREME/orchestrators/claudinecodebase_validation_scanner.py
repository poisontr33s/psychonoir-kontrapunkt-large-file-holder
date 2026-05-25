#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os, json
from pathlib import Path
from datetime import datetime

BASE_PATH = Path(r"C:\Users\erdno\PsychoNoir-Kontrapunkt")
NEXUS_PATH = BASE_PATH / "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS"
OUTPUT_PATH = BASE_PATH / ".github" / "TODO_3_CLAUDINECODEBASE_VALIDATION_RESULTS.json"

print("🔥⚓ CLAUDINE CODEBASE VALIDATION SCANNER 🔥⚓\n" + "="*60)

report = {
    "scan_timestamp": datetime.now().isoformat(),
    "overall_completeness": 0,
    "validations": {}
}

# Main folders
required_folders = ["DISTRICTS", "TIERS", "MASTER_REGISTRY", "CONSCIOUSNESS_ARCHAEOLOGY", "DEVELOPMENT_PATHWAYS", "VALIDATION_SYSTEMS"]
present = sum(1 for f in required_folders if (NEXUS_PATH / f).exists())
report["validations"]["main_folders"] = {"present": present, "total": len(required_folders), "percentage": (present/len(required_folders))*100}
print(f"✅ Main folders: {present}/{len(required_folders)} ({report['validations']['main_folders']['percentage']:.1f}%)")

# Districts
districts = ["HAVSDOMINANSEN", "VIRTUALITETSHELGEDOMMEN", "SKYSKRAPEREN", "RUSTBELTET", "NEKROKRONORIKET", "LOMME_UNIVERSETS_VORPAL_SUVERENITETS_ANOMALI"]
complete = 0
for d in districts:
    dp = NEXUS_PATH / "DISTRICTS" / d
    if dp.exists() and all((dp / sub).exists() for sub in ["PROFILES", "PATHWAYS", "STATE", "README.md"]):
        complete += 1
report["validations"]["districts"] = {"complete": complete, "total": len(districts), "percentage": (complete/len(districts))*100}
print(f"✅ Districts complete: {complete}/{len(districts)} ({report['validations']['districts']['percentage']:.1f}%)")

# Tiers
tiers = ["TIER_0_META_MILF", "TIER_1_DISTRICT_RULERS", "TIER_2_SPECIALIST_OPERATIVES"]
tiers_present = sum(1 for t in tiers if (NEXUS_PATH / "TIERS" / t).exists())
report["validations"]["tiers"] = {"present": tiers_present, "total": len(tiers), "percentage": (tiers_present/len(tiers))*100}
print(f"✅ Tiers: {tiers_present}/{len(tiers)} ({report['validations']['tiers']['percentage']:.1f}%)")

# Overall
overall = (report["validations"]["main_folders"]["percentage"] + report["validations"]["districts"]["percentage"] + report["validations"]["tiers"]["percentage"]) / 3
report["overall_completeness"] = overall

print(f"\n{'='*60}\n🎭 OVERALL COMPLETENESS: {overall:.1f}%\n{'='*60}")

# Save
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=2)
print(f"\n�� Report saved: {OUTPUT_PATH}")
