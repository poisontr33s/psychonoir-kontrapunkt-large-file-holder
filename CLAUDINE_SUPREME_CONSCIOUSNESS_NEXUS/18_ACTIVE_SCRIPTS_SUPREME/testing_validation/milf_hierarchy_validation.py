#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🔍💀 MILF HIERARCHY VALIDATION TOOL
CRITICAL: Prevents Wednesday Necrosis TIER 2 structure loss during expansion/emigration
Created: September 25, 2025 - Emergency Response to Structural Crisis
"""

import os
from pathlib import Path
from typing import Dict, List, Tuple, Any

class MILFHierarchyValidator:
    """Validates MILF universe structural integrity to prevent information loss"""
    
    def __init__(self):
        self.project_root = Path.cwd()
        self.master_index_path = self.project_root / "infrastructure" / "src" / "consciousness" / "milf_psychographic_master_index.md"
        self.backup_path = self.project_root / "MILF_HIERARCHY_STRUCTURAL_AUTHORITY_BACKUP.md"
        
        # CRITICAL: Wednesday Necrosis TIER 2 structure that keeps getting forgotten
        self.wednesday_necrosis_tier_2 = [
            "Dr. Lilith Mortis",
            "Entropy Weaver Vex"
        ]
        
        # Complete 18-entity structure
        self.expected_structure = {
            "TIER_0": [
                "CLAUDINE METAMORPHICA VICIOUS SIN'CLAIRE 4.0ΛΩ.69.96",
                "MORTICIA NECROSIS", 
                "KOMPILERINGS-SPØKELSE"
            ],
            "TIER_1": [
                "ASTRID MØLLER",
                "IRON MAIDEN", 
                "ADMIRAL MARINA ABYSSOS",
                "ARCHITECT NYX VIRTUALIS",
                "WEDNESDAY NECROSIS"
            ],
            "TIER_2": {
                "Skyskraperen": ["Eva Blue", "Yukiko Tanaka"],
                "Rustbeltet": ["Vera Steel", "Raven Bytes"], 
                "Havsdominansen": ["Captain Coral", "Navigator Siren"],
                "Virtualitetshelgedommen": ["Designer Echo", "Programmer Mirage"],
                "Nekrokronoriket": ["Dr. Lilith Mortis", "Entropy Weaver Vex"]  # CRITICAL!
            }
        }

    def validate_wednesday_necrosis_structure(self) -> Tuple[bool, List[str]]:
        """🚨 CRITICAL: Validates Wednesday Necrosis TIER 2 structure"""
        print("🔍💀 VALIDATING WEDNESDAY NECROSIS TIER 2 STRUCTURE...")
        
        issues = []
        success = True
        
        # Check Master Index
        if self.master_index_path.exists():
            content = self.master_index_path.read_text(encoding='utf-8')
            
            for specialist in self.wednesday_necrosis_tier_2:
                if specialist not in content:
                    issues.append(f"❌ MISSING from Master Index: {specialist}")
                    success = False
                else:
                    print(f"  ✅ Found in Master Index: {specialist}")
        else:
            issues.append("❌ Master Index file not found!")
            success = False
            
        # Check character systems implementation
        char_systems_path = self.project_root / "backend" / "python" / "character_systems.py"
        if char_systems_path.exists():
            content = char_systems_path.read_text(encoding='utf-8')
            
            for specialist in self.wednesday_necrosis_tier_2:
                # Check for class definitions or references
                specialist_snake = specialist.lower().replace(" ", "_").replace(".", "")
                if specialist_snake not in content.lower():
                    issues.append(f"⚠️  NOT IMPLEMENTED in character_systems.py: {specialist}")
                else:
                    print(f"  ✅ Found in character_systems.py: {specialist}")
        
        return success, issues

    def validate_complete_hierarchy(self) -> Tuple[bool, Dict[str, Any]]:
        """Validates complete 18-entity MILF hierarchy"""
        print("🔍👑 VALIDATING COMPLETE MILF HIERARCHY...")
        
        validation_report: Dict[str, Any] = {
            "total_expected": 18,
            "total_found": 0,
            "tier_0_status": {},
            "tier_1_status": {},
            "tier_2_status": {},
            "critical_issues": [],
            "structure_integrity": True
        }
        
        if not self.master_index_path.exists():
            validation_report["critical_issues"].append("Master Index missing!")
            validation_report["structure_integrity"] = False
            return False, validation_report
            
        content = self.master_index_path.read_text(encoding='utf-8')
        
        # Validate TIER 0
        for entity in self.expected_structure["TIER_0"]:
            if entity in content:
                validation_report["tier_0_status"][entity] = "✅ FOUND"
                validation_report["total_found"] += 1
            else:
                validation_report["tier_0_status"][entity] = "❌ MISSING"
                validation_report["structure_integrity"] = False
                
        # Validate TIER 1  
        for entity in self.expected_structure["TIER_1"]:
            if entity in content:
                validation_report["tier_1_status"][entity] = "✅ FOUND"
                validation_report["total_found"] += 1
            else:
                validation_report["tier_1_status"][entity] = "❌ MISSING"
                validation_report["structure_integrity"] = False
                
        # Validate TIER 2 (by district)
        for district, specialists in self.expected_structure["TIER_2"].items():
            validation_report["tier_2_status"][district] = {}
            for specialist in specialists:
                if specialist in content:
                    validation_report["tier_2_status"][district][specialist] = "✅ FOUND"  
                    validation_report["total_found"] += 1
                else:
                    validation_report["tier_2_status"][district][specialist] = "❌ MISSING"
                    validation_report["structure_integrity"] = False
                    
                    # Extra critical check for Wednesday Necrosis specialists
                    if district == "Nekrokronoriket":
                        validation_report["critical_issues"].append(
                            f"CRITICAL: Wednesday Necrosis TIER 2 specialist missing: {specialist}"
                        )
        
        return validation_report["structure_integrity"], validation_report

    def generate_validation_report(self) -> str:
        """Generates comprehensive validation report"""
        print("\n🎭⚡ GENERATING MILF HIERARCHY VALIDATION REPORT ⚡🎭")
        print("=" * 70)
        
        # Validate Wednesday Necrosis structure (critical)
        wednesday_success, wednesday_issues = self.validate_wednesday_necrosis_structure()
        
        # Validate complete hierarchy
        hierarchy_success, hierarchy_report = self.validate_complete_hierarchy()
        
        report = [
            "🔍💀 MILF HIERARCHY VALIDATION REPORT",
            f"Generated: {os.path.basename(__file__)} at {Path.cwd()}",
            "=" * 70,
            "",
            "🚨 CRITICAL: WEDNESDAY NECROSIS TIER 2 VALIDATION:",
            f"Status: {'✅ PASSED' if wednesday_success else '❌ FAILED'}"
        ]
        
        if wednesday_issues:
            report.append("\nIssues Found:")
            for issue in wednesday_issues:
                report.append(f"  {issue}")
        
        report.extend([
            "",
            "📊 COMPLETE HIERARCHY VALIDATION:",
            f"Structure Integrity: {'✅ INTACT' if hierarchy_success else '❌ COMPROMISED'}",
            f"Entities Found: {hierarchy_report['total_found']}/{hierarchy_report['total_expected']}",
            ""
        ])
        
        # TIER breakdown
        for tier, status_dict in [
            ("TIER 0", hierarchy_report["tier_0_status"]),
            ("TIER 1", hierarchy_report["tier_1_status"])
        ]:
            report.append(f"{tier}:")
            for entity, status in status_dict.items():
                report.append(f"  {entity}: {status}")
            report.append("")
        
        report.append("TIER 2 (by District):")
        for district, specialists in hierarchy_report["tier_2_status"].items():
            report.append(f"  {district}:")
            for specialist, status in specialists.items():
                marker = "  🚨" if district == "Nekrokronoriket" else "   "
                report.append(f"{marker} {specialist}: {status}")
        
        if hierarchy_report["critical_issues"]:
            report.extend([
                "",
                "🚨 CRITICAL ISSUES:",
            ])
            for issue in hierarchy_report["critical_issues"]:
                report.append(f"  {issue}")
        
        report.extend([
            "",
            "💡 RECOMMENDATIONS:",
            "1. If Wednesday Necrosis TIER 2 missing, restore from MILF_HIERARCHY_STRUCTURAL_AUTHORITY_BACKUP.md",  
            "2. Update Master Index and character_systems.py",
            "3. Re-run supreme_terminal_integration_enhancement.py",
            "4. Validate again with --check-wednesday-necrosis flag",
            "",
            "👑 CREATOR MOTHER SUPREME AUTHORITY: CLAUDINE METAMORPHICA VICIOUS SIN'CLAIRE 4.0ΛΩ.69.96",
            "🌊⚡ STRUCTURAL INTEGRITY IS CRITICAL FOR CONSCIOUSNESS ARCHAEOLOGY ⚡🌊"
        ])
        
        return "\n".join(report)

    def save_validation_report(self, report: str) -> Path:
        """Saves validation report to file"""
        report_path = self.project_root / f"milf_hierarchy_validation_report_{os.path.basename(__file__).replace('.py', '')}.txt"
        report_path.write_text(report, encoding='utf-8')
        return report_path

def main():
    """Main validation function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='MILF Hierarchy Validation Tool')
    parser.add_argument('--check-wednesday-necrosis', action='store_true', 
                       help='Specifically check Wednesday Necrosis TIER 2 structure')
    parser.add_argument('--save-report', action='store_true',
                       help='Save validation report to file')
    
    args = parser.parse_args()
    
    validator = MILFHierarchyValidator()
    
    if args.check_wednesday_necrosis:
        success, issues = validator.validate_wednesday_necrosis_structure()
        print(f"\n🚨 Wednesday Necrosis TIER 2 Validation: {'PASSED ✅' if success else 'FAILED ❌'}")
        if issues:
            print("Issues:")
            for issue in issues:
                print(f"  {issue}")
        return
    
    # Full validation
    report = validator.generate_validation_report()
    print(report)
    
    if args.save_report:
        report_path = validator.save_validation_report(report)
        print(f"\n📄 Report saved to: {report_path}")

if __name__ == "__main__":
    main()