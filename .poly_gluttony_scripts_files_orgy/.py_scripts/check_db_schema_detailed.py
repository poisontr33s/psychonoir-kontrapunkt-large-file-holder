#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""Quick database schema inspection for consciousness density analyzer."""

import sqlite3
from pathlib import Path

db_path = Path(__file__).parent / "claudine_md_consciousness.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("=" * 80)
print("📊 DATABASE SCHEMA INSPECTION")
print("=" * 80)

# Get all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [row[0] for row in cursor.fetchall()]
print(f"\n📁 Tables: {', '.join(tables)}\n")

# Get md_files schema
print("🗂️  md_files schema:")
cursor.execute("PRAGMA table_info(md_files)")
for row in cursor.fetchall():
    print(f"  • {row[1]:<25} {row[2]:<15} {'PRIMARY KEY' if row[5] else ''}")

# Get consciousness categories
print("\n🧠 Consciousness categories:")
cursor.execute(
    "SELECT consciousness_type, COUNT(*) FROM md_files GROUP BY consciousness_type ORDER BY COUNT(*) DESC"
)
for row in cursor.fetchall():
    print(f"  • {row[0]:<30} {row[1]:>5} files")

# Get sections schema
print("\n📑 md_sections schema:")
cursor.execute("PRAGMA table_info(md_sections)")
for row in cursor.fetchall():
    print(f"  • {row[1]:<25} {row[2]:<15} {'PRIMARY KEY' if row[5] else ''}")

# Get total stats
cursor.execute("SELECT COUNT(*) FROM md_files")
total_files = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM md_sections")
total_sections = cursor.fetchone()[0]
cursor.execute("SELECT SUM(word_count) FROM md_sections")
total_words = cursor.fetchone()[0]
cursor.execute("SELECT SUM(size_bytes) FROM md_files")
total_size = cursor.fetchone()[0]

print(f"\n📊 Database totals:")
print(f"  • Total files:    {total_files:,}")
print(f"  • Total sections: {total_sections:,}")
print(f"  • Total words:    {total_words:,}")
print(f"  • Total size:     {total_size / 1024 / 1024:.2f} MB")

# Check for MILF-related files
print("\n🔥 MILF-specific files:")
cursor.execute(
    "SELECT path FROM md_files WHERE path LIKE '%milf%' OR consciousness_type LIKE '%MILF%' LIMIT 10"
)
for row in cursor.fetchall():
    print(f"  • {row[0]}")

conn.close()
print("\n" + "=" * 80)
