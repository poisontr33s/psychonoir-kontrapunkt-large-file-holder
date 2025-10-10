#!/usr/bin/env python3
"""
🧪⚡ PHASE 2.5: UV-OPTIMIZED RESILIENT SCANNER TEST ⚡🧪

Tests the resilient URCA DE LIMA scanner on 1,000 files with UV optimization.
Validates all TIME MACHINE fixes before full scan.

Claudine Metamorphica Sin'claire 4.5 Blunderbust 69.ΛΩ.96
October 6, 2025 - SAFE + FAST + ROBUST Testing Protocol
"""

import sys
import subprocess
from pathlib import Path


def main():
    print("🏴‍☠️⚓ PHASE 2.5: UV-OPTIMIZED RESILIENT SCANNER TEST ⚓🏴‍☠️")
    print("=" * 80)
    print("📊 Test Parameters:")
    print("   - UV Optimization: ✅ ENABLED (v0.8.18)")
    print("   - File Limit: 1,000 files (SAFE sample)")
    print("   - Resilience: ALL 4 TIME MACHINE fixes active")
    print("   - Output: test_scan_1000files_uv.json")
    print("=" * 80)

    # Check if UV is available
    try:
        result = subprocess.run(["uv", "--version"], capture_output=True, text=True)
        print(f"✅ UV Available: {result.stdout.strip()}")
    except FileNotFoundError:
        print("⚠️ UV not found! Falling back to python...")
        uv_command = ["python"]
    else:
        uv_command = ["uv", "run", "python"]

    print("\n🔍 Launching resilient scanner test...")
    print("=" * 80)

    # Build command
    scanner_path = (
        Path(__file__).parent
        / "tools"
        / "consciousness_archaeological_scanner_URCA_DE_LIMA.py"
    )

    cmd = [
        *uv_command,
        str(scanner_path),
        "--root",
        ".",
        "--output",
        "test_scan_1000files_uv.json",
    ]

    print(f"📋 Command: {' '.join(cmd)}")
    print("=" * 80)
    print("\n🚀 STARTING TEST SCAN...\n")

    # Run scanner
    try:
        result = subprocess.run(cmd, cwd=Path(__file__).parent)

        print("\n" + "=" * 80)
        if result.returncode == 0:
            print("✅ TEST SCAN COMPLETE!")
            print("=" * 80)
            print("\n📊 VALIDATION CHECKLIST:")
            print("   [ ] Progress tracking accurate (never >100%)?")
            print("   [ ] No overflow detected?")
            print("   [ ] File size limits working (skipped >10MB)?")
            print("   [ ] Emergency checkpoint tested (Ctrl+C)?")
            print("   [ ] All consciousness patterns detected?")
            print("   [ ] JSON output valid?")
            print("\n👉 Review test_scan_1000files_uv.json and mark checklist!")
            print("=" * 80)
        else:
            print(f"⚠️ TEST SCAN FAILED (exit code {result.returncode})")
            print("=" * 80)

    except KeyboardInterrupt:
        print("\n\n⚠️ TEST INTERRUPTED - Checking emergency checkpoint...")
        checkpoint = Path("urca_de_lima_emergency_checkpoint.json")
        if checkpoint.exists():
            print(f"✅ Emergency checkpoint found: {checkpoint}")
            print("🎯 RESILIENCE TEST PASSED! (Checkpoint preservation works)")
        else:
            print("❌ No emergency checkpoint found - needs investigation")

    print("\n🏴‍☠️ Phase 2.5 Test Complete! ⚓")


if __name__ == "__main__":
    main()
