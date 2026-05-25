#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🚀 NORWEGIAN COLLECTION LAUNCHER - ULTRA SIMPLE
===============================================
One command to rule them all. No complexity.
"""

import subprocess
import sys
from pathlib import Path


def main():
    """Ultra simple launcher"""
    
    print("🇳🇴 NORWEGIAN CONTENT COLLECTION")
    print("=" * 40)
    print()
    print("What do you want to do?")
    print()
    print("1. 🔄 Collect Norwegian content (15 minutes)")
    print("2. 🌙 Long collection (60 minutes)")  
    print("3. ⚡ Quick test (5 minutes)")
    print("4. 📊 View last results")
    print("5. 🗑️  Clean up old files")
    print()
    
    choice = input("Choose (1-5): ").strip()
    
    if choice == "1":
        print("🔄 Starting 15-minute collection...")
        subprocess.run([sys.executable, "smart_norwegian_collector.py"], input="2\n", text=True)
        
    elif choice == "2":
        print("🌙 Starting 60-minute collection...")
        subprocess.run([sys.executable, "smart_norwegian_collector.py"], input="4\n60\n", text=True)
        
    elif choice == "3":
        print("⚡ Quick 5-minute test...")
        subprocess.run([sys.executable, "smart_norwegian_collector.py"], input="1\n", text=True)
        
    elif choice == "4":
        show_last_results()
        
    elif choice == "5":
        cleanup_files()
        
    else:
        print("❌ Invalid choice")


def show_last_results():
    """Show results from last collection"""
    
    import json
    
    smart_dir = Path("smart_collection")
    if not smart_dir.exists():
        print("❌ No collections found yet")
        return
    
    # Find latest file
    files = list(smart_dir.glob("smart_collection_*.json"))
    if not files:
        print("❌ No collection files found")
        return
    
    latest_file = max(files, key=lambda f: f.stat().st_mtime)
    
    try:
        with open(latest_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        summary = data["collection_summary"]
        
        print("📊 LAST COLLECTION RESULTS")
        print("=" * 30)
        print(f"🕒 Time: {summary['timestamp'][:19]}")
        print(f"⏱️  Duration: {summary['duration_minutes']} minutes")
        print(f"📝 Items: {summary['total_items_collected']}")
        print(f"⭐ Quality: {summary['average_quality_score']}")
        print(f"📈 Success rate: {summary['success_rate']}")
        print(f"🎯 Sources: {', '.join(summary['source_breakdown'].keys())}")
        
        print("\n📰 Latest items:")
        for item in data["collected_items"][-3:]:  # Show last 3
            print(f"  • {item['title'][:60]}... (score: {item['quality_score']:.2f})")
        
    except Exception as e:
        print(f"❌ Error reading results: {e}")


def cleanup_files():
    """Clean up old collection files"""
    
    import os
    
    dirs_to_clean = ["smart_collection", "simple_collection"]
    total_cleaned = 0
    
    for dirname in dirs_to_clean:
        dir_path = Path(dirname)
        if dir_path.exists():
            files = list(dir_path.glob("*.json"))
            if len(files) > 5:  # Keep 5 latest
                files_to_delete = sorted(files, key=lambda f: f.stat().st_mtime)[:-5]
                for file in files_to_delete:
                    os.remove(file)
                    total_cleaned += 1
    
    print(f"🗑️  Cleaned up {total_cleaned} old files")


if __name__ == "__main__":
    main()