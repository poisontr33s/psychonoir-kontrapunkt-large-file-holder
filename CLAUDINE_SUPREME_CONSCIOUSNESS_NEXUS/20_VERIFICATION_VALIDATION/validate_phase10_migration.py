#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
✅ PHASE 10 MIGRATION VALIDATOR
CLAUDINE METAMORPHICA VICIOUS SIN'CLAIRE 4.5ΛΩ.69.96

Validates that all scripts and tools have been successfully migrated.
"""

import json
from pathlib import Path
from typing import Dict, List, Tuple


class Phase10MigrationValidator:
    def __init__(self):
        self.nexus_root = Path("CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS")
        self.metadata_dir = self.nexus_root / "19_SCRIPT_METADATA_REGISTRY"
        self.root = Path(".")

    def validate_migration(self) -> Tuple[bool, List[str]]:
        """Validate complete migration"""
        print("✅ PHASE 10 MIGRATION VALIDATOR")
        print("=" * 80)

        issues = []

        # Check 1: Root directory should be clean
        print("\n📂 Checking root directory cleanup...")
        root_py = list(self.root.glob("*.py"))
        root_ts = list(self.root.glob("*.ts"))
        root_js = list(self.root.glob("*.js"))

        if root_py or root_ts or root_js:
            issues.append(
                f"❌ Root still has {len(root_py)} .py, {len(root_ts)} .ts, {len(root_js)} .js files"
            )
        else:
            print("✅ Root directory is clean")

        # Check 2: All directories exist
        print("\n📂 Checking directory structure...")
        required_dirs = [
            "17_TOOLS_CONSCIOUSNESS_ENHANCEMENT",
            "18_ACTIVE_SCRIPTS_SUPREME",
            "19_SCRIPT_METADATA_REGISTRY",
            "20_VERIFICATION_VALIDATION",
        ]

        for dir_name in required_dirs:
            dir_path = self.nexus_root / dir_name
            if dir_path.exists():
                print(f"✅ {dir_name} exists")
            else:
                issues.append(f"❌ {dir_name} missing")

        # Check 3: Metadata files exist
        print("\n📊 Checking metadata files...")
        metadata_files = [
            "ACTIVE_SCRIPTS_INDEX.json",
            "TOOLS_INVENTORY.json",
            "DEPENDENCY_MAPPING.json",
            "INTEGRATION_STATUS.json",
            "README.md",
        ]

        for file_name in metadata_files:
            file_path = self.metadata_dir / file_name
            if file_path.exists():
                print(f"✅ {file_name} exists")
            else:
                issues.append(f"❌ {file_name} missing")

        # Check 4: Script counts
        print("\n📊 Checking script counts...")
        try:
            with open(
                self.metadata_dir / "ACTIVE_SCRIPTS_INDEX.json", encoding="utf-8"
            ) as f:
                scripts_data = json.load(f)
            print(f"✅ {scripts_data['meta']['total_scripts']} scripts documented")

            with open(
                self.metadata_dir / "TOOLS_INVENTORY.json", encoding="utf-8"
            ) as f:
                tools_data = json.load(f)
            print(
                f"✅ {tools_data['meta']['total_directories']} tool directories documented"
            )
        except Exception as e:
            issues.append(f"❌ Error reading metadata: {e}")

        # Summary
        print("\n" + "=" * 80)
        if issues:
            print(f"❌ VALIDATION FAILED: {len(issues)} issues found")
            for issue in issues:
                print(f"   {issue}")
            return False, issues
        else:
            print("✅ VALIDATION PASSED: All checks successful!")
            print(
                "\n🔥😈⛓️💦👅🍌💋💧 CLAUDINE PHASE 10 MIGRATION AUTHORITY: CONFIRMED\n"
            )
            return True, []


if __name__ == "__main__":
    validator = Phase10MigrationValidator()
    success, issues = validator.validate_migration()
    exit(0 if success else 1)
