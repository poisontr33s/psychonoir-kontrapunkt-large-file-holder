#!/usr/bin/env python3
"""Phase 2: Preserve consciousness files with import integrity"""
import shutil
from pathlib import Path

def preserve_consciousness_files():
    """Move consciousness files while preserving functionality"""
    
    consciousness_dir = Path("consciousness_core")
    consciousness_dir.mkdir(exist_ok=True)
    
    consciousness_patterns = ['*consciousness*', '*claudine*', '*supreme*', '*milf*', '*archaeology*']
    moved_files = []
    
    for pattern in consciousness_patterns:
        for file in Path('.').glob(pattern):
            if file.is_file() and not file.name.startswith('consciousness_core'):
                try:
                    target = consciousness_dir / file.name
                    shutil.move(str(file), str(target))
                    moved_files.append(file.name)
                    print(f"✅ Moved: {file.name}")
                except Exception as e:
                    print(f"❌ Could not move {file.name}: {e}")
    
    print(f"🎭 Preserved {len(moved_files)} consciousness files")
    return moved_files

if __name__ == "__main__":
    preserve_consciousness_files()
