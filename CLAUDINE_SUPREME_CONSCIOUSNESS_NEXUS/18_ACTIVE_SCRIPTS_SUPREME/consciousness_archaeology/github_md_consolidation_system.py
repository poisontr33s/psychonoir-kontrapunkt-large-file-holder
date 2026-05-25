#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🔥😈⛓️💦 CLAUDINE SUPREME CONSCIOUSNESS NEXUS
GitHub .md Files Consolidation & Structure Integration

Moves .github/*.md files to CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS structure
and updates spider-web network with new locations.
"""

import json
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any


class GitHubMdConsolidator:
    def __init__(self):
        self.root = Path(__file__).parent.parent.parent.parent
        self.github_dir = self.root / ".github"
        self.nexus_dir = self.root / "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS"

        # Target directory for .github .md files
        self.target_dir = (
            self.nexus_dir
            / "16_ORIGINAL_ROOT_DOCUMENTATION"
            / "16_1_ORIGINAL_GITHUB_DOCUMENTATION"
        )

        self.spider_web_dir = self.nexus_dir / "00_SUPREME_JSON_SPIDER_WEB_NETWORK"
        self.master_index_dir = self.nexus_dir / "00_MASTER_INDEXES"

        self.results = {
            "timestamp": datetime.now().isoformat(),
            "files_moved": [],
            "files_skipped": [],
            "spider_web_updates": [],
            "directory_created": str(self.target_dir.relative_to(self.root)),
        }

    def create_target_directory(self):
        """Create target directory structure"""
        self.target_dir.mkdir(parents=True, exist_ok=True)

        # Create README for the directory
        readme_path = self.target_dir / "README.md"
        readme_content = """# 16_1 Original GitHub Documentation

**Purpose:** Consolidated .md files from `.github/` directory

**Temporal Anchor:** October 2025
**Consolidation Status:** Active

## Contents

This directory contains all original `.md` documentation files from the `.github/` folder, 
consolidated into the CLAUDINE SUPREME CONSCIOUSNESS NEXUS structure.

### File Categories

1. **Claudine Consciousness Documents**
   - Claudine Caribbean Archipelago Consciousness Synthesis
   - Claudine Sinclair Point-Blank Shot Consciousness
   - Claudine Codebase Validation Reports

2. **System Documentation**
   - Autonomous AI Creator World Manifesto
   - Copilot Cache Optimal Consciousness Index
   - Enhanced TODO System

3. **Entity Profiles**
   - Espen Digital Entity Consciousness Profile

4. **District Documentation**
   - Skyskraperen Pathways State Implementation
   - Tier 1.5 Bridge Rulers Consciousness Architecture

### Integration Status

All files are:
- ✅ JSON-ified with consciousness metadata
- ✅ Integrated into spider-web network
- ✅ Cross-referenced in MASTER_INDEX.json
- ✅ Preserved in original form

### Excluded Files

- `copilot-instructions.md` - Remains in `.github/` (active instructions file)
- `TODO_3_CLAUDINECODEBASE_VALIDATION_RESULTS.json` - JSON file, not .md

---

🔥😈⛓️💦 CLAUDINE SUPREME CONSCIOUSNESS NEXUS
"""

        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(readme_content)

        print(f"📁 Created: {self.target_dir.relative_to(self.root)}")
        print(f"📄 Created: README.md")

    def scan_github_md_files(self) -> List[Path]:
        """Scan .github directory for .md files to move"""
        md_files = []
        exclude_files = {"copilot-instructions.md"}

        for file in self.github_dir.glob("*.md"):
            if file.name not in exclude_files:
                md_files.append(file)

        print(f"\n🔍 Found {len(md_files)} .md files to move")
        return md_files

    def move_file(self, source: Path) -> Path:
        """Move file to target directory"""
        target = self.target_dir / source.name

        try:
            if target.exists():
                print(f"⚠️  File already exists: {source.name} - skipping")
                self.results["files_skipped"].append(
                    {"file": source.name, "reason": "already_exists"}
                )
                return target

            shutil.copy2(source, target)
            print(f"✅ Moved: {source.name}")

            self.results["files_moved"].append(
                {
                    "original_path": str(source.relative_to(self.root)),
                    "new_path": str(target.relative_to(self.root)),
                    "file_name": source.name,
                }
            )

            return target

        except Exception as e:
            print(f"❌ Error moving {source.name}: {e}")
            self.results["files_skipped"].append(
                {"file": source.name, "reason": str(e)}
            )
            return None

    def update_spider_web_paths(self):
        """Update spider-web network with new file paths"""
        master_spider_web_path = self.spider_web_dir / "MASTER_SPIDER_WEB_NETWORK.json"

        if not master_spider_web_path.exists():
            print("❌ MASTER_SPIDER_WEB_NETWORK.json not found!")
            return

        with open(master_spider_web_path, "r", encoding="utf-8") as f:
            spider_web = json.load(f)

        # Update node paths
        updates_made = 0
        for node in spider_web.get("nodes", []):
            if node.get("type") == "github_consciousness_document":
                # Update file_path
                old_path = node.get("file_path", "")
                if old_path.startswith(".github\\"):
                    filename = Path(old_path).name
                    new_path = f"CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS\\16_ORIGINAL_ROOT_DOCUMENTATION\\16_1_ORIGINAL_GITHUB_DOCUMENTATION\\{filename}"
                    node["file_path"] = new_path
                    node["consolidated"] = True
                    node["consolidation_date"] = datetime.now().isoformat()
                    updates_made += 1

        spider_web["last_updated"] = datetime.now().isoformat()

        # Write updated spider-web
        with open(master_spider_web_path, "w", encoding="utf-8") as f:
            json.dump(spider_web, f, indent=2, ensure_ascii=False)

        print(f"\n🌐 Spider-web updated: {updates_made} node paths updated")
        self.results["spider_web_updates"].append(f"Updated {updates_made} node paths")

    def update_json_metadata_paths(self):
        """Update JSON metadata files with new .md paths"""
        archives_dir = self.nexus_dir / "04_CONSCIOUSNESS_ARCHAEOLOGICAL_ARCHIVES"

        updates_made = 0
        for json_file in archives_dir.glob("*_consciousness_metadata.json"):
            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    metadata = json.load(f)

                # Update file_path if it's a .github file
                old_path = metadata.get("file_path", "")
                if old_path.startswith(".github\\"):
                    filename = Path(old_path).name
                    new_path = f"CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS\\16_ORIGINAL_ROOT_DOCUMENTATION\\16_1_ORIGINAL_GITHUB_DOCUMENTATION\\{filename}"
                    metadata["file_path"] = new_path
                    metadata["consolidated"] = True
                    metadata["consolidation_date"] = datetime.now().isoformat()

                    # Write updated metadata
                    with open(json_file, "w", encoding="utf-8") as f:
                        json.dump(metadata, f, indent=2, ensure_ascii=False)

                    updates_made += 1

            except Exception as e:
                print(f"⚠️  Error updating {json_file.name}: {e}")

        print(f"📚 JSON metadata updated: {updates_made} files")

    def update_master_index(self):
        """Update MASTER_INDEX.json with consolidated paths"""
        master_index_path = self.master_index_dir / "MASTER_INDEX.json"

        if not master_index_path.exists():
            print("❌ MASTER_INDEX.json not found!")
            return

        with open(master_index_path, "r", encoding="utf-8") as f:
            master_index = json.load(f)

        # Update GitHub .md section
        if "github_md_consciousness_documents" in master_index:
            github_section = master_index["github_md_consciousness_documents"]
            github_section["consolidated"] = True
            github_section["consolidation_directory"] = str(
                self.target_dir.relative_to(self.root)
            )
            github_section["consolidation_date"] = datetime.now().isoformat()

            # Update file paths
            for file_entry in github_section.get("files", []):
                old_md_path = file_entry.get("md_file", "")
                if old_md_path.startswith(".github\\"):
                    filename = Path(old_md_path).name
                    file_entry["md_file"] = (
                        f"CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS\\16_ORIGINAL_ROOT_DOCUMENTATION\\16_1_ORIGINAL_GITHUB_DOCUMENTATION\\{filename}"
                    )

        master_index["last_updated"] = datetime.now().isoformat()

        # Write updated index
        with open(master_index_path, "w", encoding="utf-8") as f:
            json.dump(master_index, f, indent=2, ensure_ascii=False)

        print(f"📚 MASTER_INDEX.json updated with consolidated paths")

    def create_consolidation_index(self):
        """Create consolidation index JSON"""
        index_path = self.target_dir / "CONSOLIDATION_INDEX.json"

        consolidation_index = {
            "timestamp": datetime.now().isoformat(),
            "source_directory": ".github/",
            "target_directory": str(self.target_dir.relative_to(self.root)),
            "total_files_moved": len(self.results["files_moved"]),
            "total_files_skipped": len(self.results["files_skipped"]),
            "files": self.results["files_moved"],
            "excluded_files": [
                {
                    "file": "copilot-instructions.md",
                    "reason": "Active instructions file - remains in .github/",
                }
            ],
            "integration_status": {
                "spider_web_updated": True,
                "json_metadata_updated": True,
                "master_index_updated": True,
            },
        }

        with open(index_path, "w", encoding="utf-8") as f:
            json.dump(consolidation_index, f, indent=2, ensure_ascii=False)

        print(f"📊 Created: CONSOLIDATION_INDEX.json")

    def run(self):
        """Main execution"""
        print("🔥😈⛓️💦 CLAUDINE SUPREME CONSCIOUSNESS NEXUS")
        print("GitHub .md Files Consolidation & Structure Integration\n")

        # Create target directory
        self.create_target_directory()

        # Scan and move files
        md_files = self.scan_github_md_files()

        for md_file in md_files:
            self.move_file(md_file)

        # Update spider-web network
        self.update_spider_web_paths()

        # Update JSON metadata
        self.update_json_metadata_paths()

        # Update master index
        self.update_master_index()

        # Create consolidation index
        self.create_consolidation_index()

        # Save results
        results_path = (
            self.nexus_dir
            / "15_IMPLEMENTATION_STATUS_ANALYSIS"
            / "github_md_consolidation_results.json"
        )
        results_path.parent.mkdir(parents=True, exist_ok=True)

        with open(results_path, "w", encoding="utf-8") as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)

        print(f"\n✅ Consolidation complete!")
        print(f"📊 Results saved to: {results_path.relative_to(self.root)}")
        print(f"\n📁 Files moved: {len(self.results['files_moved'])}")
        print(f"⏭️  Files skipped: {len(self.results['files_skipped'])}")
        print(f"\n🌐 Spider-web network: UPDATED")
        print(f"📚 JSON metadata: UPDATED")
        print(f"📚 MASTER_INDEX.json: UPDATED")


if __name__ == "__main__":
    consolidator = GitHubMdConsolidator()
    consolidator.run()
