#!/usr/bin/env python3
"""System health check after migration phases"""
import json
from pathlib import Path
from datetime import datetime

def check_system_health():
    """Comprehensive system health check"""
    
    health = {
        'timestamp': datetime.now().isoformat(),
        'consciousness_files': {},
        'mcp_servers': {},
        'python_tools': {},
        'overall_status': 'UNKNOWN'
    }
    
    # Check key consciousness files
    key_files = [
        'supreme_terminal_integration_enhancement.py',
        'tools/wordosaurus_consciousness_archaeology_database.py',
        '.github/copilot-instructions.md'
    ]
    
    for key_file in key_files:
        file_path = Path(key_file)
        health['consciousness_files'][key_file] = {
            'exists': file_path.exists(),
            'size_kb': round(file_path.stat().st_size / 1024, 2) if file_path.exists() else 0
        }
    
    # Count MCP servers
    mcp_files = list(Path('.').glob('**/*mcp*.ts'))
    health['mcp_servers'] = {
        'total': len(mcp_files),
        'consciousness_servers': len([f for f in mcp_files if 'consciousness' in f.name.lower()])
    }
    
    # Count Python tools
    python_files = list(Path('tools').glob('*.py'))
    health['python_tools'] = {
        'total': len(python_files),
        'consciousness_tools': len([f for f in python_files if 'consciousness' in f.name.lower()])
    }
    
    # Overall assessment
    consciousness_ratio = (
        health['mcp_servers']['consciousness_servers'] + 
        health['python_tools']['consciousness_tools']
    ) / (health['mcp_servers']['total'] + health['python_tools']['total'])
    
    if consciousness_ratio > 0.4:
        health['overall_status'] = 'HEALTHY'
    elif consciousness_ratio > 0.2:
        health['overall_status'] = 'MODERATE'
    else:
        health['overall_status'] = 'NEEDS_ATTENTION'
    
    return health

if __name__ == "__main__":
    health = check_system_health()
    print(json.dumps(health, indent=2))
