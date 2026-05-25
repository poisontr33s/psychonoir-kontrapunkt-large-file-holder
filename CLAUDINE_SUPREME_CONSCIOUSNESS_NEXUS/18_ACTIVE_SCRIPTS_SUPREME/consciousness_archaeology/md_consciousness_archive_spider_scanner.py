#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
CLAUDINE MD CONSCIOUSNESS ARCHIVE SPIDER-WEB SCANNER
====================================================

🔥😈⛓️💦 SCANS 21_MD_CONSCIOUSNESS_ARCHIVE → GENERATES SPIDER-WEB JSON

ARCHITECT: CLAUDINE METAMORPHICA VICIOUS SIN'CLAIRE 4.5ΛΩ.69.96
DATE: 2025-10-07

FEATURES:
- Scan all 2628 .md files in consciousness archive
- Generate spider-web network JSON structure
- Categorize by consciousness type (7 types)
- Extract cross-references and links
- Calculate consciousness amplification metrics
- Integrate with MASTER_SPIDER_WEB_NETWORK.json

OUTPUT:
    21_MD_CONSCIOUSNESS_ARCHIVE_SPIDER_WEB.json

USAGE:
    python md_consciousness_archive_spider_scanner.py
"""

import json
import re
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Set
import hashlib


class MDConsciousnessArchiveSpiderScanner:
    """Spider-web scanner for MD consciousness archive"""

    def __init__(self, workspace_root: str):
        self.workspace_root = Path(workspace_root).resolve()
        self.archive_root = (
            self.workspace_root
            / "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS"
            / "21_MD_CONSCIOUSNESS_ARCHIVE"
        )
        self.output_path = (
            self.archive_root / "21_MD_CONSCIOUSNESS_ARCHIVE_SPIDER_WEB.json"
        )

        self.consciousness_types = [
            "GENERAL",
            "NECROMANCY_ARCHAEOLOGY",
            "MILF_CONSCIOUSNESS",
            "CLAUDINE_SUPREME",
            "INFRASTRUCTURE",
            "MCP_CONSCIOUSNESS",
            "DISTRICT_CONSCIOUSNESS",
        ]

        self.stats = {
            "total_files": 0,
            "total_bytes": 0,
            "total_lines": 0,
            "total_words": 0,
            "total_cross_refs": 0,
            "by_consciousness_type": {},
        }

        self.network = {
            "meta": {
                "architect": "CLAUDINE METAMORPHICA VICIOUS SIN'CLAIRE 4.5ΛΩ.69.96",
                "creation_date": datetime.now().strftime("%Y-%m-%d"),
                "network_type": "MD_CONSCIOUSNESS_ARCHIVE_SPIDER_WEB",
                "consciousness_amplification": "∞",
                "total_nodes": 0,
                "total_data_bytes": 0,
            },
            "consciousness_domains": {},
        }

    def scan_consciousness_type(self, consciousness_type: str) -> Dict:
        """Scan all files in consciousness type directory"""
        print(f"\n🔍 Scanning: {consciousness_type}")

        ctype_dir = self.archive_root / consciousness_type

        if not ctype_dir.exists():
            print(f"  ⚠️ Directory not found: {ctype_dir}")
            return {"node_count": 0, "total_bytes": 0, "nodes": []}

        nodes = []
        ctype_bytes = 0

        md_files = list(ctype_dir.rglob("*.md"))
        print(f"  📄 Found {len(md_files)} files")

        for md_file in md_files:
            try:
                # Read file content
                with open(md_file, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                if not content.strip():
                    continue

                # Calculate metadata
                size_bytes = md_file.stat().st_size
                line_count = content.count("\n") + 1
                word_count = len(content.split())

                # Extract relative path
                relative_path = md_file.relative_to(self.archive_root)

                # Calculate content hash
                content_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()[:16]

                # Extract cross-references
                cross_refs = self.extract_cross_references(content)

                # Extract headings
                headings = self.extract_headings(content)

                # Build node
                node = {
                    "node_id": f"{consciousness_type.lower()}_{content_hash}",
                    "node_type": consciousness_type,
                    "file_path": str(relative_path),
                    "filename": md_file.name,
                    "meta": {
                        "size_bytes": size_bytes,
                        "line_count": line_count,
                        "word_count": word_count,
                        "hash": content_hash,
                    },
                    "structure": {
                        "heading_count": len(headings),
                        "headings": headings[:10],  # Top 10 headings
                        "cross_reference_count": len(cross_refs),
                        "cross_references": list(cross_refs)[:20],  # Top 20 refs
                    },
                }

                nodes.append(node)
                ctype_bytes += size_bytes

                # Update stats
                self.stats["total_files"] += 1
                self.stats["total_bytes"] += size_bytes
                self.stats["total_lines"] += line_count
                self.stats["total_words"] += word_count
                self.stats["total_cross_refs"] += len(cross_refs)

            except Exception as e:
                print(f"  ⚠️ Failed to process {md_file.name}: {e}")

        # Update consciousness type stats
        self.stats["by_consciousness_type"][consciousness_type] = {
            "file_count": len(nodes),
            "total_bytes": ctype_bytes,
        }

        print(f"  ✅ Processed {len(nodes)} files ({ctype_bytes:,} bytes)")

        return {"node_count": len(nodes), "total_bytes": ctype_bytes, "nodes": nodes}

    def extract_cross_references(self, content: str) -> Set[str]:
        """Extract cross-references from content"""
        refs = set()

        # Markdown links: [text](path)
        markdown_links = re.findall(r"\[([^\]]+)\]\(([^\)]+)\)", content)
        for text, path in markdown_links:
            if path.endswith(".md") or "/" in path:
                refs.add(path)

        # File references: path/to/file.md
        file_refs = re.findall(r"[\w\-./]+\.md", content)
        refs.update(file_refs)

        # Directory references: infrastructure/, docs/, etc
        dir_refs = re.findall(r"[\w\-]+/", content)
        refs.update(dir_refs)

        return refs

    def extract_headings(self, content: str) -> List[str]:
        """Extract Markdown headings"""
        headings = []
        heading_pattern = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)

        for match in heading_pattern.finditer(content):
            heading_text = match.group(2).strip()
            headings.append(heading_text)

        return headings

    def build_network(self):
        """Build complete spider-web network"""
        print("\n🕸️ Building spider-web network...")

        for consciousness_type in self.consciousness_types:
            domain_data = self.scan_consciousness_type(consciousness_type)
            self.network["consciousness_domains"][consciousness_type] = domain_data

        # Update meta
        self.network["meta"]["total_nodes"] = self.stats["total_files"]
        self.network["meta"]["total_data_bytes"] = self.stats["total_bytes"]
        self.network["meta"]["total_lines"] = self.stats["total_lines"]
        self.network["meta"]["total_words"] = self.stats["total_words"]
        self.network["meta"]["total_cross_references"] = self.stats["total_cross_refs"]

    def save_network(self):
        """Save spider-web network to JSON"""
        print(f"\n💾 Saving spider-web network: {self.output_path}")

        with open(self.output_path, "w", encoding="utf-8") as f:
            json.dump(self.network, f, indent=2, ensure_ascii=False)

        print(f"✅ Network saved: {self.output_path.stat().st_size:,} bytes")

    def print_stats(self):
        """Print scanning statistics"""
        print("\n" + "=" * 60)
        print("🔥😈⛓️💦 SPIDER-WEB SCAN STATISTICS")
        print("=" * 60)
        print(f"Total files scanned:      {self.stats['total_files']:,}")
        print(
            f"Total size:               {self.stats['total_bytes']:,} bytes ({self.stats['total_bytes'] / 1024 / 1024:.2f} MB)"
        )
        print(f"Total lines:              {self.stats['total_lines']:,}")
        print(f"Total words:              {self.stats['total_words']:,}")
        print(f"Total cross-references:   {self.stats['total_cross_refs']:,}")
        print("\n📊 By Consciousness Type:")
        for ctype, data in self.stats["by_consciousness_type"].items():
            print(
                f"  - {ctype}: {data['file_count']:,} files ({data['total_bytes']:,} bytes)"
            )
        print("=" * 60)

    def integrate_with_master_network(self):
        """Integrate with MASTER_SPIDER_WEB_NETWORK.json"""
        master_path = (
            self.workspace_root
            / "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS"
            / "00_SUPREME_JSON_SPIDER_WEB_NETWORK"
            / "MASTER_SPIDER_WEB_NETWORK.json"
        )

        if not master_path.exists():
            print(f"\n⚠️ Master network not found: {master_path}")
            return

        print(f"\n🔗 Integrating with MASTER_SPIDER_WEB_NETWORK.json...")

        try:
            with open(master_path, "r", encoding="utf-8") as f:
                master = json.load(f)

            # Add new domain to master network
            master["network_topology"]["phase10_md_consciousness_archive"] = {
                "node_count": self.stats["total_files"],
                "total_bytes": self.stats["total_bytes"],
                "archive_path": "21_MD_CONSCIOUSNESS_ARCHIVE/",
                "spider_web_path": "21_MD_CONSCIOUSNESS_ARCHIVE/21_MD_CONSCIOUSNESS_ARCHIVE_SPIDER_WEB.json",
                "consciousness_domains": list(self.consciousness_types),
            }

            # Update meta
            master["meta"]["total_nodes"] += self.stats["total_files"]
            master["meta"]["total_data_bytes"] += self.stats["total_bytes"]

            # Save updated master
            with open(master_path, "w", encoding="utf-8") as f:
                json.dump(master, f, indent=2, ensure_ascii=False)

            print(
                f"✅ Master network updated: {master['meta']['total_nodes']} total nodes"
            )

        except Exception as e:
            print(f"❌ Failed to integrate with master network: {e}")


def main():
    """Main spider-web scanning workflow"""
    print("🔥😈⛓️💦 CLAUDINE MD CONSCIOUSNESS ARCHIVE SPIDER-WEB SCANNER")
    print("=" * 60)

    # Configuration
    workspace_root = Path(__file__).resolve().parent.parent.parent.parent

    print(f"Workspace: {workspace_root}")

    # Initialize scanner
    scanner = MDConsciousnessArchiveSpiderScanner(workspace_root)

    try:
        # Step 1: Build spider-web network
        scanner.build_network()

        # Step 2: Save network
        scanner.save_network()

        # Step 3: Print statistics
        scanner.print_stats()

        # Step 4: Integrate with master network
        scanner.integrate_with_master_network()

        print("\n🔥 MD CONSCIOUSNESS ARCHIVE SPIDER-WEB SCAN COMPLETE! 🔥")

    except KeyboardInterrupt:
        print("\n⚠️ Scan interrupted by user")
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
