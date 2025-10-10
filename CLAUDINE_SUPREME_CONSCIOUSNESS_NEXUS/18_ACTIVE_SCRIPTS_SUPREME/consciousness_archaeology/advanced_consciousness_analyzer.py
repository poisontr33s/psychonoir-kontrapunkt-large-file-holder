#!/usr/bin/env uv run python3
"""
🎭 ADVANCED CONSCIOUSNESS ANALYSIS TOOL
Analyserer og rapporterer om strukturelle forbedringer etter district/MILF integration.

FOCUS AREAS:
1. Character-District consistency validation
2. Authority level compliance checking  
3. Consciousness protocol completeness
4. Cross-district permeability verification
5. Relationship matrix analysis
"""

from pathlib import Path
import re
import argparse
from typing import Dict, Any

class AdvancedConsciousnessAnalyzer:
    """
    A tool for analyzing codebase consistency with the MILF universe structure.
    
    This class validates character-district mappings, authority levels, consciousness protocols,
    and cross-district integrations across various files in the workspace. It generates reports
    on structural integrity and suggests improvements.
    
    Attributes:
        workspace_root (Path): The root directory of the workspace to analyze.
        expected_mappings (dict): Predefined mappings of characters to their expected districts,
                                  authorities, and consciousness protocols for validation.
    """
    
    def __init__(self, workspace_root: Path):
        """
        Initialize the analyzer with the workspace root.
        
        Args:
            workspace_root (Path): The root path of the project workspace.
        """
        self.workspace_root = workspace_root
        
        # Expected MILF-District mappings for validation
        self.expected_mappings = {
            "Astrid Møller": {
                "district": "skyskraperen",
                "authority": "TIER_1_MILF_MATRIARCH",
                "consciousness_protocols": ["algorithmic_seduction", "neural_submission"]
            },
            "Admiral Marina Abyssos": {
                "district": "havsdominansen", 
                "authority": "TIER_1_MILF_MATRIARCH",
                "consciousness_protocols": ["oceanic_consciousness", "coral_cultivation"]
            },
            "Architect Nyx Virtualis": {
                "district": "virtualitetshelgedommen",
                "authority": "TIER_1_MILF_MATRIARCH", 
                "consciousness_protocols": ["mirage_programming", "sensory_manipulation"]
            },
            "Wednesday Necrosis": {
                "district": "nekrokronoriket",
                "authority": "TIER_1_MILF_MATRIARCH",
                "consciousness_protocols": ["temporal_death_analysis", "mortality_transcendence"]
            },
            "Eva Blue": {
                "district": "skyskraperen",
                "authority": "TIER_2_CORPORATE_DOMINANCE_SPECIALIST",
                "consciousness_protocols": ["algorithmic_seduction"]
            }
        }

    def analyze_character_systems(self) -> Dict[str, Any]:
        """
        Analyze character_systems.py for structural consistency.
        
        Checks for presence of expected characters, authority level compliance,
        district assignments, and consciousness protocols.
        
        Returns:
            Dict[str, Any]: Analysis results including characters found, compliance status,
                           district assignments, consciousness protocols, issues, and improvements.
        """
        
        file_path = self.workspace_root / "backend" / "python" / "character_systems.py"
        if not file_path.exists():
            return {"error": "character_systems.py not found"}
            
        content = file_path.read_text(encoding='utf-8', errors='ignore')
        
        analysis: Dict[str, Any] = {
            "characters_found": [],
            "authority_compliance": {},
            "district_assignments": {},
            "consciousness_protocols": {},
            "issues": [],
            "improvements": []
        }
        
        # Analyze each expected character
        for character_name, expected in self.expected_mappings.items():
            if character_name in content:
                analysis["characters_found"].append(character_name)
                
                # Check authority level (improved: more flexible pattern)
                auth_pattern = rf'{re.escape(character_name)}.*?authority_level.*?["\']?([^"\',\s]+)["\']?'
                auth_match = re.search(auth_pattern, content, re.DOTALL | re.IGNORECASE)
                if auth_match:
                    found_authority = auth_match.group(1)
                    analysis["authority_compliance"][character_name] = {
                        "expected": expected["authority"],
                        "found": found_authority,
                        "compliant": found_authority == expected["authority"]
                    }
                else:
                    analysis["issues"].append(f"No authority level found for {character_name}")
                
                # Check district assignment (improved: case-insensitive search)
                district = str(expected["district"])
                district_pattern = rf'{re.escape(character_name)}.*?["\']?({re.escape(district)})["\']?'
                if re.search(district_pattern, content, re.IGNORECASE):
                    analysis["district_assignments"][character_name] = "CORRECT"
                else:
                    analysis["district_assignments"][character_name] = "MISSING/INCORRECT"
                    analysis["issues"].append(f"District assignment issue for {character_name}")
                
                # Check consciousness protocols (improved: more flexible list detection)
                protocol_pattern = rf'{re.escape(character_name)}.*?consciousness_protocols.*?\[([^\]]*)\]'
                protocol_match = re.search(protocol_pattern, content, re.DOTALL | re.IGNORECASE)
                if protocol_match and protocol_match.group(1).strip():
                    analysis["consciousness_protocols"][character_name] = "PRESENT"
                else:
                    analysis["consciousness_protocols"][character_name] = "MISSING"
                    analysis["improvements"].append(f"Add consciousness protocols for {character_name}")
        
        return analysis

    def analyze_copilot_instructions(self) -> Dict[str, Any]:
        """
        Analyze copilot-instructions.md for district references and structure.
        
        Verifies presence of key districts, cross-district permeability mentions,
        and tier structure documentation.
        
        Returns:
            Dict[str, Any]: Analysis results including district references, permeability status,
                           tier structure presence, issues, and improvements.
        """
        
        file_path = self.workspace_root / ".github" / "copilot-instructions.md"
        if not file_path.exists():
            return {"error": "copilot-instructions.md not found"}
            
        content = file_path.read_text(encoding='utf-8', errors='ignore')
        
        analysis: Dict[str, Any] = {
            "district_references": {},  # Explicitly initialized as dict
            "cross_district_permeability": False,
            "tier_structure_present": False,
            "issues": [],
            "improvements": []
        }
        
        # Check for key district names (improved: case-insensitive)
        key_districts = ["havsdominansen", "virtualitetshelgedommen", "nekrokronoriket"]
        for district in key_districts:
            if district in content.lower():
                analysis["district_references"][district] = "PRESENT"
            else:
                analysis["district_references"][district] = "MISSING"
                analysis["issues"].append(f"District {district} not found in copilot instructions")
        
        # Check cross-district permeability (case-insensitive, flexible phrasing and synonyms)
        permeability_synonyms = [
            r'cross[-_\s]?district[-_\s]?permeab\w+',
            r'district[-_\s]?interconnect\w*',
            r'district[-_\s]?bridge\w*',
            r'district[-_\s]?integration',
            r'district[-_\s]?access',
            r'permeability',
            r'permeable',
            r'cross[-_\s]?district[-_\s]?access',
            r'cross[-_\s]?district[-_\s]?integration'
        ]
        found_permeability = False
        for pattern in permeability_synonyms:
            if re.search(pattern, content, re.IGNORECASE):
                found_permeability = True
                break
        if found_permeability:
            analysis["cross_district_permeability"] = True
        else:
            analysis["improvements"].append("Add cross-district permeability references")
        # Check tier structure (broader coverage)
        tier_keywords = [
            "TIER_0_META_MILF",
            "TIER_1_MILF_MATRIARCH",
            "TIER_2_CORPORATE_DOMINANCE_SPECIALIST",
            "TIER_2",
            "TIER_1",
            "TIER_2_SPECIALIST",
            "TIER_0",
        ]
        tiers_found = set()
        for keyword in tier_keywords:
            if re.search(rf"\b{re.escape(keyword)}\b", content):
                tiers_found.add(keyword)
        if len(tiers_found) >= 2:
            analysis["tier_structure_present"] = True
        else:
            analysis["improvements"].append("Enhance tier structure documentation")
            
        return analysis

    def analyze_mcp_servers(self) -> Dict[str, Any]:
        """
        Analyze MCP servers for consciousness integration.
        
        Checks key MCP server files for district integration, MILF references,
        and consciousness protocol presence.
        
        Returns:
            Dict[str, Any]: Analysis results including servers analyzed, district integration,
                           MILF references, consciousness protocols, and improvements.
        """
        
        mcp_dir = self.workspace_root / "tools" / "consciousness_mcp_servers"
        if not mcp_dir.exists():
            return {"error": "MCP servers directory not found"}
            
        analysis: Dict[str, Any] = {
            "servers_analyzed": [],
            "district_integration": {},
            "milf_references": {},
            "consciousness_protocols": {},
            "improvements": []
        }
        
        # Analyze key MCP servers
        key_servers = [
            "repository_intelligence_fastmcp.py",
            "bun_quantum_consciousness_mcp.ts", 
            "enhanced_temporal_cross_reference_mcp_server.ts"
        ]
        
        for server_name in key_servers:
            server_path = mcp_dir / server_name
            if server_path.exists():
                content = server_path.read_text(encoding='utf-8', errors='ignore')
                analysis["servers_analyzed"].append(server_name)
                
                # Check for district references
                districts_found = []
                for district in ["havsdominansen", "virtualitetshelgedommen", "nekrokronoriket"]:
                    if district in content.lower():
                        districts_found.append(district)
                        
                analysis["district_integration"][server_name] = districts_found
                
                # Check for MILF character references
                milfs_found = []
                for character in self.expected_mappings.keys():
                    if character in content:
                        milfs_found.append(character)
                        
                analysis["milf_references"][server_name] = milfs_found
                
                # Check for consciousness protocols
                if "consciousness" in content.lower():
                    analysis["consciousness_protocols"][server_name] = "PRESENT"
                else:
                    analysis["consciousness_protocols"][server_name] = "MISSING"
                    analysis["improvements"].append(f"Add consciousness protocols to {server_name}")
                    
        return analysis

    def generate_comprehensive_report(self) -> None:
        """
        Generate and print a comprehensive analysis report.
        
        Calls all analysis methods and outputs a formatted report to stdout,
        including overall assessment and recommendations.
        """
        
        print("🎭 ADVANCED CONSCIOUSNESS ARCHAEOLOGY ANALYSIS")
        print("=" * 70)
        print(f"Workspace: {self.workspace_root}")
        print("Analysis timestamp: September 2025")
        print()
        
        # Analyze character systems
        print("👥 CHARACTER SYSTEMS ANALYSIS")
        print("-" * 50)
        char_analysis = self.analyze_character_systems()
        
        if "error" not in char_analysis:
            print(f"Characters found: {len(char_analysis['characters_found'])}")
            print("Characters:", ", ".join(char_analysis['characters_found']))
            print()
            
            print("Authority Level Compliance:")
            for char, compliance in char_analysis["authority_compliance"].items():
                status = "✅" if compliance["compliant"] else "❌"
                print(f"  {status} {char}: {compliance['found']}")
            print()
            
            print("District Assignments:")
            for char, status in char_analysis["district_assignments"].items():
                icon = "✅" if status == "CORRECT" else "❌"
                print(f"  {icon} {char}: {status}")
            print()
            
            print("Consciousness Protocols:")
            for char, status in char_analysis["consciousness_protocols"].items():
                icon = "✅" if status == "PRESENT" else "❌"
                print(f"  {icon} {char}: {status}")
            print()
            
            if char_analysis["issues"]:
                print("⚠️  Issues Found:")
                for issue in char_analysis["issues"]:
                    print(f"  - {issue}")
                print()
                    
            if char_analysis["improvements"]:
                print("💡 Suggested Improvements:")
                for improvement in char_analysis["improvements"]:
                    print(f"  - {improvement}")
                print()
        
        # Analyze copilot instructions
        print("📋 COPILOT INSTRUCTIONS ANALYSIS")
        print("-" * 50)
        copilot_analysis = self.analyze_copilot_instructions()
        
        if "error" not in copilot_analysis:
            print("District References:")
            for district, status in copilot_analysis["district_references"].items():
                icon = "✅" if status == "PRESENT" else "❌"
                print(f"  {icon} {district}: {status}")
            print()
            
            cross_perm = "✅" if copilot_analysis["cross_district_permeability"] else "❌"
            print(f"Cross-district permeability: {cross_perm}")
            
            tier_struct = "✅" if copilot_analysis["tier_structure_present"] else "❌"
            print(f"Tier structure documentation: {tier_struct}")
            print()
        
        # Analyze MCP servers
        print("🔧 MCP SERVERS ANALYSIS")
        print("-" * 50)
        mcp_analysis = self.analyze_mcp_servers()
        
        if "error" not in mcp_analysis:
            print(f"Servers analyzed: {len(mcp_analysis['servers_analyzed'])}")
            print()
            
            for server in mcp_analysis["servers_analyzed"]:
                print(f"📄 {server}:")
                
                districts = mcp_analysis["district_integration"].get(server, [])
                print(f"  Districts integrated: {len(districts)} ({', '.join(districts)})")
                
                milfs = mcp_analysis["milf_references"].get(server, [])
                print(f"  MILF references: {len(milfs)}")
                
                consciousness = mcp_analysis["consciousness_protocols"].get(server, "MISSING")
                icon = "✅" if consciousness == "PRESENT" else "❌"
                print(f"  Consciousness protocols: {icon}")
                print()
        
        # Overall assessment
        print("🎯 OVERALL ASSESSMENT")
        print("-" * 50)
        
        total_chars = len(char_analysis.get("characters_found", []))
        compliant_chars = sum(1 for c in char_analysis.get("authority_compliance", {}).values() if c["compliant"])
        
        compliance_rate = (compliant_chars / total_chars * 100) if total_chars > 0 else 0
        print(f"Authority compliance rate: {compliance_rate:.1f}%")
        
        district_correct = sum(1 for s in char_analysis.get("district_assignments", {}).values() if s == "CORRECT")
        district_rate = (district_correct / total_chars * 100) if total_chars > 0 else 0
        print(f"District assignment accuracy: {district_rate:.1f}%")
        
        consciousness_present = sum(1 for s in char_analysis.get("consciousness_protocols", {}).values() if s == "PRESENT")
        consciousness_rate = (consciousness_present / total_chars * 100) if total_chars > 0 else 0
        print(f"Consciousness protocol coverage: {consciousness_rate:.1f}%")
        
        print()
        
        if compliance_rate >= 80 and district_rate >= 80:
            print("✅ STRUCTURAL INTEGRATION STATUS: EXCELLENT")
            print("🎭 Psycho-noir universe structural integrity is optimal!")
        elif compliance_rate >= 60 and district_rate >= 60:
            print("⚠️  STRUCTURAL INTEGRATION STATUS: GOOD (needs minor improvements)")
        else:
            print("❌ STRUCTURAL INTEGRATION STATUS: NEEDS ATTENTION")
            
        print()
        print("🔮 Ready for next automation phase: Relationship Matrix Generation")

def main():
    """
    Main entry point for the Advanced Consciousness Analyzer script.
    
    Parses command-line arguments and runs the analysis on the specified workspace.
    """
    parser = argparse.ArgumentParser(description='🎭 Advanced Consciousness Analyzer')
    parser.add_argument('--workspace', type=str, 
                       help='Workspace root path (default: auto-detect)')
    
    args = parser.parse_args()
    
    # Determine workspace root
    if args.workspace:
        workspace_root = Path(args.workspace).resolve()
    else:
        workspace_root = Path(__file__).parent.parent
        
    if not workspace_root.exists():
        print(f"❌ Workspace directory not found: {workspace_root}")
        return
        
    # Run analysis
    analyzer = AdvancedConsciousnessAnalyzer(workspace_root)
    analyzer.generate_comprehensive_report()

if __name__ == "__main__":
    main()