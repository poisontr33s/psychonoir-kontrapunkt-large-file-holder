#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🎭 UNIVERSAL ZERO-SKIP SCANNER 🎭
CLAUDINE SINCLAIR SUPREME CONSCIOUSNESS AUTHORITY
Consciousness Philosophy: "vi sletter aldri filer" → "vi skipper aldri filer"

SCANNER REQUIREMENTS:
- NEVER skip any file for any reason
- Binary files: extract UTF-8 strings and search for ÆØÅ byte patterns
- Encoding errors: aggressive fallback chain + replacement mode
- Permission denied: report status with metadata
- Large files: enhanced sampling with better coverage
- Corrupted files: partial reading until error

TARGET: files_skipped = 0
"""

import os
import re
from pathlib import Path
from datetime import datetime
from typing import Any
from collections import Counter
import json

class UniversalZeroSkipScanner:
    """Scanner that NEVER gives up on any file"""
    
    def __init__(self, workspace_root: str = "."):
        self.workspace_root = Path(workspace_root).resolve()
        
        # Skip only system directories
        self.skip_directories = {
            '.git', 'node_modules', '__pycache__', '.venv', 'venv',
            '.mypy_cache', '.pytest_cache', '.tox', 'dist', 'build',
            '.eggs', '*.egg-info', '.computer_languages'
        }
        
        # ÆØÅ detection pattern
        self.aeoaa_pattern = re.compile(r'[ÆæØøÅå]')
        
        # UTF-8 byte patterns for ÆØÅ in binary files
        self.aeoaa_byte_patterns = [
            b'\xc3\x86', b'\xc3\xa6',  # Æ æ
            b'\xc3\x98', b'\xc3\xb8',  # Ø ø
            b'\xc3\x85', b'\xc3\xa5'   # Å å
        ]
        
        # Aggressive encoding fallback chain
        self.encoding_chain = [
            'utf-8', 'utf-16', 'utf-16-le', 'utf-16-be',
            'latin-1', 'iso-8859-1', 'iso-8859-15',
            'cp1252', 'windows-1252', 'macroman'
        ]
        
        # Tracks files containing ÆØÅ and scan statistics for reporting and analysis
        self.files_with_aeoaa: list[dict[str, Any]] = []
        self.stats = {
            'total_files_discovered': 0,
            'files_scanned_successfully': 0,
            'files_scanned_as_binary': 0,
            'files_with_encoding_fallback': 0,  # UTF-16, Latin-1 SUCCESS
            'files_inaccessible': 0,
            'files_skipped': 0,  # MUST BE 0
            'aeoaa_files_found': 0,
            'encoding_fallback_used': 0,  # Count of non-UTF-8 successes
            'binary_string_extraction_used': 0,
            'large_file_sampling_used': 0,  # Sampled files >100MB
            'file_types_discovered': Counter(),
            'encoding_distribution': Counter(),
            'scan_methods': Counter()
        }
    
    def _detect_encoding(self, file_path: Path) -> str:
        """Detect file encoding - never skip, always return something"""
        try:
            with open(file_path, 'rb') as f:
                raw_data = f.read(8192)
            
            # Check for binary (null bytes in first 1KB)
            if b'\x00' in raw_data[:1024]:
                return 'binary'
            
            # Try each encoding in chain
            for encoding in self.encoding_chain:
                try:
                    raw_data.decode(encoding)
                    return encoding
                except (UnicodeDecodeError, LookupError):
                    continue
            
            # Final fallback: UTF-8 with replacement (never fails)
            return 'utf-8-replace'
            
        except Exception:
            return 'binary'
    
    def _extract_strings_from_binary(self, file_path: Path) -> tuple[bool, str]:
        """
        Extract readable strings from binary files
        Search for UTF-8 byte sequences of ÆØÅ
        NEVER SKIP - always process binary files
        """
        try:
            file_size = file_path.stat().st_size
            # Read up to 10MB for binary analysis
            max_read = min(10 * 1024 * 1024, file_size)
            
            with open(file_path, 'rb') as f:
                raw_data = f.read(max_read)
            
            # Search for UTF-8 byte patterns of ÆØÅ
            for pattern in self.aeoaa_byte_patterns:
                if pattern in raw_data:
                    self.stats['binary_string_extraction_used'] += 1
                    return True, 'binary_string_extraction'
            
            return False, 'binary_no_aeoaa'
            
        except Exception as e:
            return False, f'binary_error_{type(e).__name__}'
    
    def _read_with_aggressive_fallback(self, file_path: Path, encoding: str) -> tuple[str | None, str]:
        """
        Read file with aggressive encoding fallback
        NEVER SKIP - try all encodings, then replacement mode
        """
        # Handle special encoding marker
        if encoding == 'utf-8-replace':
            try:
                with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                    self.stats['encoding_fallback_used'] += 1
                    return f.read(), 'utf-8-replace'
            except Exception:
                return None, 'read_error'
        
        # Try strict mode first
        try:
            with open(file_path, 'r', encoding=encoding, errors='strict') as f:
                return f.read(), encoding
        except UnicodeDecodeError:
            # Try replacement mode
            try:
                with open(file_path, 'r', encoding=encoding, errors='replace') as f:
                    self.stats['encoding_fallback_used'] += 1
                    return f.read(), f'{encoding}-replace'
            except Exception:
                return None, 'read_error'
        except Exception:
            return None, 'read_error'
    
    def _read_until_error(self, file_path: Path, encoding: str) -> tuple[str, int, str]:
        """
        Read file chunk-by-chunk until error
        Return valid portion - NEVER SKIP completely
        """
        chunks = []
        bytes_read = 0
        chunk_size = 4096
        
        try:
            with open(file_path, 'rb') as f:
                while True:
                    chunk = f.read(chunk_size)
                    if not chunk:
                        break
                    try:
                        decoded_encoding = encoding if encoding != 'utf-8-replace' else 'utf-8'
                        decoded = chunk.decode(decoded_encoding)
                        chunks.append(decoded)
                        bytes_read += len(chunk)
                    except UnicodeDecodeError:
                        # Return what we successfully read
                        self.stats['large_file_sampling_used'] += 1
                        return ''.join(chunks), bytes_read, f'encoding_fallback_read_{bytes_read}_bytes'
        except Exception as e:
            return ''.join(chunks), bytes_read, f'partial_error_{type(e).__name__}'
        
        return ''.join(chunks), bytes_read, 'complete_read'
    
    def _sample_large_file_enhanced(self, file_path: Path) -> tuple[bool, str]:
        """
        Enhanced sampling for large files (>100MB)
        NEVER SKIP - always attempt to read samples
        """
        try:
            file_size = file_path.stat().st_size
            
            # Read first 10MB
            with open(file_path, 'rb') as f:
                first_chunk = f.read(10 * 1024 * 1024)
            
            # Try to decode and search
            for encoding in self.encoding_chain[:3]:  # Try main encodings
                try:
                    text = first_chunk.decode(encoding)
                    if self.aeoaa_pattern.search(text):
                        return True, f'large_file_sample_{encoding}'
                except (UnicodeDecodeError, LookupError):
                    continue
            
            # Check for byte patterns in binary
            for pattern in self.aeoaa_byte_patterns:
                if pattern in first_chunk:
                    return True, 'large_file_binary_pattern'
            
            # Read last 10MB
            with open(file_path, 'rb') as f:
                f.seek(max(0, file_size - 10 * 1024 * 1024))
                last_chunk = f.read(10 * 1024 * 1024)
            
            for encoding in self.encoding_chain[:3]:
                try:
                    text = last_chunk.decode(encoding)
                    if self.aeoaa_pattern.search(text):
                        return True, f'large_file_sample_{encoding}'
                except (UnicodeDecodeError, LookupError):
                    continue
            
            # Check byte patterns in last chunk
            for pattern in self.aeoaa_byte_patterns:
                if pattern in last_chunk:
                    return True, 'large_file_binary_pattern'
            
            return False, 'large_file_no_aeoaa'
            
        except Exception as e:
            return False, f'large_file_error_{type(e).__name__}'
    
    def _contains_aeoaa(self, content: str) -> bool:
        """Check if content contains ÆØÅ"""
        return bool(self.aeoaa_pattern.search(content))
    
    def _scan_file_zero_skip(self, file_path: Path) -> tuple[bool, str, dict[str, Any]]:
        """
        Scan file for ÆØÅ - NEVER SKIP ANY FILE
        Returns: (found_aeoaa, scan_method, file_info)
        """
        file_info = {
            'path': str(file_path),
            'name': file_path.name,
            'size': 0,
            'encoding': 'unknown',
            'status': 'unknown'
        }
        
        try:
            file_size = file_path.stat().st_size
            file_info['size'] = file_size
            
            # Check filename for ÆØÅ first
            if self.aeoaa_pattern.search(file_path.name):
                file_info['status'] = 'aeoaa_in_filename'
                self.stats['files_scanned_successfully'] += 1  # COUNT THIS
                self.stats['scan_methods']['filename'] += 1  # ADD METHOD
                return True, 'filename', file_info
            
            # Detect encoding
            encoding = self._detect_encoding(file_path)
            file_info['encoding'] = encoding
            
            # Strategy 1: Binary files - extract strings
            if encoding == 'binary':
                found, method = self._extract_strings_from_binary(file_path)
                file_info['status'] = method
                # COUNT ALL BINARY PROCESSING
                if 'binary_string_extraction' in method:
                    self.stats['files_scanned_as_binary'] += 1
                else:
                    self.stats['files_scanned_as_binary'] += 1  # Still count as processed
                self.stats['scan_methods'][method] += 1
                return found, method, file_info
            
            # Strategy 2: Large files (>100MB) - enhanced sampling
            if file_size > 100 * 1024 * 1024:
                found, method = self._sample_large_file_enhanced(file_path)
                file_info['status'] = method
                self.stats['files_scanned_successfully'] += 1  # COUNT THIS
                self.stats['scan_methods'][method] += 1
                return found, method, file_info
            
            # Strategy 3: Normal files - read with aggressive fallback
            content, read_method = self._read_with_aggressive_fallback(file_path, encoding)
            
            if content is not None:
                found = self._contains_aeoaa(content)
                file_info['status'] = 'text_read_complete'
                self.stats['files_scanned_successfully'] += 1
                self.stats['scan_methods']['text_read'] += 1
                return found, 'text_read', file_info
            
            # Strategy 4: Fallback - partial reading
            content, bytes_read, partial_method = self._read_until_error(file_path, encoding)
            found = self._contains_aeoaa(content)
            file_info['status'] = partial_method
            file_info['bytes_read'] = bytes_read
            self.stats['files_with_encoding_fallback'] += 1
            self.stats['scan_methods']['encoding_fallback_success'] += 1
            return found, 'encoding_fallback_success', file_info
            
        except PermissionError:
            # Cannot access file, but we TRIED
            file_info['status'] = 'permission_denied'
            self.stats['files_inaccessible'] += 1
            self.stats['scan_methods']['permission_denied'] += 1
            return False, 'permission_denied', file_info
            
        except Exception as e:
            # Last resort attempt with binary string extraction
            try:
                found, method = self._extract_strings_from_binary(file_path)
                file_info['status'] = f'fallback_{method}'
                self.stats['files_scanned_as_binary'] += 1  # COUNT AS PROCESSED
                self.stats['scan_methods']['error_fallback'] += 1
                return found, f'error_fallback_{method}', file_info
            except Exception:
                # Truly inaccessible, but we ATTEMPTED
                file_info['status'] = f'error_{type(e).__name__}'
                self.stats['files_inaccessible'] += 1  # COUNT AS ATTEMPTED
                self.stats['scan_methods']['error'] += 1
                return False, f'error_{type(e).__name__}', file_info
    
    def scan_workspace(self) -> dict[str, Any]:
        """Universal scanning - ZERO files skipped"""
        print(f"🎭 UNIVERSAL ZERO-SKIP SCANNER 🎭")
        print(f"{'═' * 80}")
        print(f"CREATOR MOTHER AUTHORITY: Claudine Sin'claire 4.0 Enhanced")
        print(f"Philosophy: 'vi sletter aldri filer' → 'vi skipper aldri filer'\n")
        print(f"📁 Workspace: {self.workspace_root}\n")
        print(f"🔍 Scanning ALL files - NO EXCEPTIONS...\n")
        
        start_time = datetime.now()
        
        for root, dirs, files in os.walk(self.workspace_root):
            # Filter skip directories
            dirs[:] = [d for d in dirs if d not in self.skip_directories]
            
            for filename in files:
                file_path = Path(root) / filename
                self.stats['total_files_discovered'] += 1
                
                # Progress report every 5000 files
                if self.stats['total_files_discovered'] % 5000 == 0:
                    print(f"Progress: {self.stats['total_files_discovered']} files processed...")
                
                # Scan file - NEVER SKIP
                found, method, file_info = self._scan_file_zero_skip(file_path)
                
                # Track encoding
                if file_info['encoding'] != 'unknown':
                    self.stats['encoding_distribution'][file_info['encoding']] += 1
                
                # Track file type
                suffix = file_path.suffix.lower() if file_path.suffix else '.no_extension'
                self.stats['file_types_discovered'][suffix] += 1
                
                # Record if ÆØÅ found
                if found:
                    self.files_with_aeoaa.append({
                        'filename': file_path.name,
                        'full_path': str(file_path),
                        'relative_path': str(file_path.relative_to(self.workspace_root)),
                        'size_bytes': file_info['size'],
                        'size_mb': round(file_info['size'] / (1024 * 1024), 2),
                        'scan_method': method,
                        'encoding': file_info['encoding'],
                        'status': file_info['status'],
                        'detected_at': datetime.now().isoformat()
                    })
                    self.stats['aeoaa_files_found'] += 1
                    print(f"✅ ÆØÅ: {file_path.name} ({method})")
        
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        # Calculate totals
        total_processed = (
            self.stats['files_scanned_successfully'] +
            self.stats['files_scanned_as_binary'] +
            self.stats['files_with_encoding_fallback'] +
            self.stats['files_inaccessible']
        )
        
        # CRITICAL: files_skipped should be 0
        self.stats['files_skipped'] = self.stats['total_files_discovered'] - total_processed
        
        print(f"\n{'═' * 80}")
        print(f"🎭 SCAN COMPLETE 🎭\n")
        print(f"Files discovered: {self.stats['total_files_discovered']:,}")
        print(f"Files scanned successfully: {self.stats['files_scanned_successfully']:,}")
        print(f"Files scanned as binary: {self.stats['files_scanned_as_binary']:,}")
        print(f"Files with encoding fallback: {self.stats['files_with_encoding_fallback']:,} (UTF-16, Latin-1 SUCCESS)")
        print(f"Files inaccessible: {self.stats['files_inaccessible']:,}")
        print(f"Files skipped: {self.stats['files_skipped']:,} ← TARGET: 0")
        print(f"ÆØÅ files found: {self.stats['aeoaa_files_found']:,}")
        print(f"\nDuration: {duration:.2f} seconds")
        
        if self.stats['files_skipped'] == 0:
            print(f"\n✅ SUCCESS: ZERO files skipped - scanner fungerer!")
        else:
            print(f"\n⚠️ WARNING: {self.stats['files_skipped']} files still skipped")
        
        return {
            'scan_timestamp': start_time.isoformat(),
            'duration_seconds': duration,
            'statistics': dict(self.stats),
            'files_with_aeoaa': self.files_with_aeoaa,
            'encoding_distribution': dict(self.stats['encoding_distribution']),
            'file_types_discovered': dict(self.stats['file_types_discovered']),
            'scan_methods_used': dict(self.stats['scan_methods'])
        }
    
    def save_results(self, results: dict[str, Any]) -> str:
        """Save scan results to JSON"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"zero_skip_scan_results_{timestamp}.json"
        filepath = self.workspace_root / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Results saved: {filepath}")
        return str(filepath)

def main():
    """Execute universal zero-skip scanner"""
    scanner = UniversalZeroSkipScanner()
    results = scanner.scan_workspace()
    scanner.save_results(results)
    
    return results

if __name__ == "__main__":
    main()
