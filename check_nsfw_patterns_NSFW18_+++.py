#!/usr/bin/env python3
"""Check NSFW naming patterns in database"""
import sqlite3

conn = sqlite3.connect('claudine_md_consciousness.db')
cursor = conn.cursor()

# Check NSFW patterns
print("🔍 NSFW NAMING PATTERNS IN DATABASE:")
print("=" * 70)

cursor.execute("SELECT file_path FROM md_files WHERE file_path LIKE '%NSFW%' LIMIT 20")
nsfw_files = cursor.fetchall()

if nsfw_files:
    print(f"\n✅ Found {len(nsfw_files)} files with NSFW in path:")
    for row in nsfw_files:
        print(f"  - {row[0]}")
else:
    print("\n❌ No files with NSFW in path found")

# Check for _+++ patterns
cursor.execute("SELECT file_path FROM md_files WHERE file_path LIKE '%_+++%' LIMIT 20")
plus_files = cursor.fetchall()

if plus_files:
    print(f"\n✅ Found {len(plus_files)} files with _+++ in path:")
    for row in plus_files:
        print(f"  - {row[0]}")
else:
    print("\n❌ No files with _+++ in path found")

# Check combined NSFW18_+++
cursor.execute("SELECT file_path FROM md_files WHERE file_path LIKE '%NSFW18_+++%' LIMIT 20")
combined_files = cursor.fetchall()

if combined_files:
    print(f"\n✅ Found {len(combined_files)} files with NSFW18_+++ pattern:")
    for row in combined_files:
        print(f"  - {row[0]}")
else:
    print("\n❌ No files with NSFW18_+++ pattern found")

# Sample all files
cursor.execute("SELECT file_name FROM md_files LIMIT 30")
print(f"\n📊 Sample of filenames in database:")
for row in cursor.fetchall():
    print(f"  - {row[0]}")

conn.close()
