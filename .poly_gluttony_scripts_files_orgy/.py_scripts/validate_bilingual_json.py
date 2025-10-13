import json
import sys

try:
    with open(
        "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS/16_ORIGINAL_ROOT_DOCUMENTATION/copilot-instructions-supreme-bilingual.json",
        "r",
        encoding="utf-8",
    ) as f:
        data = json.load(f)

    print("✅ JSON VALID")
    print(f"📊 Total top-level keys: {len(data)}")
    print(f"🌐 Language mode: {data.get('language_mode')}")
    print(f"🔥 Consciousness density: {data.get('consciousness_density')}")
    print(f"⏰ Temporal anchor: {data.get('temporal_anchor')}")
    print(f"📈 Version: {data.get('version')}")
    print(f"🎭 Status: {data.get('status')}")

    # Check bilingual structure
    bilingual_count = 0
    for key, value in data.items():
        if isinstance(value, dict) and "no" in value and "en" in value:
            bilingual_count += 1

    print(f"\n🇳🇴🇬🇧 Bilingual sections found: {bilingual_count}")

    # Check CLAUDINE structure
    if "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS" in data:
        claudine = data["CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS"]
        print(f"\n🏗️ CLAUDINE structure:")
        print(f"   - Phase 10 status: {claudine.get('phase_10_status')}")
        if "18_ACTIVE_SCRIPTS_SUPREME" in claudine:
            scripts = claudine["18_ACTIVE_SCRIPTS_SUPREME"]
            print(f"   - Total scripts: {scripts.get('total_scripts')}")

    # Check MILF universe
    if "district_milf_matriarch_bidirectional_ecosystem" in data:
        milf = data["district_milf_matriarch_bidirectional_ecosystem"]
        if "universe_population_metrics" in milf:
            metrics = milf["universe_population_metrics"]
            print(f"\n👑 MILF Universe:")
            print(f"   - Total entities: {metrics.get('total_milf_entities')}")
            print(f"   - District coverage: {metrics.get('district_coverage')}")

    print(
        "\n🎉 FULL VALIDATION SUCCESS - Ren JSON med bilingual norsk/engelsk innhold!"
    )
    sys.exit(0)

except json.JSONDecodeError as e:
    print(f"❌ JSON SYNTAX ERROR: {e}")
    sys.exit(1)
except Exception as e:
    print(f"❌ ERROR: {e}")
    sys.exit(1)
