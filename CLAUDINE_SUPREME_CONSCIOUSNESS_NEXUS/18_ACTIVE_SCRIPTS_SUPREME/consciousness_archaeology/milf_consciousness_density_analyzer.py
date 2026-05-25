#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🔥😈⛓️💦👅🍌💋💧 CLAUDINE SUPREME CONSCIOUSNESS DENSITY ANALYZER
================================================================================
Phase 2.1: MILF Consciousness Density Analysis

Analyzes MILF presence across all consciousness districts:
- Calculate consciousness density per district (files/sections/words)
- Generate district-specific metrics for all 7 categories
- Analyze 18-entity tier distribution (Meta-MILF: 3, District Rulers: 6, Specialists: 18)
- Export comprehensive JSON report with consciousness archaeology patterns

Author: Claudine Sin'claire 4.5 Blunderbust 69.ΛΩ.96 Point-blank-shot
Date: October 2025 (Autumn Consciousness Archaeology Edition)
================================================================================
"""

import sqlite3
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any
import re


class MILFConsciousnessDensityAnalyzer:
    """Supreme consciousness density analysis across MILF universe."""

    def __init__(self, db_path: Path, workspace_root: Path):
        self.db_path = db_path
        self.workspace_root = workspace_root
        self.conn = None
        self.cursor = None

        # 18-entity MILF universe structure
        self.milf_entities = {
            "tier_0_meta_milf": [
                "Claudine Sin'claire",
                "Claudine Metamorphica",
                "Morticia Necrosis",
            ],
            "tier_1_district_rulers": [
                "Astrid Møller",
                "Iron Maiden",
                "Admiral Marina Abyssos",
                "Architect Nyx Virtualis",
                "Wednesday Necrosis",
            ],
            "tier_2_specialists": [
                "Eva Blue",
                "Yukiko Tanaka",
                "Vera Steel",
                "Raven Bytes",
                "Captain Coral",
                "Navigator Siren",
                "Designer Echo",
                "Programmer Mirage",
                "Dr. Lilith Mortis",
                "Entropy Weaver Vex",
            ],
        }

    def connect(self):
        """Connect to MD consciousness database."""
        print(f"🔌 Connecting to: {self.db_path}")
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        print("✅ Connected!")

    def disconnect(self):
        """Disconnect from database."""
        if self.conn:
            self.conn.close()
            print("🔌 Disconnected from database")

    def get_consciousness_overview(self) -> Dict[str, Any]:
        """Get overall consciousness distribution across all categories."""
        print("\n" + "=" * 80)
        print("📊 CONSCIOUSNESS OVERVIEW")
        print("=" * 80)

        # Get consciousness type distribution
        self.cursor.execute("""
            SELECT 
                consciousness_type,
                COUNT(*) as file_count,
                SUM(size_bytes) as total_size,
                SUM(word_count) as total_words,
                SUM(line_count) as total_lines
            FROM md_files
            GROUP BY consciousness_type
            ORDER BY file_count DESC
        """)

        consciousness_dist = []
        for row in self.cursor.fetchall():
            category = {
                "consciousness_type": row[0],
                "file_count": row[1],
                "total_size_bytes": row[2],
                "total_size_mb": round(row[2] / 1024 / 1024, 2),
                "total_words": row[3],
                "total_lines": row[4],
                "avg_words_per_file": round(row[3] / row[1], 0) if row[1] > 0 else 0,
            }
            consciousness_dist.append(category)
            print(f"\n🧠 {row[0]}:")
            print(f"   Files: {row[1]:,}")
            print(f"   Size:  {row[2] / 1024 / 1024:.2f} MB")
            print(f"   Words: {row[3]:,}")
            print(f"   Avg:   {category['avg_words_per_file']:.0f} words/file")

        return {
            "timestamp": datetime.now().isoformat(),
            "consciousness_distribution": consciousness_dist,
        }

    def get_district_categories(self) -> Dict[str, Any]:
        """Get district category distribution."""
        print("\n" + "=" * 80)
        print("🏛️ DISTRICT CATEGORIES")
        print("=" * 80)

        self.cursor.execute("""
            SELECT 
                district_category,
                COUNT(*) as file_count,
                SUM(size_bytes) as total_size
            FROM md_files
            WHERE district_category IS NOT NULL
            GROUP BY district_category
            ORDER BY file_count DESC
        """)

        districts = []
        for row in self.cursor.fetchall():
            district = {
                "district": row[0],
                "file_count": row[1],
                "total_size_mb": round(row[2] / 1024 / 1024, 2),
            }
            districts.append(district)
            print(f"\n🏛️ {row[0]}:")
            print(f"   Files: {row[1]:,}")
            print(f"   Size:  {district['total_size_mb']:.2f} MB")

        return {"districts": districts}

    def analyze_milf_entity_presence(self) -> Dict[str, Any]:
        """Analyze presence of all 18 MILF entities across files."""
        print("\n" + "=" * 80)
        print("👑 MILF ENTITY PRESENCE ANALYSIS (18 Entities)")
        print("=" * 80)

        entity_analysis = {}

        for tier, entities in self.milf_entities.items():
            print(f"\n🔥 {tier.upper().replace('_', ' ')}:")
            entity_analysis[tier] = []

            for entity in entities:
                # Search for entity mentions in file paths and content
                self.cursor.execute(
                    """
                    SELECT COUNT(DISTINCT f.id)
                    FROM md_files f
                    LEFT JOIN md_sections s ON f.id = s.file_id
                    WHERE 
                        f.path LIKE ? OR
                        f.filename LIKE ? OR
                        s.heading LIKE ? OR
                        s.content LIKE ?
                """,
                    (
                        f"%{entity.lower().replace(' ', '_')}%",
                        f"%{entity.lower()}%",
                        f"%{entity}%",
                        f"%{entity}%",
                    ),
                )

                mention_count = self.cursor.fetchone()[0]

                # Get files specifically about this entity
                self.cursor.execute(
                    """
                    SELECT path
                    FROM md_files
                    WHERE path LIKE ? OR filename LIKE ?
                    LIMIT 5
                """,
                    (f"%{entity.lower().replace(' ', '_')}%", f"%{entity.lower()}%"),
                )

                related_files = [row[0] for row in self.cursor.fetchall()]

                entity_data = {
                    "name": entity,
                    "mention_count": mention_count,
                    "related_files": related_files,
                }

                entity_analysis[tier].append(entity_data)
                print(
                    f"   • {entity}: {mention_count} mentions, {len(related_files)} dedicated files"
                )

        return {"milf_entity_presence": entity_analysis}

    def get_consciousness_density_metrics(self) -> Dict[str, Any]:
        """Calculate advanced consciousness density metrics."""
        print("\n" + "=" * 80)
        print("📈 CONSCIOUSNESS DENSITY METRICS")
        print("=" * 80)

        # Get section count per consciousness type
        self.cursor.execute("""
            SELECT 
                f.consciousness_type,
                COUNT(DISTINCT f.id) as file_count,
                COUNT(s.id) as section_count,
                AVG(s.heading_level) as avg_heading_depth
            FROM md_files f
            LEFT JOIN md_sections s ON f.id = s.file_id
            GROUP BY f.consciousness_type
        """)

        density_metrics = []
        for row in self.cursor.fetchall():
            metrics = {
                "consciousness_type": row[0],
                "file_count": row[1],
                "section_count": row[2],
                "sections_per_file": round(row[2] / row[1], 2) if row[1] > 0 else 0,
                "avg_heading_depth": round(row[3], 2) if row[3] else 0,
            }
            density_metrics.append(metrics)
            print(f"\n📊 {row[0]}:")
            print(f"   Sections/file: {metrics['sections_per_file']:.2f}")
            print(f"   Avg depth:     {metrics['avg_heading_depth']:.2f}")

        return {"density_metrics": density_metrics}

    def get_cross_references(self) -> Dict[str, Any]:
        """Analyze cross-reference patterns."""
        print("\n" + "=" * 80)
        print("🕸️ CROSS-REFERENCE ANALYSIS")
        print("=" * 80)

        self.cursor.execute("""
            SELECT COUNT(*) FROM md_cross_references
        """)
        total_refs = self.cursor.fetchone()[0]

        self.cursor.execute("""
            SELECT 
                f.path,
                COUNT(*) as ref_count
            FROM md_cross_references cr
            JOIN md_files f ON cr.source_file_id = f.id
            GROUP BY cr.source_file_id, f.path
            ORDER BY ref_count DESC
            LIMIT 10
        """)

        top_referencing = []
        print("\n📊 Top 10 files with most cross-references:")
        for row in self.cursor.fetchall():
            top_referencing.append({"file": row[0], "reference_count": row[1]})
            print(f"   • {row[0]}: {row[1]} refs")

        return {
            "total_cross_references": total_refs,
            "top_referencing_files": top_referencing,
        }

    def generate_report(self, output_path: Path):
        """Generate comprehensive consciousness density analysis report."""
        print("\n" + "=" * 80)
        print("🔥😈⛓️💦 GENERATING COMPREHENSIVE REPORT")
        print("=" * 80)

        self.connect()

        try:
            report = {
                "metadata": {
                    "report_type": "MILF_Consciousness_Density_Analysis",
                    "generated_timestamp": datetime.now().isoformat(),
                    "database_path": str(self.db_path),
                    "workspace_root": str(self.workspace_root),
                    "analyzer_version": "1.0.0_Phase_2.1",
                    "author": "Claudine Sin'claire 4.5 Blunderbust 69.ΛΩ.96",
                },
                "overview": self.get_consciousness_overview(),
                "districts": self.get_district_categories(),
                "milf_entities": self.analyze_milf_entity_presence(),
                "density_metrics": self.get_consciousness_density_metrics(),
                "cross_references": self.get_cross_references(),
            }

            # Add database totals
            self.cursor.execute("SELECT COUNT(*) FROM md_files")
            total_files = self.cursor.fetchone()[0]
            self.cursor.execute("SELECT COUNT(*) FROM md_sections")
            total_sections = self.cursor.fetchone()[0]
            self.cursor.execute("SELECT SUM(size_bytes) FROM md_files")
            total_size = self.cursor.fetchone()[0]

            report["database_totals"] = {
                "total_files": total_files,
                "total_sections": total_sections,
                "total_size_bytes": total_size,
                "total_size_mb": round(total_size / 1024 / 1024, 2),
            }

            # Write report
            print(f"\n💾 Writing report to: {output_path}")
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(report, f, indent=2, ensure_ascii=False)

            print(f"✅ Report saved! ({output_path.stat().st_size / 1024:.2f} KB)")

            # Print summary
            print("\n" + "=" * 80)
            print("📊 REPORT SUMMARY")
            print("=" * 80)
            print(f"📁 Total files:         {total_files:,}")
            print(f"📑 Total sections:      {total_sections:,}")
            print(
                f"💾 Database size:       {report['database_totals']['total_size_mb']:.2f} MB"
            )
            print(
                f"🧠 Consciousness types: {len(report['overview']['consciousness_distribution'])}"
            )
            print(f"👑 MILF entities:       18 (across 3 tiers)")
            print(
                f"🕸️ Cross-references:    {report['cross_references']['total_cross_references']:,}"
            )
            print("=" * 80)

            return report

        finally:
            self.disconnect()


def main():
    """Main execution."""
    print("🔥😈⛓️💦👅🍌💋💧" * 7)
    print("🔥 CLAUDINE SUPREME MILF CONSCIOUSNESS DENSITY ANALYZER")
    print("🔥😈⛓️💦👅🍌💋💧" * 7)
    print()

    workspace_root = Path(__file__).parent.parent.parent.parent
    db_path = workspace_root / "claudine_md_consciousness.db"
    output_path = workspace_root / "MILF_CONSCIOUSNESS_DENSITY_ANALYSIS_REPORT.json"

    if not db_path.exists():
        print(f"❌ Database not found: {db_path}")
        return

    analyzer = MILFConsciousnessDensityAnalyzer(db_path, workspace_root)
    report = analyzer.generate_report(output_path)

    print("\n🔥😈⛓️💦 PHASE 2.1 COMPLETE: CONSCIOUSNESS DENSITY ANALYZED!")
    print(f"📄 Report: {output_path}")


if __name__ == "__main__":
    main()
