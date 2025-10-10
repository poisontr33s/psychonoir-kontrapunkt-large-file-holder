#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔍 SKIPPED FILES INTELLIGENT ANALYZER 🔍
========================================

Analyser de 53 skippede filene fra consciousness archaeological scanner
for å identifisere consciousness data relevance og potensielle gaps.

CONSCIOUSNESS_SIGNATURE: 0xSKIPPED_FILES_ANALYSIS_SYSTEM
ANALYSIS_DEPTH: INTELLIGENT_CONSCIOUSNESS_ARCHAEOLOGY
"""

import json
from pathlib import Path
from typing import Dict, List, Any, Tuple
from collections import defaultdict
import datetime

class SkippedFilesIntelligentAnalyzer:
    """
    🔍 Intelligent analyzer for skipped files consciousness archaeology
    """
    
    def __init__(self, workspace_root: str = "C:\\Users\\erdno\\PsychoNoir-Kontrapunkt"):
        self.workspace_root = Path(workspace_root)
        self.skipped_files: List[Dict[str, Any]] = []
        self.analysis_results: Dict[str, Any] = {}
        
        # File extension categories for consciousness relevance
        self.consciousness_relevant_extensions = {
            'documentation': ['.md', '.txt', '.rst', '.adoc'],
            'code': ['.py', '.ts', '.js', '.tsx', '.jsx'],
            'configuration': ['.json', '.yaml', '.yml', '.toml', '.ini'],
            'data': ['.csv', '.xml', '.sql', '.db', '.sqlite'],
            'logs': ['.log', '.out'],
            'images': ['.png', '.jpg', '.jpeg', '.gif', '.svg'],
            'binary': ['.exe', '.dll', '.so', '.dylib'],
            'archives': ['.zip', '.tar', '.gz', '.7z'],
            'lock_files': ['.lock'],
            'other': []
        }
        
        # Skip patterns that are always safe to ignore
        self.safe_skip_patterns = [
            'node_modules',
            '.git',
            '__pycache__',
            '.vscode',
            'dist',
            'build',
            '.cache'
        ]
        
    def load_latest_scan_results(self) -> bool:
        """Load latest consciousness archaeological scan results"""
        try:
            # Find latest scan file
            scan_files = list(self.workspace_root.glob("consciousness_archaeological_scan_*.json"))
            if not scan_files:
                print("❌ No scan files found!")
                return False
                
            latest_scan = max(scan_files, key=lambda p: p.stat().st_mtime)
            print(f"📂 Loading: {latest_scan.name}")
            
            with open(latest_scan, 'r', encoding='utf-8') as f:
                scan_data = json.load(f)
                
            self.skipped_files = scan_data.get('skipped_files', [])
            print(f"✅ Loaded {len(self.skipped_files)} skipped files\n")
            return True
            
        except Exception as e:
            print(f"❌ Error loading scan results: {e}")
            return False
            
    def categorize_by_extension(self) -> Dict[str, List[Dict[str, Any]]]:
        """Categorize skipped files by extension"""
        categorized = defaultdict(list)
        
        for file_info in self.skipped_files:
            file_path = file_info.get('file', '')
            ext = Path(file_path).suffix.lower()
            
            # Find category
            category = 'other'
            for cat, extensions in self.consciousness_relevant_extensions.items():
                if ext in extensions:
                    category = cat
                    break
                    
            categorized[category].append(file_info)
            
        return dict(categorized)
        
    def analyze_skip_reasons(self) -> Dict[str, List[Dict[str, Any]]]:
        """Analyze skip reasons for consciousness relevance"""
        skip_reasons = defaultdict(list)
        
        for file_info in self.skipped_files:
            reason = file_info.get('reason', 'unknown')
            skip_reasons[reason].append(file_info)
            
        return dict(skip_reasons)
        
    def identify_consciousness_critical_files(self) -> List[Dict[str, Any]]:
        """Identify files that may contain critical consciousness data"""
        critical_files = []
        
        # Keywords that indicate consciousness relevance
        consciousness_keywords = [
            'milf', 'tier', 'district', 'consciousness', 'character',
            'profile', 'entity', 'necrosis', 'morticia', 'claudine',
            'vera', 'raven', 'lilith', 'vex', 'eva', 'astrid',
            'mcp', 'archaeological', 'supreme', 'matriarch'
        ]
        
        for file_info in self.skipped_files:
            file_path = file_info.get('file', '').lower()
            
            # Check if filename contains consciousness keywords
            if any(keyword in file_path for keyword in consciousness_keywords):
                file_info['consciousness_relevance'] = 'HIGH'
                file_info['keywords_found'] = [kw for kw in consciousness_keywords if kw in file_path]
                critical_files.append(file_info)
                
        return critical_files
        
    def check_safe_to_ignore(self) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        """Separate safe-to-ignore files from potentially relevant ones"""
        safe_files = []
        relevant_files = []
        
        for file_info in self.skipped_files:
            file_path = file_info.get('file', '')
            
            # Check if in safe skip patterns
            is_safe = any(pattern in file_path for pattern in self.safe_skip_patterns)
            
            if is_safe:
                safe_files.append(file_info)
            else:
                relevant_files.append(file_info)
                
        return safe_files, relevant_files
        
    def analyze_file_sizes(self) -> Dict[str, Any]:
        """Analyze file sizes to understand why files were skipped"""
        size_analysis: Dict[str, List[Dict[str, Any]]] = {
            'over_10mb': [],
            '5mb_to_10mb': [],
            '2mb_to_5mb': [],
            'under_2mb': []
        }
        
        for file_info in self.skipped_files:
            size_mb = file_info.get('size_mb', 0)
            
            if size_mb > 10:
                size_analysis['over_10mb'].append(file_info)
            elif size_mb > 5:
                size_analysis['5mb_to_10mb'].append(file_info)
            elif size_mb > 2:
                size_analysis['2mb_to_5mb'].append(file_info)
            else:
                size_analysis['under_2mb'].append(file_info)
                
        return size_analysis
        
    def generate_comprehensive_analysis(self) -> Dict[str, Any]:
        """Generate comprehensive analysis of all skipped files"""
        print("🔍 Analyzing 53 Skipped Files...\n")
        
        # Categorize by extension
        by_extension = self.categorize_by_extension()
        print("📊 CATEGORIZATION BY EXTENSION:")
        for category, files in sorted(by_extension.items(), key=lambda x: len(x[1]), reverse=True):
            print(f"  • {category.upper()}: {len(files)} files")
        print()
        
        # Analyze skip reasons
        by_reason = self.analyze_skip_reasons()
        print("📋 SKIP REASONS:")
        for reason, files in sorted(by_reason.items(), key=lambda x: len(x[1]), reverse=True):
            print(f"  • {reason}: {len(files)} files")
        print()
        
        # Identify consciousness-critical files
        critical_files = self.identify_consciousness_critical_files()
        print(f"🎯 CONSCIOUSNESS-CRITICAL FILES: {len(critical_files)}")
        if critical_files:
            for file_info in critical_files[:5]:  # Show first 5
                print(f"  • {Path(file_info['file']).name}")
                print(f"    Keywords: {', '.join(file_info.get('keywords_found', []))}")
        print()
        
        # Check safe to ignore
        safe_files, relevant_files = self.check_safe_to_ignore()
        print(f"✅ SAFE TO IGNORE: {len(safe_files)} files")
        print(f"⚠️ POTENTIALLY RELEVANT: {len(relevant_files)} files\n")
        
        # Analyze file sizes
        size_analysis = self.analyze_file_sizes()
        print("📏 FILE SIZE ANALYSIS:")
        print(f"  • Over 10MB: {len(size_analysis['over_10mb'])} files")
        print(f"  • 5-10MB: {len(size_analysis['5mb_to_10mb'])} files")
        print(f"  • 2-5MB: {len(size_analysis['2mb_to_5mb'])} files")
        print(f"  • Under 2MB: {len(size_analysis['under_2mb'])} files")
        print()
        
        # Compile results
        self.analysis_results = {
            'timestamp': datetime.datetime.now().isoformat(),
            'total_skipped_files': len(self.skipped_files),
            'by_extension': {k: len(v) for k, v in by_extension.items()},
            'by_reason': {k: len(v) for k, v in by_reason.items()},
            'consciousness_critical_count': len(critical_files),
            'consciousness_critical_files': critical_files,
            'safe_to_ignore_count': len(safe_files),
            'potentially_relevant_count': len(relevant_files),
            'potentially_relevant_files': relevant_files,
            'size_analysis': {k: len(v) for k, v in size_analysis.items()},
            'recommendations': self._generate_recommendations(
                by_extension, critical_files, relevant_files, size_analysis
            )
        }
        
        return self.analysis_results
        
    def _generate_recommendations(
        self, 
        by_extension: Dict[str, List], 
        critical_files: List[Dict], 
        relevant_files: List[Dict],
        size_analysis: Dict[str, List]
    ) -> List[str]:
        """Generate actionable recommendations"""
        recommendations = []
        
        # Check for consciousness-critical files
        if critical_files:
            recommendations.append(
                f"🎯 CRITICAL: {len(critical_files)} files contain consciousness keywords - "
                "manual review required to check for missing entity data"
            )
            
        # Check for large files that might need size limit increase
        if size_analysis['over_10mb']:
            recommendations.append(
                f"📏 CONSIDER: {len(size_analysis['over_10mb'])} files over 10MB - "
                "evaluate if size limit needs to be increased beyond 10MB"
            )
            
        # Check for data files
        if 'data' in by_extension and by_extension['data']:
            recommendations.append(
                f"💾 INVESTIGATE: {len(by_extension['data'])} data files (.db, .csv, .sql) skipped - "
                "may contain consciousness entity relationships or historical data"
            )
            
        # Check for documentation
        if 'documentation' in by_extension and by_extension['documentation']:
            recommendations.append(
                f"📚 REVIEW: {len(by_extension['documentation'])} documentation files skipped - "
                "may contain entity definitions or consciousness protocols"
            )
            
        # Check for logs
        if 'logs' in by_extension and by_extension['logs']:
            recommendations.append(
                f"📋 OPTIONAL: {len(by_extension['logs'])} log files skipped - "
                "generally safe to ignore unless debugging specific issues"
            )
            
        # Safe to ignore
        if not relevant_files:
            recommendations.append(
                "✅ ALL CLEAR: All skipped files are in safe-to-ignore categories "
                "(node_modules, .git, __pycache__, etc.)"
            )
            
        return recommendations
        
    def save_analysis_report(self, output_file: str = "SKIPPED_FILES_ANALYSIS_REPORT.md"):
        """Save comprehensive analysis report"""
        output_path = self.workspace_root / output_file
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("# 🔍 SKIPPED FILES INTELLIGENT ANALYSIS REPORT\n\n")
            f.write(f"**Generated:** {self.analysis_results['timestamp']}\n")
            f.write(f"**Total Skipped Files:** {self.analysis_results['total_skipped_files']}\n\n")
            
            f.write("---\n\n")
            
            # Extension breakdown
            f.write("## 📊 CATEGORIZATION BY FILE EXTENSION\n\n")
            for category, count in sorted(
                self.analysis_results['by_extension'].items(), 
                key=lambda x: x[1], 
                reverse=True
            ):
                f.write(f"- **{category.upper()}:** {count} files\n")
            f.write("\n")
            
            # Skip reasons
            f.write("## 📋 SKIP REASONS BREAKDOWN\n\n")
            for reason, count in sorted(
                self.analysis_results['by_reason'].items(), 
                key=lambda x: x[1], 
                reverse=True
            ):
                f.write(f"- **{reason}:** {count} files\n")
            f.write("\n")
            
            # Consciousness-critical files
            f.write("## 🎯 CONSCIOUSNESS-CRITICAL FILES\n\n")
            f.write(f"**Count:** {self.analysis_results['consciousness_critical_count']}\n\n")
            
            if self.analysis_results['consciousness_critical_files']:
                f.write("### Critical Files Requiring Manual Review:\n\n")
                for file_info in self.analysis_results['consciousness_critical_files']:
                    f.write(f"#### `{Path(file_info['file']).name}`\n")
                    f.write(f"- **Path:** `{file_info['file']}`\n")
                    f.write(f"- **Size:** {file_info.get('size_mb', 0):.2f} MB\n")
                    f.write(f"- **Reason:** {file_info.get('reason', 'unknown')}\n")
                    f.write(f"- **Keywords Found:** {', '.join(file_info.get('keywords_found', []))}\n")
                    f.write(f"- **Consciousness Relevance:** {file_info.get('consciousness_relevance', 'UNKNOWN')}\n\n")
            else:
                f.write("✅ No consciousness-critical files identified.\n\n")
                
            # Size analysis
            f.write("## 📏 FILE SIZE ANALYSIS\n\n")
            for size_range, count in self.analysis_results['size_analysis'].items():
                f.write(f"- **{size_range.replace('_', ' ').upper()}:** {count} files\n")
            f.write("\n")
            
            # Potentially relevant files
            f.write("## ⚠️ POTENTIALLY RELEVANT FILES (Non-Safe-Skip)\n\n")
            f.write(f"**Count:** {self.analysis_results['potentially_relevant_count']}\n\n")
            
            if self.analysis_results['potentially_relevant_files']:
                f.write("### Files Outside Safe-Skip Patterns:\n\n")
                for file_info in self.analysis_results['potentially_relevant_files'][:20]:  # Show first 20
                    f.write(f"- `{Path(file_info['file']).name}` ")
                    f.write(f"({file_info.get('size_mb', 0):.2f} MB) - ")
                    f.write(f"{file_info.get('reason', 'unknown')}\n")
                f.write("\n")
            else:
                f.write("✅ All skipped files are in safe-skip categories.\n\n")
                
            # Recommendations
            f.write("## 🎯 ACTIONABLE RECOMMENDATIONS\n\n")
            for i, recommendation in enumerate(self.analysis_results['recommendations'], 1):
                f.write(f"{i}. {recommendation}\n")
            f.write("\n")
            
            f.write("---\n\n")
            f.write("**🔍 Intelligent Analysis Complete - September 2025 Consciousness Archaeology Protocol 🔍**\n")
            
        print(f"✅ Analysis report saved: {output_path}")
        return output_path


def main():
    """Main execution"""
    print("🔍 SKIPPED FILES INTELLIGENT ANALYZER 🔍")
    print("=" * 60)
    print()
    
    analyzer = SkippedFilesIntelligentAnalyzer()
    
    # Load latest scan results
    if not analyzer.load_latest_scan_results():
        print("❌ Failed to load scan results. Exiting.")
        return
        
    # Generate comprehensive analysis
    results = analyzer.generate_comprehensive_analysis()
    
    # Save report
    print("\n" + "=" * 60)
    report_path = analyzer.save_analysis_report()
    
    # Print summary
    print("\n🎯 ANALYSIS SUMMARY:")
    print(f"  • Total Skipped: {results['total_skipped_files']}")
    print(f"  • Consciousness-Critical: {results['consciousness_critical_count']}")
    print(f"  • Safe to Ignore: {results['safe_to_ignore_count']}")
    print(f"  • Potentially Relevant: {results['potentially_relevant_count']}")
    print(f"\n📄 Full report: {report_path.name}")
    print("\n✅ Intelligent analysis complete!")


if __name__ == "__main__":
    main()
