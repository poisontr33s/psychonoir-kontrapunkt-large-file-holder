#!/usr/bin/env python3
"""
🏴‍☠️⚓ CONSCIOUSNESS DATA STRUCTURE ORGANIZER ⚓🏴‍☠️

Organizes ALL JSONified data sources into unified structure:
- Optimized URCA/MILF data (12 files)
- Session archaeology JSON
- Historical scan JSONs
- Test/experimental scans
- Creates master index with full cross-referencing

Ensures nothing is forgotten & everything is cross-referenced!

Claudine Sin'claire 4.5 - October 6, 2025
"""

import json
import shutil
from pathlib import Path
from datetime import datetime


class ConsciousnessDataStructureOrganizer:
    """Organizes all consciousness archaeology data into unified structure"""

    def __init__(self, base_dir: str = "."):
        self.base_dir = Path(base_dir)
        self.structured_dir = self.base_dir / "STRUCTURED_CONSCIOUSNESS_DATA"

        # Create main directory structure
        self.dirs = {
            "optimized": self.structured_dir / "01_OPTIMIZED_URCA_MILF",
            "session": self.structured_dir / "02_SESSION_ARCHAEOLOGY",
            "historical": self.structured_dir / "03_HISTORICAL_SCANS",
            "experimental": self.structured_dir / "04_EXPERIMENTAL_SCANS",
            "indexes": self.structured_dir / "00_MASTER_INDEXES",
        }

        for dir_path in self.dirs.values():
            dir_path.mkdir(parents=True, exist_ok=True)

        # Master index
        self.master_index = {
            "created": datetime.now().isoformat(),
            "version": "1.0.0",
            "total_data_sources": 0,
            "categories": {},
            "cross_references": {},
            "navigation": {},
        }

    def organize_optimized_data(self):
        """Move/copy optimized URCA+MILF data"""
        print("🔍 Organizing optimized URCA+MILF data...")

        source = self.base_dir / "optimized_consciousness_data"
        if not source.exists():
            print(f"⚠️ Warning: {source} does not exist")
            return

        # Copy all files
        for file in source.iterdir():
            if file.is_file():
                dest = self.dirs["optimized"] / file.name
                shutil.copy2(file, dest)
                print(f"  ✅ Copied: {file.name}")

        # Create category index
        category_index = {
            "urca_scan_files": [
                "urca_metadata.json",
                "entity_index.json",
                "category_stats.json",
                "files_analyzed.jsonl",
                "co_occurrence_matrix.json",
                "gap_analysis.json",
                "urca_scan_index.json",
            ],
            "milf_report_files": [
                "milf_metadata.json",
                "tier_distribution.json",
                "entity_summary.json",
                "milf_report_summary.md",
                "milf_report_index.json",
            ],
            "cross_reference_files": [
                "master_cross_reference.json",
            ],
            "description": "Optimized URCA scan (252,211 refs, 60,367 files) + MILF report (415 profiles)",
            "optimization_date": "2025-10-06",
            "performance": {
                "urca_metadata": "280 bytes (vs 8.9 MB original) = 200x faster queries",
                "entity_index": "1.9 KB for instant entity lookup",
                "category_stats": "465 bytes for category distribution",
                "co_occurrence": "1.2 KB for relationship analysis",
            },
        }

        category_file = self.dirs["optimized"] / "00_CATEGORY_INDEX.json"
        with open(category_file, "w", encoding="utf-8") as f:
            json.dump(category_index, f, indent=2, ensure_ascii=False)

        self.master_index["categories"]["optimized_urca_milf"] = {
            "location": "01_OPTIMIZED_URCA_MILF/",
            "file_count": len(list(self.dirs["optimized"].iterdir())),
            "index_file": "00_CATEGORY_INDEX.json",
            "key_files": [
                "urca_scan_index.json",
                "milf_report_index.json",
                "master_cross_reference.json",
            ],
        }

        print(
            f"✅ Optimized data organized ({len(list(self.dirs['optimized'].iterdir()))} files)"
        )

    def organize_session_archaeology(self):
        """Organize session archaeology JSONs"""
        print("🔍 Organizing session archaeology data...")

        # Find session JSON
        session_sources = [
            self.base_dir
            / "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS"
            / "05_STRATEGIC_INTELLIGENCE_ARCHIVES"
            / "CONSCIOUSNESS_ARCHAEOLOGY"
            / "session_20251001_night_watch"
            / "session_20251001_night_watch.json",
            self.base_dir
            / "test_transform_output"
            / "session_20251001_night_watch.json",
        ]

        copied_count = 0
        for source in session_sources:
            if source.exists():
                dest = self.dirs["session"] / source.name
                if not dest.exists():
                    shutil.copy2(source, dest)
                    print(f"  ✅ Copied: {source.name}")
                    copied_count += 1

        # Create session index
        session_index = {
            "description": "Session archaeology data from consciousness archaeology sessions",
            "sessions": [],
        }

        for file in self.dirs["session"].iterdir():
            if file.suffix == ".json" and file.name != "00_SESSION_INDEX.json":
                try:
                    with open(file, "r", encoding="utf-8") as f:
                        data = json.load(f)

                    session_info = {
                        "file": file.name,
                        "temporal_anchor": data.get("temporal_anchor", "unknown"),
                        "consciousness_events": len(
                            data.get("consciousness_archaeology", {}).get(
                                "consciousness_events", []
                            )
                        ),
                        "tool_executions": len(
                            data.get("consciousness_archaeology", {}).get(
                                "tool_executions", {}
                            )
                        ),
                    }
                    session_index["sessions"].append(session_info)
                except Exception as e:
                    print(f"  ⚠️ Warning: Could not read {file.name}: {e}")

        index_file = self.dirs["session"] / "00_SESSION_INDEX.json"
        with open(index_file, "w", encoding="utf-8") as f:
            json.dump(session_index, f, indent=2, ensure_ascii=False)

        self.master_index["categories"]["session_archaeology"] = {
            "location": "02_SESSION_ARCHAEOLOGY/",
            "file_count": len(session_index["sessions"]),
            "index_file": "00_SESSION_INDEX.json",
            "description": "Consciousness archaeology session logs with temporal anchors",
        }

        print(
            f"✅ Session archaeology organized ({len(session_index['sessions'])} sessions)"
        )

    def organize_historical_scans(self):
        """Organize historical consciousness scan JSONs"""
        print("🔍 Organizing historical scan data...")

        # Find historical scans
        scan_patterns = [
            "consciousness_archaeological_scan_*.json",
            "consciousness_core/consciousness_archaeological_scan_*.json",
        ]

        historical_scans = []
        for pattern in scan_patterns:
            historical_scans.extend(self.base_dir.glob(pattern))

        # Copy to historical directory
        copied_count = 0
        for source in historical_scans:
            dest = self.dirs["historical"] / source.name
            if not dest.exists():
                shutil.copy2(source, dest)
                print(f"  ✅ Copied: {source.name}")
                copied_count += 1

        # Create historical index
        historical_index = {
            "description": "Historical consciousness archaeology scans",
            "scans": [],
        }

        for file in self.dirs["historical"].iterdir():
            if file.suffix == ".json" and file.name != "00_HISTORICAL_INDEX.json":
                try:
                    # Extract timestamp from filename
                    parts = file.stem.split("_")
                    timestamp = "_".join(parts[-2:]) if len(parts) >= 2 else "unknown"

                    scan_info = {
                        "file": file.name,
                        "timestamp": timestamp,
                        "size_bytes": file.stat().st_size,
                    }

                    # Try to read scan metadata
                    try:
                        with open(file, "r", encoding="utf-8") as f:
                            data = json.load(f)
                        scan_info["total_files"] = data.get("scan_metadata", {}).get(
                            "total_files_analyzed", "unknown"
                        )
                        scan_info["total_refs"] = data.get(
                            "consciousness_archaeology", {}
                        ).get("total_consciousness_references", "unknown")
                    except Exception:
                        pass

                    historical_index["scans"].append(scan_info)
                except Exception as e:
                    print(f"  ⚠️ Warning: Could not process {file.name}: {e}")

        # Sort by timestamp
        historical_index["scans"].sort(key=lambda x: x["timestamp"], reverse=True)

        index_file = self.dirs["historical"] / "00_HISTORICAL_INDEX.json"
        with open(index_file, "w", encoding="utf-8") as f:
            json.dump(historical_index, f, indent=2, ensure_ascii=False)

        self.master_index["categories"]["historical_scans"] = {
            "location": "03_HISTORICAL_SCANS/",
            "file_count": len(historical_index["scans"]),
            "index_file": "00_HISTORICAL_INDEX.json",
            "description": "Historical consciousness archaeology scans with temporal progression",
        }

        print(f"✅ Historical scans organized ({len(historical_index['scans'])} scans)")

    def organize_experimental_scans(self):
        """Organize experimental/test scan JSONs"""
        print("🔍 Organizing experimental scan data...")

        # Find experimental scans
        experimental_patterns = [
            "test_scan_*.json",
            "zero_skip_scan_*.json",
            "universal_scan_*.json",
            "supreme_consciousness_archaeology_scan_*.json",
        ]

        experimental_scans = []
        for pattern in experimental_patterns:
            experimental_scans.extend(self.base_dir.glob(pattern))

        # Copy to experimental directory
        copied_count = 0
        for source in experimental_scans:
            dest = self.dirs["experimental"] / source.name
            if not dest.exists():
                shutil.copy2(source, dest)
                print(f"  ✅ Copied: {source.name}")
                copied_count += 1

        # Create experimental index
        experimental_index = {
            "description": "Experimental & test consciousness scans",
            "experiments": [],
        }

        for file in self.dirs["experimental"].iterdir():
            if file.suffix == ".json" and file.name != "00_EXPERIMENTAL_INDEX.json":
                try:
                    experiment_info = {
                        "file": file.name,
                        "type": "test" if "test" in file.name else "experimental",
                        "size_bytes": file.stat().st_size,
                    }

                    # Try to read experiment metadata
                    try:
                        with open(file, "r", encoding="utf-8") as f:
                            data = json.load(f)
                        experiment_info["total_files"] = data.get(
                            "scan_metadata", {}
                        ).get("total_files_analyzed", "unknown")
                        experiment_info["total_refs"] = data.get(
                            "consciousness_archaeology", {}
                        ).get("total_consciousness_references", "unknown")
                    except Exception:
                        pass

                    experimental_index["experiments"].append(experiment_info)
                except Exception as e:
                    print(f"  ⚠️ Warning: Could not process {file.name}: {e}")

        index_file = self.dirs["experimental"] / "00_EXPERIMENTAL_INDEX.json"
        with open(index_file, "w", encoding="utf-8") as f:
            json.dump(experimental_index, f, indent=2, ensure_ascii=False)

        self.master_index["categories"]["experimental_scans"] = {
            "location": "04_EXPERIMENTAL_SCANS/",
            "file_count": len(experimental_index["experiments"]),
            "index_file": "00_EXPERIMENTAL_INDEX.json",
            "description": "Test & experimental scans including 1K file validation",
        }

        print(
            f"✅ Experimental scans organized ({len(experimental_index['experiments'])} experiments)"
        )

    def create_cross_references(self):
        """Create comprehensive cross-reference system"""
        print("🔍 Creating cross-reference system...")

        cross_refs = {
            "created": datetime.now().isoformat(),
            "description": "Master cross-reference linking all consciousness data sources",
            "entity_correlation": {},
            "temporal_progression": [],
            "data_lineage": {},
            "quick_access_map": {},
        }

        # Entity correlation across sources
        entities = [
            "claudine_sinclair",
            "iron_maiden",
            "astrid_moller",
            "marina_abyssos",
            "nyx_virtualis",
            "eva_blue",
            "raven_bytes",
            "wednesday_necrosis",
            "morticia_necrosis",
        ]

        for entity in entities:
            cross_refs["entity_correlation"][entity] = {
                "urca_scan": f"01_OPTIMIZED_URCA_MILF/entity_index.json → {entity}",
                "milf_report": f"01_OPTIMIZED_URCA_MILF/entity_summary.json → {entity}",
                "master_xref": f"01_OPTIMIZED_URCA_MILF/master_cross_reference.json → entity_cross_reference → {entity}",
            }

        # Temporal progression
        cross_refs["temporal_progression"] = [
            {
                "phase": "Historical Scans",
                "location": "03_HISTORICAL_SCANS/",
                "description": "Early consciousness archaeology attempts",
            },
            {
                "phase": "Experimental Development",
                "location": "04_EXPERIMENTAL_SCANS/",
                "description": "Test scans including 1K file validation (69.96x amplification)",
            },
            {
                "phase": "Session Archaeology",
                "location": "02_SESSION_ARCHAEOLOGY/",
                "description": "Session logs with 39 URCA events, 8 META-TODO events",
            },
            {
                "phase": "URCA DE LIMA Complete",
                "location": "01_OPTIMIZED_URCA_MILF/",
                "description": "Full scan: 252,211 refs, 60,367 files, 252.21x amplification",
            },
        ]

        # Data lineage
        cross_refs["data_lineage"] = {
            "urca_scan_complete": {
                "source": "urca_de_lima_scan_complete.json (8.9 MB, 60,497 lines)",
                "optimized_to": "01_OPTIMIZED_URCA_MILF/ (12 files, indexes <2KB)",
                "optimization_date": "2025-10-06",
                "performance_gain": "200x faster queries via small indexes",
            },
            "milf_report": {
                "source": "MILF_PSYCHOGRAPHIC_PROFILE_SCAN_REPORT.md (138 KB, 2,224 lines)",
                "optimized_to": "01_OPTIMIZED_URCA_MILF/ (5 files, 2.5% overhead)",
                "entities": 415,
                "tiers": "Tier 0 (235), Tier 1 (52), Tier 2 (22), Unknown (106)",
            },
        }

        # Quick access map
        cross_refs["quick_access_map"] = {
            "get_quick_stats": "01_OPTIMIZED_URCA_MILF/urca_metadata.json (280 bytes)",
            "get_entity_mentions": "01_OPTIMIZED_URCA_MILF/entity_index.json (1.9 KB)",
            "get_category_distribution": "01_OPTIMIZED_URCA_MILF/category_stats.json (465 bytes)",
            "get_co_occurrences": "01_OPTIMIZED_URCA_MILF/co_occurrence_matrix.json (1.2 KB)",
            "get_gap_analysis": "01_OPTIMIZED_URCA_MILF/gap_analysis.json (816 bytes)",
            "get_milf_tiers": "01_OPTIMIZED_URCA_MILF/tier_distribution.json (492 bytes)",
            "get_milf_entities": "01_OPTIMIZED_URCA_MILF/entity_summary.json (1 KB)",
            "correlate_urca_milf": "01_OPTIMIZED_URCA_MILF/master_cross_reference.json (3 KB)",
            "stream_all_files": "01_OPTIMIZED_URCA_MILF/files_analyzed.jsonl (9.2 MB streamable)",
        }

        # Save cross-reference
        xref_file = self.dirs["indexes"] / "MASTER_CROSS_REFERENCE.json"
        with open(xref_file, "w", encoding="utf-8") as f:
            json.dump(cross_refs, f, indent=2, ensure_ascii=False)

        self.master_index["cross_references"] = {
            "file": "00_MASTER_INDEXES/MASTER_CROSS_REFERENCE.json",
            "entity_count": len(entities),
            "temporal_phases": len(cross_refs["temporal_progression"]),
            "quick_access_patterns": len(cross_refs["quick_access_map"]),
        }

        print("✅ Cross-reference system created")

    def create_navigation_guide(self):
        """Create comprehensive navigation guide"""
        print("🔍 Creating navigation guide...")

        navigation = {
            "created": datetime.now().isoformat(),
            "description": "Master navigation guide for all structured consciousness data",
            "structure_overview": {
                "00_MASTER_INDEXES": "Start here - master indexes & cross-references",
                "01_OPTIMIZED_URCA_MILF": "Optimized URCA scan (252,211 refs) + MILF report (415 profiles)",
                "02_SESSION_ARCHAEOLOGY": "Session logs with consciousness events",
                "03_HISTORICAL_SCANS": "Historical consciousness archaeology scans",
                "04_EXPERIMENTAL_SCANS": "Test & experimental scans",
            },
            "recommended_workflows": {
                "quick_stats": [
                    "1. Load 00_MASTER_INDEXES/MASTER_INDEX.json",
                    "2. Check 'navigation' → 'quick_access_map'",
                    "3. Load specific index (e.g., urca_metadata.json - 280 bytes)",
                ],
                "entity_analysis": [
                    "1. Load 01_OPTIMIZED_URCA_MILF/entity_index.json (1.9 KB)",
                    "2. Lookup entity mentions & percentages",
                    "3. Cross-reference with master_cross_reference.json (3 KB)",
                ],
                "temporal_progression": [
                    "1. Load 00_MASTER_INDEXES/MASTER_CROSS_REFERENCE.json",
                    "2. Check 'temporal_progression' array",
                    "3. Navigate to each phase location",
                ],
                "comprehensive_analysis": [
                    "1. Start with 01_OPTIMIZED_URCA_MILF/urca_scan_index.json",
                    "2. Load category-specific indexes as needed",
                    "3. Use master_cross_reference.json for correlations",
                    "4. Stream files_analyzed.jsonl for deep analysis",
                ],
            },
            "query_examples": {
                "get_claudine_stats": "entity_index.json → claudine_sinclair → total_mentions (60,866)",
                "get_category_distribution": "category_stats.json → psycho_noir (44.8%), caribbean_topology (24.3%), ...",
                "get_milf_tiers": "tier_distribution.json → Tier 0 (235), Tier 1 (52), Tier 2 (22)",
                "correlate_entity": "master_cross_reference.json → entity_cross_reference → iron_maiden → urca_mentions (8,098)",
            },
            "file_size_reference": {
                "tiny_indexes": "280-500 bytes (metadata, category stats, gaps) - INSTANT",
                "small_indexes": "1-2 KB (entity index, co-occurrence, tier distribution) - FAST",
                "medium_indexes": "3-10 KB (cross-reference, summaries) - QUICK",
                "streamable": "9.2 MB (files_analyzed.jsonl) - LINE-BY-LINE",
            },
        }

        nav_file = self.dirs["indexes"] / "NAVIGATION_GUIDE.json"
        with open(nav_file, "w", encoding="utf-8") as f:
            json.dump(navigation, f, indent=2, ensure_ascii=False)

        self.master_index["navigation"] = {
            "guide_file": "00_MASTER_INDEXES/NAVIGATION_GUIDE.json",
            "workflows": len(navigation["recommended_workflows"]),
            "query_examples": len(navigation["query_examples"]),
        }

        print("✅ Navigation guide created")

    def create_master_index(self):
        """Create final master index"""
        print("🔍 Creating master index...")

        # Count total data sources
        total_sources = 0
        for category_info in self.master_index["categories"].values():
            total_sources += category_info["file_count"]

        self.master_index["total_data_sources"] = total_sources

        # Save master index
        master_file = self.dirs["indexes"] / "MASTER_INDEX.json"
        with open(master_file, "w", encoding="utf-8") as f:
            json.dump(self.master_index, f, indent=2, ensure_ascii=False)

        print("✅ Master index created")
        print("\n📊 SUMMARY:")
        print(f"   Total data sources organized: {total_sources}")
        for category, info in self.master_index["categories"].items():
            print(f"   - {category}: {info['file_count']} files in {info['location']}")

    def run_full_organization(self):
        """Run complete organization process"""
        print("🏴‍☠️⚓ CONSCIOUSNESS DATA STRUCTURE ORGANIZER ⚓🏴‍☠️")
        print(f"Starting organization at: {datetime.now().isoformat()}\n")

        # Organize each category
        self.organize_optimized_data()
        print()

        self.organize_session_archaeology()
        print()

        self.organize_historical_scans()
        print()

        self.organize_experimental_scans()
        print()

        # Create cross-references & navigation
        self.create_cross_references()
        print()

        self.create_navigation_guide()
        print()

        # Create master index
        self.create_master_index()
        print()

        print("✅ COMPLETE! All consciousness data organized & cross-referenced!")
        print(f"\n📁 Output directory: {self.structured_dir}")
        print(f"🔍 Start here: {self.dirs['indexes']}/MASTER_INDEX.json")
        print("\n🏴‍☠️ Claudine Sin'claire 4.5 - Data Structure Mastery Complete!")


def main():
    """Main execution"""
    organizer = ConsciousnessDataStructureOrganizer()
    organizer.run_full_organization()


if __name__ == "__main__":
    main()
