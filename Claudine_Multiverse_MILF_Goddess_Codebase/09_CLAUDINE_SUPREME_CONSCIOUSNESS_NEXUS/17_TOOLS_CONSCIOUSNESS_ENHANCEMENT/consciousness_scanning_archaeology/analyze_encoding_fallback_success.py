#!/usr/bin/env python3
"""
🎭 PARTIAL READ FILES ANALYZER
Analyser de 17 filene med encoding-problemer
"""

import json
from pathlib import Path

def main():
    scan_results = Path("zero_skip_scan_results_20251001_030453.json")
    
    if not scan_results.exists():
        print(f"❌ Scan results not found: {scan_results}")
        return
        
    with open(scan_results, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print("🎭 PARTIAL READ FILES ANALYSIS")
    print("=" * 80)
    
    # Search in aeoaa_files for partial_read
    partial_files = []
    for file_entry in data.get('aeoaa_files', []):
        if 'partial' in file_entry.get('scan_method', ''):
            partial_files.append(file_entry)
    
    print(f"\n📊 Total files with partial_read in aeoaa_files: {len(partial_files)}")
    
    if partial_files:
        print("\n🔍 FILES WITH ENCODING PROBLEMS (in aeoaa_files):")
        print("-" * 80)
        
        for i, file_info in enumerate(partial_files, 1):
            print(f"\n{i}. {file_info['relative_path']}")
            print(f"   Size: {file_info.get('size_mb', 0):.2f} MB")
            print(f"   Scan method: {file_info.get('scan_method', 'unknown')}")
            print(f"   Encoding: {file_info.get('encoding', 'unknown')}")
            print(f"   Status: {file_info.get('status', 'unknown')}")
    
    # Also check scan_methods statistics
    scan_methods = data.get('statistics', {}).get('scan_methods', {})
    print(f"\n📊 Scan methods statistics:")
    print(f"   partial_read: {scan_methods.get('partial_read', 0)}")
    print(f"   encoding_fallback_used: {data.get('statistics', {}).get('encoding_fallback_used', 0)}")
    
    # Check encoding distribution
    encoding_dist = data.get('statistics', {}).get('encoding_distribution', {})
    print(f"\n📊 Encoding distribution:")
    for encoding, count in encoding_dist.items():
        print(f"   {encoding}: {count}")
        
    print("\n" + "=" * 80)
    print("🎭 Analysis complete")
    
    return partial_files

if __name__ == "__main__":
    main()
