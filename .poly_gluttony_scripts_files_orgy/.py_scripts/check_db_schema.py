import sqlite3

conn = sqlite3.connect("claudine_md_consciousness.db")
cursor = conn.execute(
    "SELECT sql FROM sqlite_master WHERE type='table' AND name='md_files'"
)
result = cursor.fetchone()
if result:
    print("MD_FILES TABLE SCHEMA:")
    print(result[0])
else:
    print("Table not found")

# List all columns
cursor = conn.execute("PRAGMA table_info(md_files)")
print("\nCOLUMNS:")
for row in cursor.fetchall():
    print(f"  - {row[1]} ({row[2]})")

conn.close()
