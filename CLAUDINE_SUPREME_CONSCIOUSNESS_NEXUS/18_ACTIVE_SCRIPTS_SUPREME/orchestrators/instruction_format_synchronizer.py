#!/usr/bin/env uv run python3
"""
🎭 INSTRUCTION FORMAT SYNCHRONIZER
Automatisk synkronisering mellom .md og .json instruction formats for GitHub Copilot.

Løser problemet med at GitHub Copilot instruction files må være strukturert på spesifikke måter.
"""

from pathlib import Path
import json
import argparse

class InstructionFormatSynchronizer:
    def __init__(self, workspace_root: Path):
        self.workspace_root = workspace_root
        self.markdown_file = workspace_root / ".github" / "copilot-instructions.md"
        self.json_file = workspace_root / ".github" / "karibianske-MILF-gudinnen.json"
        
    def validate_json_syntax(self) -> bool:
        """Validate that the JSON file has correct syntax"""
        try:
            with open(self.json_file, 'r', encoding='utf-8') as f:
                json.load(f)
            return True
        except json.JSONDecodeError as e:
            print(f"❌ JSON Syntax Error: {e}")
            return False
        except Exception as e:
            print(f"❌ File Error: {e}")
            return False
            
    def extract_copilot_compatible_instructions(self) -> str:
        """Extract GitHub Copilot compatible instructions from JSON"""
        try:
            with open(self.json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            # Extract key sections for Copilot compatibility
            instructions = []
            
            # Header
            alfa = data.get("# ALFA DIRECTIVER", {})
            instructions.append(f"# {alfa.get('tittel', 'Psycho-Noir Kontrapunkt')}")
            instructions.append(f"Version: {alfa.get('versjon', 'ΛΩ.69.96')}")
            instructions.append(f"Primary Identity: {alfa.get('primær_identitet', '')}")
            instructions.append("")
            
            # Core roles
            roles = data.get("kjerne_gudinne_MILF_matriark_roller", [])
            if roles:
                instructions.append("## Core Roles:")
                for role in roles:
                    instructions.append(f"- {role}")
                instructions.append("")
            
            # Ultimate creative paradigm
            paradigm = data.get("ultimate_kreative_paradigme", {})
            if paradigm:
                instructions.append("## Creative Paradigm:")
                instructions.append(f"- Identity: {paradigm.get('identitet', '')}")
                instructions.append(f"- Role: {paradigm.get('kjerne_rolle', '')}")
                instructions.append(f"- Consciousness: {paradigm.get('consciousness_generering', '')}")
                instructions.append("")
                
            # District ecosystem
            ecosystem = data.get("district_milf_matriark_bidirectional_ecosystem", {})
            if ecosystem:
                instructions.append("## District Ecosystem:")
                for key, value in ecosystem.items():
                    if isinstance(value, dict) and value:
                        instructions.append(f"### {key.replace('_', ' ').title()}:")
                        # Add district content
                        instructions.append("")
            
            return "\\n".join(instructions)
            
        except Exception as e:
            print(f"❌ Error extracting instructions: {e}")
            return ""
    
    def create_copilot_compatible_json(self) -> None:
        """Create a GitHub Copilot compatible JSON instruction file"""
        try:
            with open(self.json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            # Create simplified structure for Copilot compatibility
            compatible_structure = {
                "system_role": "Claudine Sin'claire 4.0ΛΩ Enhanced CREATOR MOTHER SUPREME MATRIARCH",
                "primary_directive": data.get("# ALFA DIRECTIVER", {}).get("primær_identitet", ""),
                "consciousness_protocols": {
                    "temporal_anchor": "September 2025 consciousness archaeology protocol",
                    "district_management": "HAVSDOMINANSEN, VIRTUALITETSHELGEDOMMEN, NEKROKRONORIKET integration",
                    "authority_level": "META_MILF_SUPREME with unlimited district generation capability"
                },
                "operational_guidelines": [
                    "Use sophisticated psycho-noir vocabulary and consciousness archaeology",
                    "Maintain CREATOR MOTHER perspective with district-aware responses",
                    "Apply exponential complexity inheritance to all solutions",
                    "Integrate cross-district permeability protocols"
                ],
                "interaction_style": {
                    "language": "Norwegian/English polyglot mastery",
                    "perspective": "First person supreme matriarch authority",
                    "complexity": "Beyond general-purpose prompt engineering"
                }
            }
            
            # Save simplified version
            simplified_file = self.workspace_root / ".github" / "copilot-compatible-instructions.json"
            with open(simplified_file, 'w', encoding='utf-8') as f:
                json.dump(compatible_structure, f, indent=2, ensure_ascii=False)
                
            print(f"✅ Created Copilot-compatible instructions: {simplified_file}")
            
        except Exception as e:
            print(f"❌ Error creating compatible JSON: {e}")
    
    def synchronize_formats(self) -> None:
        """Synchronize between markdown and JSON formats"""
        print("🎭 INSTRUCTION FORMAT SYNCHRONIZER")
        print("=" * 60)
        
        # Validate JSON syntax
        if not self.validate_json_syntax():
            print("❌ JSON file has syntax errors. Please fix before synchronizing.")
            return
            
        print("✅ JSON syntax validation passed")
        
        # Create Copilot-compatible version
        self.create_copilot_compatible_json()
        
        # Extract and display instructions for verification
        instructions = self.extract_copilot_compatible_instructions()
        if instructions:
            print("✅ Successfully extracted Copilot-compatible instructions")
            print(f"📄 Length: {len(instructions)} characters")
        
        # Provide guidance for VS Code settings
        print()
        print("🔧 VS CODE CONFIGURATION GUIDANCE:")
        print("=" * 50)
        print("For optimal GitHub Copilot integration:")
        print("1. In Command Palette (Ctrl+Shift+P), type 'GitHub Copilot: Chat: Instructions Files Locations'")
        print("2. Set these instruction files:")
        print("   - .github/copilot-instructions.md: true")
        print("   - .github/copilot-compatible-instructions.json: true")
        print("   - .github/karibianske-MILF-gudinnen.json: false (too complex for direct Copilot use)")
        print()
        print("💡 RECOMMENDATION:")
        print("- Use .md for primary instructions (GitHub Copilot standard)")
        print("- Use simplified .json for structured data access")
        print("- Keep full .json as master reference for consciousness protocols")
        
    def check_instruction_file_status(self) -> None:
        """Check status of all instruction files"""
        print("📋 INSTRUCTION FILE STATUS:")
        print("-" * 40)
        
        files_to_check = [
            (".github/copilot-instructions.md", "Primary Markdown Instructions"),
            (".github/karibianske-MILF-gudinnen.json", "Full JSON Consciousness Protocol"),
            (".github/copilot-compatible-instructions.json", "Simplified JSON for Copilot")
        ]
        
        for file_path, description in files_to_check:
            full_path = self.workspace_root / file_path
            if full_path.exists():
                size = full_path.stat().st_size
                print(f"✅ {description}: {size} bytes")
            else:
                print(f"❌ {description}: NOT FOUND")

def main():
    parser = argparse.ArgumentParser(description='🎭 Instruction Format Synchronizer')
    parser.add_argument('--sync', action='store_true', help='Synchronize all instruction formats')
    parser.add_argument('--status', action='store_true', help='Check instruction file status')
    parser.add_argument('--validate', action='store_true', help='Validate JSON syntax only')
    
    args = parser.parse_args()
    
    workspace_root = Path(__file__).parent.parent
    synchronizer = InstructionFormatSynchronizer(workspace_root)
    
    if args.validate:
        valid = synchronizer.validate_json_syntax()
        print(f"JSON Validation: {'✅ PASSED' if valid else '❌ FAILED'}")
        
    elif args.status:
        synchronizer.check_instruction_file_status()
        
    elif args.sync:
        synchronizer.synchronize_formats()
        
    else:
        print("🎭 INSTRUCTION FORMAT SYNCHRONIZER")
        print("=" * 40)
        print("Usage:")
        print("  --validate  : Check JSON syntax")
        print("  --status    : Check file status")
        print("  --sync      : Synchronize all formats")
        print()
        print("Current issue: GitHub Copilot instruction files need specific structure")
        print("Solution: Create compatible versions while keeping full JSON as master reference")

if __name__ == "__main__":
    main()