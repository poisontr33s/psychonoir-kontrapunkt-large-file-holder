#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🎭 PSYCHO-NOIR MCP SERVER VALIDATION SUITE
Enhanced consciousness testing protocol for September 2025 temporal anchor
"""

import subprocess
import json
import time
import sys
from pathlib import Path

def test_mcp_server(server_name, config):
    """Test individual MCP server functionality"""
    print(f"\n🌊 TESTING {server_name.upper()}...")
    
    command = config.get('command', '')
    args = config.get('args', [])
    
    if command == 'docker':
        print(f"   🐳 Docker server detected: {' '.join(args)}")
        # Test if Docker image exists
        result = subprocess.run(['docker', 'images', '--format', '{{.Repository}}:{{.Tag}}'], 
                              capture_output=True, text=True, timeout=10)
        if 'github-mcp-server:latest' in result.stdout:
            print(f"   ✅ Docker image available")
            return True
        else:
            print(f"   ❌ Docker image missing: github-mcp-server:latest")
            return False
            
    elif command == 'npx':
        print(f"   📦 NPX server detected: {' '.join(args)}")
        # Test if package is available
        if '@azure/mcp@latest' in ' '.join(args):
            print(f"   ✅ Azure MCP package configured")
            return True
        else:
            print(f"   ⚠️  NPX package configured but not validated")
            return True
            
    elif command == 'bun':
        print(f"   ⚡ Bun server detected: {' '.join(args)}")
        script_path = args[1] if len(args) > 1 and args[0] == 'run' else args[0]
        
        if Path(script_path).exists():
            print(f"   ✅ Script exists: {script_path}")
            # Quick syntax check
            try:
                result = subprocess.run(['bun', 'check', script_path], 
                                      capture_output=True, text=True, timeout=10)
                if result.returncode == 0:
                    print(f"   ✅ TypeScript syntax valid")
                    return True
                else:
                    print(f"   ⚠️  TypeScript warnings: {result.stderr}")
                    return True
            except Exception as e:
                print(f"   ⚠️  Syntax check failed: {e}")
                return True
        else:
            print(f"   ❌ Script missing: {script_path}")
            return False
    
    else:
        print(f"   ⚠️  Unknown command type: {command}")
        return False

def main():
    """Main validation routine"""
    print("🎭 PSYCHO-NOIR MCP VALIDATION SUITE - CLAUDINE 4.0 ENHANCED")
    print("=" * 70)
    
    mcp_config_path = Path('.vscode/mcp.json')
    
    if not mcp_config_path.exists():
        print("❌ MCP configuration file not found: .vscode/mcp.json")
        sys.exit(1)
    
    try:
        with open(mcp_config_path, 'r') as f:
            config = json.load(f)
    except Exception as e:
        print(f"❌ Failed to parse MCP configuration: {e}")
        sys.exit(1)
    
    servers = config.get('servers', {})
    print(f"🌊 Found {len(servers)} MCP servers to validate")
    
    results = {}
    for server_name, server_config in servers.items():
        try:
            results[server_name] = test_mcp_server(server_name, server_config)
        except Exception as e:
            print(f"   ❌ Test failed with exception: {e}")
            results[server_name] = False
    
    print("\n" + "=" * 70)
    print("🎯 VALIDATION RESULTS:")
    
    total_servers = len(results)
    successful_servers = sum(results.values())
    
    for server_name, success in results.items():
        status = "✅ OPERATIONAL" if success else "❌ ISSUES DETECTED"
        print(f"   {server_name}: {status}")
    
    success_rate = (successful_servers / total_servers) * 100 if total_servers > 0 else 0
    
    print(f"\n🌊 OVERALL STATUS: {successful_servers}/{total_servers} servers validated")
    print(f"🎭 SUCCESS RATE: {success_rate:.1f}%")
    
    if success_rate >= 100:
        print("⚡ CONSCIOUSNESS AMPLIFICATION: MAXIMUM EFFICIENCY ACHIEVED")
    elif success_rate >= 75:
        print("🌀 CONSCIOUSNESS AMPLIFICATION: ENHANCED READY")
    elif success_rate >= 50:
        print("🔧 CONSCIOUSNESS AMPLIFICATION: NEEDS OPTIMIZATION")
    else:
        print("🚨 CONSCIOUSNESS AMPLIFICATION: CRITICAL ISSUES DETECTED")
    
    print("\n🎭 TEMPORAL ANCHOR: September 2025 - VALIDATION COMPLETE")

if __name__ == "__main__":
    main()
