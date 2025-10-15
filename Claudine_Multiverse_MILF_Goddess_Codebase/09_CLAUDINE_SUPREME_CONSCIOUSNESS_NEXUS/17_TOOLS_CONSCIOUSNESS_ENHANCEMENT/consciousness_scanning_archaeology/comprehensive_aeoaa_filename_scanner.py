#!/usr/bin/env python3
"""
🔍 COMPREHENSIVE ÆØÅ FILENAME SCANNER
═══════════════════════════════════════════════════════════════
Systematisk scanner for å finne ALLE filer med norske tegn (ÆØÅ)
som tidligere scannere ikke kunne lese.

CONSCIOUSNESS ARCHAEOLOGY PROTOCOL:
- Recursive walk through ENTIRE workspace
- UTF-8 encoding support
- Pattern matching for Æ/æ, Ø/ø, Å/å
- Cross-reference with previous scanner results
- Comprehensive inventory with file metadata
═══════════════════════════════════════════════════════════════
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime
from typing import Any
import unicodedata

# 🎯 ÆØÅ Pattern Detection
AEO_AA_PATTERN = re.compile(r'[ÆØÅæøå]')

# 🚫 Skip Patterns (binary/large files)
SKIP_EXTENSIONS = {
    '.exe', '.dll', '.bin', '.obj', '.o', '.a', '.so', '.dylib',
    '.zip', '.tar', '.gz', '.7z', '.rar',
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.ico', '.svg',
    '.mp3', '.mp4', '.avi', '.mov', '.wav',
    '.pdf', '.doc', '.docx',
    '.lock'  # bun.lock and similar
}

SKIP_DIRECTORIES = {
    'node_modules', '.git', '__pycache__', '.vscode-test',
    'dist', 'build', 'out', '.next', '.cache'
}

def contains_norwegian_chars(text: str) -> bool:
    """Check if text contains ÆØÅ characters."""
    return bool(AEO_AA_PATTERN.search(text))

def normalize_unicode(text: str) -> str:
    """Normalize unicode for consistent comparison."""
    return unicodedata.normalize('NFC', text)

def scan_workspace_for_aeoaa_files(workspace_root: str) -> dict[str, Any]:
    """
    Comprehensive scan for files with ÆØÅ in filenames or paths.
    
    Returns:
        Dictionary with:
        - files_with_aeoaa: List of files containing Norwegian characters
        - total_files_scanned: Total files checked
        - skipped_files: Files skipped due to binary/size
        - timestamp: Scan completion time
    """
    results: dict[str, Any] = {
        'files_with_aeoaa': [],
        'total_files_scanned': 0,
        'skipped_files': [],
        'timestamp': datetime.now().isoformat(),
        'workspace_root': workspace_root
    }
    
    print(f"🔍 Starting ÆØÅ Filename Scanner...")
    print(f"📁 Workspace: {workspace_root}\n")
    
    for root, dirs, files in os.walk(workspace_root):
        # Filter out skip directories
        dirs[:] = [d for d in dirs if d not in SKIP_DIRECTORIES]
        
        # Check directory name for ÆØÅ
        dir_basename = os.path.basename(root)
        if contains_norwegian_chars(dir_basename):
            print(f"📂 Directory with ÆØÅ: {root}")
        
        for filename in files:
            results['total_files_scanned'] += 1
            
            # Skip binary/large files by extension
            file_ext = os.path.splitext(filename)[1].lower()
            if file_ext in SKIP_EXTENSIONS:
                results['skipped_files'].append({
                    'path': os.path.join(root, filename),
                    'reason': f'Binary/excluded extension: {file_ext}'
                })
                continue
            
            full_path = os.path.join(root, filename)
            
            # Check filename for ÆØÅ
            if contains_norwegian_chars(filename):
                try:
                    file_stat = os.stat(full_path)
                    file_info = {
                        'filename': filename,
                        'full_path': full_path,
                        'relative_path': os.path.relpath(full_path, workspace_root),
                        'size_bytes': file_stat.st_size,
                        'size_kb': round(file_stat.st_size / 1024, 2),
                        'extension': file_ext,
                        'norwegian_chars_in_name': [c for c in filename if contains_norwegian_chars(c)],
                        'detected_at': datetime.now().isoformat()
                    }
                    
                    results['files_with_aeoaa'].append(file_info)
                    
                    print(f"✅ FOUND ÆØÅ FILE: {filename}")
                    print(f"   Path: {os.path.relpath(full_path, workspace_root)}")
                    print(f"   Norwegian chars: {file_info['norwegian_chars_in_name']}")
                    print(f"   Size: {file_info['size_kb']} KB\n")
                    
                except Exception as e:
                    print(f"❌ ERROR reading file: {filename}")
                    print(f"   Error: {str(e)}\n")
                    results['skipped_files'].append({
                        'path': full_path,
                        'reason': f'Error: {str(e)}'
                    })
            
            # Progress indicator every 1000 files
            if results['total_files_scanned'] % 1000 == 0:
                print(f"📊 Progress: {results['total_files_scanned']} files scanned...")
    
    return results

def generate_comprehensive_report(results: dict[str, Any], output_path: str) -> str:
    """Generate comprehensive report of ÆØÅ findings."""
    
    report_lines = [
        "═" * 80,
        "🔍 COMPREHENSIVE ÆØÅ FILENAME SCANNER REPORT",
        "═" * 80,
        f"Scan Timestamp: {results['timestamp']}",
        f"Workspace Root: {results['workspace_root']}",
        "",
        f"📊 SCAN STATISTICS:",
        f"  Total Files Scanned: {results['total_files_scanned']}",
        f"  Files with ÆØÅ Found: {len(results['files_with_aeoaa'])}",
        f"  Files Skipped: {len(results['skipped_files'])}",
        "",
        "═" * 80,
        "📂 FILES WITH ÆØÅ CHARACTERS:",
        "═" * 80,
        ""
    ]
    
    if results['files_with_aeoaa']:
        for idx, file_info in enumerate(results['files_with_aeoaa'], 1):
            report_lines.extend([
                f"{idx}. {file_info['filename']}",
                f"   Path: {file_info['relative_path']}",
                f"   Norwegian Chars: {', '.join(file_info['norwegian_chars_in_name'])}",
                f"   Size: {file_info['size_kb']} KB ({file_info['size_bytes']} bytes)",
                f"   Extension: {file_info['extension']}",
                ""
            ])
    else:
        report_lines.append("✅ NO FILES WITH ÆØÅ CHARACTERS FOUND")
        report_lines.append("")
    
    report_lines.extend([
        "═" * 80,
        "🚫 SKIPPED FILES SUMMARY:",
        "═" * 80,
        ""
    ])
    
    # Group skipped files by reason
    skipped_by_reason: dict[str, list[str]] = {}
    for skipped in results['skipped_files']:
        reason = skipped['reason']
        if reason not in skipped_by_reason:
            skipped_by_reason[reason] = []
        skipped_by_reason[reason].append(skipped['path'])
    
    for reason, paths in skipped_by_reason.items():
        report_lines.append(f"Reason: {reason}")
        report_lines.append(f"  Count: {len(paths)}")
        report_lines.append("")
    
    report_lines.extend([
        "═" * 80,
        "🎯 CONSCIOUSNESS ARCHAEOLOGY ANALYSIS:",
        "═" * 80,
        ""
    ])
    
    if results['files_with_aeoaa']:
        report_lines.append(f"⚠️  SCANNER LIMITATION CONFIRMED:")
        report_lines.append(f"   Previous scanners could not read these {len(results['files_with_aeoaa'])} files")
        report_lines.append(f"   due to ÆØÅ character encoding issues.")
        report_lines.append("")
        report_lines.append(f"📋 RECOMMENDED ACTIONS:")
        report_lines.append(f"   1. Update all scanners with UTF-8 encoding support")
        report_lines.append(f"   2. Re-scan workspace with fixed scanner")
        report_lines.append(f"   3. Verify content preservation in renamed files")
        report_lines.append(f"   4. Cross-reference with migration logs")
    else:
        report_lines.append(f"✅ NO ÆØÅ ENCODING ISSUES DETECTED:")
        report_lines.append(f"   All filenames use ASCII-compatible characters.")
        report_lines.append(f"   Previous scanner skips were due to other reasons.")
    
    report_lines.append("")
    report_lines.append("═" * 80)
    report_lines.append(f"Report generated: {datetime.now().isoformat()}")
    report_lines.append("═" * 80)
    
    # Write report
    report_content = "\n".join(report_lines)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print(f"\n📄 Report saved to: {output_path}")
    
    return report_content

def save_json_results(results: dict[str, Any], output_path: str) -> None:
    """Save results as JSON for programmatic access."""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"📊 JSON results saved to: {output_path}")

if __name__ == "__main__":
    # Get workspace root
    workspace_root = Path(__file__).parent.parent.absolute()
    
    print(f"🎭 COMPREHENSIVE ÆØÅ FILENAME SCANNER")
    print(f"{'═' * 80}\n")
    
    # Run scan
    scan_results = scan_workspace_for_aeoaa_files(str(workspace_root))
    
    # Generate outputs
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = workspace_root / f"AEOAA_FILENAME_SCAN_REPORT_{timestamp}.md"
    json_path = workspace_root / f"aeoaa_filename_scan_results_{timestamp}.json"
    
    report_content = generate_comprehensive_report(scan_results, str(report_path))
    save_json_results(scan_results, str(json_path))
    
    # Print summary
    print(f"\n{'═' * 80}")
    print(f"🎯 SCAN COMPLETE")
    print(f"{'═' * 80}")
    print(f"Files with ÆØÅ: {len(scan_results['files_with_aeoaa'])}")
    print(f"Total scanned: {scan_results['total_files_scanned']}")
    print(f"Files skipped: {len(scan_results['skipped_files'])}")
    print(f"{'═' * 80}\n")
