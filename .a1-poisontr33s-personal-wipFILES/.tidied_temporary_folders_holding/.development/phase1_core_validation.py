#!/usr/bin/env python3
"""Phase 1: Core system validation"""
import sys
import importlib.util

def test_core_imports():
    """Test that core consciousness systems can be imported"""
    tests = [
        ("Supreme Terminal Integration", "supreme_terminal_integration_enhancement"),
        ("Wordosaurus Database", "tools.wordosaurus_consciousness_archaeology_database")
    ]
    
    results = {}
    for name, module in tests:
        try:
            if "tools." in module:
                sys.path.append("tools")
                module = module.replace("tools.", "")
            
            spec = importlib.util.find_spec(module)
            if spec is not None:
                results[name] = "✅ PASS"
            else:
                results[name] = "❌ FAIL - Module not found"
        except Exception as e:
            results[name] = f"❌ FAIL - {e}"
    
    for name, result in results.items():
        print(f"{name}: {result}")
    
    return all("✅" in result for result in results.values())

if __name__ == "__main__":
    success = test_core_imports()
    sys.exit(0 if success else 1)
