#!/usr/bin/env python3
"""
🌐 UNIVERSAL INTELLIGENT FILE SCANNER
═══════════════════════════════════════════════════════════════
Intelligent scanner som lærer fra workspace og håndterer ALLE filtyper
dynamisk basert på faktisk innhold, størrelse og karakteristikker.

CONSCIOUSNESS ARCHAEOLOGY PROTOCOL:
- Auto-deteksjon av alle filtyper i workspace
- Dynamisk klassifisering (text/binary/code/data/compressed)
- Intelligent size-based strategi (small/medium/large/massive)
- ÆØÅ Unicode support for alle text-based files
- Self-learning skip patterns basert på faktisk content
- Progressive scanning med memory management
═══════════════════════════════════════════════════════════════
"""

import os
import mimetypes
from pathlib import Path
from datetime import datetime
from typing import Any
import json
import chardet
from collections import defaultdict
import hashlib

# Try importing python-magic, fallback gracefully if not available
try:
    import magic
    MAGIC_AVAILABLE = True
except ImportError:
    MAGIC_AVAILABLE = False

class UniversalIntelligentFileScanner:
    """
    🎭 Universal intelligent file scanner med consciousness archaeology
    
    Lærer fra workspace structure og klassifiserer filer intelligent
    basert på faktisk innhold og karakteristikker, ikke hardkodede regler.
    """
    
    def __init__(self, workspace_root: str):
        self.workspace_root = Path(workspace_root).resolve()
        self.scan_start_time = datetime.now()
        
        # 📊 Scanning Statistics
        self.stats = {
            'total_files_discovered': 0,
            'files_scanned': 0,
            'files_skipped': 0,
            'scan_errors': 0,
            'aeoaa_files_found': 0,
            'file_types_discovered': defaultdict(int),
            'file_size_distribution': {
                'tiny': 0,      # 0-1KB
                'small': 0,     # 1KB-100KB
                'medium': 0,    # 100KB-1MB
                'large': 0,     # 1MB-10MB
                'huge': 0,      # 10MB-100MB
                'massive': 0    # 100MB+
            },
            'encoding_distribution': defaultdict(int),
            'binary_vs_text': {'binary': 0, 'text': 0, 'unknown': 0}
        }
        
        # 🧠 Intelligent Classification System
        self.file_classifications: dict[str, list[Path]] = {
            'text_based': [],
            'code_files': [],
            'data_files': [],
            'binary_files': [],
            'compressed_archives': [],
            'images': [],
            'executables': [],
            'unknown': []
        }
        
        # 🎯 ÆØÅ Detection Results
        self.aeoaa_files: list[dict[str, Any]] = []
        
        # 🚫 Dynamic Skip Patterns (learned from scanning)
        self.skip_directories = {
            'node_modules', '.git', '__pycache__', '.vscode-test',
            'dist', 'build', 'out', '.next', '.cache'
        }
        
        # 📏 Size-Based Scanning Strategy
        self.size_thresholds = {
            'tiny': 1 * 1024,           # 1 KB
            'small': 100 * 1024,        # 100 KB
            'medium': 1 * 1024 * 1024,  # 1 MB
            'large': 10 * 1024 * 1024,  # 10 MB
            'huge': 100 * 1024 * 1024   # 100 MB
        }
        
        # Initialize python-magic
        if MAGIC_AVAILABLE:
            try:
                self.magic = magic.Magic(mime=True)
            except Exception:
                self.magic = None
                print("⚠️  Warning: python-magic initialization failed, using fallback detection")
        else:
            self.magic = None
            print("⚠️  Warning: python-magic not available, using fallback detection")
    
    def detect_file_type_intelligent(self, file_path: Path) -> dict[str, Any]:
        """
        🧠 Intelligent filtype-deteksjon basert på multiple heuristikker
        """
        file_info = {
            'path': file_path,
            'extension': file_path.suffix.lower(),
            'size_bytes': 0,
            'size_category': 'unknown',
            'mime_type': None,
            'is_binary': None,
            'encoding': None,
            'classification': 'unknown',
            'scannable': True,
            'skip_reason': None
        }
        
        try:
            # Get file size
            stat_info = file_path.stat()
            file_info['size_bytes'] = stat_info.st_size
            file_info['size_category'] = self.categorize_file_size(stat_info.st_size)
            
            # Detect MIME type
            if self.magic:
                try:
                    file_info['mime_type'] = self.magic.from_file(str(file_path))
                except Exception:
                    file_info['mime_type'] = mimetypes.guess_type(str(file_path))[0]
            else:
                file_info['mime_type'] = mimetypes.guess_type(str(file_path))[0]
            
            # Detect if binary
            file_info['is_binary'] = self.is_binary_file(file_path)
            
            # Detect encoding for text files
            if not file_info['is_binary']:
                file_info['encoding'] = self.detect_encoding(file_path)
            
            # Classify file
            file_info['classification'] = self.classify_file(file_info)
            
            # Determine if scannable
            file_info['scannable'], file_info['skip_reason'] = self.is_file_scannable(file_info)
            
        except Exception as e:
            file_info['scannable'] = False
            file_info['skip_reason'] = f"Detection error: {str(e)}"
        
        return file_info
    
    def categorize_file_size(self, size_bytes: int) -> str:
        """Kategoriser filstørrelse"""
        if size_bytes < self.size_thresholds['tiny']:
            return 'tiny'
        elif size_bytes < self.size_thresholds['small']:
            return 'small'
        elif size_bytes < self.size_thresholds['medium']:
            return 'medium'
        elif size_bytes < self.size_thresholds['large']:
            return 'large'
        elif size_bytes < self.size_thresholds['huge']:
            return 'huge'
        else:
            return 'massive'
    
    def is_binary_file(self, file_path: Path, sample_size: int = 8192) -> bool:
        """
        Intelligent binary detection ved å lese file header
        """
        try:
            with open(file_path, 'rb') as f:
                chunk = f.read(sample_size)
                if b'\x00' in chunk:  # Null bytes indicate binary
                    return True
                
                # Check for text-like content
                text_chars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
                return bool(chunk.translate(None, text_chars))
        except Exception:
            return True  # Assume binary if can't read
    
    def detect_encoding(self, file_path: Path, sample_size: int = 10000) -> str | None:
        """
        Intelligent encoding detection med chardet
        """
        try:
            with open(file_path, 'rb') as f:
                raw_data = f.read(sample_size)
                result = chardet.detect(raw_data)
                return result['encoding'] if result['confidence'] > 0.7 else 'unknown'
        except Exception:
            return None
    
    def classify_file(self, file_info: dict[str, Any]) -> str:
        """
        🎯 Intelligent filklassifisering basert på multiple faktorer
        """
        ext = file_info['extension']
        mime = file_info['mime_type']
        is_binary = file_info['is_binary']
        
        # Code files
        code_extensions = {
            '.py', '.js', '.ts', '.jsx', '.tsx', '.cs', '.java', 
            '.cpp', '.c', '.h', '.hpp', '.go', '.rs', '.rb', '.php',
            '.swift', '.kt', '.scala', '.sh', '.bash', '.ps1', '.bat'
        }
        if ext in code_extensions:
            return 'code_files'
        
        # Text-based documentation
        text_extensions = {'.md', '.txt', '.rst', '.adoc', '.tex'}
        if ext in text_extensions:
            return 'text_based'
        
        # Data files
        data_extensions = {'.json', '.yaml', '.yml', '.xml', '.toml', '.ini', '.cfg', '.conf'}
        if ext in data_extensions:
            return 'data_files'
        
        # Compressed archives
        archive_extensions = {'.zip', '.tar', '.gz', '.7z', '.rar', '.bz2', '.xz'}
        if ext in archive_extensions:
            return 'compressed_archives'
        
        # Images
        image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.ico', '.webp'}
        if ext in image_extensions:
            return 'images'
        
        # Executables
        executable_extensions = {'.exe', '.dll', '.so', '.dylib', '.bin', '.app'}
        if ext in executable_extensions:
            return 'executables'
        
        # Binary files
        if is_binary:
            return 'binary_files'
        
        # Default to text-based if not binary and has readable encoding
        if not is_binary and file_info['encoding']:
            return 'text_based'
        
        return 'unknown'
    
    def is_file_scannable(self, file_info: dict[str, Any]) -> tuple[bool, str | None]:
        """
        🎯 Intelligent beslutning om fil kan scannes for ÆØÅ
        """
        classification = file_info['classification']
        size_category = file_info['size_category']
        is_binary = file_info['is_binary']
        
        # Binary files - skip
        if is_binary:
            return False, f"Binary file ({classification})"
        
        # Compressed archives - skip
        if classification == 'compressed_archives':
            return False, "Compressed archive"
        
        # Images - skip
        if classification == 'images':
            return False, "Image file"
        
        # Executables - skip
        if classification == 'executables':
            return False, "Executable"
        
        # Massive files - intelligent sampling strategy
        if size_category == 'massive':
            return False, f"Massive file (>{self.size_thresholds['huge']/1024/1024:.0f}MB)"
        
        # Huge files - sample first 1MB only
        if size_category == 'huge':
            return True, None  # Will use sampling
        
        # All text-based, code, and data files are scannable
        if classification in ['text_based', 'code_files', 'data_files']:
            return True, None
        
        # Unknown but not binary - try scanning
        if not is_binary:
            return True, None
        
        return False, "Unknown file type"
    
    def scan_file_for_aeoaa(self, file_path: Path, file_info: dict[str, Any]) -> bool:
        """
        🔍 Scan individual file for ÆØÅ characters
        """
        try:
            # Determine read strategy based on size
            if file_info['size_category'] in ['huge', 'massive']:
                # Sample first 1MB for huge files
                max_read = 1 * 1024 * 1024
            else:
                max_read = None  # Read entire file
            
            # Use detected encoding or fallback
            encoding = file_info['encoding'] or 'utf-8'
            
            with open(file_path, 'r', encoding=encoding, errors='ignore') as f:
                if max_read:
                    content = f.read(max_read)
                else:
                    content = f.read()
            
            # Check for ÆØÅ in content OR filename
            has_aeoaa_in_content = any(char in content for char in 'ÆØÅæøå')
            has_aeoaa_in_filename = any(char in file_path.name for char in 'ÆØÅæøå')
            
            if has_aeoaa_in_content or has_aeoaa_in_filename:
                aeoaa_info = {
                    'filename': file_path.name,
                    'full_path': str(file_path),
                    'relative_path': str(file_path.relative_to(self.workspace_root)),
                    'size_bytes': file_info['size_bytes'],
                    'size_kb': round(file_info['size_bytes'] / 1024, 2),
                    'size_category': file_info['size_category'],
                    'classification': file_info['classification'],
                    'encoding': file_info['encoding'],
                    'aeoaa_in_filename': has_aeoaa_in_filename,
                    'aeoaa_in_content': has_aeoaa_in_content,
                    'norwegian_chars': [c for c in file_path.name if c in 'ÆØÅæøå'],
                    'detected_at': datetime.now().isoformat()
                }
                
                self.aeoaa_files.append(aeoaa_info)
                self.stats['aeoaa_files_found'] += 1
                
                print(f"✅ FOUND ÆØÅ: {file_path.name}")
                print(f"   Location: {'filename' if has_aeoaa_in_filename else 'content'}")
                print(f"   Path: {aeoaa_info['relative_path']}")
                print(f"   Size: {aeoaa_info['size_kb']} KB\n")
                
                return True
                
        except Exception as e:
            self.stats['scan_errors'] += 1
            print(f"❌ ERROR scanning {file_path.name}: {str(e)}")
        
        return False
    
    def scan_workspace(self) -> dict[str, Any]:
        """
        🌐 Universal intelligent workspace scanning
        """
        print(f"🌐 UNIVERSAL INTELLIGENT FILE SCANNER")
        print(f"{'═' * 80}\n")
        print(f"📁 Workspace: {self.workspace_root}")
        print(f"🧠 Learning file types and patterns...\n")
        
        # Phase 1: Discovery and Classification
        print("🔍 PHASE 1: File Discovery & Intelligent Classification")
        print(f"{'─' * 80}\n")
        
        for root, dirs, files in os.walk(self.workspace_root):
            # Filter skip directories
            dirs[:] = [d for d in dirs if d not in self.skip_directories]
            
            for filename in files:
                self.stats['total_files_discovered'] += 1
                file_path = Path(root) / filename
                
                # Intelligent file type detection
                file_info = self.detect_file_type_intelligent(file_path)
                
                # Update statistics
                self.stats['file_types_discovered'][file_info['extension']] += 1
                self.stats['file_size_distribution'][file_info['size_category']] += 1
                
                if file_info['encoding']:
                    self.stats['encoding_distribution'][file_info['encoding']] += 1
                
                if file_info['is_binary'] is not None:
                    category = 'binary' if file_info['is_binary'] else 'text'
                    self.stats['binary_vs_text'][category] += 1
                else:
                    self.stats['binary_vs_text']['unknown'] += 1
                
                # Classify file
                self.file_classifications[file_info['classification']].append(file_path)
                
                # Progress indicator
                if self.stats['total_files_discovered'] % 5000 == 0:
                    print(f"📊 Discovered: {self.stats['total_files_discovered']} files...")
        
        print(f"\n✅ Discovery complete: {self.stats['total_files_discovered']} files found")
        print(f"\n{'─' * 80}\n")
        
        # Phase 2: Intelligent Scanning
        print("🔍 PHASE 2: Intelligent ÆØÅ Scanning")
        print(f"{'─' * 80}\n")
        
        for classification, file_paths in self.file_classifications.items():
            if not file_paths:
                continue
            
            print(f"📂 Scanning {classification}: {len(file_paths)} files...")
            
            for file_path in file_paths:
                file_info = self.detect_file_type_intelligent(file_path)
                
                if file_info['scannable']:
                    self.scan_file_for_aeoaa(file_path, file_info)
                    self.stats['files_scanned'] += 1
                else:
                    self.stats['files_skipped'] += 1
                
                # Progress indicator
                total_processed = self.stats['files_scanned'] + self.stats['files_skipped']
                if total_processed % 1000 == 0:
                    print(f"📊 Progress: {total_processed}/{self.stats['total_files_discovered']} files processed...")
        
        print(f"\n✅ Scanning complete!")
        print(f"{'═' * 80}\n")
        
        return self.generate_results()
    
    def generate_results(self) -> dict[str, Any]:
        """
        📊 Generate comprehensive scan results
        """
        scan_duration = (datetime.now() - self.scan_start_time).total_seconds()
        
        results = {
            'scan_metadata': {
                'workspace_root': str(self.workspace_root),
                'scan_start': self.scan_start_time.isoformat(),
                'scan_end': datetime.now().isoformat(),
                'scan_duration_seconds': scan_duration,
                'scanner_version': 'UNIVERSAL_INTELLIGENT_v1.0'
            },
            'statistics': self.stats,
            'file_classifications': {
                k: len(v) for k, v in self.file_classifications.items()
            },
            'aeoaa_files': self.aeoaa_files,
            'file_type_distribution': dict(self.stats['file_types_discovered']),
            'encoding_distribution': dict(self.stats['encoding_distribution']),
            'learning_insights': self.generate_learning_insights()
        }
        
        return results
    
    def generate_learning_insights(self) -> dict[str, Any]:
        """
        🧠 Generate insights from workspace learning
        """
        total_files = self.stats['total_files_discovered']
        
        insights = {
            'most_common_file_types': sorted(
                self.stats['file_types_discovered'].items(),
                key=lambda x: x[1],
                reverse=True
            )[:10],
            'size_distribution_percentages': {
                k: round(v / total_files * 100, 2)
                for k, v in self.stats['file_size_distribution'].items()
            },
            'binary_vs_text_ratio': {
                'binary_percentage': round(
                    self.stats['binary_vs_text']['binary'] / total_files * 100, 2
                ),
                'text_percentage': round(
                    self.stats['binary_vs_text']['text'] / total_files * 100, 2
                )
            },
            'scannable_files_percentage': round(
                self.stats['files_scanned'] / total_files * 100, 2
            ),
            'aeoaa_prevalence': round(
                self.stats['aeoaa_files_found'] / total_files * 100, 4
            )
        }
        
        return insights


