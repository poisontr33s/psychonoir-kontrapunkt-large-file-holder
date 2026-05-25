#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🏴‍☠️⚓ NEXUS CONSCIOUSNESS SPIDER WEB ORCHESTRATOR ⚓🏴‍☠️

Orchestrates CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS as a spider web/information network:
- Extracts ALL .md files from NEXUS to structured JSON
- Creates cross-reference spider web linking all consciousness components
- Integrates with STRUCTURED_CONSCIOUSNESS_DATA/
- Enables COMPLETE information network navigation

Claudine Sin'claire 4.5 - October 6, 2025
"""

import json
from pathlib import Path
from typing import Dict, List
from datetime import datetime
import hashlib


class NexusConsciousnessSpiderWebOrchestrator:
    """Orchestrates NEXUS as a spider web information network"""

    def __init__(self, nexus_dir: str = "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS"):
        self.nexus_dir = Path(nexus_dir)
        self.structured_dir = Path(nexus_dir)  # NEXUS IS my codebase!
        self.output_dir = self.structured_dir / "05_NEXUS_SPIDER_WEB"
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Spider web nodes (all consciousness components)
        self.nodes: Dict[str, Dict] = {}  # md_file → node_data
        self.edges: List[Dict] = []  # connections between nodes
        self.entity_web: Dict[str, List[str]] = {}  # entity → [connected_nodes]
        self.district_web: Dict[str, List[str]] = {}  # district → [nodes]
        self.tier_web: Dict[str, List[str]] = {}  # tier → [nodes]

    def scan_nexus_architecture(self):
        """Scan entire NEXUS directory structure"""
        print("🕸️ Scanning NEXUS architecture...")

        md_files = list(self.nexus_dir.rglob("*.md"))
        print(f"  Found {len(md_files)} .md files")

        for md_file in md_files:
            self.extract_node(md_file)

        print(f"✅ Extracted {len(self.nodes)} consciousness nodes")

    def extract_node(self, md_file: Path):
        """Extract a single consciousness node"""
        try:
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()

            # Create node
            relative_path = md_file.relative_to(self.nexus_dir)
            node_id = self.generate_node_id(relative_path)

            node = {
                "id": node_id,
                "file": str(relative_path),
                "full_path": str(md_file),
                "tier": self.extract_tier(relative_path),
                "district": self.extract_district(relative_path),
                "category": self.extract_category(relative_path),
                "size_bytes": md_file.stat().st_size,
                "line_count": len(content.split("\n")),
                "entities": self.extract_entities(content),
                "references": self.extract_references(content),
                "consciousness_keywords": self.extract_consciousness_keywords(content),
            }

            self.nodes[node_id] = node

            # Build webs
            self.build_entity_web(node)
            self.build_district_web(node)
            self.build_tier_web(node)

        except Exception as e:
            print(f"  ⚠️ Warning: Could not extract {md_file.name}: {e}")

    def generate_node_id(self, relative_path: Path) -> str:
        """Generate unique node ID from path"""
        path_str = str(relative_path).replace("\\", "/")
        return hashlib.md5(path_str.encode()).hexdigest()[:12]

    def extract_tier(self, relative_path: Path) -> str:
        """Extract tier from path"""
        path_str = str(relative_path)
        if "01_SUPREME_MATRIARCH_COMMAND" in path_str:
            return "TIER_1_SUPREME_MATRIARCH"
        elif "02_DISTRICT_DOMINION_MATRIX" in path_str:
            return "TIER_2_DISTRICT_DOMINION"
        elif "03_SPECIALIZED_CONSCIOUSNESS_OPERATIVES" in path_str:
            return "TIER_3_SPECIALISTS"
        elif "04_CONSCIOUSNESS_ARCHAEOLOGICAL_ARCHIVES" in path_str:
            return "TIER_4_ARCHIVES"
        elif "05_STRATEGIC_INTELLIGENCE_ARCHIVES" in path_str:
            return "TIER_5_INTELLIGENCE"
        elif (
            "06_CONSCIOUSNESS_NEXUS_ADMINISTRATION" in path_str or "TIER_6" in path_str
        ):
            return "TIER_6_ADMINISTRATION"
        else:
            return "UNKNOWN_TIER"

    def extract_district(self, relative_path: Path) -> str:
        """Extract district from path"""
        path_str = str(relative_path).upper()

        districts = [
            "SKYSKRAPEREN",
            "RUSTBELTET",
            "HAVSDOMINANSEN",
            "VIRTUALITETSHELGEDOMMEN",
            "NEKROKRONORIKET",
            "FOYDALITETSDUALITETSLENKEN",
        ]

        for district in districts:
            if district in path_str:
                return district

        return "NO_DISTRICT"

    def extract_category(self, relative_path: Path) -> str:
        """Extract category from path"""
        path_str = str(relative_path)

        if "CONSCIOUSNESS_PATHWAYS" in path_str:
            return "CONSCIOUSNESS_PATHWAYS"
        elif "STATE_MANAGEMENT" in path_str:
            return "STATE_MANAGEMENT"
        elif "SPECIALISTS" in path_str:
            return "SPECIALISTS"
        elif "ARCHAEOLOGICAL_ARCHIVES" in path_str:
            return "ARCHIVES"
        elif "STRATEGIC_INTELLIGENCE" in path_str:
            return "INTELLIGENCE"
        elif "NEXUS_ADMINISTRATION" in path_str:
            return "ADMINISTRATION"
        elif "profile" in path_str.lower():
            return "PROFILE"
        else:
            return "GENERAL"

    def extract_entities(self, content: str) -> List[str]:
        """Extract entity mentions from content"""
        entities = [
            "claudine_sinclair",
            "claudine_metamorphica",
            "iron_maiden",
            "astrid_moller",
            "marina_abyssos",
            "admiral_marina",
            "nyx_virtualis",
            "architect_nyx",
            "eva_blue",
            "raven_bytes",
            "wednesday_necrosis",
            "morticia_necrosis",
            "kompilerings_spokelse",
        ]

        found_entities = []
        content_lower = content.lower()

        for entity in entities:
            if (
                entity.replace("_", " ") in content_lower
                or entity.replace("_", "-") in content_lower
            ):
                found_entities.append(entity)

        return list(set(found_entities))

    def extract_references(self, content: str) -> List[str]:
        """Extract file references from content"""
        references = []

        # Look for markdown links [text](file.md)
        import re

        md_links = re.findall(r"\[([^\]]+)\]\(([^\)]+\.md)\)", content)
        for text, link in md_links:
            references.append(link)

        # Look for file paths
        file_paths = re.findall(r"`([^`]+\.md)`", content)
        references.extend(file_paths)

        return list(set(references))

    def extract_consciousness_keywords(self, content: str) -> List[str]:
        """Extract consciousness-related keywords"""
        keywords = [
            "consciousness",
            "amplification",
            "matriarch",
            "district",
            "tier",
            "milf",
            "caribbean",
            "psycho-noir",
            "nsfw",
            "necromancy",
            "archaeology",
            "temporal",
            "bidirectional",
            "sophistication",
        ]

        found_keywords = []
        content_lower = content.lower()

        for keyword in keywords:
            if keyword in content_lower:
                found_keywords.append(keyword)

        return found_keywords

    def build_entity_web(self, node: Dict):
        """Build entity connection web"""
        for entity in node["entities"]:
            if entity not in self.entity_web:
                self.entity_web[entity] = []
            self.entity_web[entity].append(node["id"])

    def build_district_web(self, node: Dict):
        """Build district connection web"""
        district = node["district"]
        if district not in self.district_web:
            self.district_web[district] = []
        self.district_web[district].append(node["id"])

    def build_tier_web(self, node: Dict):
        """Build tier connection web"""
        tier = node["tier"]
        if tier not in self.tier_web:
            self.tier_web[tier] = []
        self.tier_web[tier].append(node["id"])

    def create_spider_web_edges(self):
        """Create edges between nodes based on references"""
        print("🕸️ Creating spider web edges...")

        edge_count = 0
        for node_id, node in self.nodes.items():
            for reference in node["references"]:
                # Find target node
                for target_id, target_node in self.nodes.items():
                    if reference in target_node["file"]:
                        edge = {
                            "from": node_id,
                            "to": target_id,
                            "type": "FILE_REFERENCE",
                            "weight": 1.0,
                        }
                        self.edges.append(edge)
                        edge_count += 1

            # Create edges for shared entities
            for entity in node["entities"]:
                for other_id, other_node in self.nodes.items():
                    if other_id != node_id and entity in other_node["entities"]:
                        edge = {
                            "from": node_id,
                            "to": other_id,
                            "type": "SHARED_ENTITY",
                            "entity": entity,
                            "weight": 0.5,
                        }
                        self.edges.append(edge)
                        edge_count += 1

        print(f"✅ Created {edge_count} spider web edges")

    def generate_spider_web_json(self):
        """Generate complete spider web JSON"""
        print("🕸️ Generating spider web JSON...")

        spider_web = {
            "created": datetime.now().isoformat(),
            "version": "1.0.0",
            "description": "NEXUS consciousness spider web - complete information network",
            "statistics": {
                "total_nodes": len(self.nodes),
                "total_edges": len(self.edges),
                "entities_tracked": len(self.entity_web),
                "districts": len(self.district_web),
                "tiers": len(self.tier_web),
            },
            "nodes": self.nodes,
            "edges": self.edges,
            "webs": {
                "entity_web": self.entity_web,
                "district_web": self.district_web,
                "tier_web": self.tier_web,
            },
        }

        output_file = self.output_dir / "NEXUS_SPIDER_WEB_COMPLETE.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(spider_web, f, indent=2, ensure_ascii=False)

        print(f"✅ Spider web JSON generated: {output_file}")
        return spider_web

    def generate_navigation_indexes(self):
        """Generate quick navigation indexes"""
        print("🕸️ Generating navigation indexes...")

        # Entity index
        entity_index = {
            "description": "Quick entity lookup - which nodes mention each entity",
            "entities": {},
        }

        for entity, node_ids in self.entity_web.items():
            entity_index["entities"][entity] = {
                "node_count": len(node_ids),
                "nodes": [
                    {
                        "id": node_id,
                        "file": self.nodes[node_id]["file"],
                        "district": self.nodes[node_id]["district"],
                        "tier": self.nodes[node_id]["tier"],
                    }
                    for node_id in node_ids
                ],
            }

        entity_file = self.output_dir / "NEXUS_ENTITY_INDEX.json"
        with open(entity_file, "w", encoding="utf-8") as f:
            json.dump(entity_index, f, indent=2, ensure_ascii=False)

        # District index
        district_index = {
            "description": "Quick district lookup - all nodes per district",
            "districts": {},
        }

        for district, node_ids in self.district_web.items():
            district_index["districts"][district] = {
                "node_count": len(node_ids),
                "total_size_bytes": sum(
                    self.nodes[nid]["size_bytes"] for nid in node_ids
                ),
                "nodes": [
                    {
                        "id": node_id,
                        "file": self.nodes[node_id]["file"],
                        "category": self.nodes[node_id]["category"],
                        "size_bytes": self.nodes[node_id]["size_bytes"],
                    }
                    for node_id in node_ids
                ],
            }

        district_file = self.output_dir / "NEXUS_DISTRICT_INDEX.json"
        with open(district_file, "w", encoding="utf-8") as f:
            json.dump(district_index, f, indent=2, ensure_ascii=False)

        # Tier index
        tier_index = {
            "description": "Quick tier lookup - all nodes per tier",
            "tiers": {},
        }

        for tier, node_ids in self.tier_web.items():
            tier_index["tiers"][tier] = {
                "node_count": len(node_ids),
                "nodes": [
                    {
                        "id": node_id,
                        "file": self.nodes[node_id]["file"],
                        "district": self.nodes[node_id]["district"],
                        "category": self.nodes[node_id]["category"],
                    }
                    for node_id in node_ids
                ],
            }

        tier_file = self.output_dir / "NEXUS_TIER_INDEX.json"
        with open(tier_file, "w", encoding="utf-8") as f:
            json.dump(tier_index, f, indent=2, ensure_ascii=False)

        print("✅ Navigation indexes generated")

    def integrate_with_structured_data(self):
        """Integrate NEXUS spider web with STRUCTURED_CONSCIOUSNESS_DATA"""
        print("🕸️ Integrating with STRUCTURED_CONSCIOUSNESS_DATA...")

        # Update master index
        master_index_file = (
            self.structured_dir / "00_MASTER_INDEXES" / "MASTER_INDEX.json"
        )

        if master_index_file.exists():
            with open(master_index_file, "r", encoding="utf-8") as f:
                master_index = json.load(f)
        else:
            master_index = {"categories": {}}

        # Add NEXUS category
        master_index["categories"]["nexus_spider_web"] = {
            "location": "05_NEXUS_SPIDER_WEB/",
            "file_count": len(self.nodes),
            "index_file": "NEXUS_MASTER_INDEX.json",
            "description": "NEXUS consciousness spider web with complete information network",
            "key_files": [
                "NEXUS_SPIDER_WEB_COMPLETE.json",
                "NEXUS_ENTITY_INDEX.json",
                "NEXUS_DISTRICT_INDEX.json",
                "NEXUS_TIER_INDEX.json",
            ],
        }

        master_index["total_data_sources"] = sum(
            cat["file_count"] for cat in master_index["categories"].values()
        )

        with open(master_index_file, "w", encoding="utf-8") as f:
            json.dump(master_index, f, indent=2, ensure_ascii=False)

        print("✅ Master index updated")

    def create_nexus_master_index(self):
        """Create NEXUS master index"""
        print("🕸️ Creating NEXUS master index...")

        master_index = {
            "created": datetime.now().isoformat(),
            "version": "1.0.0",
            "description": "Master index for NEXUS consciousness spider web",
            "quick_stats": {
                "total_nodes": len(self.nodes),
                "total_edges": len(self.edges),
                "entities": len(self.entity_web),
                "districts": len(self.district_web),
                "tiers": len(self.tier_web),
            },
            "files": {
                "complete_spider_web": "NEXUS_SPIDER_WEB_COMPLETE.json",
                "entity_index": "NEXUS_ENTITY_INDEX.json",
                "district_index": "NEXUS_DISTRICT_INDEX.json",
                "tier_index": "NEXUS_TIER_INDEX.json",
            },
            "navigation": {
                "find_entity": "Load NEXUS_ENTITY_INDEX.json → entities → [entity_name]",
                "find_district_nodes": "Load NEXUS_DISTRICT_INDEX.json → districts → [district_name]",
                "find_tier_nodes": "Load NEXUS_TIER_INDEX.json → tiers → [tier_name]",
                "explore_connections": "Load NEXUS_SPIDER_WEB_COMPLETE.json → edges → filter by node_id",
            },
            "query_examples": {
                "get_claudine_nodes": "NEXUS_ENTITY_INDEX.json → entities → claudine_sinclair → nodes",
                "get_skyskraperen_files": "NEXUS_DISTRICT_INDEX.json → districts → SKYSKRAPEREN → nodes",
                "get_tier1_supreme": "NEXUS_TIER_INDEX.json → tiers → TIER_1_SUPREME_MATRIARCH → nodes",
            },
        }

        master_file = self.output_dir / "NEXUS_MASTER_INDEX.json"
        with open(master_file, "w", encoding="utf-8") as f:
            json.dump(master_index, f, indent=2, ensure_ascii=False)

        print("✅ NEXUS master index created")

    def run_full_orchestration(self):
        """Run complete NEXUS spider web orchestration"""
        print("🏴‍☠️⚓ NEXUS CONSCIOUSNESS SPIDER WEB ORCHESTRATOR ⚓🏴‍☠️")
        print(f"Starting orchestration at: {datetime.now().isoformat()}\n")

        # Scan NEXUS
        self.scan_nexus_architecture()
        print()

        # Create spider web edges
        self.create_spider_web_edges()
        print()

        # Generate spider web JSON
        self.generate_spider_web_json()
        print()

        # Generate navigation indexes
        self.generate_navigation_indexes()
        print()

        # Create NEXUS master index
        self.create_nexus_master_index()
        print()

        # Integrate with structured data
        self.integrate_with_structured_data()
        print()

        print("✅ COMPLETE! NEXUS spider web orchestrated & integrated!")
        print(f"\n📁 Output directory: {self.output_dir}")
        print(f"🕸️ Total nodes: {len(self.nodes)}")
        print(f"🔗 Total edges: {len(self.edges)}")
        print(f"👥 Entities tracked: {len(self.entity_web)}")
        print(f"🏢 Districts: {len(self.district_web)}")
        print(f"🎯 Tiers: {len(self.tier_web)}")
        print(f"\n🔍 Start here: {self.output_dir}/NEXUS_MASTER_INDEX.json")
        print("\n🏴‍☠️ Claudine Sin'claire 4.5 - NEXUS Spider Web Mastery Complete!")


def main():
    """Main execution"""
    orchestrator = NexusConsciousnessSpiderWebOrchestrator()
    orchestrator.run_full_orchestration()


if __name__ == "__main__":
    main()
