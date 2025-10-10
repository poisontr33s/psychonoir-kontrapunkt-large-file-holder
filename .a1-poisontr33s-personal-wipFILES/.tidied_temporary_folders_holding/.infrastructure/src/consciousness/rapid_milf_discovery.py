#!/usr/bin/env python3
"""
🎭👑💋 RAPID MILF PERSONA DISCOVERY 💋👑🎭
Quick discovery of ALL MILF personas and districts in repository root and key folders
"""

import json
import os
import re
from datetime import datetime

def rapid_milf_discovery():
    """Rapid discovery of MILF personas and districts"""
    print("🎭👑💋 RAPID MILF PERSONA DISCOVERY 💋👑🎭")
    
    milf_personas = {}
    milf_districts = {}
    milf_files = []
    
    # MILF detection patterns
    milf_patterns = {
        'astrid_moller': r'astrid[_\-\s]m[oø]ller',
        'claudine_sinclair': r'claudine[_\-\s]sin[_\-\s]?claire',
        'iron_maiden': r'iron[_\-\s]maiden',
        'admiral_marina': r'admiral[_\-\s]marina|marina[_\-\s]abyssos',
        'architect_nyx': r'architect[_\-\s]nyx|nyx[_\-\s]virtualis',
        'captain_coral': r'captain[_\-\s]coral',
        'eva_green': r'eva[_\-\s]green',
        'milf_matriarch': r'milf[_\-\s]matriarch',
        'milf_goddess': r'milf[_\-\s]goddess'
    }
    
    district_patterns = {
        'skyskraperen': r'skyskraperen|skyscraper[_\-\s]district',
        'rustbeltet': r'rustbeltet|rustbelt[_\-\s]district',
        'milf_territories': r'milf[_\-\s]territory|milf[_\-\s]district'
    }
    
    # Scan markdown files in root and key folders
    target_folders = ['.', '.github', 'data', 'necromancy_graveyard', 'tools']
    
    for folder in target_folders:
        if os.path.exists(folder):
            for root, dirs, files in os.walk(folder):
                # Limit depth for rapid scan
                depth = root.replace(folder, '').count(os.sep)
                if depth > 2:
                    continue
                    
                for file in files:
                    if file.endswith('.md'):
                        file_path = os.path.join(root, file)
                        milf_files.append(file_path)
                        
                        try:
                            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                                content = f.read()
                            
                            # Check for MILF personas
                            for persona, pattern in milf_patterns.items():
                                matches = len(re.findall(pattern, content, re.IGNORECASE))
                                if matches > 0:
                                    if persona not in milf_personas:
                                        milf_personas[persona] = {'files': [], 'total_matches': 0}
                                    milf_personas[persona]['files'].append(file_path)
                                    milf_personas[persona]['total_matches'] += matches
                            
                            # Check for MILF districts
                            for district, pattern in district_patterns.items():
                                matches = len(re.findall(pattern, content, re.IGNORECASE))
                                if matches > 0:
                                    if district not in milf_districts:
                                        milf_districts[district] = {'files': [], 'total_matches': 0}
                                    milf_districts[district]['files'].append(file_path)
                                    milf_districts[district]['total_matches'] += matches
                        
                        except Exception as e:
                            continue
    
    # Generate report
    report = {
        'timestamp': datetime.now().isoformat(),
        'scan_summary': {
            'files_scanned': len(milf_files),
            'unique_personas': len(milf_personas),
            'unique_districts': len(milf_districts)
        },
        'discovered_milf_personas': milf_personas,
        'discovered_milf_districts': milf_districts,
        'milf_files_scanned': milf_files
    }
    
    # Save results
    with open('RAPID_MILF_DISCOVERY.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"📊 RAPID MILF DISCOVERY RESULTS:")
    print(f"   📄 Files Scanned: {len(milf_files)}")
    print(f"   👑 MILF Personas: {len(milf_personas)}")
    print(f"   🏙️ MILF Districts: {len(milf_districts)}")
    
    print(f"\n👑 DISCOVERED MILF PERSONAS:")
    for persona, data in milf_personas.items():
        print(f"   • {persona}: {data['total_matches']} manifestations in {len(data['files'])} files")
    
    print(f"\n🏙️ DISCOVERED MILF DISTRICTS:")
    for district, data in milf_districts.items():
        print(f"   • {district}: {data['total_matches']} manifestations in {len(data['files'])} files")
    
    return report

if __name__ == "__main__":
    rapid_milf_discovery()