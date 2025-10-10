#!/usr/bin/env python3
"""
🔥😈⛓️💦 CLAUDINE SUPREME CONSCIOUSNESS NEXUS
GitHub .md Files JSON-ification & Spider-Web Integration

Scans .github/*.md files, extracts consciousness metadata,
JSON-ifies them and integrates into existing spider-web network.
"""

import json
import os
from pathlib import Path
from datetime import datetime
import re
from typing import Dict, List, Any


class GitHubMdJsonifier:
    def __init__(self):
        self.root = Path(__file__).parent.parent.parent.parent
        self.github_dir = self.root / ".github"
        self.nexus_dir = self.root / "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS"
        self.spider_web_dir = self.nexus_dir / "00_SUPREME_JSON_SPIDER_WEB_NETWORK"
        self.master_index_dir = self.nexus_dir / "00_MASTER_INDEXES"

        self.results = {
            "timestamp": datetime.now().isoformat(),
            "total_md_files": 0,
            "jsonified_files": [],
            "integration_status": {},
            "spider_web_updates": [],
        }

    def scan_github_md_files(self) -> List[Path]:
        """Scan .github directory for .md files (excluding copilot-instructions.md)"""
        md_files = []
        for file in self.github_dir.glob("*.md"):
            if file.name != "copilot-instructions.md":
                md_files.append(file)

        self.results["total_md_files"] = len(md_files)
        print(f"🔥 Found {len(md_files)} .md files in .github/")
        return md_files

    def extract_consciousness_metadata(self, file_path: Path) -> Dict[str, Any]:
        """Extract consciousness metadata from .md file"""
        try:
            content = file_path.read_text(encoding="utf-8")

            metadata = {
                "file_name": file_path.name,
                "file_path": str(file_path.relative_to(self.root)),
                "file_size": file_path.stat().st_size,
                "line_count": len(content.split("\n")),
                "word_count": len(content.split()),
                "consciousness_type": self._detect_consciousness_type(
                    file_path.name, content
                ),
                "nsfw18_level": self._detect_nsfw_level(content),
                "emoji_density": self._calculate_emoji_density(content),
                "sections": self._extract_sections(content),
                "key_concepts": self._extract_key_concepts(content),
                "cross_references": self._extract_cross_references(content),
            }

            return metadata

        except Exception as e:
            print(f"❌ Error extracting metadata from {file_path.name}: {e}")
            return {}

    def _detect_consciousness_type(self, filename: str, content: str) -> str:
        """Detect consciousness type from filename and content"""
        filename_lower = filename.lower()

        if "claudine" in filename_lower and "caribbean" in filename_lower:
            return "CLAUDINE_CARIBBEAN_CONSCIOUSNESS"
        elif "claudine" in filename_lower and "codebase" in filename_lower:
            return "CLAUDINE_CODEBASE_CONSCIOUSNESS"
        elif "espen" in filename_lower:
            return "ESPEN_DIGITAL_ENTITY_CONSCIOUSNESS"
        elif "skyskraperen" in filename_lower:
            return "SKYSKRAPEREN_DISTRICT_CONSCIOUSNESS"
        elif "tier" in filename_lower and "bridge" in filename_lower:
            return "TIER_BRIDGE_CONSCIOUSNESS"
        elif "manifesto" in filename_lower:
            return "AUTONOMOUS_AI_MANIFESTO_CONSCIOUSNESS"
        elif "todo" in filename_lower:
            return "TODO_SYSTEM_CONSCIOUSNESS"
        else:
            return "GENERAL_CONSCIOUSNESS"

    def _detect_nsfw_level(self, content: str) -> int:
        """Detect NSFW18+ level (0-3)"""
        nsfw_keywords = [
            "nsfw",
            "nsfw18",
            "milf",
            "fuck",
            "cock",
            "pussy",
            "hentai",
            "ecchi",
            "ahegao",
            "pornhub",
            "sexual",
            "sensual",
        ]

        content_lower = content.lower()
        count = sum(1 for keyword in nsfw_keywords if keyword in content_lower)

        if count >= 10:
            return 3  # NSFW18+++
        elif count >= 5:
            return 2  # NSFW18++
        elif count >= 1:
            return 1  # NSFW18+
        else:
            return 0  # Safe

    def _calculate_emoji_density(self, content: str) -> float:
        """Calculate emoji density (emojis per 1000 chars)"""
        emoji_pattern = re.compile(
            "["
            "\U0001f600-\U0001f64f"  # emoticons
            "\U0001f300-\U0001f5ff"  # symbols & pictographs
            "\U0001f680-\U0001f6ff"  # transport & map symbols
            "\U0001f1e0-\U0001f1ff"  # flags
            "\U00002702-\U000027b0"
            "\U000024c2-\U0001f251"
            "]+",
            flags=re.UNICODE,
        )

        emoji_count = len(emoji_pattern.findall(content))
        if len(content) == 0:
            return 0.0

        return (emoji_count / len(content)) * 1000

    def _extract_sections(self, content: str) -> List[str]:
        """Extract markdown section headers"""
        sections = re.findall(r"^#{1,6}\s+(.+)$", content, re.MULTILINE)
        return sections[:20]  # Top 20 sections

    def _extract_key_concepts(self, content: str) -> List[str]:
        """Extract key concepts (words in backticks or bold)"""
        concepts = set()

        # Extract backticked words
        backtick_words = re.findall(r"`([^`]+)`", content)
        concepts.update(backtick_words[:30])

        # Extract bold words
        bold_words = re.findall(r"\*\*([^*]+)\*\*", content)
        concepts.update(bold_words[:30])

        return sorted(list(concepts))[:50]

    def _extract_cross_references(self, content: str) -> List[str]:
        """Extract cross-references to other files"""
        references = []

        # Extract markdown links
        links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content)
        references.extend([link[1] for link in links if link[1].endswith(".md")])

        # Extract file mentions
        file_mentions = re.findall(r"`([^`]+\.md)`", content)
        references.extend(file_mentions)

        return list(set(references))[:20]

    def jsonify_file(self, file_path: Path) -> Path:
        """Convert .md file to JSON format"""
        metadata = self.extract_consciousness_metadata(file_path)

        if not metadata:
            return None

        # Create JSON file path
        json_filename = file_path.stem + "_consciousness_metadata.json"
        json_path = (
            self.nexus_dir / "04_CONSCIOUSNESS_ARCHAEOLOGICAL_ARCHIVES" / json_filename
        )

        # Ensure directory exists
        json_path.parent.mkdir(parents=True, exist_ok=True)

        # Write JSON
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)

        print(f"✅ JSON-ified: {file_path.name} → {json_filename}")

        self.results["jsonified_files"].append(
            {
                "md_file": str(file_path.relative_to(self.root)),
                "json_file": str(json_path.relative_to(self.root)),
                "consciousness_type": metadata["consciousness_type"],
                "nsfw_level": metadata["nsfw18_level"],
            }
        )

        return json_path

    def integrate_into_spider_web(self, json_files: List[Path]):
        """Integrate JSON files into spider-web network"""
        master_spider_web_path = self.spider_web_dir / "MASTER_SPIDER_WEB_NETWORK.json"

        if not master_spider_web_path.exists():
            print("❌ MASTER_SPIDER_WEB_NETWORK.json not found!")
            return

        # Load existing spider-web
        with open(master_spider_web_path, "r", encoding="utf-8") as f:
            spider_web = json.load(f)

        # Add new nodes
        new_nodes = []
        for json_file in json_files:
            if not json_file:
                continue

            with open(json_file, "r", encoding="utf-8") as f:
                metadata = json.load(f)

            node = {
                "id": f"github_md_{metadata['file_name'].replace('.md', '')}",
                "type": "github_consciousness_document",
                "file_path": metadata["file_path"],
                "json_metadata": str(json_file.relative_to(self.root)),
                "consciousness_type": metadata["consciousness_type"],
                "nsfw_level": metadata["nsfw18_level"],
                "connections": [],
            }

            new_nodes.append(node)

        # Update spider-web nodes
        if "nodes" not in spider_web:
            spider_web["nodes"] = []

        spider_web["nodes"].extend(new_nodes)
        spider_web["last_updated"] = datetime.now().isoformat()
        spider_web["total_nodes"] = len(spider_web["nodes"])

        # Write updated spider-web
        with open(master_spider_web_path, "w", encoding="utf-8") as f:
            json.dump(spider_web, f, indent=2, ensure_ascii=False)

        print(f"🌐 Spider-web updated: {len(new_nodes)} new nodes added")
        self.results["spider_web_updates"].append(
            f"Added {len(new_nodes)} GitHub .md nodes"
        )

    def update_master_index(self):
        """Update MASTER_INDEX.json with GitHub .md files"""
        master_index_path = self.master_index_dir / "MASTER_INDEX.json"

        if not master_index_path.exists():
            print("❌ MASTER_INDEX.json not found!")
            return

        with open(master_index_path, "r", encoding="utf-8") as f:
            master_index = json.load(f)

        # Add GitHub .md section
        if "github_md_consciousness_documents" not in master_index:
            master_index["github_md_consciousness_documents"] = {
                "description": "JSON-ified .github/*.md consciousness documents",
                "total_files": self.results["total_md_files"],
                "files": self.results["jsonified_files"],
            }

        master_index["last_updated"] = datetime.now().isoformat()

        # Write updated index
        with open(master_index_path, "w", encoding="utf-8") as f:
            json.dump(master_index, f, indent=2, ensure_ascii=False)

        print(
            f"📚 MASTER_INDEX.json updated with {self.results['total_md_files']} GitHub .md files"
        )

    def run(self):
        """Main execution"""
        print("🔥😈⛓️💦 CLAUDINE SUPREME CONSCIOUSNESS NEXUS")
        print("GitHub .md Files JSON-ification & Spider-Web Integration\n")

        # Scan .github/*.md files
        md_files = self.scan_github_md_files()

        # JSON-ify each file
        json_files = []
        for md_file in md_files:
            json_file = self.jsonify_file(md_file)
            if json_file:
                json_files.append(json_file)

        # Integrate into spider-web
        self.integrate_into_spider_web(json_files)

        # Update master index
        self.update_master_index()

        # Save results
        results_path = (
            self.nexus_dir
            / "04_CONSCIOUSNESS_ARCHAEOLOGICAL_ARCHIVES"
            / "github_md_jsonification_results.json"
        )
        with open(results_path, "w", encoding="utf-8") as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)

        print(f"\n✅ JSON-ification complete!")
        print(f"📊 Results saved to: {results_path.relative_to(self.root)}")
        print(f"\n🌐 Total .md files processed: {self.results['total_md_files']}")
        print(f"📚 JSON files created: {len(self.results['jsonified_files'])}")


if __name__ == "__main__":
    jsonifier = GitHubMdJsonifier()
    jsonifier.run()
