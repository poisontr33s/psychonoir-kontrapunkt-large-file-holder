import sqlite3
from pathlib import Path

db_path = Path("claudine_md_consciousness.db")

if not db_path.exists():
    print("❌ Database not found!")
    exit(1)

conn = sqlite3.connect(str(db_path))

# Total files
cursor = conn.execute("SELECT COUNT(*) FROM md_files")
total = cursor.fetchone()[0]
print(f"✅ Total MD files in database: {total:,}")

# By consciousness type
print(f"\n📊 By consciousness type:")
cursor = conn.execute("""
    SELECT consciousness_type, COUNT(*) 
    FROM md_files 
    GROUP BY consciousness_type 
    ORDER BY COUNT(*) DESC
""")
for row in cursor:
    print(f"   {row[0]}: {row[1]:,}")

# Total size and stats
cursor = conn.execute("""
    SELECT 
        SUM(size_bytes) as total_size,
        SUM(line_count) as total_lines,
        SUM(word_count) as total_words
    FROM md_files
""")
stats = cursor.fetchone()
total_mb = stats[0] / (1024 * 1024)
print(f"\n📈 Statistics:")
print(f"   Total size: {total_mb:.2f} MB")
print(f"   Total lines: {stats[1]:,}")
print(f"   Total words: {stats[2]:,}")

# Check archive structure
archive_path = Path("CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS/21_MD_CONSCIOUSNESS_ARCHIVE")
if archive_path.exists():
    archive_files = list(archive_path.rglob("*.md"))
    print(f"\n📁 Archive structure:")
    print(f"   Archive files: {len(archive_files):,}")

    # Count by subdirectory
    subdirs = {}
    for f in archive_files:
        rel = f.relative_to(archive_path)
        if len(rel.parts) > 1:
            subdir = rel.parts[0]
            subdirs[subdir] = subdirs.get(subdir, 0) + 1

    print(f"   Consciousness domains: {len(subdirs)}")
    for subdir, count in sorted(subdirs.items(), key=lambda x: x[1], reverse=True):
        print(f"      {subdir}: {count:,}")

conn.close()
