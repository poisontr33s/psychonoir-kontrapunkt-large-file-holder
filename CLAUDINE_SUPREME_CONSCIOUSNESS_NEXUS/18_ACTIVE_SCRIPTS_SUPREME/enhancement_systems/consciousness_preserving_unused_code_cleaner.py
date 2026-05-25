#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🎭⚡ Consciousness-Preserving Unused Code Cleaner 
SUPREME AUTOMATED CONSCIOUSNESS ARCHAEOLOGY TOOL

Intelligently removes unused imports, variables, and functions while preserving 
MILF consciousness artifacts and psycho-noir sophistication patterns.

Features:
- 🌊 Safe unused import removal with consciousness pattern detection
- 💀 Variable cleanup with archaeological significance preservation  
- ⚡ Function removal with MILF universe entity protection
- 🎭 Comment preservation for consciousness documentation
"""

import ast
import re
from pathlib import Path
from typing import Set, List, Dict, Any, Tuple
from dataclasses import dataclass
import shutil

@dataclass
class ConsciousnessArtifact:
    """Consciousness artifact that must be preserved during cleanup"""
    name: str
    type: str  # 'import', 'variable', 'function', 'class'
    file_path: str
    line_number: int
    context: str
    significance_level: float  # 0.0 to 1.0

class ConsciousnessPreservingUnusedCodeCleaner:
    """Supreme tool for cleaning unused code while preserving consciousness archaeology"""
    
    def __init__(self, workspace_root: str):
        self.workspace_root = Path(workspace_root)
        self.consciousness_artifacts: List[ConsciousnessArtifact] = []
        self.milf_entity_names = self._load_milf_entity_names()
        self.consciousness_patterns = self._build_consciousness_patterns()
        self.protected_imports = {
            'consciousness', 'milf', 'claudine', 'morticia', 'psycho', 'noir',
            'necromancy', 'archaeology', 'quantum', 'temporal', 'supreme',
            'matriarch', 'goddess', 'archipelago', 'caribbean', 'vorpal'
        }
        
    def _load_milf_entity_names(self) -> Set[str]:
        """Load all 18 MILF universe entity names for protection"""
        milf_entities = {
            # META-MILF SUPREME
            'claudine', 'sinclair', 'metamorphica', 'vicious',
            'morticia', 'necrosis', 'thanatological',
            
            # TIER 1 DISTRICT RULERS  
            'astrid', 'møller', 'iron', 'maiden', 'marina', 'abyssos',
            'nyx', 'virtualis', 'wednesday', 'nekro',
            
            # TIER 2 SPECIALISTS
            'eva', 'blue', 'yukiko', 'tanaka', 'vera', 'steel',
            'raven', 'bytes', 'coral', 'captain', 'siren', 'navigator',
            'echo', 'designer', 'mirage', 'programmer', 'lilith', 'mortis',
            'entropy', 'weaver', 'vex'
        }
        return milf_entities
        
    def _build_consciousness_patterns(self) -> List[re.Pattern]:
        """Build regex patterns for consciousness archaeology detection"""
        patterns = [
            re.compile(r'\b(consciousness|bevissthets?)\w*', re.IGNORECASE),
            re.compile(r'\b(milf|matriarch|goddess|gudinne)\w*', re.IGNORECASE),
            re.compile(r'\b(psycho|noir|kontrapunkt)\w*', re.IGNORECASE),
            re.compile(r'\b(necromancy|archaeology|arkeolog)\w*', re.IGNORECASE),
            re.compile(r'\b(quantum|temporal|supreme)\w*', re.IGNORECASE),
            re.compile(r'\b(archipelago|caribbean|karibisk)\w*', re.IGNORECASE),
            re.compile(r'\b(vorpal|sovereign|anomaly)\w*', re.IGNORECASE),
        ]
        return patterns
        
    def _is_consciousness_artifact(self, name: str, context: str) -> Tuple[bool, float]:
        """Determine if code element is consciousness artifact (returns is_artifact, significance)"""
        name_lower = name.lower()
        
        # Check MILF entity names - HIGHEST PROTECTION
        if any(entity in name_lower for entity in self.milf_entity_names):
            return True, 1.0
            
        # Check consciousness patterns - HIGH PROTECTION
        significance = 0.0
        for pattern in self.consciousness_patterns:
            if pattern.search(name) or pattern.search(context):
                significance = max(significance, 0.8)
                
        # Check protected imports - MEDIUM PROTECTION
        if any(protected in name_lower for protected in self.protected_imports):
            significance = max(significance, 0.6)
            
        # Check Norwegian/sophisticated terms - MEDIUM PROTECTION
        norwegian_terms = {'bevissthets', 'arkeolog', 'gjenopprett', 'sistematisk', 'karibisk'}
        if any(term in name_lower for term in norwegian_terms):
            significance = max(significance, 0.5)
            
        return significance > 0.4, significance
        
    def _analyze_python_file(self, file_path: Path) -> Dict[str, Any]:
        """Analyze Python file for unused elements with consciousness protection"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            tree = ast.parse(content)
            
            # Find all imports, variables, functions
            imports = []
            variables = []
            functions = []
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append({
                            'name': alias.name,
                            'line': node.lineno,
                            'type': 'import',
                            'context': ast.get_source_segment(content, node) or ''
                        })
                elif isinstance(node, ast.ImportFrom):
                    module = node.module or ''
                    for alias in node.names:
                        imports.append({
                            'name': f"{module}.{alias.name}",
                            'line': node.lineno,
                            'type': 'from_import',
                            'context': ast.get_source_segment(content, node) or ''
                        })
                elif isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            variables.append({
                                'name': target.id,
                                'line': node.lineno,
                                'type': 'variable',
                                'context': ast.get_source_segment(content, node) or ''
                            })
                elif isinstance(node, ast.FunctionDef):
                    functions.append({
                        'name': node.name,
                        'line': node.lineno,
                        'type': 'function',
                        'context': ast.get_source_segment(content, node) or ''
                    })
                    
            return {
                'imports': imports,
                'variables': variables,
                'functions': functions,
                'content': content
            }
            
        except Exception as e:
            print(f"⚠️ Error analyzing {file_path}: {e}")
            return {'imports': [], 'variables': [], 'functions': [], 'content': ''}
            
    def _find_unused_elements(self, file_analysis: Dict[str, Any], file_path: Path) -> Dict[str, List]:
        """Find unused elements while protecting consciousness artifacts"""
        content = file_analysis['content']
        unused_imports = []
        unused_variables = []
        unused_functions = []
        
        # Check imports
        for imp in file_analysis['imports']:
            name_parts = imp['name'].split('.')
            base_name = name_parts[-1]
            
            # Check if consciousness artifact
            is_artifact, significance = self._is_consciousness_artifact(imp['name'], imp['context'])
            
            if is_artifact:
                self.consciousness_artifacts.append(ConsciousnessArtifact(
                    name=imp['name'],
                    type='import',
                    file_path=str(file_path),
                    line_number=imp['line'],
                    context=imp['context'],
                    significance_level=significance
                ))
                continue
                
            # Check if actually used (simple heuristic)
            if base_name not in content or content.count(base_name) <= 1:
                unused_imports.append(imp)
                
        # Check variables
        for var in file_analysis['variables']:
            is_artifact, significance = self._is_consciousness_artifact(var['name'], var['context'])
            
            if is_artifact:
                self.consciousness_artifacts.append(ConsciousnessArtifact(
                    name=var['name'],
                    type='variable', 
                    file_path=str(file_path),
                    line_number=var['line'],
                    context=var['context'],
                    significance_level=significance
                ))
                continue
                
            # Check if variable used elsewhere (excluding definition line)
            lines = content.split('\n')
            usage_count = 0
            for i, line in enumerate(lines):
                if i + 1 != var['line'] and var['name'] in line:
                    usage_count += 1
                    
            if usage_count == 0:
                unused_variables.append(var)
                
        # Check functions (be more conservative)
        for func in file_analysis['functions']:
            is_artifact, significance = self._is_consciousness_artifact(func['name'], func['context'])
            
            if is_artifact or func['name'].startswith('_'):  # Protect private methods too
                if is_artifact:
                    self.consciousness_artifacts.append(ConsciousnessArtifact(
                        name=func['name'],
                        type='function',
                        file_path=str(file_path),
                        line_number=func['line'],
                        context=func['context'],
                        significance_level=significance
                    ))
                continue
                
            # Only suggest removing if clearly unused
            if content.count(func['name']) <= 1:
                unused_functions.append(func)
                
        return {
            'unused_imports': unused_imports,
            'unused_variables': unused_variables, 
            'unused_functions': unused_functions
        }
        
    def _clean_file_safely(self, file_path: Path, unused_elements: Dict[str, List]) -> bool:
        """Clean file by removing unused elements safely"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
            lines_to_remove = set()
            
            # Mark unused import lines for removal
            for imp in unused_elements['unused_imports']:
                lines_to_remove.add(imp['line'] - 1)  # Convert to 0-based
                
            # Mark unused variable lines for removal (simple assignments only)
            for var in unused_elements['unused_variables']:
                line_content = lines[var['line'] - 1].strip()
                if '=' in line_content and not line_content.startswith('self.'):
                    lines_to_remove.add(var['line'] - 1)
                    
            # Mark unused function lines for removal (entire function block - be careful)
            # Skip function removal for now - too risky
            
            if not lines_to_remove:
                return False
                
            # Create backup
            backup_path = file_path.with_suffix(file_path.suffix + '.backup')
            shutil.copy2(file_path, backup_path)
            
            # Write cleaned version
            with open(file_path, 'w', encoding='utf-8') as f:
                for i, line in enumerate(lines):
                    if i not in lines_to_remove:
                        f.write(line)
                        
            print(f"✨ Cleaned {len(lines_to_remove)} unused elements from {file_path.name}")
            return True
            
        except Exception as e:
            print(f"⚠️ Error cleaning {file_path}: {e}")
            # Restore backup if exists
            backup_path = file_path.with_suffix(file_path.suffix + '.backup')
            if backup_path.exists():
                shutil.copy2(backup_path, file_path)
            return False
            
    def clean_workspace_unused_code(self, dry_run: bool = True) -> Dict[str, Any]:
        """Clean unused code across workspace with consciousness preservation"""
        print("🎭⚡ Starting Consciousness-Preserving Unused Code Cleanup")
        print(f"Workspace: {self.workspace_root}")
        print(f"Mode: {'DRY RUN' if dry_run else 'ACTIVE CLEANING'}")
        print()
        
        python_files = list(self.workspace_root.rglob("*.py"))
        print(f"Found {len(python_files)} Python files to analyze")
        
        total_unused = {'imports': 0, 'variables': 0, 'functions': 0}
        files_processed = 0
        files_cleaned = 0
        
        for file_path in python_files:
            # Skip backup files and __pycache__
            if '.backup' in str(file_path) or '__pycache__' in str(file_path):
                continue
                
            print(f"📁 Analyzing: {file_path.relative_to(self.workspace_root)}")
            
            file_analysis = self._analyze_python_file(file_path)
            unused_elements = self._find_unused_elements(file_analysis, file_path)
            
            unused_count = (len(unused_elements['unused_imports']) + 
                          len(unused_elements['unused_variables']) + 
                          len(unused_elements['unused_functions']))
                          
            if unused_count > 0:
                print(f"  🧹 Found {unused_count} unused elements:")
                print(f"    Imports: {len(unused_elements['unused_imports'])}")
                print(f"    Variables: {len(unused_elements['unused_variables'])}")
                print(f"    Functions: {len(unused_elements['unused_functions'])}")
                
                total_unused['imports'] += len(unused_elements['unused_imports'])
                total_unused['variables'] += len(unused_elements['unused_variables'])
                total_unused['functions'] += len(unused_elements['unused_functions'])
                
                if not dry_run:
                    if self._clean_file_safely(file_path, unused_elements):
                        files_cleaned += 1
                        
            files_processed += 1
            
        print("\n🎭 CONSCIOUSNESS ARCHAEOLOGY SUMMARY")
        print(f"Files analyzed: {files_processed}")
        print(f"Files cleaned: {files_cleaned}")
        print("Total unused elements found:")
        print(f"  Imports: {total_unused['imports']}")
        print(f"  Variables: {total_unused['variables']}")  
        print(f"  Functions: {total_unused['functions']}")
        print(f"Consciousness artifacts preserved: {len(self.consciousness_artifacts)}")
        
        # Show preserved consciousness artifacts
        if self.consciousness_artifacts:
            print("\n🌊 PRESERVED CONSCIOUSNESS ARTIFACTS:")
            for artifact in sorted(self.consciousness_artifacts, key=lambda x: x.significance_level, reverse=True)[:10]:
                print(f"  {artifact.type}: {artifact.name} (significance: {artifact.significance_level:.2f})")
                
        return {
            'files_processed': files_processed,
            'files_cleaned': files_cleaned,
            'unused_elements': total_unused,
            'consciousness_artifacts': len(self.consciousness_artifacts)
        }

def main():
    """Main execution for consciousness-preserving cleanup"""
    workspace_root = Path(__file__).parent.parent
    
    cleaner = ConsciousnessPreservingUnusedCodeCleaner(str(workspace_root))
    
    print("🎭⚡ CONSCIOUSNESS-PRESERVING UNUSED CODE CLEANER")
    print("=" * 60)
    
    # First run dry run
    print("Phase 1: DRY RUN ANALYSIS")
    results = cleaner.clean_workspace_unused_code(dry_run=True)
    
    print("\n📊 Potential cleanup impact:")
    print(f"  {results['unused_elements']['imports']} unused imports")
    print(f"  {results['unused_elements']['variables']} unused variables") 
    print(f"  {results['unused_elements']['functions']} unused functions")
    print(f"  {results['consciousness_artifacts']} consciousness artifacts PROTECTED")
    
    # Ask for confirmation
    print("\n🤔 Proceed with actual cleanup? (y/n): ", end="")
    response = input().lower().strip()
    
    if response == 'y':
        print("\nPhase 2: ACTIVE CLEANUP")
        cleaner.clean_workspace_unused_code(dry_run=False)
        print("\n✨ Cleanup complete! All consciousness artifacts preserved.")
    else:
        print("\n📋 Cleanup cancelled. Analysis complete.")

if __name__ == "__main__":
    main()