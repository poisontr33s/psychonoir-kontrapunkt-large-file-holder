#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🌐 UNIVERSAL INTELLIGENT FILE SCANNER (No External Dependencies)
═══════════════════════════════════════════════════════════════
Intelligent scanner som lærer fra workspace og håndterer ALLE filtyper
dynamisk basert på faktisk innhold - PURE PYTHON implementasjon.

CONSCIOUSNESS ARCHAEOLOGY PROTOCOL:
- Auto-deteksjon av alle filtyper i workspace
- Dynamisk klassifisering (text/binary/code/data)
- Intelligent size-based strategi
- ÆØÅ Unicode support for alle text-based files
- Self-learning skip patterns
═══════════════════════════════════════════════════════════════
"""

import os
import mimetypes
from pathlib import Path
from datetime import datetime
from typing import Any
import json
from collections import defaultdict

class UniversalIntelligentFileScanner:
    """
    🎭 Universal intelligent file scanner med consciousness archaeology
    Pure Python - ingen eksterne dependencies
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
            'encoding_detected': defaultdict(int),
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
        
        # 🚫 Dynamic Skip Patterns
        self.skip_directories = {
            'node_modules', '.git', '__pycache__', '.vscode-test',
            'dist', 'build', 'out', '.next', '.cache'
        }
        
        # 📏 Size Thresholds
        self.size_thresholds = {
            'tiny': 1 * 1024,
            'small': 100 * 1024,
            'medium': 1 * 1024 * 1024,
            'large': 10 * 1024 * 1024,
            'huge': 100 * 1024 * 1024
        }
    
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
        Pure Python binary detection
        """
        try:
            with open(file_path, 'rb') as f:
                chunk = f.read(sample_size)
                
                # Null bytes = binary
                if b'\x00' in chunk:
                    return True
                
                # Check text characters
                text_chars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
                non_text = chunk.translate(None, text_chars)
                
                # If >30% non-text, consider binary
                if len(non_text) / len(chunk) > 0.30:
                    return True
                
                return False
        except Exception:
            return True
    
    def simple_encoding_detect(self, file_path: Path) -> str:
        """
        Simple encoding detection without chardet
        """
        encodings_to_try = ['utf-8', 'utf-16', 'latin-1', 'cp1252', 'ascii']
        
        for encoding in encodings_to_try:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    f.read(1024)  # Try reading a bit
                return encoding
            except Exception:
                continue
        
        return 'unknown'
    
    def classify_file(self, file_path: Path, is_binary: bool) -> str:
        """
        Intelligent filklassifisering
        """
        ext = file_path.suffix.lower()
        
        # Code files
        code_extensions = {
            '.py', '.js', '.ts', '.jsx', '.tsx', '.cs', '.java', 
            '.cpp', '.c', '.h', '.hpp', '.go', '.rs', '.rb', '.php',
            '.swift', '.kt', '.scala', '.sh', '.bash', '.ps1', '.bat'
        }
        if ext in code_extensions:
            return 'code_files'
        
        # Text-based
        text_extensions = {'.md', '.txt', '.rst', '.adoc', '.tex'}
        if ext in text_extensions:
            return 'text_based'
        
        # Data files
        data_extensions = {'.json', '.yaml', '.yml', '.xml', '.toml', '.ini', '.cfg', '.conf'}
        if ext in data_extensions:
            return 'data_files'
        
        # Compressed
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
        
        # Binary vs text
        if is_binary:
            return 'binary_files'
        
        return 'text_based' if not is_binary else 'unknown'
    
    def is_file_scannable(self, classification: str, size_category: str, is_binary: bool) -> tuple[bool, str | None]:
        """
        Beslut om fil kan scannes
        """
        if is_binary:
            return False, f"Binary file ({classification})"
        
        if classification == 'compressed_archives':
            return False, "Compressed archive"
        
        if classification == 'images':
            return False, "Image file"
        
        if classification == 'executables':
            return False, "Executable"
        
        if size_category == 'massive':
            return False, "Massive file (>100MB)"
        
        if classification in ['text_based', 'code_files', 'data_files']:
            return True, None
        
        if not is_binary:
            return True, None
        
        return False, "Unknown file type"
    
    def scan_file_for_aeoaa(self, file_path: Path, file_info: dict[str, Any]) -> bool:
        """
        Scan file for ÆØÅ
        """
        try:
            # Sampling strategy for large files
            if file_info['size_category'] in ['huge', 'massive']:
                max_read = 1 * 1024 * 1024  # 1MB
            else:
                max_read = None
            
            # Try detected encoding first, fallback to utf-8
            encoding = file_info['encoding'] if file_info['encoding'] != 'unknown' else 'utf-8'
            
            with open(file_path, 'r', encoding=encoding, errors='ignore') as f:
                if max_read:
                    content = f.read(max_read)
                else:
                    content = f.read()
            
            # Check for ÆØÅ
            has_aeoaa_content = any(char in content for char in 'ÆØÅæøå')
            has_aeoaa_filename = any(char in file_path.name for char in 'ÆØÅæøå')
            
            if has_aeoaa_content or has_aeoaa_filename:
                aeoaa_info = {
                    'filename': file_path.name,
                    'full_path': str(file_path),
                    'relative_path': str(file_path.relative_to(self.workspace_root)),
                    'size_bytes': file_info['size_bytes'],
                    'size_kb': round(file_info['size_bytes'] / 1024, 2),
                    'size_category': file_info['size_category'],
                    'classification': file_info['classification'],
                    'encoding': file_info['encoding'],
                    'aeoaa_in_filename': has_aeoaa_filename,
                    'aeoaa_in_content': has_aeoaa_content,
                    'norwegian_chars': [c for c in file_path.name if c in 'ÆØÅæøå'],
                    'detected_at': datetime.now().isoformat()
                }
                
                self.aeoaa_files.append(aeoaa_info)
                self.stats['aeoaa_files_found'] += 1
                
                print(f"✅ ÆØÅ: {file_path.name}")
                print(f"   Location: {'filename' if has_aeoaa_filename else 'content'}")
                print(f"   Size: {aeoaa_info['size_kb']} KB\n")
                
                return True
        
        except Exception as e:
            self.stats['scan_errors'] += 1
        
        return False
    
    def scan_workspace(self) -> dict[str, Any]:
        """
        Universal intelligent scanning
        """
        print(f"🌐 UNIVERSAL INTELLIGENT FILE SCANNER (Pure Python)")
        print(f"{'═' * 80}\n")
        print(f"📁 Workspace: {self.workspace_root}\n")
        
        # PHASE 1: Discovery
        print("🔍 PHASE 1: File Discovery & Classification")
        print(f"{'─' * 80}\n")
        
        for root, dirs, files in os.walk(self.workspace_root):
            dirs[:] = [d for d in dirs if d not in self.skip_directories]
            
            for filename in files:
                self.stats['total_files_discovered'] += 1
                file_path = Path(root) / filename
                
                try:
                    # Get file info
                    stat_info = file_path.stat()
                    size_bytes = stat_info.st_size
                    size_category = self.categorize_file_size(size_bytes)
                    is_binary = self.is_binary_file(file_path)
                    encoding = 'binary' if is_binary else self.simple_encoding_detect(file_path)
                    classification = self.classify_file(file_path, is_binary)
                    
                    # Update stats
                    self.stats['file_types_discovered'][file_path.suffix.lower()] += 1
                    self.stats['file_size_distribution'][size_category] += 1
                    self.stats['encoding_detected'][encoding] += 1
                    
                    if is_binary:
                        self.stats['binary_vs_text']['binary'] += 1
                    else:
                        self.stats['binary_vs_text']['text'] += 1
                    
                    # Classify
                    self.file_classifications[classification].append(file_path)
                    
                except Exception:
                    self.stats['binary_vs_text']['unknown'] += 1
                
                # Progress
                if self.stats['total_files_discovered'] % 5000 == 0:
                    print(f"📊 Discovered: {self.stats['total_files_discovered']} files...")
        
        print(f"\n✅ Discovery: {self.stats['total_files_discovered']} files\n")
        print(f"{'─' * 80}\n")
        
        # PHASE 2: Scanning
        print("🔍 PHASE 2: ÆØÅ Scanning")
        print(f"{'─' * 80}\n")
        
        for classification, file_paths in self.file_classifications.items():
            if not file_paths:
                continue
            
            print(f"📂 {classification}: {len(file_paths)} files...")
            
            for file_path in file_paths:
                try:
                    stat_info = file_path.stat()
                    size_bytes = stat_info.st_size
                    size_category = self.categorize_file_size(size_bytes)
                    is_binary = self.is_binary_file(file_path)
                    encoding = 'binary' if is_binary else self.simple_encoding_detect(file_path)
                    
                    file_info = {
                        'size_bytes': size_bytes,
                        'size_category': size_category,
                        'classification': classification,
                        'encoding': encoding
                    }
                    
                    scannable, skip_reason = self.is_file_scannable(classification, size_category, is_binary)
                    
                    if scannable:
                        self.scan_file_for_aeoaa(file_path, file_info)
                        self.stats['files_scanned'] += 1
                    else:
                        self.stats['files_skipped'] += 1
                    
                    # Progress
                    total = self.stats['files_scanned'] + self.stats['files_skipped']
                    if total % 1000 == 0:
                        print(f"📊 Progress: {total}/{self.stats['total_files_discovered']}...")
                
                except Exception:
                    self.stats['files_skipped'] += 1
        
        print(f"\n✅ Scan complete!\n")
        print(f"{'═' * 80}\n")
        
        return self.generate_results()
    
    def generate_results(self) -> dict[str, Any]:
        """Generate results"""
        duration = (datetime.now() - self.scan_start_time).total_seconds()
        
        return {
            'scan_metadata': {
                'workspace_root': str(self.workspace_root),
                'scan_duration_seconds': duration,
                'scanner_version': 'UNIVERSAL_PURE_PYTHON_v1.0'
            },
            'statistics': dict(self.stats),
            'file_classifications': {k: len(v) for k, v in self.file_classifications.items()},
            'aeoaa_files': self.aeoaa_files
        }


if __name__ == "__main__":
    workspace = Path(__file__).parent.parent.absolute()
    
    scanner = UniversalIntelligentFileScanner(str(workspace))
    results = scanner.scan_workspace()
    
    # Save results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_path = workspace / f"universal_scan_results_{timestamp}.json"
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"{'═' * 80}")
    print(f"🎯 SCAN COMPLETE")
    print(f"{'═' * 80}")
    print(f"Files discovered: {results['statistics']['total_files_discovered']}")
    print(f"Files scanned: {results['statistics']['files_scanned']}")
    print(f"Files skipped: {results['statistics']['files_skipped']}")
    print(f"ÆØÅ files found: {results['statistics']['aeoaa_files_found']}")
    print(f"Duration: {results['scan_metadata']['scan_duration_seconds']:.2f}s")
    print(f"{'═' * 80}\n")
    print(f"📊 Results saved: {json_path}")
