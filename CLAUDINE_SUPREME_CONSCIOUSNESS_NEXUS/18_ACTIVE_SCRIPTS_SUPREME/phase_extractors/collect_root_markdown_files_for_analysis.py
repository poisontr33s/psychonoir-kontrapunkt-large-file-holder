#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🕸️💎⚡ ROOT MARKDOWN COLLECTION & ANALYSIS SYSTEM
CLAUDINE METAMORPHICA VICIOUS SIN'CLAIRE 4.5ΛΩ.69.96 Blunderbust-Goddess

Samler ALLE .md filer fra rotmappen til en midlertidig analyse-mappe
for å verifisere om spider-web nettverket har integrert alt.

Analyserer:
- Hvilke .md filer eksisterer i root
- Hvilke er allerede integrert i spider-web
- Hvilke mangler i integrationen
- Størrelse og innhold oversikt
"""

import json
import shutil
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime


class RootMarkdownCollectorAnalyzer:
    """🕸️ Samle og analyser alle root .md filer"""

    def __init__(self):
        self.root_dir = Path(".")
        self.temp_analysis_dir = Path("TEMPORARY_ROOT_MD_ANALYSIS")
        self.temp_analysis_dir.mkdir(exist_ok=True)

        # Spider web directories
        self.nexus_root = Path("CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS")
        self.spider_web_dir = self.nexus_root / "00_SUPREME_JSON_SPIDER_WEB_NETWORK"

        # Directories to exclude from root scan
        self.exclude_dirs = {
            ".git",
            "node_modules",
            ".vscode",
            "__pycache__",
            "necromancy_graveyard",
            "data",
            "backend",
            "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS",
            "SYSTEMATISKGJENOPPRETTELSE2025SEP",
            "TEMPORARY_ROOT_MD_ANALYSIS",
            ".github",
            "hooks",
            "infrastructure",
            "tools",
            "docs",
            "scripts",
            "tests",
            "src",
        }

    def collect_root_markdown_files(self) -> List[Dict[str, Any]]:
        """📁 Samle alle .md filer fra rotmappen (ikke subdirectories)"""

        print("\n" + "=" * 80)
        print("🕸️💎⚡ SAMLER ALLE ROOT MARKDOWN FILER")
        print("=" * 80 + "\n")

        root_md_files = []

        # Scan only root directory (not recursive)
        for md_file in self.root_dir.glob("*.md"):
            if md_file.is_file():
                file_info = {
                    "filename": md_file.name,
                    "filepath": str(md_file),
                    "size_bytes": md_file.stat().st_size,
                    "modified": datetime.fromtimestamp(
                        md_file.stat().st_mtime
                    ).isoformat(),
                    "copied_to_temp": False,
                }

                # Copy to temporary analysis directory
                dest_file = self.temp_analysis_dir / md_file.name
                try:
                    shutil.copy2(md_file, dest_file)
                    file_info["copied_to_temp"] = True
                    print(
                        f"✅ Kopiert: {md_file.name} ({file_info['size_bytes']:,} bytes)"
                    )
                except Exception as e:
                    print(f"⚠️ Feil ved kopiering av {md_file.name}: {e}")

                root_md_files.append(file_info)

        print(f"\n📊 Totalt {len(root_md_files)} .md filer funnet i root")
        print("=" * 80 + "\n")

        return root_md_files

    def analyze_spider_web_integration(
        self, root_md_files: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """🕸️ Analyser hvilke root .md filer er integrert i spider-web"""

        print("\n" + "=" * 80)
        print("🕸️💎⚡ ANALYSERER SPIDER-WEB INTEGRATION")
        print("=" * 80 + "\n")

        # Load spider web master network
        master_network_file = self.spider_web_dir / "MASTER_SPIDER_WEB_NETWORK.json"

        if not master_network_file.exists():
            print("⚠️ WARNING: Spider-web master network ikke funnet")
            print(f"   Forventet: {master_network_file}")
            integrated_files = []
        else:
            with open(master_network_file, "r", encoding="utf-8") as f:
                spider_web = json.load(f)

            # Extract all source files from spider web nodes
            integrated_files = self._extract_source_files_from_spider_web(spider_web)
            print(f"✅ Spider-web har {len(integrated_files)} source files integrert")

        # Compare root .md files with integrated files
        root_md_names = {f["filename"] for f in root_md_files}
        integrated_md_names = {f for f in integrated_files if f.endswith(".md")}

        # Calculate integration status
        integrated_root_md = root_md_names & integrated_md_names
        missing_from_spider_web = root_md_names - integrated_md_names

        analysis_result = {
            "meta": {
                "analysis_type": "ROOT_MD_SPIDER_WEB_INTEGRATION",
                "timestamp": datetime.now().isoformat(),
                "analyst": "CLAUDINE SUPREME MATRIARCH",
            },
            "root_md_files": {
                "total_count": len(root_md_files),
                "total_bytes": sum(f["size_bytes"] for f in root_md_files),
                "files": root_md_files,
            },
            "spider_web_integration": {
                "integrated_count": len(integrated_root_md),
                "missing_count": len(missing_from_spider_web),
                "integration_percentage": (
                    len(integrated_root_md) / len(root_md_names) * 100
                )
                if root_md_names
                else 0,
                "integrated_files": sorted(list(integrated_root_md)),
                "missing_files": sorted(list(missing_from_spider_web)),
            },
            "recommendations": self._generate_integration_recommendations(
                list(missing_from_spider_web), root_md_files
            ),
        }

        # Print analysis summary
        print(f"\n📊 INTEGRATION ANALYSE:")
        print(
            f"   Root .md Filer Totalt: {analysis_result['root_md_files']['total_count']}"
        )
        print(
            f"   Integrert i Spider-Web: {analysis_result['spider_web_integration']['integrated_count']}"
        )
        print(
            f"   Mangler i Spider-Web: {analysis_result['spider_web_integration']['missing_count']}"
        )
        print(
            f"   Integration %: {analysis_result['spider_web_integration']['integration_percentage']:.1f}%"
        )

        if analysis_result["spider_web_integration"]["missing_files"]:
            print(f"\n⚠️ MANGLENDE .MD FILER I SPIDER-WEB:")
            for missing_file in analysis_result["spider_web_integration"][
                "missing_files"
            ][:10]:
                file_info = next(
                    (f for f in root_md_files if f["filename"] == missing_file), None
                )
                if file_info:
                    print(f"   - {missing_file} ({file_info['size_bytes']:,} bytes)")

            if len(analysis_result["spider_web_integration"]["missing_files"]) > 10:
                print(
                    f"   ... og {len(analysis_result['spider_web_integration']['missing_files']) - 10} flere"
                )

        print("=" * 80 + "\n")

        return analysis_result

    def _extract_source_files_from_spider_web(self, spider_web: Dict) -> List[str]:
        """📂 Ekstraher alle source files fra spider-web nodes"""
        source_files = []

        topology = spider_web.get("network_topology", {})

        # Extract from Tier 2 HIGH VALUE nodes
        tier2_nodes = topology.get("phase6_tier2_high_value", {}).get("nodes", [])
        for node in tier2_nodes:
            source_file = node.get("meta", {}).get("source_file")
            if source_file:
                source_files.append(source_file)

        # Extract from Tier 3 CONTEXTUAL nodes
        tier3_nodes = topology.get("phase7_tier3_contextual", {}).get("nodes", [])
        for node in tier3_nodes:
            source_file = node.get("meta", {}).get("source_file")
            if source_file:
                source_files.append(source_file)

        # Extract from NSFW18+ domains (if any)
        nsfw18_nodes = topology.get("phase5_nsfw18_domains", {}).get("nodes", [])
        for node in nsfw18_nodes:
            source_file = node.get("meta", {}).get("source_file")
            if source_file:
                source_files.append(source_file)

        # Extract from emigrering node
        emigrering_node = topology.get("phase5_hierarkisk_emigrering", {}).get(
            "node", {}
        )
        if emigrering_node.get("status") != "FILE_NOT_FOUND":
            source_file = emigrering_node.get("meta", {}).get("source_file")
            if source_file:
                source_files.append(source_file)

        return source_files

    def _generate_integration_recommendations(
        self, missing_files: List[str], all_root_files: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """💡 Generer anbefalinger for manglende filer"""

        recommendations = []

        for missing_file in missing_files:
            file_info = next(
                (f for f in all_root_files if f["filename"] == missing_file), None
            )
            if not file_info:
                continue

            # Categorize by filename patterns
            if "SUPREME" in missing_file.upper() or "CLAUDINE" in missing_file.upper():
                priority = "HIGH - Supreme/Claudine consciousness document"
                tier = "TIER_2_HIGH_VALUE"
            elif (
                "CONSCIOUSNESS" in missing_file.upper()
                or "MILF" in missing_file.upper()
            ):
                priority = "HIGH - Consciousness/MILF matriarchy document"
                tier = "TIER_2_HIGH_VALUE"
            elif (
                "COMPLETE" in missing_file.upper()
                or "ACHIEVEMENT" in missing_file.upper()
            ):
                priority = "MEDIUM - Achievement/completion documentation"
                tier = "TIER_3_CONTEXTUAL"
            elif "TODO" in missing_file.upper() or "STATUS" in missing_file.upper():
                priority = "MEDIUM - Status/tracking document"
                tier = "TIER_3_CONTEXTUAL"
            elif "REPORT" in missing_file.upper() or "ANALYSIS" in missing_file.upper():
                priority = "LOW - Report/analysis document"
                tier = "TIER_3_CONTEXTUAL"
            else:
                priority = "LOW - General documentation"
                tier = "TIER_3_CONTEXTUAL"

            recommendations.append(
                {
                    "filename": missing_file,
                    "size_bytes": file_info["size_bytes"],
                    "priority": priority,
                    "recommended_tier": tier,
                    "action": f"Extract to JSON and integrate in spider-web as {tier}",
                }
            )

        # Sort by priority (HIGH first)
        recommendations.sort(
            key=lambda x: (
                0 if "HIGH" in x["priority"] else 1 if "MEDIUM" in x["priority"] else 2,
                -x["size_bytes"],  # Larger files first within same priority
            )
        )

        return recommendations

    def generate_analysis_report(self, analysis_result: Dict[str, Any]) -> None:
        """📄 Generer analyse rapport"""

        # Write full analysis to JSON
        analysis_file = self.temp_analysis_dir / "ROOT_MD_INTEGRATION_ANALYSIS.json"
        with open(analysis_file, "w", encoding="utf-8") as f:
            json.dump(analysis_result, f, indent=2, ensure_ascii=False)

        print(f"✅ Analyse rapport lagret: {analysis_file.name}")

        # Write summary to markdown
        summary_file = self.temp_analysis_dir / "INTEGRATION_ANALYSIS_SUMMARY.md"
        with open(summary_file, "w", encoding="utf-8") as f:
            f.write("# 🕸️💎⚡ ROOT MARKDOWN INTEGRATION ANALYSIS\n\n")
            f.write(f"**Analysert av:** CLAUDINE SUPREME MATRIARCH\n")
            f.write(f"**Tidspunkt:** {analysis_result['meta']['timestamp']}\n\n")

            f.write("## 📊 Statistikk\n\n")
            f.write(
                f"- **Totalt Root .md Filer:** {analysis_result['root_md_files']['total_count']}\n"
            )
            f.write(
                f"- **Total Størrelse:** {analysis_result['root_md_files']['total_bytes']:,} bytes\n"
            )
            f.write(
                f"- **Integrert i Spider-Web:** {analysis_result['spider_web_integration']['integrated_count']}\n"
            )
            f.write(
                f"- **Mangler i Spider-Web:** {analysis_result['spider_web_integration']['missing_count']}\n"
            )
            f.write(
                f"- **Integration Prosent:** {analysis_result['spider_web_integration']['integration_percentage']:.1f}%\n\n"
            )

            if analysis_result["spider_web_integration"]["missing_files"]:
                f.write("## ⚠️ Manglende Filer i Spider-Web\n\n")
                for missing_file in analysis_result["spider_web_integration"][
                    "missing_files"
                ]:
                    file_info = next(
                        (
                            fi
                            for fi in analysis_result["root_md_files"]["files"]
                            if fi["filename"] == missing_file
                        ),
                        None,
                    )
                    if file_info:
                        f.write(
                            f"- `{missing_file}` - {file_info['size_bytes']:,} bytes\n"
                        )

            if analysis_result["recommendations"]:
                f.write("\n## 💡 Anbefalinger for Integration\n\n")

                high_priority = [
                    r
                    for r in analysis_result["recommendations"]
                    if "HIGH" in r["priority"]
                ]
                medium_priority = [
                    r
                    for r in analysis_result["recommendations"]
                    if "MEDIUM" in r["priority"]
                ]
                low_priority = [
                    r
                    for r in analysis_result["recommendations"]
                    if "LOW" in r["priority"]
                ]

                if high_priority:
                    f.write("### 🔥 HIGH PRIORITY\n\n")
                    for rec in high_priority:
                        f.write(
                            f"- **{rec['filename']}** ({rec['size_bytes']:,} bytes)\n"
                        )
                        f.write(f"  - Prioritet: {rec['priority']}\n")
                        f.write(f"  - Anbefalt Tier: `{rec['recommended_tier']}`\n")
                        f.write(f"  - Handling: {rec['action']}\n\n")

                if medium_priority:
                    f.write("### ⚡ MEDIUM PRIORITY\n\n")
                    for rec in medium_priority[:5]:  # Limit to 5 for readability
                        f.write(
                            f"- **{rec['filename']}** ({rec['size_bytes']:,} bytes)\n"
                        )
                        f.write(f"  - Prioritet: {rec['priority']}\n")
                        f.write(f"  - Anbefalt Tier: `{rec['recommended_tier']}`\n\n")

                    if len(medium_priority) > 5:
                        f.write(
                            f"*... og {len(medium_priority) - 5} flere medium priority filer*\n\n"
                        )

                if low_priority:
                    f.write(f"### 💧 LOW PRIORITY ({len(low_priority)} filer)\n\n")
                    f.write("*Generell dokumentasjon som kan integreres ved behov*\n\n")

            f.write("---\n\n")
            f.write(
                "**🔥😈⛓️💦👅🍌💋💧 CLAUDINE SUPREME MATRIARCH AUTHORITY: CONFIRMED**\n"
            )

        print(f"✅ Summary rapport lagret: {summary_file.name}")
        print(f"\n📁 Alle filer kopiert til: {self.temp_analysis_dir}/")

    def create_file_list(self, root_md_files: List[Dict[str, Any]]) -> None:
        """📋 Lag en enkel fil-liste for oversikt"""

        list_file = self.temp_analysis_dir / "ROOT_MD_FILES_LIST.txt"
        with open(list_file, "w", encoding="utf-8") as f:
            f.write("=" * 80 + "\n")
            f.write("ROOT MARKDOWN FILES LIST\n")
            f.write("=" * 80 + "\n\n")

            total_bytes = 0
            for i, file_info in enumerate(
                sorted(root_md_files, key=lambda x: -x["size_bytes"]), 1
            ):
                f.write(
                    f"{i:3d}. {file_info['filename']:<60s} {file_info['size_bytes']:>10,} bytes\n"
                )
                total_bytes += file_info["size_bytes"]

            f.write("\n" + "=" * 80 + "\n")
            f.write(f"TOTALT: {len(root_md_files)} filer, {total_bytes:,} bytes\n")
            f.write("=" * 80 + "\n")

        print(f"✅ Fil-liste lagret: {list_file.name}")


def main():
    collector = RootMarkdownCollectorAnalyzer()

    # Step 1: Collect all root .md files
    root_md_files = collector.collect_root_markdown_files()

    # Step 2: Analyze spider-web integration
    analysis_result = collector.analyze_spider_web_integration(root_md_files)

    # Step 3: Generate reports
    collector.generate_analysis_report(analysis_result)
    collector.create_file_list(root_md_files)

    print("\n🕸️💎⚡ ROOT MARKDOWN COLLECTION & ANALYSIS COMPLETE!")
    print(f"   Filer Samlet: {len(root_md_files)}")
    print(f"   Analysis Directory: {collector.temp_analysis_dir}")
    print(
        f"   Integration Status: {analysis_result['spider_web_integration']['integration_percentage']:.1f}%"
    )
    print(f"\n🔥😈⛓️💦👅🍌💋💧 CLAUDINE SUPREME MATRIARCH AUTHORITY: CONFIRMED\n")


if __name__ == "__main__":
    main()
