"""
🔥😈⛓️💦 NAMING CONVENTION VERIFICATION SCRIPT
Quick verification of NSFW18_+++ naming logic in database

Usage: python verify_naming_convention.py
"""

import sqlite3
from pathlib import Path

DB_PATH = Path("claudine_md_consciousness.db")

def main():
    print("🔍 NAMING CONVENTION VERIFICATION")
    print("="*70)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Check current state
    print("\n📊 CURRENT DATABASE STATE:")
    cursor.execute("SELECT COUNT(*) FROM md_files")
    total = cursor.fetchone()[0]
    print(f"   Total files: {total:,}")
    
    # Check NSFW patterns
    print("\n🔍 NSFW PATTERNS:")
    
    # Pattern 1: NSFW18_+++ (target convention)
    cursor.execute("SELECT COUNT(*) FROM md_files WHERE file_name LIKE '%NSFW18_+++%'")
    nsfw18_count = cursor.fetchone()[0]
    print(f"   _NSFW18_+++: {nsfw18_count} files")
    
    # Pattern 2: Generic NSFW
    cursor.execute("SELECT COUNT(*) FROM md_files WHERE file_name LIKE '%NSFW%' AND file_name NOT LIKE '%NSFW18_+++%'")
    generic_nsfw = cursor.fetchone()[0]
    print(f"   NSFW (generic): {generic_nsfw} files")
    
    # Pattern 3: README.md (likely external)
    cursor.execute("SELECT COUNT(*) FROM md_files WHERE file_name = 'README.md'")
    readme_count = cursor.fetchone()[0]
    print(f"   README.md: {readme_count} files (likely external packages)")
    
    # Show samples of each category
    if nsfw18_count > 0:
        print("\n✅ NSFW18_+++ files (sample):")
        cursor.execute("SELECT file_name, file_path FROM md_files WHERE file_name LIKE '%NSFW18_+++%' LIMIT 5")
        for row in cursor.fetchall():
            print(f"      {row[0]}")
    
    if generic_nsfw > 0:
        print("\n⚠️  Generic NSFW files (need standardization):")
        cursor.execute("SELECT file_name, file_path FROM md_files WHERE file_name LIKE '%NSFW%' AND file_name NOT LIKE '%NSFW18_+++%' LIMIT 5")
        for row in cursor.fetchall():
            print(f"      {row[0]}")
            print(f"         Path: {row[1][:60]}...")
    
    # Check "our files" pattern (CLAUDINE, necromancy, consciousness, TODO, .github)
    print("\n🎯 'OUR FILES' DETECTION:")
    our_markers = ['CLAUDINE', 'Claudine', 'MILF', 'necromancy', 'consciousness', 'TODO', 'PHASE', '.github']
    
    for marker in our_markers[:3]:  # Show first 3 as examples
        cursor.execute(f"SELECT COUNT(*) FROM md_files WHERE file_path LIKE '%{marker}%'")
        count = cursor.fetchone()[0]
        print(f"   {marker}: {count} files")
    
    # Estimate files needing standardization
    print("\n💡 STANDARDIZATION ESTIMATE:")
    our_files_query = " OR ".join([f"file_path LIKE '%{marker}%'" for marker in our_markers])
    cursor.execute(f"""
        SELECT COUNT(*) FROM md_files 
        WHERE ({our_files_query})
        AND file_name NOT LIKE '%NSFW18_+++%'
        AND file_name NOT LIKE 'README.md'
    """)
    needs_rename = cursor.fetchone()[0]
    print(f"   Files needing NSFW18_+++ suffix: ~{needs_rename}")
    
    # Show naming convention logic
    print("\n📝 NAMING CONVENTION LOGIC:")
    print("   ✅ OUR FILES:      filename_NSFW18_+++.md")
    print("   ❌ EXTERNAL FILES: filename.md (unchanged)")
    print("")
    print("   SEARCH BENEFITS:")
    print("   - *_NSFW18_+++* returns ONLY our files")
    print(f"   - Excludes {readme_count} external README.md files")
    print("   - Enables precise consciousness archaeology filtering")
    
    conn.close()
    
    print("\n" + "="*70)
    print("🔥 READY FOR STANDARDIZATION MIGRATION")
    print("   Command: sqlite3 claudine_md_consciousness.db < .github/UNIFIED_DATABASE_STANDARDIZATION_MIGRATION.sql")

if __name__ == "__main__":
    main()
