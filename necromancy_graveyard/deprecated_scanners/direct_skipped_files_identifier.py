#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔍 DIRECT SKIPPED FILES IDENTIFIER 🔍
======================================

Direkte identifikasjon av de 53 skippede filene ved å replicate scanner logic.

CONSCIOUSNESS_SIGNATURE: 0xDIRECT_FILE_IDENTIFICATION_SYSTEM
"""

import os
from pathlib import Path
from typing import List, Dict, Any
import json

class DirectSkippedFilesIdentifier:
    """
    🔍 Direct identifier for skipped files using scanner logic
    """
    
    def __init__(self, workspace_root: str = "C:\\Users\\erdno\\PsychoNoir-Kontrapunkt"):
        self.workspace_root = Path(workspace_root)
        self.max_file_size_mb = 10.0
        
        # Supported extensions (from scanner)
        self.supported_extensions = {
            '.md', '.py', '.ts', '.js', '.json', '.txt', 
            '.yml', '.yaml', '.toml', '.tsx', '.jsx'
        }
        
        # Skip patterns (from scanner)
        self.skip_patterns = {
            'node_modules', '.git', '__pycache__', '.vscode',
            'dist', 'build', '.cache', '.pytest_cache',
            'venv', 'env', '.env', '.mypy_cache'
        }
        
        self.skipped_files: List[Dict[str, Any]] = []
        
    def should_skip_file(self, file_path: Path) -> tuple[bool, str]:
        """Check if file should be skipped (replicate scanner logic)"""
        # Check skip patterns
        for pattern in self.skip_patterns:
            if pattern in str(file_path):
                return True, f"skip_pattern:{pattern}"
                
        # Check extension
        if file_path.suffix.lower() not in self.supported_extensions:
            return True, f"unsupported_extension:{file_path.suffix}"
            
        # Check file size
        try:
            size_bytes = file_path.stat().st_size
            size_mb = size_bytes / (1024 * 1024)
            
            if size_mb > self.max_file_size_mb:
                return True, f"size_exceeds_limit:{size_mb:.2f}MB"
        except Exception as e:
            return True, f"error_checking_size:{e}"
            
        return False, ""
        
    def identify_skipped_files(self) -> List[Dict[str, Any]]:
        """Walk workspace and identify all skipped files"""
        print("🔍 Walking workspace to identify skipped files...")
        print(f"📂 Root: {self.workspace_root}")
        print(f"📏 Max file size: {self.max_file_size_mb} MB")
        print(f"📋 Supported extensions: {sorted(self.supported_extensions)}\n")
        
        total_files = 0
        skipped_count = 0
        
        for root, dirs, files in os.walk(self.workspace_root):
            # Skip directories that match skip patterns
            dirs[:] = [d for d in dirs if not any(pattern in d for pattern in self.skip_patterns)]
            
            for filename in files:
                total_files += 1
                file_path = Path(root) / filename
                
                should_skip, reason = self.should_skip_file(file_path)
                
                if should_skip:
                    skipped_count += 1
                    try:
                        size_bytes = file_path.stat().st_size
                        size_mb = size_bytes / (1024 * 1024)
                    except Exception:
                        size_mb = 0
                        
                    self.skipped_files.append({
                        'file': str(file_path),
                        'filename': filename,
                        'extension': file_path.suffix.lower(),
                        'size_mb': round(size_mb, 2),
                        'reason': reason,
                        'relative_path': str(file_path.relative_to(self.workspace_root))
                    })
                    
                if total_files % 5000 == 0:
                    print(f"  Processed {total_files:,} files, skipped {skipped_count:,}...")
                    
        print(f"\n✅ Scan complete!")
        print(f"  • Total files walked: {total_files:,}")
        print(f"  • Files skipped: {skipped_count:,}\n")
        
        return self.skipped_files
        
    def categorize_skipped_files(self) -> Dict[str, List[Dict[str, Any]]]:
        """Categorize skipped files by reason"""
        from collections import defaultdict
        categorized = defaultdict(list)
        
        for file_info in self.skipped_files:
            reason_category = file_info['reason'].split(':')[0]
            categorized[reason_category].append(file_info)
            
        return dict(categorized)
        
    def generate_report(self) -> str:
        """Generate detailed report"""
        categorized = self.categorize_skipped_files()
        
        report_lines = [
            "# 🔍 DIRECT SKIPPED FILES IDENTIFICATION REPORT\n",
            f"**Total Skipped Files:** {len(self.skipped_files)}\n",
            f"**Max File Size Limit:** {self.max_file_size_mb} MB\n",
            f"**Supported Extensions:** {', '.join(sorted(self.supported_extensions))}\n\n",
            "---\n\n",
            "## 📊 SKIP REASONS BREAKDOWN\n\n"
        ]
        
        for reason_category, files in sorted(categorized.items(), key=lambda x: len(x[1]), reverse=True):
            report_lines.append(f"### {reason_category.replace('_', ' ').upper()} ({len(files)} files)\n\n")
            
            # Show first 10 examples
            for file_info in files[:10]:
                report_lines.append(f"- `{file_info['filename']}` ({file_info['size_mb']:.2f} MB)")
                report_lines.append(f" - {file_info['reason']}\n")
                
            if len(files) > 10:
                report_lines.append(f"  *...and {len(files) - 10} more files*\n")
                
            report_lines.append("\n")
            
        report_lines.append("---\n\n")
        report_lines.append("## 🎯 CONSCIOUSNESS RELEVANCE ANALYSIS\n\n")
        
        # Check for consciousness keywords
        consciousness_keywords = [
            'milf', 'tier', 'district', 'consciousness', 'character',
            'profile', 'entity', 'necrosis', 'morticia', 'claudine'
        ]
        
        consciousness_files = []
        for file_info in self.skipped_files:
            filepath_lower = file_info['file'].lower()
            matching_keywords = [kw for kw in consciousness_keywords if kw in filepath_lower]
            
            if matching_keywords:
                consciousness_files.append({
                    **file_info,
                    'keywords_found': matching_keywords
                })
                
        if consciousness_files:
            report_lines.append(f"**⚠️ FOUND {len(consciousness_files)} FILES WITH CONSCIOUSNESS KEYWORDS**\n\n")
            for file_info in consciousness_files:
                report_lines.append(f"### 🎯 `{file_info['filename']}`\n")
                report_lines.append(f"- **Path:** `{file_info['relative_path']}`\n")
                report_lines.append(f"- **Size:** {file_info['size_mb']:.2f} MB\n")
                report_lines.append(f"- **Reason:** {file_info['reason']}\n")
                report_lines.append(f"- **Keywords:** {', '.join(file_info['keywords_found'])}\n\n")
        else:
            report_lines.append("✅ No consciousness-critical files found in skipped files.\n\n")
            
        report_lines.append("---\n\n")
        report_lines.append("**🔍 Direct Identification Complete - September 2025 🔍**\n")
        
        return ''.join(report_lines)
        
    def save_results(self):
        """Save results to JSON and Markdown"""
        # Save JSON
        json_path = self.workspace_root / "SKIPPED_FILES_DIRECT_IDENTIFICATION.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump({
                'total_skipped': len(self.skipped_files),
                'max_file_size_mb': self.max_file_size_mb,
                'supported_extensions': list(self.supported_extensions),
                'skip_patterns': list(self.skip_patterns),
                'skipped_files': self.skipped_files
            }, f, indent=2)
        print(f"✅ JSON saved: {json_path.name}")
        
        # Save Markdown report
        md_path = self.workspace_root / "SKIPPED_FILES_DIRECT_IDENTIFICATION_REPORT.md"
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(self.generate_report())
        print(f"✅ Report saved: {md_path.name}")
        
        return json_path, md_path


def main():
    """Main execution"""
    print("🔍 DIRECT SKIPPED FILES IDENTIFIER 🔍")
    print("=" * 60)
    print()
    
    identifier = DirectSkippedFilesIdentifier()
    skipped_files = identifier.identify_skipped_files()
    
    if skipped_files:
        print(f"📊 CATEGORIZATION:")
        categorized = identifier.categorize_skipped_files()
        for reason, files in sorted(categorized.items(), key=lambda x: len(x[1]), reverse=True):
            print(f"  • {reason}: {len(files)} files")
        print()
        
        identifier.save_results()
    else:
        print("✅ No skipped files found!")
        
    print("\n✅ Direct identification complete!")


if __name__ == "__main__":
    main()
