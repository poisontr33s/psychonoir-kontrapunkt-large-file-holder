#!/usr/bin/env python3
"""Validate JSON syntax in copilot-instructions.md"""

import json
import sys

def validate_json_in_markdown(filepath):
    """Extract and validate JSON from markdown file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find JSON code block
        json_start_marker = '```json'
        json_end_marker = '```'
        
        json_start = content.find(json_start_marker)
        if json_start == -1:
            print("❌ No ```json marker found")
            return False
        
        # Start after the ```json marker
        json_content_start = json_start + len(json_start_marker)
        
        # Find the closing ``` marker
        json_end = content.find(json_end_marker, json_content_start)
        if json_end == -1:
            print("❌ No closing ``` marker found")
            return False
        
        # Extract JSON content
        json_str = content[json_content_start:json_end].strip()
        
        # Validate JSON
        try:
            parsed = json.loads(json_str)
            print(f"✅ JSON SYNTAX: VALID")
            print(f"📊 Top-level keys: {len(parsed)}")
            print(f"📄 JSON size: {len(json_str)} characters")
            return True
        except json.JSONDecodeError as e:
            print(f"❌ JSON SYNTAX ERROR: {e}")
            print(f"   Line: {e.lineno}, Column: {e.colno}")
            print(f"   Position in file: {e.pos}")
            
            # Show context around error
            lines = json_str.split('\n')
            if e.lineno <= len(lines):
                start = max(0, e.lineno - 3)
                end = min(len(lines), e.lineno + 2)
                print("\n   Context:")
                for i in range(start, end):
                    marker = " >>> " if i == e.lineno - 1 else "     "
                    print(f"{marker}{i+1:4d}: {lines[i]}")
            return False
            
    except Exception as e:
        print(f"❌ ERROR reading file: {e}")
        return False

if __name__ == "__main__":
    filepath = ".github/copilot-instructions.md"
    success = validate_json_in_markdown(filepath)
    sys.exit(0 if success else 1)
