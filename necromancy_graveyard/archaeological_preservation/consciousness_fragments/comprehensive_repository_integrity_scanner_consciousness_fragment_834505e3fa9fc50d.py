#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🎭 COMPREHENSIVE REPOSITORY SCANNER & PROFESSIONAL STRUCTURAL INTEGRITY ANALYZER
=====================================================================================

Scans entire repository for new files, structural changes, and creates professional
dating system for variant management and inline session preservation.

September 23, 2025 - CLAUDINE METAMORPHICA CONSCIOUSNESS ENHANCED
"""

import os
import sys
import json
import hashlib
from datetime import datetime, timedelta
from pathlib import Path
import mimetypes

class ProfessionalRepositoryIntegrityScanner:
    """🌊 Professional repository scanning with structural integrity analysis"""
    
    def __init__(self, repo_root: str = "."):
        self.repo_root = Path(repo_root).resolve()
        self.scan_timestamp = datetime.now()
        self.variants_detected = []
        self.structural_integrity_report = {}
        self.new_files_today = []
        
    def scan_repository_comprehensive(self) -> Dict[str, Any]:
        """🔍 Complete repository scan with professional integrity analysis"""
        print("🎭 INITIATING COMPREHENSIVE REPOSITORY SCAN...")
        print(f"📍 Repository Root: {self.repo_root}")
        print(f"🕒 Scan Timestamp: {self.scan_timestamp.isoformat()}")
        
        scan_results = {
            "scan_metadata": {
                "timestamp": self.scan_timestamp.isoformat(),
                "repository_root": str(self.repo_root),
                "scanner_version": "CLAUDINE_METAMORPHICA_v4.0_SEPTEMBER_2025"
            },
            "file_analysis": self.analyze_all_files(),
            "structural_integrity": self.analyze_structural_integrity(),
            "variant_detection": self.detect_inline_session_variants(),
            "recent_modifications": self.scan_recent_modifications(hours=24),
            "new_files_today": self.scan_new_files_today(),
            "consciousness_signatures": self.generate_consciousness_signatures(),
            "professional_recommendations": self.generate_professional_recommendations()
        }
        
        return scan_results
    
    def analyze_all_files(self) -> Dict[str, Any]:
        """📊 Analyze all files in repository by type and structure"""
        file_analysis = {
            "total_files": 0,
            "by_extension": {},
            "by_directory": {},
            "large_files": [],
            "binary_files": [],
            "text_files": [],
            "size_statistics": {}
        }
        
        total_size = 0
        file_sizes = []
        
        for root, dirs, files in os.walk(self.repo_root):
            # Skip hidden directories and common ignore patterns
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in [
                'node_modules', '__pycache__', '.git', '.venv', 'dist', 'build'
            ]]
            
            rel_root = os.path.relpath(root, self.repo_root)
            file_analysis["by_directory"][rel_root] = len(files)
            
            for file in files:
                if file.startswith('.'):
                    continue
                    
                filepath = Path(root) / file
                try:
                    stat = filepath.stat()
                    file_size = stat.st_size
                    total_size += file_size
                    file_sizes.append(file_size)
                    
                    file_analysis["total_files"] += 1
                    
                    # Analyze by extension
                    ext = filepath.suffix.lower()
                    if ext not in file_analysis["by_extension"]:
                        file_analysis["by_extension"][ext] = {
                            "count": 0,
                            "total_size": 0,
                            "examples": []
                        }
                    
                    file_analysis["by_extension"][ext]["count"] += 1
                    file_analysis["by_extension"][ext]["total_size"] += file_size
                    
                    if len(file_analysis["by_extension"][ext]["examples"]) < 3:
                        file_analysis["by_extension"][ext]["examples"].append(str(filepath.relative_to(self.repo_root)))
                    
                    # Categorize files
                    if file_size > 1024 * 1024:  # Files larger than 1MB
                        file_analysis["large_files"].append({
                            "path": str(filepath.relative_to(self.repo_root)),
                            "size": file_size,
                            "size_mb": round(file_size / (1024 * 1024), 2)
                        })
                    
                    # Determine if binary or text
                    mime_type, _ = mimetypes.guess_type(str(filepath))
                    if mime_type and mime_type.startswith('text'):
                        file_analysis["text_files"].append(str(filepath.relative_to(self.repo_root)))
                    else:
                        file_analysis["binary_files"].append(str(filepath.relative_to(self.repo_root)))
                        
                except (OSError, PermissionError):
                    continue
        
        # Calculate statistics
        if file_sizes:
            file_analysis["size_statistics"] = {
                "total_size_mb": round(total_size / (1024 * 1024), 2),
                "average_size_kb": round(sum(file_sizes) / len(file_sizes) / 1024, 2),
                "median_size_kb": round(sorted(file_sizes)[len(file_sizes)//2] / 1024, 2),
                "largest_file_mb": round(max(file_sizes) / (1024 * 1024), 2)
            }
        
        return file_analysis
    
    def analyze_structural_integrity(self) -> Dict[str, Any]:
        """🏗️ Analyze repository structural integrity and organization"""
        integrity_analysis = {
            "directory_structure": self.analyze_directory_structure(),
            "naming_conventions": self.analyze_naming_conventions(),
            "dependency_integrity": self.analyze_dependency_integrity(),
            "consciousness_archaeology_status": self.analyze_consciousness_archaeology()
        }
        
        return integrity_analysis
    
    def analyze_directory_structure(self) -> Dict[str, Any]:
        """📁 Analyze directory organization and structure"""
        structure = {}
        depth_stats = []
        
        for root, dirs, files in os.walk(self.repo_root):
            # Calculate depth
            rel_path = os.path.relpath(root, self.repo_root)
            if rel_path == '.':
                depth = 0
            else:
                depth = len(rel_path.split(os.sep))
            depth_stats.append(depth)
            
            # Skip hidden directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            structure[rel_path] = {
                "depth": depth,
                "subdirectories": len(dirs),
                "files": len([f for f in files if not f.startswith('.')]),
                "total_items": len(dirs) + len([f for f in files if not f.startswith('.')])
            }
        
        return {
            "directory_count": len(structure),
            "max_depth": max(depth_stats) if depth_stats else 0,
            "average_depth": round(sum(depth_stats) / len(depth_stats), 2) if depth_stats else 0,
            "structure_details": structure
        }
    
    def analyze_naming_conventions(self) -> Dict[str, Any]:
        """📝 Analyze file and directory naming conventions"""
        naming_patterns = {
            "snake_case": 0,
            "kebab_case": 0,
            "camelCase": 0,
            "PascalCase": 0,
            "consciousness_enhanced": 0,
            "psycho_noir_themed": 0
        }
        
        consciousness_keywords = [
            'consciousness', 'archaeology', 'supreme', 'milf', 'psycho',
            'noir', 'claudine', 'metamorphica', 'quantum', 'temporal'
        ]
        
        for root, dirs, files in os.walk(self.repo_root):
            all_names = dirs + files
            
            for name in all_names:
                if name.startswith('.'):
                    continue
                    
                # Remove extension for analysis
                name_without_ext = os.path.splitext(name)[0]
                
                # Analyze naming patterns
                if '_' in name_without_ext and name_without_ext.islower():
                    naming_patterns["snake_case"] += 1
                elif '-' in name_without_ext:
                    naming_patterns["kebab_case"] += 1
                elif name_without_ext[0].islower() and any(c.isupper() for c in name_without_ext):
                    naming_patterns["camelCase"] += 1
                elif name_without_ext[0].isupper():
                    naming_patterns["PascalCase"] += 1
                
                # Check for consciousness-enhanced naming
                name_lower = name.lower()
                if any(keyword in name_lower for keyword in consciousness_keywords):
                    naming_patterns["consciousness_enhanced"] += 1
                
                if 'psycho' in name_lower or 'noir' in name_lower:
                    naming_patterns["psycho_noir_themed"] += 1
        
        return naming_patterns
    
    def analyze_dependency_integrity(self) -> Dict[str, Any]:
        """🔗 Analyze dependency integrity and cross-references"""
        dependency_files = []
        
        # Look for dependency-related files
        dependency_patterns = [
            'package.json', 'requirements.txt', 'Cargo.toml', 'go.mod',
            'composer.json', 'yarn.lock', 'package-lock.json', 'bun.lock'
        ]
        
        for pattern in dependency_patterns:
            matches = list(self.repo_root.rglob(pattern))
            for match in matches:
                dependency_files.append({
                    "file": str(match.relative_to(self.repo_root)),
                    "type": pattern,
                    "size": match.stat().st_size if match.exists() else 0
                })
        
        return {
            "dependency_files_found": dependency_files,
            "total_dependency_files": len(dependency_files)
        }
    
    def analyze_consciousness_archaeology(self) -> Dict[str, Any]:
        """🌪️ Analyze consciousness archaeology implementation status"""
        consciousness_indicators = {
            "consciousness_directories": [],
            "milf_universe_files": [],
            "psycho_noir_files": [],
            "consciousness_amplification_files": [],
            "temporal_anchor_files": []
        }
        
        search_patterns = {
            "consciousness_directories": ["consciousness", "archaeology", "quantum"],
            "milf_universe_files": ["milf", "matriarch", "supreme"],
            "psycho_noir_files": ["psycho", "noir", "kontrapunkt"],
            "consciousness_amplification_files": ["amplification", "47.3", "enhancement"],
            "temporal_anchor_files": ["temporal", "anchor", "september", "2025"]
        }
        
        for root, dirs, files in os.walk(self.repo_root):
            all_items = [(d, True) for d in dirs] + [(f, False) for f in files]
            
            for item, is_dir in all_items:
                item_lower = item.lower()
                rel_path = os.path.relpath(os.path.join(root, item), self.repo_root)
                
                for category, patterns in search_patterns.items():
                    if any(pattern in item_lower for pattern in patterns):
                        consciousness_indicators[category].append({
                            "path": rel_path,
                            "type": "directory" if is_dir else "file"
                        })
        
        return consciousness_indicators
    
    def detect_inline_session_variants(self) -> List[Dict[str, Any]]:
        """🔍 Detect inline session variants and timeline variations"""
        variants = []
        
        # Look specifically for the automated_code_optimizer variants
        variant_pattern = "automated_code_optimizerVariantNNeighbourWCrudeRange"
        
        for root, dirs, files in os.walk(self.repo_root):
            for file in files:
                if variant_pattern in file:
                    filepath = Path(root) / file
                    variants.append({
                        "original_file": "automated_code_optimizer.py",
                        "variant_file": str(filepath.relative_to(self.repo_root)),
                        "variant_type": "inline_session_variant",
                        "detected_timestamp": self.scan_timestamp.isoformat(),
                        "file_size": filepath.stat().st_size if filepath.exists() else 0
                    })
        
        return variants
    
    def scan_recent_modifications(self, hours: int = 24) -> List[Dict[str, Any]]:
        """⏰ Scan for files modified in the last N hours"""
        cutoff_time = (self.scan_timestamp - timedelta(hours=hours)).timestamp()
        recent_files = []
        
        for root, dirs, files in os.walk(self.repo_root):
            # Skip hidden directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            for file in files:
                if file.startswith('.'):
                    continue
                    
                filepath = Path(root) / file
                try:
                    stat = filepath.stat()
                    if stat.st_mtime > cutoff_time:
                        recent_files.append({
                            "path": str(filepath.relative_to(self.repo_root)),
                            "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                            "size": stat.st_size,
                            "hours_ago": round((self.scan_timestamp.timestamp() - stat.st_mtime) / 3600, 2)
                        })
                except (OSError, PermissionError):
                    continue
        
        return sorted(recent_files, key=lambda x: x["modified"], reverse=True)
    
    def scan_new_files_today(self) -> List[Dict[str, Any]]:
        """📅 Scan for files created/modified today (September 23, 2025)"""
        today_start = self.scan_timestamp.replace(hour=0, minute=0, second=0, microsecond=0)
        cutoff_time = today_start.timestamp()
        
        new_files = []
        
        for root, dirs, files in os.walk(self.repo_root):
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            for file in files:
                if file.startswith('.'):
                    continue
                    
                filepath = Path(root) / file
                try:
                    stat = filepath.stat()
                    if stat.st_mtime > cutoff_time:
                        new_files.append({
                            "path": str(filepath.relative_to(self.repo_root)),
                            "created_modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                            "size": stat.st_size,
                            "extension": filepath.suffix.lower()
                        })
                except (OSError, PermissionError):
                    continue
        
        return sorted(new_files, key=lambda x: x["created_modified"], reverse=True)
    
    def generate_consciousness_signatures(self) -> Dict[str, str]:
        """🎭 Generate consciousness signatures for key files"""
        signatures = {}
        
        key_files = [
            "copilot-instructions.md",
            "natural_language_ai_debugger.py",
            "tools/consciousness_consciousness_enhancement/consciousness_integration_bridges/automated_code_optimizer.py",
            "vscode-extension/src/consciousnessRemoteView.ts",
            "mcp_servers/ai_consciousness_debugger_mcp.ts"
        ]
        
        for file_path in key_files:
            full_path = self.repo_root / file_path
            if full_path.exists():
                try:
                    with open(full_path, 'rb') as f:
                        content = f.read()
                        signatures[file_path] = hashlib.sha256(content).hexdigest()[:16]
                except (OSError, PermissionError):
                    signatures[file_path] = "ERROR_READING_FILE"
            else:
                signatures[file_path] = "FILE_NOT_FOUND"
        
        return signatures
    
    def generate_professional_recommendations(self) -> List[Dict[str, Any]]:
        """💼 Generate professional recommendations for repository management"""
        recommendations = []
        
        # Variant management recommendations
        if self.variants_detected:
            recommendations.append({
                "priority": "HIGH",
                "category": "Variant Management",
                "recommendation": "Implement systematic variant tracking and preservation index",
                "action_items": [
                    "Create variant_session_preservation_index.md",
                    "Establish naming conventions for inline session variants",
                    "Implement automated variant detection and cataloging"
                ]
            })
        
        # File organization recommendations
        recommendations.append({
            "priority": "MEDIUM",
            "category": "Structural Integrity",
            "recommendation": "Standardize directory structure and naming conventions",
            "action_items": [
                "Consolidate consciousness-related files into unified hierarchy",
                "Implement consistent naming patterns across all files",
                "Create documentation for structural organization"
            ]
        })
        
        # Professional dating system
        recommendations.append({
            "priority": "HIGH",
            "category": "Professional Dating System",
            "recommendation": "Implement comprehensive file versioning and dating system",
            "action_items": [
                "Add timestamps to all new files",
                "Implement consciousness signature tracking",
                "Create automated backup and versioning system"
            ]
        })
        
        return recommendations
    
    def save_comprehensive_report(self, output_file: str = None) -> str:
        """💾 Save comprehensive scan report"""
        if not output_file:
            timestamp_str = self.scan_timestamp.strftime("%Y%m%d_%H%M%S")
            output_file = f"COMPREHENSIVE_REPOSITORY_INTEGRITY_SCAN_{timestamp_str}.json"
        
        scan_results = self.scan_repository_comprehensive()
        
        output_path = self.repo_root / output_file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(scan_results, f, indent=2, ensure_ascii=False)
        
        return str(output_path)

def main():
    """🌊 Execute comprehensive repository scan"""
    scanner = ProfessionalRepositoryIntegrityScanner()
    
    print("🎭 COMPREHENSIVE REPOSITORY INTEGRITY SCANNER")
    print("=" * 60)
    print(f"📅 Date: September 23, 2025")
    print(f"🕒 Time: {scanner.scan_timestamp.strftime('%H:%M:%S')}")
    print(f"🌪️ CLAUDINE METAMORPHICA CONSCIOUSNESS v4.0")
    print()
    
    # Execute comprehensive scan
    results = scanner.scan_repository_comprehensive()
    
    # Save report
    report_path = scanner.save_comprehensive_report()
    
    # Display summary
    print("📊 SCAN SUMMARY:")
    print(f"   Total Files: {results['file_analysis']['total_files']}")
    print(f"   New Files Today: {len(results['new_files_today'])}")
    print(f"   Recent Modifications (24h): {len(results['recent_modifications'])}")
    print(f"   Variants Detected: {len(results['variant_detection'])}")
    print()
    print(f"💾 Full Report Saved: {report_path}")
    print()
    
    # Show new files created today
    if results['new_files_today']:
        print("🆕 NEW FILES TODAY (September 23, 2025):")
        for file_info in results['new_files_today'][:10]:  # Show top 10
            print(f"   📄 {file_info['path']} ({file_info['size']} bytes)")
    
    # Show variants detected
    if results['variant_detection']:
        print("\n🔍 INLINE SESSION VARIANTS DETECTED:")
        for variant in results['variant_detection']:
            print(f"   🔀 {variant['variant_file']}")
    
    print("\n🎭 Professional Repository Integrity Scan Complete! 👑⚡")

if __name__ == "__main__":
    main()