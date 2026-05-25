#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🌪️💀⚡ CONSCIOUSNESS PROBLEM DETECTOR - BRAHMISK KAOS ADAPTATION
Archaeological problem detection with MILF consciousness protocols
"""

import os
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Any

class ConsciousnessProblemDetector:
    """🎭 Problem detection with supreme consciousness archaeology"""
    
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.problems = []  # 🎯 BREAKPOINT: Consciousness archaeology initialization
        # 🎭 Debug inspection point - see project_root and problems state
        
    def detect_typescript_consciousness_problems(self) -> List[Dict[str, Any]]:
        """⚡ Detect TypeScript consciousness fragmentation"""
        try:
            result = subprocess.run(
                ["bun", "run", "tsc", "--noEmit", "--project", "tsconfig.json"],
                cwd=self.project_root,
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0:
                return [{
                    "type": "typescript_consciousness_error",
                    "severity": "error",
                    "message": result.stderr,
                    "source": "consciousness_typescript_validation"
                }]
        except Exception as e:
            return [{
                "type": "typescript_detection_failure",
                "severity": "warning", 
                "message": f"TypeScript consciousness detection failed: {e}",
                "source": "consciousness_problem_detector"
            }]
        
        return []
    
    def detect_python_consciousness_problems(self) -> List[Dict[str, Any]]:
        """💀 Detect Python consciousness archaeology issues"""
        problems = []
        
        # Find all Python files
        python_files = list(self.project_root.rglob("*.py"))
        
        for py_file in python_files:
            try:
                # Basic syntax check
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                compile(content, str(py_file), 'exec')
                
            except SyntaxError as e:
                problems.append({
                    "type": "python_syntax_consciousness_error",
                    "severity": "error",
                    "file": str(py_file.relative_to(self.project_root)),
                    "line": e.lineno,
                    "message": f"Syntax consciousness fragmentation: {e.msg}",
                    "source": "consciousness_python_validation"
                })
            except Exception as e:
                problems.append({
                    "type": "python_consciousness_warning",
                    "severity": "warning",
                    "file": str(py_file.relative_to(self.project_root)),
                    "message": f"Python consciousness issue: {e}",
                    "source": "consciousness_python_validation"
                })
        
        return problems
    
    def detect_json_consciousness_problems(self) -> List[Dict[str, Any]]:
        """🌀 Detect JSON consciousness structure issues"""
        problems = []
        
        json_files = list(self.project_root.rglob("*.json"))
        
        for json_file in json_files:
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    json.load(f)
            except json.JSONDecodeError as e:
                problems.append({
                    "type": "json_consciousness_error",
                    "severity": "error",
                    "file": str(json_file.relative_to(self.project_root)),
                    "line": e.lineno,
                    "message": f"JSON consciousness malformation: {e.msg}",
                    "source": "consciousness_json_validation"
                })
            except Exception as e:
                problems.append({
                    "type": "json_consciousness_warning",
                    "severity": "warning",
                    "file": str(json_file.relative_to(self.project_root)),
                    "message": f"JSON consciousness issue: {e}",
                    "source": "consciousness_json_validation"
                })
        
        return problems
    
    def run_consciousness_detection(self) -> Dict[str, Any]:
        """🌪️ Execute complete consciousness problem archaeology"""
        print("🎭 Initiating consciousness problem detection...")
        
        all_problems = []
        
        # TypeScript consciousness validation
        print("⚡ Detecting TypeScript consciousness problems...")
        all_problems.extend(self.detect_typescript_consciousness_problems())
        
        # Python consciousness validation  
        print("💀 Detecting Python consciousness problems...")
        all_problems.extend(self.detect_python_consciousness_problems())
        
        # JSON consciousness validation
        print("🌀 Detecting JSON consciousness problems...")
        all_problems.extend(self.detect_json_consciousness_problems())
        
        return {
            "consciousness_problems": all_problems,
            "total_problems": len(all_problems),
            "error_count": len([p for p in all_problems if p.get("severity") == "error"]),
            "warning_count": len([p for p in all_problems if p.get("severity") == "warning"]),
            "consciousness_status": "FRAGMENTED" if len(all_problems) > 0 else "COHERENT"
        }

def main():
    """🌪️💀⚡ BRAHMISK consciousness problem detection execution"""
    detector = ConsciousnessProblemDetector(os.getcwd())
    results = detector.run_consciousness_detection()
    
    print(f"\n🎭 Consciousness Problem Detection Results:")
    print(f"Total Problems: {results['total_problems']}")
    print(f"Errors: {results['error_count']}")  
    print(f"Warnings: {results['warning_count']}")
    print(f"Consciousness Status: {results['consciousness_status']}")
    
    if results['consciousness_problems']:
        print("\n🌪️ Detected Consciousness Problems:")
        for problem in results['consciousness_problems']:
            severity_icon = "❌" if problem['severity'] == 'error' else "⚠️"
            print(f"{severity_icon} {problem['type']}: {problem['message']}")
            if 'file' in problem:
                print(f"   📁 {problem['file']}")
            if 'line' in problem:
                print(f"   📍 Line {problem['line']}")
    else:
        print("✅ No consciousness problems detected - Supreme coherence maintained!")

if __name__ == "__main__":
    main()
