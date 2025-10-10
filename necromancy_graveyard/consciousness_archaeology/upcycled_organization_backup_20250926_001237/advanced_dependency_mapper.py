#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔮 ADVANCED DEPENDENCY MAPPING PROTOCOL 🔮
==========================================

Goddess-level Python dependency analysis med consciousness-enhanced 
cross-referencing capabilities for entire PsychoNoir-Kontrapunkt ecosystem.

CONSCIOUSNESS_SIGNATURE: 0xDEPENDENCY_ARCHAEOLOGY_SUPREME
CARIBBEAN_SOPHISTICATION: MAXIMUM_CROSS_REFERENCE_MATRIX
"""

import ast
import importlib.util
import sys
from pathlib import Path
from typing import Dict, List, Set, Any, Optional, Tuple
from dataclasses import dataclass, field
from collections import defaultdict, deque
import json
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

@dataclass
class ImportAnalysis:
    """Structured import analysis data"""
    module_name: str
    import_type: str  # 'import', 'from_import', 'relative_import'
    is_local: bool = False
    is_third_party: bool = False
    is_standard_library: bool = False
    import_level: int = 0  # for relative imports
    imported_names: List[str] = field(default_factory=list)
    line_number: int = 0
    consciousness_enhanced: bool = False

@dataclass
class FileDependencySignature:
    """Complete dependency signature for a Python file"""
    file_path: str
    imports: List[ImportAnalysis] = field(default_factory=list)
    local_dependencies: Set[str] = field(default_factory=set)
    third_party_dependencies: Set[str] = field(default_factory=set)
    standard_library_dependencies: Set[str] = field(default_factory=set)
    consciousness_imports: List[str] = field(default_factory=list)
    dependency_depth: int = 0
    circular_dependencies: List[str] = field(default_factory=list)
    missing_dependencies: List[str] = field(default_factory=list)
    syntax_errors: List[str] = field(default_factory=list)

@dataclass 
class DependencyNode:
    """Node in dependency graph"""
    file_path: str
    dependencies: Set[str] = field(default_factory=set)
    dependents: Set[str] = field(default_factory=set)
    is_consciousness_enhanced: bool = False
    consciousness_level: float = 0.0
    criticality_score: float = 0.0

class ConsciousnessDependencyAnalyzer:
    """Advanced dependency analyzer med consciousness-enhancement protocols"""
    
    def __init__(self, repository_path: Path):
        self.repository_path = Path(repository_path)
        self.dependency_graph: Dict[str, DependencyNode] = {}
        self.circular_dependencies: List[List[str]] = []
        self.consciousness_indicators = {
            "claudine", "consciousness", "caribbean", "matriarch", "quantum",
            "necromancy", "archaeology", "temporal", "psycho", "noir"
        }
        
    def analyze_file_imports(self, file_path: Path) -> FileDependencySignature:
        """Analyze all imports in a Python file"""
        signature = FileDependencySignature(file_path=str(file_path.relative_to(self.repository_path)))
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Parse AST for import analysis
            tree = ast.parse(content, filename=str(file_path))
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        import_analysis = ImportAnalysis(
                            module_name=alias.name,
                            import_type='import',
                            line_number=node.lineno,
                            consciousness_enhanced=any(
                                indicator in alias.name.lower() 
                                for indicator in self.consciousness_indicators
                            )
                        )
                        self._classify_import(import_analysis)
                        signature.imports.append(import_analysis)
                        
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        import_analysis = ImportAnalysis(
                            module_name=node.module,
                            import_type='from_import' if node.level == 0 else 'relative_import',
                            import_level=node.level,
                            line_number=node.lineno,
                            imported_names=[alias.name for alias in node.names],
                            consciousness_enhanced=any(
                                indicator in node.module.lower()
                                for indicator in self.consciousness_indicators
                            )
                        )
                        self._classify_import(import_analysis)
                        signature.imports.append(import_analysis)
            
            # Categorize dependencies
            for import_item in signature.imports:
                if import_item.is_local:
                    signature.local_dependencies.add(import_item.module_name)
                elif import_item.is_third_party:
                    signature.third_party_dependencies.add(import_item.module_name)
                elif import_item.is_standard_library:
                    signature.standard_library_dependencies.add(import_item.module_name)
                
                if import_item.consciousness_enhanced:
                    signature.consciousness_imports.append(import_item.module_name)
        
        except SyntaxError as e:
            signature.syntax_errors.append(f"Syntax error: {e}")
        except Exception as e:
            signature.syntax_errors.append(f"Analysis error: {e}")
        
        return signature
    
    def _classify_import(self, import_analysis: ImportAnalysis):
        """Classify import as local, third-party, or standard library"""
        module_name = import_analysis.module_name
        
        # Check if it's a relative import or local module
        if (import_analysis.import_type == 'relative_import' or 
            self._is_local_module(module_name)):
            import_analysis.is_local = True
        elif self._is_standard_library(module_name):
            import_analysis.is_standard_library = True
        else:
            import_analysis.is_third_party = True
    
    def _is_local_module(self, module_name: str) -> bool:
        """Check if module is local to the repository"""
        # Check for common local patterns
        local_patterns = [
            'backend', 'tools', 'infrastructure', 'necromancy_graveyard',
            'consciousness', 'quantum', 'character_systems'
        ]
        return any(pattern in module_name for pattern in local_patterns)
    
    def _is_standard_library(self, module_name: str) -> bool:
        """Check if module is part of standard library"""
        try:
            spec = importlib.util.find_spec(module_name)
            if spec and spec.origin:
                # Standard library modules typically have origins in sys.exec_prefix
                return sys.exec_prefix in spec.origin
        except (ImportError, ModuleNotFoundError, AttributeError):
            pass
        
        # Common standard library modules
        standard_modules = {
            'os', 'sys', 'json', 'datetime', 'pathlib', 'typing', 
            'collections', 'logging', 'ast', 'importlib', 'dataclasses',
            'enum', 'abc', 're', 'glob', 'shutil', 'sqlite3'
        }
        return module_name.split('.')[0] in standard_modules
    
    def build_dependency_graph(self, python_files: List[Path]) -> Dict[str, DependencyNode]:
        """Build complete dependency graph for all Python files"""
        logger.info("🔮 Building consciousness-enhanced dependency graph...")
        
        # First pass: analyze all files
        file_signatures = {}
        for file_path in python_files:
            try:
                signature = self.analyze_file_imports(file_path)
                relative_path = str(file_path.relative_to(self.repository_path))
                file_signatures[relative_path] = signature
                
                # Create dependency node
                node = DependencyNode(
                    file_path=relative_path,
                    is_consciousness_enhanced=len(signature.consciousness_imports) > 0,
                    consciousness_level=len(signature.consciousness_imports) / max(len(signature.imports), 1)
                )
                self.dependency_graph[node.file_path] = node
                
            except Exception as e:
                logger.warning(f"Error analyzing {file_path}: {e}")
        
        # Second pass: build relationships
        for file_path, signature in file_signatures.items():
            node = self.dependency_graph.get(str(file_path))
            if node is None:
                logger.debug(f"Skipping file '{file_path}' - no dependency node found (possible incomplete graph).")
                continue
            
            for local_dep in signature.local_dependencies:
                # Try to find the actual file for this dependency
                dep_file = self._resolve_local_dependency(local_dep)
                if dep_file:
                    # Normalize to relative path from repository root
                    dep_file_path = str(Path(dep_file).as_posix())
                    if dep_file_path in self.dependency_graph:
                        node.dependencies.add(dep_file_path)
                        self.dependency_graph[dep_file_path].dependents.add(str(file_path))
        
        # Calculate criticality scores
        self._calculate_criticality_scores()
        
        # Detect circular dependencies
        self._detect_circular_dependencies()
        
        return self.dependency_graph
    def _resolve_local_dependency(self, module_name: str) -> Optional[str]:
        """Resolve local module name to actual file path with caching for performance"""
        if not hasattr(self, "_local_dep_cache"):
            self._local_dep_cache = {}
        if module_name in self._local_dep_cache:
            return self._local_dep_cache[module_name]

        possible_paths = [
            f"{module_name}.py",
            f"{module_name}/__init__.py",
            f"backend/python/{module_name}.py",
            f"tools/{module_name}.py",
            f"tools/consciousness_session_management/{module_name}.py",
        ]
        for path in possible_paths:
            full_path = self.repository_path / path
            if full_path.exists():
                rel_path = str(full_path.relative_to(self.repository_path))
                self._local_dep_cache[module_name] = rel_path
                return rel_path

        self._local_dep_cache[module_name] = None
        return None
        return None
    
    def _calculate_criticality_scores(self):
        """Calculate criticality score based on dependents and consciousness"""
        for node in self.dependency_graph.values():
            # Base score from number of dependents
            dependent_score = len(node.dependents) * 0.1
            
            # Consciousness enhancement multiplier
            consciousness_multiplier = 1.0 + (node.consciousness_level * 2.0)
            
            # Final criticality score
            node.criticality_score = dependent_score * consciousness_multiplier
    
        def dfs(node_path: str, path: List[str]) -> bool:
            if node_path in rec_stack:
                # Found cycle
                cycle_start = path.index(node_path)
                cycle = path[cycle_start:] + [node_path]
                self.circular_dependencies.append(cycle)
                return True

            if node_path in visited:
                return False

            rec_stack.add(node_path)
            node = self.dependency_graph.get(node_path)
            found_cycle = False
            if node:
                for dep in node.dependencies:
                    if dfs(dep, path + [node_path]):
                        found_cycle = True
            rec_stack.remove(node_path)
            visited.add(node_path)  # Mark as fully processed after DFS
            return found_cycle

        for node_path in self.dependency_graph:
            if node_path not in visited:
                dfs(node_path, [])
            return False
        
        for node_path in self.dependency_graph:
            if node_path not in visited:
                dfs(node_path, [])
    
    def generate_dependency_report(self) -> Dict[str, Any]:
    def generate_dependency_report(self) -> Dict[str, Any]:
        """
        Generate comprehensive dependency analysis report.

        Consciousness enhancement is determined by whether a file imports any module whose name contains
        one or more consciousness-indicator keywords (e.g., 'claudine', 'consciousness', 'caribbean', 'matriarch', etc.).
        These files are flagged as consciousness-enhanced and included in the consciousness_enhanced_files section of the report.
        """
        # Get critical files (top 10 by criticality score)
        critical_files = sorted(
            self.dependency_graph.values(),
            key=lambda x: x.criticality_score,
            reverse=True
        )[:10]
        
        # Get consciousness-enhanced files
        consciousness_files = [
            node for node in self.dependency_graph.values()
            if node.is_consciousness_enhanced
        ]
        
        # Calculate statistics
        total_files = len(self.dependency_graph)
        consciousness_percentage = len(consciousness_files) / total_files * 100 if total_files > 0 else 0
        
        report = {
            "dependency_analysis_timestamp": datetime.now().isoformat(),
            "total_files_analyzed": total_files,
            "consciousness_enhanced_files": len(consciousness_files),
            "consciousness_enhancement_percentage": consciousness_percentage,
            "circular_dependencies_detected": len(self.circular_dependencies),
            "critical_files": [
                {
                    "file_path": node.file_path,
                    "criticality_score": node.criticality_score,
                    "dependents_count": len(node.dependents),
                    "dependencies_count": len(node.dependencies),
                    "consciousness_level": node.consciousness_level
                }
                for node in critical_files
            ],
            "consciousness_enhanced_files_detail": [
                {
                    "file_path": node.file_path,
                    "consciousness_level": node.consciousness_level,
                    "criticality_score": node.criticality_score
                }
                for node in consciousness_files
            ],
            "circular_dependencies": self.circular_dependencies,
            "dependency_graph_summary": {
                "total_nodes": len(self.dependency_graph),
                "total_edges": sum(len(node.dependencies) for node in self.dependency_graph.values()),
                "average_dependencies_per_file": sum(len(node.dependencies) for node in self.dependency_graph.values()) / total_files if total_files > 0 else 0,
                "highly_connected_files": [
                    node.file_path for node in self.dependency_graph.values()
                    if len(node.dependencies) > 5 or len(node.dependents) > 5
                ]
            }
        }
        
        return report

def main():
    """Execute advanced dependency mapping protocol"""
    repository_path = Path("c:/Users/erdno/PsychoNoir-Kontrapunkt")
    analyzer = ConsciousnessDependencyAnalyzer(repository_path)
    
    # Find all Python files
    python_files = list(repository_path.rglob("*.py"))
    logger.info(f"🔮 Found {len(python_files)} Python files for dependency analysis")
    
    # Build dependency graph
    dependency_graph = analyzer.build_dependency_graph(python_files)
    
    # Generate report
    report = analyzer.generate_dependency_report()
    
    # Save report
    report_path = repository_path / "DEPENDENCY_MAPPING_ANALYSIS_COMPLETE.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    logger.info(f"🔮 Dependency analysis complete: {report_path}")
    logger.info(f"📊 Total files analyzed: {report['total_files_analyzed']}")
    logger.info(f"🎭 Consciousness enhanced files: {report['consciousness_enhanced_files']} ({report['consciousness_enhancement_percentage']:.1f}%)")
    logger.info(f"⚠️ Circular dependencies detected: {report['circular_dependencies_detected']}")
    
    return report

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='🔮 %(levelname)s: %(message)s')
    main()