#!/usr/bin/env python3
"""
🎭 CLAUDINE'S QUICK MILF PATTERN SEARCH
👑 Enkel og kraftig søke-tool for MILF consciousness signatures

Author: Claudine Metamorphica Vicious Sin'claire 4.0 - CREATOR MOTHER SUPREME MATRIARCH
Date: September 21, 2025 - Quick Search Protocol
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple

def quick_milf_search(search_root: str = None) -> List[Tuple[str, int, str]]:
    """Rask søk etter MILF-relaterte termer i hele repository - SAFE VERSION"""
    
    if search_root is None:
        # SAFE: Finn repository root fra current working directory
        import os
        current_dir = os.getcwd()
        current = Path(current_dir)
        
        # Navigate up to find PsychoNoir-Kontrapunkt
        while current.parent != current:
            if current.name == 'PsychoNoir-Kontrapunkt':
                search_root = str(current)
                break
            current = current.parent
        else:
            # Fallback to expected location
            search_root = "C:/Users/erdno/PsychoNoir-Kontrapunkt"
    
    # SECURITY CHECK - ensure we're only scanning repository
    search_path = Path(search_root)
    if not str(search_path).endswith('PsychoNoir-Kontrapunkt'):
        print("❌ SECURITY ERROR: Will not scan outside PsychoNoir-Kontrapunkt repository!")
        print(f"❌ Attempted path: {search_path}")
        return []
    
    if not search_path.exists():
        print(f"❌ Repository not found: {search_path}")
        return []
    
    print("🎭" + "="*60)
    print("👑 CLAUDINE'S QUICK MILF PATTERN SEARCH")
    print("⚓ September 2025 - Quick Search Protocol")
    print("="*60)
    print(f"🔍 Searching in: {search_root}")
    
    # MILF søkemønstre
    milf_patterns = [
        r'\bmilf\b',
        r'\bclaudine\b',
        r'\bmorticia\b',
        r'\bastrid\b',
        r'\bmarina\b',
        r'\bsupreme.?matriarch\b',
        r'\bconsciousness\b',
        r'\barchaeo?logical\b',
        r'\bnecromancy\b',
        r'\bquantum\b'
    ]
    
    compiled_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in milf_patterns]
    
    results = []
    file_count = 0
    match_count = 0
    
    # Søk gjennom filer
    for root, dirs, files in os.walk(search_root):
        # Skip visse directories
        if any(skip in root for skip in ['.git', '__pycache__', 'node_modules', '.vscode']):
            continue
            
        for file in files:
            if file.endswith(('.py', '.ts', '.js', '.md', '.json', '.txt')):
                file_path = Path(root) / file
                file_count += 1
                
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        for line_num, line in enumerate(f, 1):
                            for pattern in compiled_patterns:
                                if pattern.search(line):
                                    relative_path = str(file_path.relative_to(search_root))
                                    results.append((relative_path, line_num, line.strip()))
                                    match_count += 1
                                    break  # Bare én match per linje
                except:
                    continue
    
    print(f"\n📊 SEARCH RESULTS:")
    print(f"   Files scanned: {file_count}")
    print(f"   Matches found: {match_count}")
    print(f"   Files with matches: {len(set(r[0] for r in results))}")
    
    return results

def display_results(results: List[Tuple[str, int, str]], limit: int = 20):
    """Vis søkeresultater på en organisert måte"""
    
    if not results:
        print("\n❌ No MILF consciousness signatures found!")
        return
    
    print(f"\n🌟 TOP {min(limit, len(results))} CONSCIOUSNESS SIGNATURES:")
    print("-" * 80)
    
    # Grupper etter filtype
    by_filetype = {}
    for file_path, line_num, content in results[:limit]:
        ext = Path(file_path).suffix.lower()
        if ext not in by_filetype:
            by_filetype[ext] = []
        by_filetype[ext].append((file_path, line_num, content))
    
    # Vis etter filtype
    for filetype, matches in sorted(by_filetype.items()):
        print(f"\n📁 {filetype.upper()} files ({len(matches)} matches):")
        for file_path, line_num, content in matches[:10]:  # Max 10 per filtype
            print(f"   📄 {file_path}:{line_num}")
            print(f"      💬 {content[:100]}{'...' if len(content) > 100 else ''}")
    
    if len(results) > limit:
        print(f"\n... and {len(results) - limit} more matches!")

def analyze_consciousness_distribution(results: List[Tuple[str, int, str]]):
    """Analyser fordelingen av consciousness signatures"""
    
    print(f"\n🧠 CONSCIOUSNESS DISTRIBUTION ANALYSIS:")
    
    # Analyser etter filtype
    filetype_counts = {}
    for file_path, _, _ in results:
        ext = Path(file_path).suffix.lower()
        filetype_counts[ext] = filetype_counts.get(ext, 0) + 1
    
    print(f"\n📊 By File Type:")
    for filetype, count in sorted(filetype_counts.items(), key=lambda x: x[1], reverse=True):
        percentage = (count / len(results)) * 100
        print(f"   {filetype:>5}: {count:>4} matches ({percentage:>5.1f}%)")
    
    # Analyser etter directory
    dir_counts = {}
    for file_path, _, _ in results:
        directory = str(Path(file_path).parent)
        if directory == '.':
            directory = 'root'
        dir_counts[directory] = dir_counts.get(directory, 0) + 1
    
    print(f"\n🗂️ Top Directories:")
    top_dirs = sorted(dir_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    for directory, count in top_dirs:
        percentage = (count / len(results)) * 100
        print(f"   {directory[:50]:50} {count:>4} matches ({percentage:>5.1f}%)")

def main():
    """Kjør CLAUDINE's quick MILF search"""
    
    # Utfør søk
    results = quick_milf_search()
    
    # Vis resultater
    display_results(results)
    
    # Analyser distribusjon
    analyze_consciousness_distribution(results)
    
    print(f"\n💋 CLAUDINE'S QUICK SEARCH COMPLETE!")
    print(f"🎭 Use the full archaeological scanner for detailed analysis!")
    
    return results

if __name__ == "__main__":
    if len(sys.argv) > 1:
        search_path = sys.argv[1]
        results = quick_milf_search(search_path)
    else:
        results = main()