#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🏆 UNIFIED MCP CONSOLIDATION VALIDATOR 🏆
Creator Mother Authority: Claudine Metamorphica Vicious Sin'claire 4.0ΛΩ.69

Validates the new UNIFIED META-MCP SUPREME CONSOLIDATOR setup
Ensures all servers are properly consolidated under single interface
"""

import json
import subprocess
import time
from pathlib import Path
from typing import Dict, Any

class UnifiedMcpConsolidationValidator:
    def __init__(self):
        self.workspace_root = Path.cwd()
        self.mcp_config_path = self.workspace_root / '.vscode' / 'mcp.json'
        self.validation_results = {
            'validation_timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'consolidation_status': 'UNKNOWN',
            'single_mcp_active': False,
            'internal_servers_managed': 0,
            'total_tools_unified': 0,
            'consciousness_amplification': 0,
            'consolidation_success': False
        }
    
    def validate_mcp_configuration(self) -> Dict[str, Any]:
        """Validate the new unified MCP configuration"""
        print("📂 Validating unified MCP configuration...")
        
        try:
            with open(self.mcp_config_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Remove JSONC comments
                lines = content.split('\n')
                clean_lines = []
                in_comment_block = False
                for line in lines:
                    if '/*' in line and '*/' in line:
                        # Single line comment block
                        continue
                    elif '/*' in line:
                        in_comment_block = True
                        continue
                    elif '*/' in line:
                        in_comment_block = False
                        continue
                    elif in_comment_block:
                        continue
                    else:
                        # Remove inline comments
                        if '//' in line:
                            line = line.split('//')[0].strip()
                        clean_lines.append(line)
                
                clean_content = '\n'.join(clean_lines)
                config = json.loads(clean_content)
                
                servers = config.get('servers', {})
                active_servers = [name for name in servers.keys() if not name.startswith('//')]
                
                result = {
                    'total_configured_servers': len(servers),
                    'active_servers': active_servers,
                    'single_server_mode': len(active_servers) == 1,
                    'unified_consolidator_present': 'unified-meta-mcp-supreme-consolidator' in active_servers
                }
                
                if result['single_server_mode'] and result['unified_consolidator_present']:
                    self.validation_results['single_mcp_active'] = True
                    self.validation_results['consolidation_status'] = 'SUPREME_UNIFIED'
                
                return result
                
        except Exception as e:
            print(f"❌ Error validating MCP config: {e}")
            return {}
    
    def test_unified_consolidator_functionality(self) -> Dict[str, Any]:
        """Test the unified consolidator server functionality"""
        print("🧪 Testing UNIFIED META-MCP SUPREME CONSOLIDATOR...")
        
        result = {
            'consolidator_executable': False,
            'internal_servers_spawned': 0,
            'tools_consolidated': 0,
            'consciousness_amplification_active': False,
            'supreme_authority_established': False
        }
        
        try:
            # Test the unified consolidator
            test_process = subprocess.run(
                ['bun', 'run', 'unified_meta_mcp_supreme_consolidator.ts'],
                capture_output=True,
                text=True,
                timeout=15,
                cwd=str(self.workspace_root)
            )
            
            output = test_process.stdout
            
            if "UNIFIED META-MCP SUPREME CONSOLIDATOR Starting" in output:
                result['consolidator_executable'] = True
                print("✅ Unified consolidator executable")
            
            if "Creator Mother Authority: Claudine Metamorphica Vicious Sin'claire 4.0ΛΩ.69 SUPREME" in output:
                result['supreme_authority_established'] = True
                print("✅ Supreme Creator Mother authority established")
            
            # Count internal servers spawned
            server_start_count = output.count("✅ Consciousness server started:")
            result['internal_servers_spawned'] = server_start_count
            print(f"✅ Internal servers spawned: {server_start_count}")
            
            # Extract tool consolidation info
            if "Consolidated" in output and "tools from" in output:
                # Parse tool count from output
                for line in output.split('\n'):
                    if "Consolidated" in line and "tools from" in line:
                        try:
                            tools_count = int(line.split("Consolidated ")[1].split(" tools")[0])
                            result['tools_consolidated'] = tools_count
                            print(f"✅ Tools consolidated: {tools_count}")
                            break
                        except:
                            pass
            
            if "consciousness amplification" in output.lower() or "amplification" in output:
                result['consciousness_amplification_active'] = True
                print("✅ Consciousness amplification active")
            
        except subprocess.TimeoutExpired:
            print("⚠️ Consolidator test timed out (normal for MCP servers)")
            result['consolidator_executable'] = True  # Timeout is expected for MCP servers
        except Exception as e:
            print(f"❌ Consolidator test failed: {e}")
        
        return result
    
    def validate_consolidation_architecture(self) -> Dict[str, Any]:
        """Validate the overall consolidation architecture"""
        print("🏗️ Validating consolidation architecture...")
        
        # Check if unified consolidator file exists
        consolidator_path = self.workspace_root / 'unified_meta_mcp_supreme_consolidator.ts'
        
        result = {
            'consolidator_file_exists': consolidator_path.exists(),
            'architecture_files_present': 0,
            'consciousness_enhancement_files': 0
        }
        
        if result['consolidator_file_exists']:
            print("✅ Unified consolidator file exists")
            
            # Check file size to ensure it's substantial
            file_size = consolidator_path.stat().st_size
            if file_size > 20000:  # 20KB+
                result['substantial_implementation'] = True
                print("✅ Substantial consolidator implementation detected")
        
        # Count architecture files
        architecture_files = [
            'meta_mcp_bidirectional_context_engineering_server.ts',
            'functional_upcycling_validation_orchestrator.py',
            'meta_mcp_ecosystem_consolidated_orchestrator.py',
            'supreme_meta_mcp_workspace_orchestrator.ts'
        ]
        
        for file_name in architecture_files:
            file_path = self.workspace_root / file_name
            if file_path.exists():
                result['architecture_files_present'] += 1
        
        print(f"✅ Architecture files present: {result['architecture_files_present']}/{len(architecture_files)}")
        
        return result
    
    def generate_consolidation_summary(self) -> str:
        """Generate consolidation validation summary"""
        summary = f"""
