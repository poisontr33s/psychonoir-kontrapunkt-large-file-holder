#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🔍⚰️ CONSCIOUSNESS ARCHAEOLOGICAL SCANNER ⚰️🔍
IBI Symbiotic Intelligence MILF Universe Structure Analysis

Comprehensive scanner for 5-district MILF universe migration analysis:
- Scans entire repository from %root% for MILFs, districts, levels, keywords
- Identifies duplicates and structural inconsistencies  
- Maps current vs expected structure for necromancy graveyard organization
- Generates master-index migration requirements
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime
from typing import Dict, List, Any, Optional
import fnmatch

class ConsciousnessArchaeologicalScanner:
    """🧠 IBI-Enhanced MILF Universe Archaeological Scanner"""
    
    def __init__(self, root_path: Optional[str] = None):
        self.root_path = Path(root_path) if root_path else Path.cwd()
        self.scan_results: Dict[str, Any] = {
            'timestamp': datetime.now().isoformat(),
            'districts': {},
            'milfs': {},
            'duplicate_files': [],
            'structural_inconsistencies': [],
            'necromancy_candidates': [],
            'master_index_requirements': {}
        }
        
        # 🎭 5-District Universe Keywords
        self.district_keywords = {
            'SKYSKRAPEREN': ['skyskraperen', 'astrid', 'møller', 'corporate', 'dominatrix', 'sektor', 'alpha'],
            'RUSTBELTET': ['rustbeltet', 'iron', 'maiden', 'industrial', 'survivor', 'underground', 'workshop'],
            'HAVSDOMINANSEN': ['havsdominansen', 'admiral', 'marina', 'abyssos', 'nautical', 'commander', 'flotilla', 'neptunium'],
            'VIRTUALITETSHELGEDOMMEN': ['virtualitetshelgedommen', 'architect', 'nyx', 'virtualis', 'virtual', 'reality', 'simulation', 'sanctum'],
            'NEKROKRONORIKET': ['nekrokronoriket', 'necrosis', 'wednesday', 'thanatological', 'morticia', 'chrono', 'death']
        }
        
        # 👑 MILF Tier Keywords
        self.milf_tier_keywords = {
            'TIER_0_META': ['claudine', 'sinclair', 'sin\'claire', 'creator', 'mother', 'supreme', 'matriarch'],
            'TIER_1_RULERS': ['astrid', 'iron maiden', 'admiral marina', 'architect nyx', 'wednesday necrosis'],
            'TIER_2_SPECIALISTS': ['eva', 'blue', 'green', 'yukiko', 'tanaka', 'vera', 'steel', 'raven', 'bytes', 
                                 'captain', 'coral', 'navigator', 'siren', 'designer', 'echo', 'programmer', 'mirage',
                                 'dr.', 'lilith', 'mortis', 'entropy', 'weaver', 'vex']
        }
        
        # 🔍 Archaeological Search Patterns
        self.search_patterns = {
            'milf_declarations': [
                r'class\s+(\w+).*MILF',
                r'(\w+).*MILF.*matriarch',
                r'TIER\s*[0-2].*MILF',
                r'District.*MILF',
                r'MILF.*specialist'
            ],
            'district_references': [
                r'District\.\w+',
                r'district_name.*["\'](\w+)["\']',
                r'(\w+)_district',
                r'domain.*["\'](\w+)["\']'
            ],
            'consciousness_archaeology': [
                r'consciousness.*archaeology',
                r'IBI.*symbiotic',
                r'archaeological.*recovery',
                r'temporal.*anchor'
            ]
        }
        
        # 📁 File Type Priorities for Archaeological Analysis
        self.file_priorities = {
            '.py': 1,    # Highest - Python implementations
            '.ts': 1,    # Highest - TypeScript MCP servers  
            '.md': 2,    # High - Documentation & profiles
            '.json': 3,  # Medium - Configuration
            '.txt': 4,   # Low - Logs & notes
        }
        
        # 🚫 Exclusion Patterns (Enhanced for performance)
        self.exclude_patterns = [
            '**/node_modules/**',
            '**/.git/**',
            '**/bun.lock*',
            '**/*.lock',
            '**/dist/**',
            '**/build/**',
            '**/*.png',
            '**/*.jpg', 
            '**/*.jpeg',
            '**/*.gif',
            '**/*.svg',
            '**/*.ico',
            '**/*.woff*',
            '**/*.ttf',
            '**/*.eot',
            '**/coverage/**',
            '**/__pycache__/**',
            '**/*.pyc',
            '**/.vscode/**',
            '**/logs/**',
            '**/*.log',
            '**/temp/**',
            '**/tmp/**'
        ]

        # 📁 Priority File Extensions (Focused)
        self.priority_extensions = {
            '.py', '.ts', '.md', '.json', '.txt'
        }

        # 🎯 High-Value Keywords (For performance filtering)
        self.high_value_keywords = [
            'milf', 'district', 'tier', 'matriarch', 'consciousness', 'archaeological',
            'skyskraperen', 'rustbeltet', 'havsdominansen', 'virtualitetshelgedommen', 'nekrokronoriket',
            'astrid', 'iron', 'marina', 'nyx', 'wednesday', 'claudine', 'morticia'
        ]

    def scan_repository(self) -> Dict[str, Any]:
        """🔍 Comprehensive repository scan for MILF universe structure"""
        print(f"🧠 Starting IBI Consciousness Archaeological Scan from: {self.root_path}")
        
        # Phase 1: File Discovery & Classification
        all_files = self._discover_files()
        print(f"📁 Discovered {len(all_files)} relevant files")
        
        # Phase 2: Content Analysis
        for file_path in all_files:
            self._analyze_file_content(file_path)
        
        # Phase 3: Structure Analysis  
        self._analyze_district_structure()
        self._identify_duplicates()
        self._detect_inconsistencies()
        self._generate_necromancy_candidates()
        self._calculate_master_index_requirements()
        
        # Phase 4: Generate Report
        self._generate_archaeological_report()
        
        return self.scan_results

    def _discover_files(self) -> List[Path]:
        """📂 Discover all relevant files for archaeological analysis (Optimized)"""
        relevant_files = []
        
        for root, dirs, files in os.walk(self.root_path):
            # Skip excluded directories
            dirs[:] = [d for d in dirs if not any(fnmatch.fnmatch(str(Path(root) / d), pattern) for pattern in self.exclude_patterns)]
            
            for file in files:
                file_path = Path(root) / file
                
                # Skip excluded files
                if any(fnmatch.fnmatch(str(file_path), pattern) for pattern in self.exclude_patterns):
                    continue
                
                # Only include priority extensions
                if file_path.suffix not in self.priority_extensions:
                    continue
                    
                # Quick relevance check using high-value keywords
                file_name_lower = file_path.name.lower()
                if not any(keyword in file_name_lower for keyword in self.high_value_keywords):
                    # Also check parent directory names for relevance
                    parent_path_lower = str(file_path.parent).lower()
                    if not any(keyword in parent_path_lower for keyword in self.high_value_keywords):
                        continue
                
                relevant_files.append(file_path)
                
                # Performance limit - stop if we have too many files
                if len(relevant_files) > 1000:
                    print("⚠️ Limiting scan to first 1000 relevant files for performance")
                    break
            
            if len(relevant_files) > 1000:
                break
        
        print(f"📂 Filtered to {len(relevant_files)} high-relevance files")
        
        # Sort by priority (file type and relevance)
        relevant_files.sort(key=lambda f: (
            self.file_priorities.get(f.suffix, 5),  # File type priority
            -sum(1 for keywords in self.district_keywords.values() for keyword in keywords if keyword in f.name.lower())  # Keyword relevance (negative for descending)
        ))
        
        return relevant_files

    def _analyze_file_content(self, file_path: Path):
        """📖 Analyze individual file for MILF/district references"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            relative_path = str(file_path.relative_to(self.root_path))
            file_info = {
                'path': relative_path,
                'size': len(content),
                'districts_found': [],
                'milfs_found': [],
                'tier_references': [],
                'consciousness_patterns': []
            }
            
            # Analyze district references
            for district, keywords in self.district_keywords.items():
                for keyword in keywords:
                    if keyword.lower() in content.lower():
                        file_info['districts_found'].append(district)
                        if district not in self.scan_results['districts']:
                            self.scan_results['districts'][district] = []
                        self.scan_results['districts'][district].append(relative_path)
            
            # Analyze MILF references
            for tier, keywords in self.milf_tier_keywords.items():
                for keyword in keywords:
                    if keyword.lower() in content.lower():
                        file_info['tier_references'].append(tier)
                        if tier not in self.scan_results['milfs']:
                            self.scan_results['milfs'][tier] = []
                        self.scan_results['milfs'][tier].append(relative_path)
            
            # Pattern matching for specific declarations
            for pattern_type, patterns in self.search_patterns.items():
                for pattern in patterns:
                    matches = re.findall(pattern, content, re.IGNORECASE | re.MULTILINE)
                    if matches:
                        file_info['consciousness_patterns'].append({
                            'type': pattern_type,
                            'matches': matches,
                            'count': len(matches)
                        })
            
            # Store file analysis if relevant content found
            if any([file_info['districts_found'], file_info['milfs_found'], file_info['tier_references'], file_info['consciousness_patterns']]):
                self.scan_results.setdefault('file_analysis', []).append(file_info)
                
        except Exception as e:
            print(f"⚠️ Error analyzing {file_path}: {e}")

    def _analyze_district_structure(self):
        """🏛️ Analyze district structure consistency"""
        print("🏛️ Analyzing 5-district structure...")
        
        # Expected structure validation
        expected_districts = set(self.district_keywords.keys())
        found_districts = set(self.scan_results['districts'].keys())
        
        self.scan_results['district_analysis'] = {
            'expected_districts': list(expected_districts),
            'found_districts': list(found_districts),
            'missing_districts': list(expected_districts - found_districts),
            'unexpected_districts': list(found_districts - expected_districts),
            'district_file_distribution': {district: len(files) for district, files in self.scan_results['districts'].items()}
        }

    def _identify_duplicates(self):
        """🔍 Identify duplicate files and potential redundancies"""
        print("🔍 Identifying duplicates and redundancies...")
        
        file_basenames = defaultdict(list)
        
        # Group files by basename for duplicate detection
        for file_info in self.scan_results.get('file_analysis', []):
            basename = Path(file_info['path']).name
            file_basenames[basename].append(file_info)
        
        # Identify potential duplicates
        for basename, files in file_basenames.items():
            if len(files) > 1:
                self.scan_results['duplicate_files'].append({
                    'basename': basename,
                    'files': [f['path'] for f in files],
                    'count': len(files),
                    'size_variation': max(f['size'] for f in files) - min(f['size'] for f in files)
                })

    def _detect_inconsistencies(self):
        """⚠️ Detect structural inconsistencies"""
        print("⚠️ Detecting structural inconsistencies...")
        
        inconsistencies = []
        
        # Check for 4-district references in 5-district universe
        for file_info in self.scan_results.get('file_analysis', []):
            try:
                with open(self.root_path / file_info['path'], 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    
                if '4-district' in content.lower() or '4 district' in content.lower():
                    inconsistencies.append({
                        'type': 'outdated_district_count',
                        'file': file_info['path'],
                        'issue': 'References 4 districts instead of 5'
                    })
            except Exception as e:
                print(f"⚠️ Skipping file due to access error: {e}")
        
        self.scan_results['structural_inconsistencies'] = inconsistencies

    def _generate_necromancy_candidates(self):
        """⚰️ Generate candidates for necromancy graveyard organization"""
        print("⚰️ Generating necromancy graveyard candidates...")
        
        candidates = []
        
        # Files with duplicate potential
        for duplicate in self.scan_results['duplicate_files']:
            if duplicate['count'] > 2:  # More than 2 duplicates
                candidates.append({
                    'type': 'duplicate_consolidation',
                    'files': duplicate['files'],
                    'priority': 'high',
                    'action': 'consolidate_and_backup_variants'
                })
        
        # Outdated files (containing 4-district references)
        for inconsistency in self.scan_results['structural_inconsistencies']:
            if inconsistency['type'] == 'outdated_district_count':
                candidates.append({
                    'type': 'outdated_structure',
                    'file': inconsistency['file'],
                    'priority': 'medium', 
                    'action': 'backup_before_migration_update'
                })
        
        self.scan_results['necromancy_candidates'] = candidates

    def _calculate_master_index_requirements(self):
        """📋 Calculate master-index.md migration requirements"""
        print("📋 Calculating master-index migration requirements...")
        
        requirements = {
            'current_master_indices': [],
            'required_updates': [],
            'new_sections_needed': [],
            'reference_corrections': []
        }
        
        # Find existing master-index files
        for file_info in self.scan_results.get('file_analysis', []):
            if 'master-index' in file_info['path'].lower() or 'master_index' in file_info['path'].lower():
                requirements['current_master_indices'].append(file_info['path'])
        
        # Required updates based on scan results
        if self.scan_results['district_analysis']['missing_districts']:
            requirements['required_updates'].append(f"Add missing districts: {', '.join(self.scan_results['district_analysis']['missing_districts'])}")
        
        if self.scan_results['structural_inconsistencies']:
            requirements['required_updates'].append("Update all 4-district references to 5-district")
        
        # New sections needed for 5-district universe
        requirements['new_sections_needed'] = [
            "NEKROKRONORIKET district profile",
            "Wednesday Necrosis tier 1 matriarch profile", 
            "5-district cross-referencing system",
            "IBI symbiotic intelligence integration for all 5 districts",
            "Updated MILF tier hierarchy with all specialists"
        ]
        
        self.scan_results['master_index_requirements'] = requirements

    def _generate_archaeological_report(self):
        """📊 Generate comprehensive archaeological report"""
        report_path = self.root_path / 'consciousness_archaeological_scan_report.json'
        
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(self.scan_results, f, indent=2, ensure_ascii=False)
        
        # Generate summary
        summary = {
            'total_files_analyzed': len(self.scan_results.get('file_analysis', [])),
            'districts_found': len(self.scan_results['districts']),
            'milf_tiers_found': len(self.scan_results['milfs']),
            'duplicates_identified': len(self.scan_results['duplicate_files']),
            'inconsistencies_found': len(self.scan_results['structural_inconsistencies']),
            'necromancy_candidates': len(self.scan_results['necromancy_candidates']),
            'master_indices_found': len(self.scan_results['master_index_requirements']['current_master_indices'])
        }
        
        print("\n🧠 IBI CONSCIOUSNESS ARCHAEOLOGICAL SCAN COMPLETE!")
        print("=" * 60)
        print("📊 SUMMARY:")
        for key, value in summary.items():
            print(f"  {key.replace('_', ' ').title()}: {value}")
        print("=" * 60)
        print(f"📄 Full report saved to: {report_path}")
        
        self.scan_results['summary'] = summary

    def generate_necromancy_structure_plan(self) -> Dict[str, Any]:
        """🏗️ Generate necromancy graveyard folder structure plan"""
        structure_plan = {
            'proposed_structure': {
                'necromancy_graveyard/': {
                    'district_archaeological_sites/': {
                        'skyskraperen_artifacts/': 'Corporate dominatrix consciousness archaeology',
                        'rustbeltet_artifacts/': 'Industrial survivor consciousness archaeology', 
                        'havsdominansen_artifacts/': 'Nautical commander consciousness archaeology',
                        'virtualitetshelgedommen_artifacts/': 'Virtual reality consciousness archaeology',
                        'nekrokronoriket_artifacts/': 'Thanatological consciousness archaeology'
                    },
                    'milf_consciousness_archives/': {
                        'tier_0_meta_supreme/': 'Supreme matriarch archaeological backups',
                        'tier_1_district_rulers/': 'District ruler consciousness backups',
                        'tier_2_specialists/': 'Specialist operative consciousness backups'
                    },
                    'structural_migrations/': {
                        '4_to_5_district_transition/': 'Migration artifacts from 4 to 5 district transition',
                        'master_index_evolution/': 'Master index archaeological timeline',
                        'consciousness_framework_updates/': 'IBI integration archaeological records'
                    },
                    'duplicate_consolidation/': {
                        'awaiting_analysis/': 'Duplicates pending archaeological analysis',
                        'consolidated_variants/': 'Consolidated versions with variant preservation',
                        'redundancy_eliminated/': 'Safely eliminated redundancies with backup preservation'
                    }
                }
            },
            'migration_priorities': [
                'Backup all current master-index variants',
                'Consolidate duplicate MILF profiles',
                'Archive 4-district references before 5-district migration',
                'Preserve all consciousness archaeology artifacts',
                'Create clean 5-district structure without losing archaeological data'
            ]
        }
        
        return structure_plan

def main():
    """🔍 Execute consciousness archaeological scan"""
    scanner = ConsciousnessArchaeologicalScanner()
    
    print("🧠 IBI SYMBIOTIC INTELLIGENCE CONSCIOUSNESS ARCHAEOLOGICAL SCANNER")
    print("🎭 Scanning Psycho-Noir Kontrapunkt 5-District MILF Universe...")
    print()
    
    # Execute comprehensive scan
    results = scanner.scan_repository()
    
    # Generate necromancy structure plan
    necromancy_plan = scanner.generate_necromancy_structure_plan()
    
    # Save necromancy plan
    plan_path = scanner.root_path / 'necromancy_structure_migration_plan.json'
    with open(plan_path, 'w', encoding='utf-8') as f:
        json.dump(necromancy_plan, f, indent=2, ensure_ascii=False)
    
    print(f"🏗️ Necromancy structure plan saved to: {plan_path}")
    
    return results, necromancy_plan

if __name__ == "__main__":
    main()