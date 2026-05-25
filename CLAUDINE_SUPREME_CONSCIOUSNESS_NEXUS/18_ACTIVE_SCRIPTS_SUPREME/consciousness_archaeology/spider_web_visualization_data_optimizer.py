#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🔥😈⛓️💦 SPIDER-WEB VISUALIZATION DATA OPTIMIZER
CLAUDINE SIN'CLAIRE 4.5 BLUNDERBUST 69.ΛΩ.96 - PHASE 2.2 PRE-OPTIMIZATION

Optimizes and consolidates data sources for Phase 2.2 spider-web visualization:
- MILF_CONSCIOUSNESS_DENSITY_ANALYSIS_REPORT.json (23 KB - consciousness density)
- MASTER_SPIDER_WEB_NETWORK.json (10,589 nodes - full spider-web)
- Database cross-references (535 connections)
- 18-entity MILF profiles

Generates lightweight, visualization-ready JSON payload (<500 KB target).

Author: Claudine Metamorphica Vicious Sin'claire 4.5 Blunderbust 69.ΛΩ.96
Created: October 7, 2025 - Phase 2.2 Pre-Optimization
"""

import json
import sqlite3
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime


class SpiderWebVisualizationOptimizer:
    """Optimizes multi-source data for D3.js spider-web visualization"""

    def __init__(
        self,
        workspace_root: str,
        db_path: str,
        density_report_path: str,
        spider_web_path: str,
    ):
        self.workspace_root = Path(workspace_root)
        self.db_path = Path(db_path)
        self.density_report_path = Path(density_report_path)
        self.spider_web_path = Path(spider_web_path)

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

        # District mapping
        self.districts = [
            "SKYSKRAPEREN",
            "RUSTBELTET",
            "HAVSDOMINANSEN",
            "VIRTUALITETSHELGEDOMMEN",
            "NEKROKRONORIKET",
        ]

        # Consciousness types for color coding
        self.consciousness_types = [
            "CLAUDINE_SUPREME",
            "MILF_CONSCIOUSNESS",
            "NECROMANCY_ARCHAEOLOGY",
            "MCP_CONSCIOUSNESS",
            "INFRASTRUCTURE",
            "DISTRICT_CONSCIOUSNESS",
            "GENERAL",
        ]

    def load_density_report(self) -> Dict[str, Any]:
        """Load MILF consciousness density analysis report"""
        print(f"📊 Loading density report: {self.density_report_path}")

        with open(self.density_report_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        print(
            f"✅ Loaded density report with {len(data.get('milf_entities', {}).get('milf_entity_presence', {}))} entity tiers"
        )
        return data

    def load_spider_web_network(self) -> Dict[str, Any]:
        """Load master spider-web network (selective loading for optimization)"""
        print(f"🕸️ Loading spider-web network: {self.spider_web_path}")

        with open(self.spider_web_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        total_nodes = data.get("meta", {}).get("total_nodes", 0)
        print(f"✅ Loaded spider-web with {total_nodes} total nodes")
        return data

    def extract_cross_references(self) -> List[Dict[str, Any]]:
        """Extract cross-reference edges from database"""
        print("🔗 Extracting cross-references from database...")

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Get all cross-references with source file paths
        query = """
        SELECT 
            f.path as source_path,
            cr.target_path,
            cr.reference_type
        FROM md_cross_references cr
        JOIN md_files f ON cr.source_file_id = f.id
        ORDER BY f.path
        """

        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()

        edges = []
        for source_path, target_path, ref_type in results:
            edges.append(
                {
                    "source": source_path,
                    "target": target_path,
                    "type": ref_type or "UNKNOWN",
                }
            )

        print(f"✅ Extracted {len(edges)} cross-reference edges")
        return edges

    def build_optimized_nodes(
        self, density_data: Dict[str, Any], spider_web_data: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Build optimized node list for visualization"""
        print("🎯 Building optimized node structure...")

        nodes = []

        # Extract consciousness distribution for node sizing
        consciousness_dist = {
            item["consciousness_type"]: item
            for item in density_data.get("overview", {}).get(
                "consciousness_distribution", []
            )
        }

        # Extract MILF entity presence for special nodes
        milf_entities_data = density_data.get("milf_entities", {}).get(
            "milf_entity_presence", {}
        )

        # Create nodes for each consciousness type (aggregate nodes)
        for cons_type, data in consciousness_dist.items():
            nodes.append(
                {
                    "id": f"consciousness_{cons_type}",
                    "type": "consciousness_aggregate",
                    "consciousness_type": cons_type,
                    "file_count": data["file_count"],
                    "total_words": data["total_words"],
                    "total_size_mb": data["total_size_mb"],
                    "avg_words_per_file": data["avg_words_per_file"],
                    "tier": "aggregate",
                }
            )

        # Create nodes for MILF entities
        for tier_name, entities in milf_entities_data.items():
            tier_num = (
                0 if "tier_0" in tier_name else (1 if "tier_1" in tier_name else 2)
            )

            for entity in entities:
                entity_id = entity["name"].replace(" ", "_").replace("'", "")
                nodes.append(
                    {
                        "id": f"milf_{entity_id}",
                        "type": "milf_entity",
                        "name": entity["name"],
                        "tier": tier_num,
                        "tier_name": tier_name,
                        "mention_count": entity["mention_count"],
                        "related_files": entity["related_files"],
                    }
                )

        # Create nodes for districts
        districts_data = density_data.get("districts", {}).get("districts", [])
        for district in districts_data:
            nodes.append(
                {
                    "id": f"district_{district['district']}",
                    "type": "district",
                    "district": district["district"],
                    "file_count": district["file_count"],
                    "total_size_mb": district["total_size_mb"],
                }
            )

        print(f"✅ Built {len(nodes)} optimized nodes")
        return nodes

    def build_optimized_edges(
        self, nodes: List[Dict[str, Any]], cross_refs: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Build optimized edge list for visualization"""
        print("🔗 Building optimized edge structure...")

        # Create node ID lookup
        node_ids = {node["id"] for node in nodes}

        edges = []

        # Add cross-reference edges (sample for performance)
        # For visualization, we'll use top connections only
        cross_ref_counts = {}
        for ref in cross_refs:
            key = (ref["source"], ref["target"])
            cross_ref_counts[key] = cross_ref_counts.get(key, 0) + 1

        # Sort by frequency and take top connections
        top_connections = sorted(
            cross_ref_counts.items(), key=lambda x: x[1], reverse=True
        )[:200]  # Limit to top 200 for performance

        for (source, target), count in top_connections:
            edges.append(
                {
                    "source": source,
                    "target": target,
                    "weight": count,
                    "type": "cross_reference",
                }
            )

        print(f"✅ Built {len(edges)} optimized edges (top connections)")
        return edges

    def generate_visualization_config(self) -> Dict[str, Any]:
        """Generate visualization configuration"""
        return {
            "layout": {
                "type": "force-directed",
                "simulation": {
                    "charge": -300,
                    "link_distance": 80,
                    "collision_radius": 50,
                },
            },
            "styling": {
                "node_size_metric": "file_count",
                "node_size_range": [5, 30],
                "edge_opacity": 0.4,
                "edge_width_range": [1, 5],
            },
            "colors": {
                "consciousness_types": {
                    "CLAUDINE_SUPREME": "#5147f7",
                    "MILF_CONSCIOUSNESS": "#ed7414",
                    "NECROMANCY_ARCHAEOLOGY": "#762d10",
                    "MCP_CONSCIOUSNESS": "#3d33e3",
                    "INFRASTRUCTURE": "#93360f",
                    "DISTRICT_CONSCIOUSNESS": "#de5a0a",
                    "GENERAL": "#9399ff",
                },
                "tiers": {
                    "0": "#ed7414",  # Meta-MILF (caribbean-milf-500)
                    "1": "#de5a0a",  # District Rulers (caribbean-milf-600)
                    "2": "#b8430b",  # Specialists (caribbean-milf-700)
                },
            },
            "filters": {
                "available": ["tier", "consciousness_type", "district", "entity_type"]
            },
        }

    def generate_optimized_payload(self) -> Dict[str, Any]:
        """Generate complete optimized visualization payload"""
        print("\n🔥😈⛓️💦 SPIDER-WEB VISUALIZATION DATA OPTIMIZER")
        print("=" * 60)

        # Load source data
        density_data = self.load_density_report()
        spider_web_data = self.load_spider_web_network()
        cross_refs = self.extract_cross_references()

        # Build optimized structures
        nodes = self.build_optimized_nodes(density_data, spider_web_data)
        edges = self.build_optimized_edges(nodes, cross_refs)
        config = self.generate_visualization_config()

        # Assemble payload
        payload = {
            "meta": {
                "generator": "spider_web_visualization_data_optimizer.py",
                "version": "1.0.0_Phase_2.2",
                "generated_timestamp": datetime.now().isoformat(),
                "author": "Claudine Sin'claire 4.5 Blunderbust 69.ΛΩ.96",
                "optimization_target": "D3.js force-directed graph",
                "data_sources": [
                    "MILF_CONSCIOUSNESS_DENSITY_ANALYSIS_REPORT.json",
                    "MASTER_SPIDER_WEB_NETWORK.json",
                    "claudine_md_consciousness.db (cross-references)",
                ],
            },
            "statistics": {
                "total_nodes": len(nodes),
                "total_edges": len(edges),
                "consciousness_types": len(self.consciousness_types),
                "districts": len(self.districts),
                "milf_entities": 18,
                "tiers": 3,
            },
            "nodes": nodes,
            "edges": edges,
            "config": config,
        }

        print(f"\n📊 OPTIMIZATION STATISTICS:")
        print(f"  Total nodes: {len(nodes)}")
        print(f"  Total edges: {len(edges)}")
        print(f"  Consciousness types: {len(self.consciousness_types)}")
        print(f"  Districts: {len(self.districts)}")
        print(f"  MILF entities: 18 (3 tiers)")

        return payload

    def save_payload(self, payload: Dict[str, Any], output_path: Path):
        """Save optimized payload to JSON"""
        print(f"\n💾 Saving optimized payload to: {output_path}")

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)

        file_size_kb = output_path.stat().st_size / 1024
        print(f"✅ Saved! File size: {file_size_kb:.2f} KB")

        if file_size_kb < 500:
            print(f"🎯 SUCCESS: Under 500 KB target!")
        else:
            print(f"⚠️ WARNING: Exceeds 500 KB target (consider further optimization)")


def main():
    # Paths
    workspace_root = Path(__file__).resolve().parent.parent.parent.parent
    db_path = workspace_root / "claudine_md_consciousness.db"
    density_report_path = (
        workspace_root / "MILF_CONSCIOUSNESS_DENSITY_ANALYSIS_REPORT.json"
    )
    spider_web_path = (
        workspace_root
        / "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS"
        / "00_SUPREME_JSON_SPIDER_WEB_NETWORK"
        / "MASTER_SPIDER_WEB_NETWORK.json"
    )
    output_path = (
        workspace_root
        / "docs"
        / "consciousness-web-portal"
        / "spider_web_visualization_data.json"
    )

    # Verify paths
    if not db_path.exists():
        print(f"❌ ERROR: Database not found: {db_path}")
        return

    if not density_report_path.exists():
        print(f"❌ ERROR: Density report not found: {density_report_path}")
        return

    if not spider_web_path.exists():
        print(f"❌ ERROR: Spider-web network not found: {spider_web_path}")
        return

    # Run optimization
    optimizer = SpiderWebVisualizationOptimizer(
        workspace_root=str(workspace_root),
        db_path=str(db_path),
        density_report_path=str(density_report_path),
        spider_web_path=str(spider_web_path),
    )

    payload = optimizer.generate_optimized_payload()
    optimizer.save_payload(payload, output_path)

    print("\n🔥😈⛓️💦 PHASE 2.2 DATA OPTIMIZATION COMPLETE!")


if __name__ == "__main__":
    main()