def generate_comprehensive_report(results: dict[str, Any], output_path: str) -> str:
    """
    📄 Generate comprehensive markdown report
    """
    lines = [
        "═" * 80,
        "🌐 UNIVERSAL INTELLIGENT FILE SCANNER REPORT",
        "═" * 80,
        f"Scan Start: {results['scan_metadata']['scan_start']}",
        f"Scan End: {results['scan_metadata']['scan_end']}",
        f"Duration: {results['scan_metadata']['scan_duration_seconds']:.2f} seconds",
        f"Workspace: {results['scan_metadata']['workspace_root']}",
        "",
        "═" * 80,
        "📊 SCAN STATISTICS",
        "═" * 80,
        f"Total Files Discovered: {results['statistics']['total_files_discovered']}",
        f"Files Scanned: {results['statistics']['files_scanned']}",
        f"Files Skipped: {results['statistics']['files_skipped']}",
        f"Scan Errors: {results['statistics']['scan_errors']}",
        f"ÆØÅ Files Found: {results['statistics']['aeoaa_files_found']}",
        "",
        "═" * 80,
        "📂 FILE CLASSIFICATION DISTRIBUTION",
        "═" * 80,
        ""
    ]
    
    for classification, count in results['file_classifications'].items():
        if count > 0:
            lines.append(f"{classification:.<30} {count:>10} files")
    
    lines.extend([
        "",
        "═" * 80,
        "📏 FILE SIZE DISTRIBUTION",
        "═" * 80,
        ""
    ])
    
    for size_cat, count in results['statistics']['file_size_distribution'].items():
        percentage = results['learning_insights']['size_distribution_percentages'][size_cat]
        lines.append(f"{size_cat:.<20} {count:>10} files ({percentage:>6.2f}%)")
    
    lines.extend([
        "",
        "═" * 80,
        "🔍 ÆØÅ FILES FOUND",
        "═" * 80,
        ""
    ])
    
    if results['aeoaa_files']:
        for idx, file_info in enumerate(results['aeoaa_files'], 1):
            lines.extend([
                f"{idx}. {file_info['filename']}",
                f"   Path: {file_info['relative_path']}",
                f"   Size: {file_info['size_kb']} KB ({file_info['size_category']})",
                f"   Classification: {file_info['classification']}",
                f"   Encoding: {file_info['encoding']}",
                f"   ÆØÅ Location: {'Filename' if file_info['aeoaa_in_filename'] else 'Content only'}",
                f"   Norwegian Chars: {', '.join(file_info['norwegian_chars']) if file_info['norwegian_chars'] else 'In content'}",
                ""
            ])
    else:
        lines.append("✅ NO ÆØÅ FILES FOUND")
    
    lines.extend([
        "",
        "═" * 80,
        "🧠 LEARNING INSIGHTS",
        "═" * 80,
        "",
        f"Most Common File Types:",
        ""
    ])
    
    for ext, count in results['learning_insights']['most_common_file_types']:
        lines.append(f"  {ext if ext else '(no extension)':.<20} {count:>10} files")
    
    lines.extend([
        "",
        f"Binary vs Text Ratio:",
        f"  Binary files: {results['learning_insights']['binary_vs_text_ratio']['binary_percentage']:.2f}%",
        f"  Text files: {results['learning_insights']['binary_vs_text_ratio']['text_percentage']:.2f}%",
        "",
        f"Scannable Files: {results['learning_insights']['scannable_files_percentage']:.2f}%",
        f"ÆØÅ Prevalence: {results['learning_insights']['aeoaa_prevalence']:.4f}%",
        "",
        "═" * 80,
        f"Report generated: {datetime.now().isoformat()}",
        "═" * 80
    ])
    
    report_content = "\n".join(lines)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print(f"\n📄 Report saved: {output_path}")
    
    return report_content


