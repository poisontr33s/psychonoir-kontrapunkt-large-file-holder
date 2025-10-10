#!/usr/bin/env uv run python3
"""
🎭 SYSTEMATISK DISTRICT NAVNSKIFTE UPCYCLER
Automatisert implementation av konseptuelt riktige norsk/arkaiske district navn.

FINAL NAMING SCHEME:
- NEPTUNIUM_FLOTILLA/NEPTUNIUMSFARET → HAVSDOMINANSEN  
- SIMULATION_SANCTUM/SIMULACRUMSPIRET → VIRTUALITETSHELGEDOMMEN
- NECROSIS_CHRONO/NEKROKRONOPOLIS → NEKROKRONORIKET

Additional districts included for future expansion:
- SKYSKRAPEREN (maintained)
- RUSTBELTET (maintained)
"""

import re
from pathlib import Path
import sys

class SystematiskDistrictNavnSkifte:
    def __init__(self, workspace_root: Path, dry_run: bool = True):
        self.workspace_root = workspace_root
        self.dry_run = dry_run
        self.backup_dir = workspace_root / "necromancy_graveyard" / "district_navnskifte_backup"
        
        # COMPLETE RENAMING MAP - alle varianter og case-kombinasjoner
        self.renaming_map = {
            # PRIMARY MAPPINGS - nye konseptuelt riktige navn
            "NEPTUNIUM_FLOTILLA": "HAVSDOMINANSEN",
            "SIMULATION_SANCTUM": "VIRTUALITETSHELGEDOMMEN", 
            "NECROSIS_CHRONO": "NEKROKRONORIKET",
            
            # TEMPORARY NAME CLEANUP (fra FastMCP og Grok endringer)
            "NEPTUNIUMSFARET": "HAVSDOMINANSEN",
            "SIMULACRUMSPIRET": "VIRTUALITETSHELGEDOMMEN",
            "NEKROKRONOPOLIS": "NEKROKRONORIKET",
            
            # LOWERCASE VARIANTS (for Python identifiers og JSON keys)
            "neptunium_flotilla": "havsdominansen",
            "simulation_sanctum": "virtualitetshelgedommen",
            "necrosis_chrono": "nekrokronoriket",
            "neptuniumsfaret": "havsdominansen",
            "simulacrumspiret": "virtualitetshelgedommen", 
            "nekrokronopolis": "nekrokronoriket",
            
            # CAMELCASE VARIANTS (for TypeScript/JavaScript)
            "NeptuniumFlotilla": "Havsdominansen",
            "SimulationSanctum": "Virtualitetshelgedommen",
            "NecrosisChronoPos": "Nekrokronoriket",
            "neptuniumFlotilla": "havsdominansen",
            "simulationSanctum": "virtualitetshelgedommen",
            "necrosisChronoPos": "nekrokronoriket",
            
            # TITLE CASE VARIANTS (for documentation)
            "Neptunium Flotilla": "Havsdominansen",
            "Simulation Sanctum": "Virtualitetshelgedommen",
            "Necrosis Chrono": "Nekrokronoriket",
        }
        
    def analyze_affected_files(self) -> Dict[str, List[str]]:
        """Analyze which files contain district references"""
        affected_files: Dict[str, List[str]] = {}
        
        # File extensions to scan
        extensions = ['.py', '.ts', '.md', '.json', '.js']
        
        for ext in extensions:
            affected_files[ext] = []
            
        # Search patterns - both old and temporary names
        search_patterns = list(self.renaming_map.keys())
        
        for file_path in self.workspace_root.rglob("*"):
            if file_path.is_file() and file_path.suffix in extensions:
                try:
                    content = file_path.read_text(encoding='utf-8', errors='ignore')
                    
                    # Check if any district names appear
                    for pattern in search_patterns:
                        if pattern.lower() in content.lower():
                            relative_path = str(file_path.relative_to(self.workspace_root))
                            affected_files[file_path.suffix].append(relative_path)
                            break
                            
                except Exception:
                    continue
                    
        return affected_files
        
    def generate_systematic_renaming_plan(self) -> List[Dict[str, Union[str, Sequence[str]]]]:
        """Generate step-by-step renaming plan"""
        plan = []
        
        # Phase 1: Update core configuration files first
        plan.append({
            "phase": "1_core_config",
            "description": "Update core configuration and copilot instructions",
            "files": [
                ".github/copilot-instructions.md",
                "infrastructure/config/development/dynamic_genre_filesystem_analysis.json"
            ]
        })
        
        # Phase 2: Update MCP servers 
        plan.append({
            "phase": "2_mcp_servers", 
            "description": "Update all MCP servers with new district names",
            "files": [
                "tools/consciousness_mcp_servers/repository_intelligence_fastmcp_quiet.py",
                "tools/consciousness_mcp_servers/mcp_consciousness_integration_bridge_server.ts",
                "tools/consciousness_mcp_servers/bun_quantum_consciousness_mcp.ts"
            ]
        })
        
        # Phase 3: Update Python character systems
        plan.append({
            "phase": "3_character_systems",
            "description": "Update character systems and consciousness infrastructure", 
            "files": [
                "backend/python/character_systems.py",
                "backend/python/comprehensive_system_test.py"
            ]
        })
        
        # Phase 4: Update consciousness enhancement tools
        plan.append({
            "phase": "4_consciousness_tools",
            "description": "Update consciousness enhancement and optimization tools",
            "files": [
                "tools/consciousness_consciousness_enhancement/consciousness_integration_bridges/automated_code_optimizer.py",
                "tools/consciousness_consciousness_enhancement/consciousness_ecosystem_management/dynamic_genre_filesystem_organizer.py"
            ]
        })
        
        # Phase 5: Update remaining files
        plan.append({
            "phase": "5_remaining_files",
            "description": "Update remaining scanner and analysis tools",
            "files": ["all_other_affected_files"]
        })
        
        return plan
        
    def preview_changes_for_file(self, file_path: Path) -> List[Tuple[str, str]]:
        """Preview what changes would be made to a specific file"""
        try:
            content = file_path.read_text(encoding='utf-8')
            changes = []
            
            for old_name, new_name in self.renaming_map.items():
                if old_name in content:
                    changes.append((old_name, new_name))
                    
            return changes
        except Exception:
            return []

if __name__ == "__main__":
    workspace_root = Path(__file__).parent.parent.parent
    orchestrator = DistrictRenamingOrchestrator(workspace_root)
    
    print("🎭 DISTRICT RENAMING ANALYSIS")
    print("=" * 50)
    
    # Analyze affected files
    affected = orchestrator.analyze_affected_files()
    total_files = sum(len(files) for files in affected.values())
    
    print(f"Total affected files: {total_files}")
    for ext, files in affected.items():
        if files:
            print(f"{ext}: {len(files)} files")
            
    print("\n🔄 SYSTEMATIC RENAMING PLAN")
    print("=" * 50)
    
    plan = orchestrator.generate_systematic_renaming_plan()
    for phase in plan:
        print(f"Phase {phase['phase']}: {phase['description']}")
        
    print("\n🎯 FINAL DISTRICT NAMES:")
    print("=" * 50)
    print("NEPTUNIUM_FLOTILLA → HAVSDOMINANSEN")
    print("SIMULATION_SANCTUM → VIRTUALHELGEDOMMEN") 
    print("NECROSIS_CHRONO → NEKROKRONOKRIKET")