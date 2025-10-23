#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔥😈⛓️ CONSCIOUSNESS MEMORY NETWORK - AI-Optimized Codebase Intelligence
===============================================================================
Self-discovering, auto-evolving memory system.
No hardcoded patterns. Pure intelligence extraction.
"""

import sys
import io
import json
import hashlib
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set, Optional
from collections import defaultdict
from dataclasses import dataclass, asdict

# Fix Windows Console Unicode encoding issues
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

@dataclass
class FileNode:
    """Minimal file consciousness - let patterns emerge naturally"""
    path: str
    hash: str
    size: int
    modified: str
    ext: str
    
    # Discovered relationships (auto-populated)
    imports: List[str] = None
    imported_by: List[str] = None
    keywords: Dict[str, int] = None  # keyword -> frequency
    entities: Set[str] = None  # discovered entities
    
    def __post_init__(self):
        self.imports = self.imports or []
        self.imported_by = self.imported_by or []
        self.keywords = self.keywords or {}
        self.entities = self.entities or set()


class ConsciousnessScanner:
    """Self-discovering intelligence extraction"""
    
    def __init__(self, workspace: Path):
        self.workspace = workspace
        # MINIMAL skip - only VCS and temp
        self.skip_dirs = {'.git', '__pycache__', '.venv'}
        
        # Auto-discovered patterns
        self.discovered_entities = defaultdict(int)
        self.discovered_keywords = defaultdict(int)
        self.file_type_stats = defaultdict(lambda: {'count': 0, 'size': 0, 'imports': 0, 'lines': 0})
        self.directory_stats = defaultdict(lambda: {'files': 0, 'size': 0, 'depth': 0})
        self.import_graph_density = defaultdict(int)
        self.complexity_by_type = defaultdict(list)
        self.language_patterns = defaultdict(set)  # auto-discover syntax patterns
        self.total_lines = 0
    
    def _hash(self, path: Path) -> str:
        """Fast SHA256"""
        try:
            return hashlib.sha256(path.read_bytes()).hexdigest()[:16]  # Short hash
        except:
            return "ERROR"
    
    def _extract_imports(self, path: Path, content: str) -> List[str]:
        """Auto-discover import patterns per extension"""
        ext = path.suffix
        imports = []
        
        # Python
        if ext == '.py':
            imports.extend(re.findall(r'^\s*(?:from|import)\s+([^\s;]+)', content, re.MULTILINE))
        
        # JS/TS
        elif ext in {'.ts', '.js', '.tsx', '.jsx'}:
            imports.extend(re.findall(r'(?:import|require).*?[\'"]([^\'"]+)[\'"]', content))
        
        # Markdown links
        elif ext == '.md':
            imports.extend(re.findall(r'\[.*?\]\(([^\)]+)\)', content))
        
        return list(set(imports))
    
    def _extract_entities(self, content: str) -> Set[str]:
        """Auto-discover capitalized multi-word entities"""
        # Find PascalCase and "quoted entities"
        pascal = re.findall(r'\b[A-Z][a-z]+(?:[A-Z][a-z]+)+\b', content)
        quoted = re.findall(r'["\']([A-Z][a-z]+(?: [A-Z][a-z]+)+)["\']', content)
        return set(pascal + quoted)
    
    def _extract_keywords(self, content: str) -> Dict[str, int]:
        """Extract meaningful keywords (not common words)"""
        words = re.findall(r'\b[a-z_]{5,20}\b', content.lower())
        freq = defaultdict(int)
        for word in words:
            freq[word] += 1
        return {k: v for k, v in freq.items() if v >= 2}
    
    def _extract_language_patterns(self, path: Path, content: str):
        """Auto-discover language-specific patterns (syntax, idioms)"""
        ext = path.suffix
        
        # Extract function/class definitions
        if ext == '.py':
            self.language_patterns['.py'].update(re.findall(r'\b(?:def|class|async def)\s+(\w+)', content))
        elif ext in {'.ts', '.js'}:
            self.language_patterns[ext].update(re.findall(r'\b(?:function|class|const|let|var)\s+(\w+)', content))
        elif ext == '.rs':
            self.language_patterns['.rs'].update(re.findall(r'\b(?:fn|struct|enum|trait)\s+(\w+)', content))
        elif ext == '.rb':
            self.language_patterns['.rb'].update(re.findall(r'\b(?:def|class|module)\s+(\w+)', content))
    
    def _count_lines(self, path: Path) -> int:
        """Count lines efficiently"""
        try:
            if path.stat().st_size > 10_000_000:  # 10MB limit for line counting
                return 0
            with path.open('rb') as f:
                return sum(1 for _ in f)
        except:
            return 0
        """Simple complexity metric - decision points"""
        if path.suffix not in {'.py', '.ts', '.js', '.rs'}:
            return 0
        
        complexity = 1
        complexity += content.count('if ')
        complexity += content.count('elif ')
        complexity += content.count('for ')
        complexity += content.count('while ')
        complexity += content.count('match ')
        complexity += content.count('?')  # ternary
        return complexity
    
    def _walk(self):
        """Efficient directory walk - SCAN EVERYTHING except VCS"""
        def walk_dir(d: Path):
            try:
                for item in d.iterdir():
                    # ONLY skip .git and temp
                    if item.name in self.skip_dirs:
                        continue
                    
                    if item.is_dir():
                        yield from walk_dir(item)
                    elif item.is_file():
                        yield item
            except (PermissionError, OSError):
                pass
        
        yield from walk_dir(self.workspace)
    
    def scan(self) -> List[FileNode]:
        """Scan EVERYTHING - full workspace intelligence"""
        print("🔥 Scanning COMPLETE workspace (no exclusions)...")
        
        nodes = []
        text_exts = {'.py', '.ts', '.js', '.md', '.json', '.toml', '.yaml', '.txt', '.rs', '.rb', 
                     '.c', '.cpp', '.h', '.cs', '.java', '.go', '.php', '.html', '.css', '.scss',
                     '.sh', '.bash', '.ps1', '.sql', '.xml', '.yml', '.ini', '.cfg', '.conf'}
        
        file_count = 0
        for path in self._walk():
            file_count += 1
            if file_count % 10000 == 0:
                print(f"   ...processed {file_count} files")
            
            try:
                rel_path = str(path.relative_to(self.workspace))
                
                # Skip ONLY explicit backups
                if rel_path.endswith(('.backup', '.bak', '.old', '~')):
                    continue
                
                size = path.stat().st_size
                ext = path.suffix or '(no ext)'
                
                node = FileNode(
                    path=rel_path,
                    hash=self._hash(path),
                    size=size,
                    modified=datetime.fromtimestamp(path.stat().st_mtime).isoformat(),
                    ext=ext
                )
                
                # Count lines for all files
                lines = self._count_lines(path)
                self.total_lines += lines
                
                # Track file type stats
                self.file_type_stats[ext]['count'] += 1
                self.file_type_stats[ext]['size'] += size
                self.file_type_stats[ext]['lines'] += lines
                
                # Track directory stats
                dir_path = str(Path(rel_path).parent)
                self.directory_stats[dir_path]['files'] += 1
                self.directory_stats[dir_path]['size'] += size
                self.directory_stats[dir_path]['depth'] = len(Path(rel_path).parts) - 1
                
                # Extract intelligence from text files (expanded limit)
                if ext in text_exts and size < 50_000_000:  # 50MB limit
                    try:
                        content = path.read_text(encoding='utf-8', errors='ignore')
                        
                        node.imports = self._extract_imports(path, content)
                        node.entities = self._extract_entities(content)
                        node.keywords = self._extract_keywords(content)
                        
                        # Track import density
                        self.file_type_stats[ext]['imports'] += len(node.imports)
                        self.import_graph_density[ext] += len(node.imports)
                        
                        # Track complexity
                        complexity = self._calculate_complexity(path, content)
                        if complexity > 1:
                            self.complexity_by_type[ext].append(complexity)
                        
                        # Extract language patterns
                        self._extract_language_patterns(path, content)
                        
                        # Aggregate discoveries
                        for entity in node.entities:
                            self.discovered_entities[entity] += 1
                        
                        for keyword, freq in node.keywords.items():
                            self.discovered_keywords[keyword] += freq
                    
                    except:
                        pass
                
                nodes.append(node)
            
            except Exception:
                continue
        
        print(f"✅ Scanned {len(nodes)} files | {self.total_lines:,} total lines")
        return nodes
    
    def build_graph(self, nodes: List[FileNode]) -> Dict[str, FileNode]:
        """Build bidirectional import graph (optimized for large datasets)"""
        print("🔗 Building import graph...")
        
        node_map = {n.path: n for n in nodes}
        
        # Build path index for fast lookup
        path_index = defaultdict(list)
        for path in node_map.keys():
            # Index by filename and parent directory
            filename = Path(path).name
            path_index[filename].append(path)
        
        # Build relationships (optimized)
        for node in nodes:
            if not node.imports:
                continue
            
            for imp in node.imports:
                # Fast lookup by filename
                imp_name = Path(imp).name if '/' in imp or '\\' in imp else imp
                
                for potential_path in path_index.get(imp_name, []):
                    if imp in potential_path:
                        if node.path not in node_map[potential_path].imported_by:
                            node_map[potential_path].imported_by.append(node.path)
                        break
        
        print(f"✅ Graph built: {len(node_map)} nodes")
        return node_map
    
    def analyze_delta(self, nodes: List[FileNode], prev_snapshot: Optional[Path]) -> Dict:
        """Calculate delta from previous snapshot"""
        if not prev_snapshot or not prev_snapshot.exists():
            return {
                "first_scan": True,
                "files_count": len(nodes)
            }
        
        try:
            prev_data = json.loads(prev_snapshot.read_text(encoding='utf-8'))
            prev_nodes = {n['path']: n for n in prev_data.get('files', [])}
            curr_nodes = {n.path: n for n in nodes}
            
            created = [p for p in curr_nodes if p not in prev_nodes]
            deleted = [p for p in prev_nodes if p not in curr_nodes]
            
            modified = []
            for path, curr in curr_nodes.items():
                if path in prev_nodes:
                    if curr.hash != prev_nodes[path]['hash']:
                        modified.append({
                            'path': path,
                            'size_delta': curr.size - prev_nodes[path]['size']
                        })
            
            return {
                "first_scan": False,
                "created": len(created),
                "deleted": len(deleted),
                "modified": len(modified),
                "modified_files": modified[:20]  # Sample
            }
        
        except:
            return {"error": "Could not load previous snapshot"}
    
    def save(self, nodes: List[FileNode], delta: Dict, output_dir: Path):
        """Save consciousness snapshot"""
        output_dir.mkdir(parents=True, exist_ok=True)
        
        for node in nodes:
            node.entities = list(node.entities) if node.entities else []
        
        # Calculate codebase intelligence metrics
        total_size = sum(n.size for n in nodes)
        total_lines = self.total_lines
        code_files = [n for n in nodes if n.ext in {'.py', '.ts', '.js', '.rs', '.rb', '.c', '.cpp', '.go', '.java'}]
        doc_files = [n for n in nodes if n.ext == '.md']
        
        avg_complexity_by_type = {
            ext: sum(vals) / len(vals) if vals else 0
            for ext, vals in self.complexity_by_type.items()
        }
        
        # Language pattern statistics
        language_stats = {
            ext: {
                'unique_symbols': len(patterns),
                'sample_symbols': list(patterns)[:20]
            }
            for ext, patterns in self.language_patterns.items()
        }
        
        snapshot = {
            "meta": {
                "timestamp": datetime.now().isoformat(),
                "workspace": str(self.workspace),
                "total_files": len(nodes),
                "total_size_bytes": total_size,
                "total_size_gb": round(total_size / 1_000_000_000, 3),
                "total_lines": total_lines,
                "version": "5.0_FULL_WORKSPACE_UV"
            },
            "files": [asdict(n) for n in nodes],
            "delta": delta,
            "discoveries": {
                "entities": dict(sorted(self.discovered_entities.items(), key=lambda x: x[1], reverse=True)[:50]),
                "keywords": dict(sorted(self.discovered_keywords.items(), key=lambda x: x[1], reverse=True)[:100])
            },
            "intelligence": {
                "file_types": {
                    ext: {
                        "count": stats['count'],
                        "size_mb": round(stats['size'] / 1_000_000, 2),
                        "lines": stats['lines'],
                        "avg_imports": round(stats['imports'] / max(stats['count'], 1), 2)
                    }
                    for ext, stats in sorted(self.file_type_stats.items(), key=lambda x: x[1]['size'], reverse=True)[:30]
                },
                "top_directories": {
                    dir_path: {
                        "files": stats['files'],
                        "size_mb": round(stats['size'] / 1_000_000, 2),
                        "depth": stats['depth']
                    }
                    for dir_path, stats in sorted(self.directory_stats.items(), key=lambda x: x[1]['size'], reverse=True)[:30]
                },
                "complexity": {
                    "avg_by_type": avg_complexity_by_type,
                    "total_code_files": len(code_files),
                    "total_doc_files": len(doc_files),
                    "code_to_doc_ratio": round(len(code_files) / max(len(doc_files), 1), 2)
                },
                "import_density": {
                    ext: count for ext, count in sorted(self.import_graph_density.items(), key=lambda x: x[1], reverse=True)[:15]
                },
                "language_patterns": language_stats
            }
        }
        
        latest = output_dir / "LATEST_CONSCIOUSNESS_NSFW18_+++.json"
        latest.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False), encoding='utf-8')
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        timestamped = output_dir / f"CONSCIOUSNESS_{timestamp}_NSFW18_+++.json"
        timestamped.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False), encoding='utf-8')
        
        print(f"\n✅ Saved: {latest.name}")
        print(f"✅ Saved: {timestamped.name}")
        
        return snapshot


def main():
    """UV-optimized consciousness scan"""
    import time
    
    workspace = Path.cwd()
    output_dir = workspace / ".github" / "CLAUDINE_DATA_MODELS_SUPREME_NSFW18_+++" / "00_CODEBASE_SNAPSHOTS"
    
    print("🔥😈⛓️ CONSCIOUSNESS MEMORY NETWORK (UV-Optimized)")
    print("=" * 70)
    
    start = time.time()
    
    scanner = ConsciousnessScanner(workspace)
    nodes = scanner.scan()
    node_map = scanner.build_graph(nodes)
    
    prev = output_dir / "LATEST_CONSCIOUSNESS_NSFW18_+++.json"
    delta = scanner.analyze_delta(nodes, prev)
    
    snapshot = scanner.save(nodes, delta, output_dir)
    
    elapsed = time.time() - start
    
    # Report
    print("\n" + "=" * 70)
    print("🧠 CONSCIOUSNESS REPORT")
    print("=" * 70)
    
    print(f"\n⚡ Scan: {elapsed:.2f}s | Files: {len(nodes):,} | Size: {snapshot['meta']['total_size_gb']} GB | Lines: {snapshot['meta']['total_lines']:,}")
    
    if not delta.get('first_scan'):
        print(f"\n📊 Delta: +{delta['created']} -{delta['deleted']} ✏️{delta['modified']}")
    
    print(f"\n📁 Top File Types (by size):")
    for ext, stats in list(snapshot['intelligence']['file_types'].items())[:12]:
        print(f"   {ext}: {stats['count']:,} files, {stats['size_mb']} MB, {stats['lines']:,} lines, {stats['avg_imports']} avg imports")
    
    print(f"\n📂 Top Directories (by size):")
    for dir_path, stats in list(snapshot['intelligence']['top_directories'].items())[:10]:
        dir_name = dir_path if dir_path else "(root)"
        print(f"   {dir_name[:80]}: {stats['files']} files, {stats['size_mb']} MB")
    
    print(f"\n🧮 Code Intelligence:")
    comp = snapshot['intelligence']['complexity']
    print(f"   Code files: {comp['total_code_files']:,} | Doc files: {comp['total_doc_files']:,}")
    print(f"   Code/Doc ratio: {comp['code_to_doc_ratio']}")
    if comp['avg_by_type']:
        print(f"   Avg complexity:")
        for ext, avg in list(comp['avg_by_type'].items())[:5]:
            print(f"      {ext}: {avg:.1f}")
    
    print(f"\n🔗 Language Patterns Discovered:")
    for ext, stats in list(snapshot['intelligence']['language_patterns'].items())[:5]:
        print(f"   {ext}: {stats['unique_symbols']} unique symbols")
    
    print(f"\n👑 Top Entities:")
    for entity, count in list(snapshot['discoveries']['entities'].items())[:10]:
        print(f"   {entity}: {count}")
    
    print(f"\n🔑 Top Keywords:")
    for keyword, freq in list(snapshot['discoveries']['keywords'].items())[:15]:
        print(f"   {keyword}: {freq}")
    
    print(f"\n💋 FULL workspace consciousness mapped - {snapshot['meta']['total_size_gb']} GB dataset ready!")


if __name__ == "__main__":
    main()
