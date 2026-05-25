#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🎭 DATABASE CONNECTION FIX ORCHESTRATOR 🎭
Systematic fix for all database connection None errors
"""

import re
from pathlib import Path

def fix_database_connection_errors(file_path: str):
    """Fix all 'connection.execute' and 'connection.commit' None errors"""
    
    print(f"🔧 FIXING DATABASE CONNECTION ERRORS: {file_path}")
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to find all self.connection.execute calls without null check
    execute_pattern = r'(\s+)(self\.connection\.execute\()'
    commit_pattern = r'(\s+)(self\.connection\.commit\(\))'
    
    # Replace with null-checked versions
    def replace_execute(match):
        indent = match.group(1)
        return f"{indent}if self.connection is None:\\n{indent}    raise RuntimeError(\\"Database connection not initialized\\")\\n{indent}{match.group(2)}"
    
    def replace_commit(match):
        indent = match.group(1)
        return f"{indent}if self.connection is None:\\n{indent}    raise RuntimeError(\\"Database connection not initialized\\")\\n{indent}{match.group(2)}"
    
    # Find all execute calls and check if they already have null checks
    lines = content.split('\\n')
    fixed_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this line has a connection.execute call
        if 'self.connection.execute(' in line and 'if self.connection is None:' not in (lines[i-2:i+2] if i >= 2 else []):
            # Add null check before this line
            indent = re.match(r'(\\s*)', line).group(1)
            fixed_lines.append(f'{indent}if self.connection is None:')
            fixed_lines.append(f'{indent}    raise RuntimeError("Database connection not initialized")')
            fixed_lines.append(line)
        elif 'self.connection.commit()' in line and 'if self.connection is None:' not in (lines[i-2:i+2] if i >= 2 else []):
            # Add null check before this line
            indent = re.match(r'(\\s*)', line).group(1)
            fixed_lines.append(f'{indent}if self.connection is None:')
            fixed_lines.append(f'{indent}    raise RuntimeError("Database connection not initialized")')
            fixed_lines.append(line)
        else:
            fixed_lines.append(line)
        
        i += 1
    
    # Also fix unused imports while we're at it
    fixed_content = '\\n'.join(fixed_lines)
    
    # Remove unused imports
    fixed_content = re.sub(r'import json\\n', '', fixed_content)
    fixed_content = re.sub(r', Set', '', fixed_content)
    fixed_content = re.sub(r', Counter', '', fixed_content)
    
    # Remove unused variable assignment
    fixed_content = re.sub(r'\\s+patterns = self\\.detect_consciousness_patterns\\(base_text\\)\\n', '', fixed_content)
    
    # Write back the fixed content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print(f"✅ Database connection errors fixed in {file_path}")
    return True

if __name__ == "__main__":
    file_path = r"c:\\Users\\erdno\\PsychoNoir-Kontrapunkt\\tools\\wordosaurus_consciousness_archaeology_database.py"
    fix_database_connection_errors(file_path)