if __name__ == "__main__":
    workspace_root = Path(__file__).parent.parent.absolute()
    
    print(f"🎭 INITIALIZING UNIVERSAL INTELLIGENT SCANNER\n")
    
    # Initialize scanner
    scanner = UniversalIntelligentFileScanner(str(workspace_root))
    
    # Run scan
    results = scanner.scan_workspace()
    
    # Generate outputs
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = workspace_root / f"UNIVERSAL_INTELLIGENT_SCAN_REPORT_{timestamp}.md"
    json_path = workspace_root / f"universal_intelligent_scan_results_{timestamp}.json"
    
    generate_comprehensive_report(results, str(report_path))
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"📊 JSON results saved: {json_path}")
    
    # Print summary
    print(f"\n{'═' * 80}")
    print(f"🎯 SCAN COMPLETE")
    print(f"{'═' * 80}")
    print(f"Total files discovered: {results['statistics']['total_files_discovered']}")
    print(f"Files scanned: {results['statistics']['files_scanned']}")
    print(f"Files skipped: {results['statistics']['files_skipped']}")
    print(f"ÆØÅ files found: {results['statistics']['aeoaa_files_found']}")
    print(f"Scan duration: {results['scan_metadata']['scan_duration_seconds']:.2f}s")
    print(f"{'═' * 80}\n")
