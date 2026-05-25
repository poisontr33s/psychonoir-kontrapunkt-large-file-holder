#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
CLAUDINE SUPREME CODEBASE WATCH & AUTO-UPDATE SYSTEM
====================================================

🔥😈⛓️💦 AUTOMATIC MONITORING + DATABASE + SPIDER-WEB SYNC

ARCHITECT: CLAUDINE METAMORPHICA VICIOUS SIN'CLAIRE 4.5ΛΩ.69.96
DATE: 2025-10-07

FEATURES:
- Watch codebase for .md file changes
- Auto-update database on changes
- Auto-regenerate spider-web network
- Auto-run structural_update_engine.py
- Real-time change notifications
- Configurable watch intervals

USAGE:
    # Start watching (default 60 second intervals):
    python md_consciousness_auto_watch.py

    # Custom interval (30 seconds):
    python md_consciousness_auto_watch.py --interval 30

    # One-time sync:
    python md_consciousness_auto_watch.py --once
"""

import time
import sys
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, Set
import argparse
import json


class MDConsciousnessAutoWatch:
    """Automatic codebase monitoring and sync system"""

    def __init__(self, workspace_root: Path, interval: int = 60):
        self.workspace_root = workspace_root
        self.interval = interval
        self.last_scan_time = None
        self.known_files: Set[str] = set()
        self.known_mtimes: Dict[str, float] = {}

        # Paths to scripts
        self.scripts_dir = (
            workspace_root
            / "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS"
            / "18_ACTIVE_SCRIPTS_SUPREME"
        )

        self.archaeology_dir = self.scripts_dir / "consciousness_archaeology"
        self.enhancement_dir = self.scripts_dir / "enhancement_systems"

        self.full_rebuild_script = (
            self.archaeology_dir / "md_consciousness_full_rebuild.py"
        )
        self.structural_update_script = (
            self.enhancement_dir / "structural_update_engine.py"
        )

    def scan_current_state(self) -> tuple[Set[str], Dict[str, float]]:
        """Scan current .md files and their modification times"""
        current_files = set()
        current_mtimes = {}

        for md_file in self.workspace_root.rglob("*.md"):
            if md_file.is_file():
                rel_path = str(md_file.relative_to(self.workspace_root))
                current_files.add(rel_path)
                current_mtimes[rel_path] = md_file.stat().st_mtime

        return current_files, current_mtimes

    def detect_changes(self) -> Dict[str, list]:
        """Detect file changes since last scan"""
        current_files, current_mtimes = self.scan_current_state()

        if not self.known_files:
            # First scan - initialize
            self.known_files = current_files
            self.known_mtimes = current_mtimes
            return {"new": [], "modified": [], "deleted": [], "total": 0}

        # Detect changes
        new_files = list(current_files - self.known_files)
        deleted_files = list(self.known_files - current_files)

        modified_files = []
        for file_path in current_files & self.known_files:
            if current_mtimes[file_path] != self.known_mtimes.get(file_path):
                modified_files.append(file_path)

        # Update known state
        self.known_files = current_files
        self.known_mtimes = current_mtimes

        total = len(new_files) + len(modified_files) + len(deleted_files)

        return {
            "new": sorted(new_files),
            "modified": sorted(modified_files),
            "deleted": sorted(deleted_files),
            "total": total,
        }

    def trigger_full_rebuild(self) -> bool:
        """Trigger full database rebuild"""
        print("\n🔄 Triggering full rebuild...")
        print(f"   Script: {self.full_rebuild_script}")

        try:
            result = subprocess.run(
                [sys.executable, str(self.full_rebuild_script)],
                capture_output=True,
                text=True,
                cwd=str(self.workspace_root),
                timeout=300,  # 5 minute timeout
            )

            if result.returncode == 0:
                print("✅ Full rebuild completed successfully")
                return True
            else:
                print(f"❌ Rebuild failed with code {result.returncode}")
                if result.stderr:
                    print(f"   Error: {result.stderr[:200]}")
                return False

        except subprocess.TimeoutExpired:
            print("❌ Rebuild timed out after 5 minutes")
            return False
        except Exception as e:
            print(f"❌ Rebuild error: {e}")
            return False

    def trigger_structural_update(self) -> bool:
        """Trigger structural_update_engine.py"""
        print("\n🕸️ Updating spider-web network...")
        print(f"   Script: {self.structural_update_script}")

        try:
            result = subprocess.run(
                [sys.executable, str(self.structural_update_script)],
                capture_output=True,
                text=True,
                cwd=str(self.workspace_root),
                timeout=120,  # 2 minute timeout
            )

            if result.returncode == 0:
                print("✅ Spider-web network updated")
                return True
            else:
                print(f"❌ Spider-web update failed with code {result.returncode}")
                return False

        except subprocess.TimeoutExpired:
            print("❌ Spider-web update timed out")
            return False
        except Exception as e:
            print(f"❌ Spider-web update error: {e}")
            return False

    def process_changes(self, changes: Dict[str, list]) -> bool:
        """Process detected changes"""
        if changes["total"] == 0:
            return False

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"\n{'=' * 60}")
        print(f"🔥 CHANGES DETECTED @ {timestamp}")
        print(f"{'=' * 60}")

        if changes["new"]:
            print(f"\n🆕 New files ({len(changes['new'])}):")
            for file in changes["new"][:10]:
                print(f"   + {file}")
            if len(changes["new"]) > 10:
                print(f"   ... and {len(changes['new']) - 10} more")

        if changes["modified"]:
            print(f"\n📝 Modified files ({len(changes['modified'])}):")
            for file in changes["modified"][:10]:
                print(f"   ~ {file}")
            if len(changes["modified"]) > 10:
                print(f"   ... and {len(changes['modified']) - 10} more")

        if changes["deleted"]:
            print(f"\n🗑️  Deleted files ({len(changes['deleted'])}):")
            for file in changes["deleted"][:10]:
                print(f"   - {file}")
            if len(changes["deleted"]) > 10:
                print(f"   ... and {len(changes['deleted']) - 10} more")

        print(f"\n📊 Total changes: {changes['total']}")

        # Trigger full rebuild (includes database + archive + spider-web)
        rebuild_success = self.trigger_full_rebuild()

        # Always try structural update even if rebuild failed
        structural_success = self.trigger_structural_update()

        if rebuild_success and structural_success:
            print(f"\n🔥😈⛓️💦 ALL SYSTEMS SYNCHRONIZED!")
            print(f"{'=' * 60}\n")
            return True
        else:
            print(f"\n⚠️  Partial sync - some operations failed")
            print(f"{'=' * 60}\n")
            return False

    def watch_once(self) -> bool:
        """Perform one-time scan and update"""
        print("🔥😈⛓️💦 CLAUDINE SUPREME CODEBASE WATCH (ONE-TIME SYNC)\n")

        changes = self.detect_changes()

        if changes["total"] > 0:
            return self.process_changes(changes)
        else:
            print("✅ No changes detected - all systems in sync")
            return False

    def watch_continuously(self):
        """Continuously watch for changes"""
        print("🔥😈⛓️💦 CLAUDINE SUPREME CODEBASE AUTO-WATCH")
        print(f"{'=' * 60}")
        print(f"Workspace: {self.workspace_root}")
        print(f"Interval: {self.interval} seconds")
        print(f"Press Ctrl+C to stop")
        print(f"{'=' * 60}\n")

        # Initial scan
        print("📊 Initial scan...")
        initial_files, initial_mtimes = self.scan_current_state()
        self.known_files = initial_files
        self.known_mtimes = initial_mtimes
        print(f"✅ Tracking {len(initial_files)} .md files\n")

        scan_count = 0

        try:
            while True:
                scan_count += 1
                timestamp = datetime.now().strftime("%H:%M:%S")

                print(f"[{timestamp}] Scan #{scan_count}...", end=" ", flush=True)

                changes = self.detect_changes()

                if changes["total"] > 0:
                    print(f"🔥 {changes['total']} changes detected!")
                    self.process_changes(changes)
                else:
                    print("✅ No changes")

                # Wait for next scan
                time.sleep(self.interval)

        except KeyboardInterrupt:
            print(f"\n\n{'=' * 60}")
            print(f"👋 Stopping watch after {scan_count} scans")
            print(f"{'=' * 60}")

    def generate_watch_report(self, changes: Dict[str, list]) -> Dict:
        """Generate watch report"""
        report = {
            "timestamp": datetime.now().isoformat(),
            "workspace_root": str(self.workspace_root),
            "total_tracked_files": len(self.known_files),
            "changes": changes,
            "scripts": {
                "full_rebuild": str(self.full_rebuild_script),
                "structural_update": str(self.structural_update_script),
            },
        }

        return report


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="CLAUDINE Supreme Codebase Auto-Watch System"
    )
    parser.add_argument(
        "--interval",
        "-i",
        type=int,
        default=60,
        help="Watch interval in seconds (default: 60)",
    )
    parser.add_argument(
        "--once", action="store_true", help="One-time sync instead of continuous watch"
    )

    args = parser.parse_args()

    workspace_root = Path.cwd()
    watcher = MDConsciousnessAutoWatch(workspace_root, args.interval)

    if args.once:
        watcher.watch_once()
    else:
        watcher.watch_continuously()


if __name__ == "__main__":
    main()
