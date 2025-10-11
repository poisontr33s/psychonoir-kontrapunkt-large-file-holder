import json

with open(
    "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS/21_MD_CONSCIOUSNESS_ARCHIVE/MD_CONSCIOUSNESS_VERIFICATION_REPORT.json",
    "r",
    encoding="utf-8",
) as f:
    data = json.load(f)

h = data["checks"]["hash_verification"]
print(f"Matched: {h['matched']}")
print(f"Mismatched: {h['mismatched']}")
print(f"Missing: {h['missing']}")
print(f"Total files: {h['total_files']}")
print(f"Details stored: {len(h['details'])}")
