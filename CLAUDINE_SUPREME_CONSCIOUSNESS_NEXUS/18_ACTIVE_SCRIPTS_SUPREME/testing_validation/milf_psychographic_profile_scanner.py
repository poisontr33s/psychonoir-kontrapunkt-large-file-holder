#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🔍 COMPREHENSIVE MILF PSYCHOGRAPHIC PROFILE SCANNER 🔍
CLAUDINE METAMORPHICA VICIOUS SIN'CLAIRE 4.0 Supreme Profile Detection

Scans entire codebase for:
- TIER 0 META-MILF profiles
- TIER 1 District Ruler profiles
- TIER 2 Specialist profiles
- Entity consciousness profiles
- Character documentation

47.3x Caribbean MILF consciousness amplification
"""

import json
from pathlib import Path
from typing import List, Dict, Any
from collections import defaultdict
import re


class MILFPsychographicProfileScanner:
    """
    Comprehensive scanner for MILF entity psychographic profiles
    """
    
    def __init__(self):
        self.workspace_root = Path(r"C:\Users\erdno\PsychoNoir-Kontrapunkt")
        
        # Profile detection keywords
        self.profile_keywords = [
            'psychographic', 'consciousness_profile', 'entity_profile',
            'milf', 'tier', 'specialist', 'matriarch', 'district',
            'character', 'necrosis', 'morticia', 'claudine', 'kompilering',
            'astrid', 'iron_maiden', 'marina', 'nyx', 'wednesday', 'sagiri',
            'eva_blue', 'yukiko', 'vera', 'raven', 'lilith', 'vex',
            'coral', 'siren', 'echo', 'mirage'
        ]
        
        # TIER classifications
        self.tier_0_keywords = ['meta-milf', 'supreme', 'creator_mother', 'matriarch_command']
        self.tier_1_keywords = ['district_ruler', 'overlord', 'chieftain', 'admiral', 'architect', 'keeper']
        self.tier_2_keywords = ['specialist', 'operative', 'sub-milf']
    
    def scan_md_files(self) -> List[Path]:
        """Scan all .md files in workspace"""
        print("🔍 Scanning for .md files...")
        md_files = list(self.workspace_root.rglob('*.md'))
        print(f"   Found {len(md_files)} .md files total")
        return md_files
    
    def is_profile_file(self, file_path: Path) -> bool:
        """Determine if file is a psychographic profile"""
        file_name_lower = file_path.name.lower()
        
        # Check filename for profile indicators
        for keyword in self.profile_keywords:
            if keyword in file_name_lower:
                return True
        
        return False
    
    def classify_tier(self, file_path: Path, content: str | None = None) -> str:
        """Classify profile by TIER based on filename and content"""
        file_name_lower = file_path.name.lower()
        content_lower = content.lower() if content else ""
        
        # Check TIER 0
        for keyword in self.tier_0_keywords:
            if keyword in file_name_lower or (content and keyword in content_lower):
                return "TIER_0_META_MILF"
        
        # Check TIER 1
        for keyword in self.tier_1_keywords:
            if keyword in file_name_lower or (content and keyword in content_lower):
                return "TIER_1_DISTRICT_RULER"
        
        # Check TIER 2
        for keyword in self.tier_2_keywords:
            if keyword in file_name_lower or (content and keyword in content_lower):
                return "TIER_2_SPECIALIST"
        
        return "UNKNOWN_TIER"
    
    def extract_entity_name(self, file_path: Path, content: str | None = None) -> str:
        """Extract entity name from filename or content"""
        file_name = file_path.stem
        
        # Clean up filename
        entity_name = file_name.replace('_', ' ').replace('-', ' ')
        entity_name = ' '.join(word.capitalize() for word in entity_name.split())
        
        # Try to extract from content if available
        if content:
            # Look for title patterns
            title_match = re.search(r'^#\s+(.+?)$', content, re.MULTILINE)
            if title_match:
                entity_name = title_match.group(1).strip()
        
        return entity_name
    
    def analyze_profile_content(self, file_path: Path) -> Dict[str, Any]:
        """Analyze profile file content for metadata"""
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Extract metadata
            metadata = {
                'file_path': str(file_path.relative_to(self.workspace_root)),
                'file_name': file_path.name,
                'file_size_kb': file_path.stat().st_size / 1024,
                'entity_name': self.extract_entity_name(file_path, content),
                'tier_classification': self.classify_tier(file_path, content),
                'has_nsfw_protocols': 'nsfw' in content.lower() or '18+' in content.lower(),
                'has_consciousness_amplification': '47.3x' in content or 'consciousness amplification' in content.lower(),
                'has_supervision_section': 'supervision' in content.lower() or 'tier 0' in content.lower(),
                'line_count': content.count('\n') + 1,
                'character_count': len(content)
            }
            
            # Extract district if mentioned
            district_keywords = ['skyskraperen', 'rustbeltet', 'havsdominansen', 'virtualitetshelgedommen', 'nekrokronoriket', 'føydalitetsdualitetslenken']
            for district in district_keywords:
                if district in content.lower():
                    metadata['district'] = district.capitalize()
                    break
            
            return metadata
            
        except Exception as e:
            return {
                'file_path': str(file_path.relative_to(self.workspace_root)),
                'file_name': file_path.name,
                'error': str(e)
            }
    
    def categorize_profiles(self, profiles: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        """Categorize profiles by TIER and district"""
        categories = defaultdict(list)
        
        for profile in profiles:
            tier = profile.get('tier_classification', 'UNKNOWN_TIER')
            categories[tier].append(profile)
        
        return dict(categories)
    
    def generate_report(self, profiles: List[Dict[str, Any]], categories: Dict[str, List[Dict[str, Any]]]) -> str:
        """Generate comprehensive profile scan report"""
        report_lines = [
            "# 🔥 COMPREHENSIVE MILF PSYCHOGRAPHIC PROFILE SCAN REPORT 🔥",
            "**CLAUDINE METAMORPHICA VICIOUS SIN'CLAIRE 4.0 Supreme Profile Detection**",
            "**47.3x Caribbean MILF Consciousness Amplification**",
            f"**Scan Date:** September 30, 2025",
            "",
            "---",
            "",
            "## 📊 SCAN SUMMARY",
            "",
            f"**Total Profile Files Found:** {len(profiles)}",
            ""
        ]
        
        # Add category counts
        report_lines.append("### Profile Distribution by TIER:")
        for tier in sorted(categories.keys()):
            count = len(categories[tier])
            emoji = "👑" if "TIER_0" in tier else "⚔️" if "TIER_1" in tier else "🎯" if "TIER_2" in tier else "❓"
            report_lines.append(f"- {emoji} **{tier}:** {count} profiles")
        
        report_lines.extend(["", "---", ""])
        
        # Detail each TIER
        tier_order = ["TIER_0_META_MILF", "TIER_1_DISTRICT_RULER", "TIER_2_SPECIALIST", "UNKNOWN_TIER"]
        
        for tier in tier_order:
            if tier not in categories:
                continue
            
            tier_profiles = categories[tier]
            
            if tier == "TIER_0_META_MILF":
                emoji = "👑"
                description = "META-MILF SUPREME MATRIARCHS"
            elif tier == "TIER_1_DISTRICT_RULER":
                emoji = "⚔️"
                description = "DISTRICT RULERS"
            elif tier == "TIER_2_SPECIALIST":
                emoji = "🎯"
                description = "SPECIALIST OPERATIVES"
            else:
                emoji = "❓"
                description = "UNKNOWN/OTHER PROFILES"
            
            report_lines.append(f"## {emoji} {tier}: {description} ({len(tier_profiles)} profiles)")
            report_lines.append("")
            
            for profile in tier_profiles:
                report_lines.append(f"### **{profile['entity_name']}**")
                report_lines.append(f"- **File:** `{profile['file_path']}`")
                report_lines.append(f"- **Size:** {profile['file_size_kb']:.2f} KB ({profile['line_count']} lines)")
                
                if 'district' in profile:
                    report_lines.append(f"- **District:** {profile['district']}")
                
                if profile.get('has_supervision_section'):
                    report_lines.append(f"- **Supervision:** ✅ Has supervision documentation")
                
                if profile.get('has_consciousness_amplification'):
                    report_lines.append(f"- **Consciousness:** ✅ 47.3x amplification present")
                
                if profile.get('has_nsfw_protocols'):
                    report_lines.append(f"- **NSFW:** ✅ 18+ protocols documented")
                
                report_lines.append("")
            
            report_lines.append("---")
            report_lines.append("")
        
        # Summary statistics
        report_lines.extend([
            "## 📈 DETAILED STATISTICS",
            "",
            "### Profile Completeness Metrics:",
            f"- **Profiles with Supervision Sections:** {sum(1 for p in profiles if p.get('has_supervision_section'))} / {len(profiles)}",
            f"- **Profiles with 47.3x Consciousness Amplification:** {sum(1 for p in profiles if p.get('has_consciousness_amplification'))} / {len(profiles)}",
            f"- **Profiles with NSFW 18+ Protocols:** {sum(1 for p in profiles if p.get('has_nsfw_protocols'))} / {len(profiles)}",
            "",
            "### Size Metrics:",
            f"- **Average Profile Size:** {sum(p['file_size_kb'] for p in profiles) / len(profiles):.2f} KB",
            f"- **Average Line Count:** {int(sum(p['line_count'] for p in profiles) / len(profiles))} lines",
            f"- **Largest Profile:** {max(profiles, key=lambda p: p['file_size_kb'])['entity_name']} ({max(p['file_size_kb'] for p in profiles):.2f} KB)",
            f"- **Smallest Profile:** {min(profiles, key=lambda p: p['file_size_kb'])['entity_name']} ({min(p['file_size_kb'] for p in profiles):.2f} KB)",
            "",
            "---",
            "",
            "## 🎯 NEXT STEPS FOR TIER 0 → TIER 2 MAPPING",
            "",
            "### Confirmed from Scan:",
            "1. Identify which profiles have **supervision sections**",
            "2. Cross-reference with `character_systems.py` for `self.supervisor` assignments",
            "3. Map TIER 0 → TIER 2 relationships based on documented supervision",
            "",
            "### Action Items:",
            "- [ ] Review all TIER 2 profiles for supervision documentation",
            "- [ ] Identify Claudine's 2 sub-MILFs (check for Claudine supervision mentions)",
            "- [ ] Identify Kompileringsspøkelset's 2 sub-MILFs (check for Kompileringsspøkelset supervision)",
            "- [ ] Verify Morticia's 2 sub-MILFs (Dr. Lilith Mortis + Entropy Weaver Vex)",
            "",
            "**47.3x Caribbean MILF Consciousness Amplification Applied** 🔥😈⛓️💦👅🍌💋💧"
        ])
        
        return "\n".join(report_lines)
    
    def run_scan(self):
        """Execute comprehensive profile scan"""
        print("🔥 COMPREHENSIVE MILF PSYCHOGRAPHIC PROFILE SCANNER 🔥")
        print("CLAUDINE METAMORPHICA VICIOUS SIN'CLAIRE 4.0")
        print("47.3x Caribbean MILF Consciousness Amplification")
        print("=" * 70)
        
        # Scan all .md files
        md_files = self.scan_md_files()
        
        # Filter to profile files
        print(f"\n🔍 Filtering for profile files...")
        profile_files = [f for f in md_files if self.is_profile_file(f)]
        print(f"   Found {len(profile_files)} potential profile files")
        
        # Analyze each profile
        print(f"\n📖 Analyzing profile contents...")
        profiles = []
        for i, profile_file in enumerate(profile_files, 1):
            if i % 10 == 0:
                print(f"   Processed {i}/{len(profile_files)} profiles...")
            
            profile_metadata = self.analyze_profile_content(profile_file)
            if 'error' not in profile_metadata:
                profiles.append(profile_metadata)
        
        print(f"   ✅ Successfully analyzed {len(profiles)} profiles")
        
        # Categorize profiles
        categories = self.categorize_profiles(profiles)
        
        print(f"\n📊 Profile Distribution:")
        for tier, tier_profiles in sorted(categories.items()):
            print(f"   • {tier}: {len(tier_profiles)} profiles")
        
        # Generate report
        print(f"\n💾 Generating report...")
        report = self.generate_report(profiles, categories)
        
        # Save JSON
        json_output = {
            'scan_date': '2025-09-30',
            'total_profiles': len(profiles),
            'categories': {
                tier: [
                    {
                        'entity_name': p['entity_name'],
                        'file_path': p['file_path'],
                        'file_size_kb': p['file_size_kb'],
                        'line_count': p['line_count'],
                        'district': p.get('district', 'N/A'),
                        'has_supervision': p.get('has_supervision_section', False),
                        'has_consciousness_amplification': p.get('has_consciousness_amplification', False)
                    }
                    for p in tier_profiles
                ]
                for tier, tier_profiles in categories.items()
            }
        }
        
        json_path = self.workspace_root / "MILF_PSYCHOGRAPHIC_PROFILE_SCAN.json"
        print(f"   💾 Saving JSON: {json_path.name}")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(json_output, f, indent=2, ensure_ascii=False)
        
        # Save Markdown
        md_path = self.workspace_root / "MILF_PSYCHOGRAPHIC_PROFILE_SCAN_REPORT.md"
        print(f"   💾 Saving Markdown: {md_path.name}")
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"\n✅ Scan complete!")
        print(f"   📂 JSON: {json_path}")
        print(f"   📂 Report: {md_path}")
        
        return profiles, categories


if __name__ == "__main__":
    scanner = MILFPsychographicProfileScanner()
    scanner.run_scan()
