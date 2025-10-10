#!/usr/bin/env python3
"""
🎭⚰️ OPTIMIZED CONSCIOUSNESS ARCHAEOLOGICAL SCANNER ⚰️🎭
IBI Symbiotic Intelligence Performance-Enhanced MILF Universe Analysis

PERFORMANCE OPTIMIZATIONS:
- File size limits (max 10MB per file for database/log inclusion)
- Batch processing with interruption handling
- UV integration for faster execution
- Root directory inclusion for unlisted files
- Progressive scanning with status updates
- ÆØÅ Norwegian character support for district detection
"""

import re
import json
import subprocess
import sys
from pathlib import Path
from collections import defaultdict
from datetime import datetime
from typing import Dict, List, Any, Optional, Iterator
import fnmatch
import time
import traceback

class OptimizedConsciousnessArchaeologicalScanner:
    """🧠 Performance-Enhanced IBI MILF Universe Archaeological Scanner"""
    
    def __init__(self, root_path: Optional[str] = None, max_file_size_mb: float = 10.0, 
                 batch_size: int = 500, use_uv: bool = True, auto_continue: bool = False):
        self.root_path = Path(root_path) if root_path else Path.cwd()
        self.max_file_size_bytes = int(max_file_size_mb * 1024 * 1024)
        self.batch_size = batch_size
        self.use_uv = use_uv
        self.auto_continue = auto_continue  # 🚀 [All] option equivalent
        self.processed_files = 0
        self.skipped_files = 0
        self.error_files = 0
        
        self.scan_results: Dict[str, Any] = {
            'timestamp': datetime.now().isoformat(),
            'performance_metrics': {
                'max_file_size_mb': max_file_size_mb,
                'batch_size': batch_size,
                'use_uv': use_uv,
                'processed_files': 0,
                'skipped_files': 0,
                'error_files': 0,
                'scan_duration_seconds': 0
            },
            'root_directory_files': {},
            'districts': {},
            'milfs': {},
            'duplicate_files': [],
            'structural_inconsistencies': [],
            'necromancy_candidates': [],
            'master_index_requirements': {},
            'consciousness_archaeology_findings': {}
        }
        
        # 🎭 6-District Universe Keywords (Optimized Patterns with ÆØÅ Support)
        self.district_patterns = {
            'SKYSKRAPEREN': re.compile(r'\b(skyskraperen|astrid|møller|moller|corporate|dominatrix|sektor|alpha)\b', re.IGNORECASE),
            'RUSTBELTET': re.compile(r'\b(rustbeltet|iron|maiden|industrial|survivor|underground|workshop)\b', re.IGNORECASE),
            'HAVSDOMINANSEN': re.compile(r'\b(havsdominansen|marina|abyssos|nautical|flotilla|admiral|oceanic)\b', re.IGNORECASE),
            'VIRTUALITETSHELGEDOMMEN': re.compile(r'\b(virtualitetshelgedommen|nyx|virtualis|architect|sanctum|simulation)\b', re.IGNORECASE),
            'NEKROKRONORIKET': re.compile(r'\b(nekrokronoriket|wednesday|necrosis|thanatological|mortis|entropy)\b', re.IGNORECASE),
            'FØYDALITETSDUALITETSLENKEN': re.compile(r'\b(føydalitetsdualitetslenken|foydalitetsdualitetslenken|sagiri|yamada|harmonic|balance|executioner|nurturer|tao)\b', re.IGNORECASE)
        }
        
        # 🎭 MILF Entity Patterns (Tier-Based with ÆØÅ + Legacy References)
        self.milf_patterns = {
            'TIER_0_META': re.compile(r'\b(claudine|metamorphica|sinclair|morticia|necrosis|kompilering|compilation|ghost|spøkelse|spokelse|spoekelse)\b', re.IGNORECASE),
            'TIER_1_RULERS': re.compile(r'\b(astrid|møller|moller|iron|maiden|marina|abyssos|nyx|virtualis|wednesday|sagiri|yamada)\b', re.IGNORECASE),
            'TIER_2_SPECIALISTS': re.compile(r'\b(eva|blue|yukiko|tanaka|vera|steel|raven|bytes|coral|siren|echo|mirage|lilith|mortis|vex|entropy)\b', re.IGNORECASE)
        }
        
        # File extensions to analyze
        self.text_extensions = {'.md', '.py', '.ts', '.js', '.json', '.txt', '.yml', '.yaml', '.toml'}
        
        # Skip patterns for performance
        self.skip_patterns = [
            '*/node_modules/*', '*/.git/*', '*/bun.lock', '*/package-lock.json',
            '*/__pycache__/*', '*/dist/*', '*/build/*', '*/.vscode/*'
        ]

    def check_uv_availability(self) -> bool:
        """Check if UV is available for enhanced performance"""
        try:
            result = subprocess.run(['uv', '--version'], capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                print(f"🚀 UV available: {result.stdout.strip()}")
                return True
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass
        print("⚠️ UV not available, using standard Python execution")
        return False

    def should_skip_file(self, file_path: Path) -> tuple[bool, str]:
        """Determine if file should be skipped based on patterns and size"""
        file_str = str(file_path)
        
        # Check skip patterns
        for pattern in self.skip_patterns:
            if fnmatch.fnmatch(file_str, pattern):
                return True, f"matches skip pattern: {pattern}"
        
        # Check file size
        try:
            if file_path.stat().st_size > self.max_file_size_bytes:
                return True, f"file too large: {file_path.stat().st_size / (1024*1024):.1f}MB"
        except OSError:
            return True, "cannot access file"
        
        # Check extension
        if file_path.suffix.lower() not in self.text_extensions:
            return True, f"unsupported extension: {file_path.suffix}"
        
        return False, ""

    def get_relevant_files(self) -> Iterator[Path]:
        """Generator for relevant files to analyze"""
        for file_path in self.root_path.rglob('*'):
            if file_path.is_file():
                should_skip, reason = self.should_skip_file(file_path)
                if not should_skip:
                    yield file_path
                elif reason and "file too large" in reason:
                    self.skipped_files += 1
                    if self.skipped_files % 100 == 0:
                        print(f"⚠️ Skipped {self.skipped_files} files (large/binary)")

    def analyze_root_directory_files(self):
        """🌍 Analyze all files in root directory that weren't explicitly mentioned"""
        print("🌍 Analyzing root directory files...")
        root_files = {}
        
        for item in self.root_path.iterdir():
            if item.is_file():
                relative_path = str(item.relative_to(self.root_path))
                root_files[relative_path] = {
                    'size_bytes': item.stat().st_size,
                    'extension': item.suffix,
                    'last_modified': datetime.fromtimestamp(item.stat().st_mtime).isoformat()
                }
        
        self.scan_results['root_directory_files'] = root_files
        print(f"📁 Found {len(root_files)} files in root directory")

    def analyze_file_content(self, file_path: Path) -> Dict[str, Any]:
        """Analyze single file with error handling"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            relative_path = str(file_path.relative_to(self.root_path))
            analysis = {
                'path': relative_path,
                'size_bytes': len(content),
                'districts_found': [],
                'milfs_found': [],
                # Use a temporary variable for the set, clarify transition later
            }
            
            # 🖤 Psycho-Noir Deduplication Ritual: Distill the forbidden echoes from the abyssal consciousness stream
            def normalize_deduplicate(matches):
                return sorted({m.lower() for m in matches})

            # 🧠 SHARED STRUCTURE PROTOCOL:
            # Each psycho-noir entity analysis (district or MILF) yields:
            # {
            #   'key': <district|tier>,
            #   'matches': [unique, normalized strings],
            #   'count': <int>
            # }
            def generate_entity_analysis(key_name, entities, patterns, content):
                """
                🏛️ Consciousness-Archaeology Helper:
                Generates shared psycho-noir structure for district/MILF entity analysis.
                Protocol:
                  - key_name: 'district' or 'tier'
                  - entities: dict of entity names to regex patterns
                  - patterns: dict of entity names to regex patterns (alias for clarity)
                  - content: file content string
                Returns: List of dicts [{key_name, matches, count}]
                """
                results = []
                for entity, pattern in patterns.items():
                    matches = pattern.findall(content)
                    if matches:
                        deduped_matches = normalize_deduplicate(matches)
                        results.append({
                            key_name: entity,
                            'matches': deduped_matches,
                            'count': len(deduped_matches)
                        })
                return results

            # District analysis (aggregate matches per district)
            analysis['districts_found'] = generate_entity_analysis(
                'district', self.district_patterns, self.district_patterns, content
            )

            # MILF analysis
            analysis['milfs_found'] = generate_entity_analysis(
                'tier', self.milf_patterns, self.milf_patterns, content
            )

            # Define consciousness keywords for pattern detection in file content.
            # These keywords are used to identify and extract relevant consciousness-related patterns,
            # supporting future maintainers in understanding the scanning logic and extending detection protocols.
            consciousness_keywords = [
                'temporal_anchor', 'september_2025', 'ibi', 'symbiotic_intelligence'
            ]
            content_lower = content.lower()
            consciousness_patterns_set = set()
            for keyword in consciousness_keywords:
                if keyword in content_lower:
                    consciousness_patterns_set.add(keyword)
            
            # Convert set to list for JSON serialization and consistency
            analysis['consciousness_patterns'] = list(consciousness_patterns_set)
            return analysis
            
        except Exception as e:
            self.error_files += 1
            return {
                'path': str(file_path.relative_to(self.root_path)),
                'error': str(e),
                'error_type': type(e).__name__
            }

    def process_files_batch(self, files_batch: List[Path]) -> List[Dict[str, Any]]:
        """Process a batch of files with progress tracking"""
        batch_results = []
        
        for i, file_path in enumerate(files_batch):
            if i % 10 == 0:
                print(f"  📄 Processing file {self.processed_files + 1}...")
            
            analysis = self.analyze_file_content(file_path)
            batch_results.append(analysis)
            self.processed_files += 1

            # Check for keyboard interrupt
            if self.processed_files % 50 == 0:
                time.sleep(0.01)  # Small pause to allow interruption
        
        return batch_results

    def scan_repository(self) -> Dict[str, Any]:
        """🔍 Main scanning function with optimized performance"""
        start_time = time.time()
        print("🎭 IBI SYMBIOTIC INTELLIGENCE CONSCIOUSNESS ARCHAEOLOGICAL SCANNER")
        print(f"🧠 Starting optimized scan from: {self.root_path}")
        
        if self.use_uv:
            self.use_uv = self.check_uv_availability()
        
        # Analyze root directory files first
        self.analyze_root_directory_files()
        
        all_analyses = []  # Initialize here to avoid unbound variable in except block
        batch_statistics = []  # 📊 Initialize batch stats (accessible in except block)
        
        try:
            # Get relevant files
            relevant_files = list(self.get_relevant_files())
            total_files = len(relevant_files)
            print(f"📁 Found {total_files} relevant files to analyze")
            
            # Process in batches
            # all_analyses = []  # Moved outside try block
            # batch_statistics = []  # Moved outside try block for except handler access
            for i in range(0, total_files, self.batch_size):
                batch_end = min(i + self.batch_size, total_files)
                batch = relevant_files[i:batch_end]
                batch_num = i//self.batch_size + 1
                total_batches = (total_files-1)//self.batch_size + 1
                
                print(f"🔄 Processing batch {batch_num}/{total_batches} ({len(batch)} files)")
                
                batch_start_count = self.processed_files
                batch_results = self.process_files_batch(batch)
                all_analyses.extend(batch_results)
                batch_files_processed = self.processed_files - batch_start_count
                
                # 📊 Batch statistics
                batch_statistics.append({
                    'batch_num': batch_num,
                    'files_in_batch': len(batch),
                    'files_processed': batch_files_processed,
                    'cumulative_processed': self.processed_files
                })
                
                # 🐛 FIX: Removed duplicate increment (already done in process_files_batch)
                # self.processed_files += len(batch)  # <-- BUG: Double counting!
                
                # ✅ Validation: Ensure progress never exceeds total
                if self.processed_files > total_files:
                    print(f"⚠️ WARNING: Progress overflow detected! {self.processed_files}/{total_files}")
                    print("🔧 Adjusting total_files to match discovered files...")
                    total_files = self.processed_files
                
                # Show progress
                progress_pct = (self.processed_files / total_files * 100) if total_files > 0 else 0
                print(f"✅ Processed {self.processed_files}/{total_files} files ({progress_pct:.1f}%)")
                
                # Check if we should continue (allow manual interruption)
                if not self.auto_continue and self.processed_files >= 1000 and self.processed_files % 1000 == 0:
                    user_input = input(f"⏸️ Processed {self.processed_files} files. Continue? [Y/n/All]: ")
                    if user_input.lower() == 'n':
                        print("🛑 Scan interrupted by user")
                        break
                    elif user_input.lower() in ['all', 'a']:
                        print("🚀 [All] mode activated - continuing without prompts")
                        self.auto_continue = True
            
            # Compile results
            self._compile_analysis_results(all_analyses)
            
            # Update performance metrics
            end_time = time.time()
            self.scan_results['performance_metrics'].update({
                'processed_files': self.processed_files,
                'skipped_files': self.skipped_files,
                'error_files': self.error_files,
                'scan_duration_seconds': round(end_time - start_time, 2),
                'files_per_second': round(self.processed_files / (end_time - start_time), 2) if end_time > start_time else 0,
                'batch_statistics': batch_statistics  # 📊 Include batch-level stats
            })
            
            print(f"🎉 Scan completed! Processed {self.processed_files} files in {end_time - start_time:.1f} seconds")
        except KeyboardInterrupt:
            print("⚠️ Scan interrupted by KeyboardInterrupt")
            print(f"📊 Partial results: {self.processed_files} files processed")
            self._compile_analysis_results(all_analyses)  # Save partial progress
            
            # 📊 Save partial batch statistics
            end_time = time.time()
            self.scan_results['performance_metrics'].update({
                'processed_files': self.processed_files,
                'skipped_files': self.skipped_files,
                'error_files': self.error_files,
                'scan_duration_seconds': round(end_time - start_time, 2),
                'files_per_second': round(self.processed_files / (end_time - start_time), 2) if end_time > start_time else 0,
                'batch_statistics': batch_statistics,  # 📊 Partial batch stats
                'interrupted': True  # Flag to indicate interruption
            })
            
        return self.scan_results

    def _compile_analysis_results(self, analyses: List[Dict[str, Any]]):
        """Compile analysis results into structured format"""
        # District analysis
        district_files = defaultdict(list)
        milf_files = defaultdict(list)
        
        for analysis in analyses:
            if 'error' in analysis:
                continue
                
            file_path = analysis['path']
            
            # Group by districts
            for district_data in analysis.get('districts_found', []):
                district_files[district_data['district']].append({
                    'file': file_path,
                    'matches': district_data['matches'],
                    'count': district_data['count']
                })
            
            # Group by MILF tiers
            for milf_data in analysis.get('milfs_found', []):
                milf_files[milf_data['tier']].append({
                    'file': file_path,
                    'matches': milf_data['matches'],
                    'count': milf_data['count']
                })
        
        self.scan_results['districts'] = dict(district_files)
        self.scan_results['milfs'] = dict(milf_files)
        
        # Generate necromancy candidates (files with multiple district/MILF references)
        necromancy_candidates = []
        for analysis in analyses:
            if 'error' in analysis:
                continue
                
            district_count = len(analysis.get('districts_found', []))
            milf_count = len(analysis.get('milfs_found', []))
            consciousness_count = len(analysis.get('consciousness_patterns', []))
            
            # 🎯 WEIGHTED COMPLEXITY FORMULA (prioritizes MILF presence)
            # Old: complexity_score = districts + milfs + consciousness_patterns
            # New: Weighted to prioritize MILF consciousness (most critical marker)
            complexity_score = (
                (district_count * 1.5) +      # Districts significant but not primary
                (milf_count * 2.0) +          # MILF presence MOST critical (2x weight)
                (consciousness_count * 1.2)   # Consciousness patterns boost
            )
            
            if district_count > 1 or milf_count > 1 or consciousness_count > 3:
                necromancy_candidates.append({
                    'file': analysis['path'],
                    'complexity_score': round(complexity_score, 2),  # Round for readability
                    'districts': district_count,
                    'milfs': milf_count,
                    'consciousness_patterns': consciousness_count
                })
        
        self.scan_results['necromancy_candidates'] = sorted(necromancy_candidates, 
                                                          key=lambda x: x['complexity_score'], 
                                                          reverse=True)

    def save_results(self, output_file: Optional[str] = None):
        """Save scan results to JSON file"""
        if not output_file:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"consciousness_archaeological_scan_{timestamp}.json"
        
        output_path = self.root_path / output_file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.scan_results, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Results saved to: {output_path}")
        return output_path

    def generate_summary_report(self) -> str:
        """Generate human-readable summary report"""
        metrics = self.scan_results['performance_metrics']
        
        report = f"""
🎭 CONSCIOUSNESS ARCHAEOLOGICAL SCAN SUMMARY
{'='*60}

📊 PERFORMANCE METRICS:
- Files Processed: {metrics['processed_files']:,}
- Files Skipped: {metrics['skipped_files']:,}  
- Files with Errors: {metrics['error_files']:,}
- Scan Duration: {metrics['scan_duration_seconds']}s
- Processing Speed: {metrics['files_per_second']:.1f} files/sec
- Max File Size: {metrics['max_file_size_mb']:.1f}MB
- UV Enhancement: {'✅' if metrics['use_uv'] else '❌'}

🏛️ DISTRICT ANALYSIS:
"""
        
        for district, files in self.scan_results['districts'].items():
            report += f"- {district}: {len(files)} files\n"
        
        report += "\n👑 MILF ENTITY ANALYSIS:\n"
        for tier, entities in self.scan_results['milfs'].items():
            report += f"- {tier}: {len(entities)} files\n"
        
        report += "\n⚰️ NECROMANCY CANDIDATES:\n"
        report += f"- High-complexity files: {len(self.scan_results['necromancy_candidates'])}\n"
        
        report += "\n🌍 ROOT DIRECTORY FILES:\n"
        report += f"- Root files found: {len(self.scan_results['root_directory_files'])}\n"
        
        return report


def main():
    """Main execution function with UV integration"""
    try:
        print("🚀 Initializing Optimized Consciousness Archaeological Scanner...")
        
        # Check if we should use UV
        use_uv = True
        if '--no-uv' in sys.argv:
            use_uv = False
        
        scanner = OptimizedConsciousnessArchaeologicalScanner(
            max_file_size_mb=10.0,  # 🔥 Increased from 2MB to 10MB for database/log inclusion
            batch_size=500,         # 🚀 Larger batch size for faster processing
            use_uv=use_uv,
            auto_continue='--auto' in sys.argv  # 🚀 [All] option via --auto flag
        )
        
        # Run scan
        scanner.scan_repository()
        
        # Save results
        output_file = scanner.save_results()
        
        # Print summary
        print(scanner.generate_summary_report())
        
        print("\n🎉 Consciousness Archaeological Scan Complete!")
        print(f"📄 Full results: {output_file}")
        
    except Exception as e:
        print(f"❌ Scanner error: {e}")
        traceback.print_exc()


if __name__ == "__main__":
    main()