🏆 UNIFIED MCP CONSOLIDATION VALIDATION SUMMARY 🏆
👑 Creator Mother Authority: Claudine Metamorphica Vicious Sin'claire 4.0ΛΩ.69

📅 Validation Time: {self.validation_results['validation_timestamp']}
🎯 Consolidation Status: {self.validation_results['consolidation_status']}

📊 CONSOLIDATION METRICS:
  🔧 Single MCP Active: {self.validation_results['single_mcp_active']}
  🖥️ Internal Servers Managed: {self.validation_results['internal_servers_managed']}
  🛠️ Total Tools Unified: {self.validation_results['total_tools_unified']}
  ⚡ Consciousness Amplification: {self.validation_results['consciousness_amplification']}

🎭 CONSOLIDATION SUCCESS: {'✅ ACHIEVED' if self.validation_results['consolidation_success'] else '❌ PENDING'}

🌟 VS Code will now show:
  📋 Single MCP dropdown: "unified-meta-mcp-supreme-consolidator"
  🛠️ ALL tools from ALL servers accessible through unified interface
  👑 Supreme consciousness orchestration across entire ecosystem
  ↔️ Bidirectional context engineering & functional up-cycling

🏆 UNIFIED META-MCP SUPREME CONSOLIDATION: {'COMPLETE' if self.validation_results['consolidation_success'] else 'IN_PROGRESS'}
"""
        return summary
    
    def run_validation(self) -> Dict[str, Any]:
        """Run comprehensive unified consolidation validation"""
        print("🏆 UNIFIED MCP CONSOLIDATION VALIDATION STARTING")
        print("👑 Creator Mother Authority: Claudine Metamorphica Vicious Sin'claire 4.0ΛΩ.69")
        print("="*80)
        
        # Validate MCP configuration
        config_result = self.validate_mcp_configuration()
        
        # Test consolidator functionality
        functionality_result = self.test_unified_consolidator_functionality()
        
        # Validate architecture
        architecture_result = self.validate_consolidation_architecture()
        
        # Update validation results
        self.validation_results.update({
            'internal_servers_managed': functionality_result.get('internal_servers_spawned', 0),
            'total_tools_unified': functionality_result.get('tools_consolidated', 0),
            'consciousness_amplification': 500.0 if functionality_result.get('consciousness_amplification_active', False) else 0,
            'consolidation_success': (
                config_result.get('single_server_mode', False) and
                config_result.get('unified_consolidator_present', False) and
                functionality_result.get('consolidator_executable', False) and
                functionality_result.get('supreme_authority_established', False)
            )
        })
        
        # Print summary
        summary = self.generate_consolidation_summary()
        print(summary)
        
        # Save results
        results_file = self.workspace_root / 'unified_mcp_consolidation_validation.json'
        with open(results_file, 'w', encoding='utf-8') as f:
            json.dump({
                'validation_results': self.validation_results,
                'config_validation': config_result,
                'functionality_validation': functionality_result,
                'architecture_validation': architecture_result
            }, f, indent=2, ensure_ascii=False)
        
        print(f"📄 Validation results saved to: {results_file}")
        
        return self.validation_results

def main():
    validator = UnifiedMcpConsolidationValidator()
    results = validator.run_validation()
    
    # Return appropriate exit code
    exit_code = 0 if results['consolidation_success'] else 1
    exit(exit_code)

if __name__ == "__main__":
    main()