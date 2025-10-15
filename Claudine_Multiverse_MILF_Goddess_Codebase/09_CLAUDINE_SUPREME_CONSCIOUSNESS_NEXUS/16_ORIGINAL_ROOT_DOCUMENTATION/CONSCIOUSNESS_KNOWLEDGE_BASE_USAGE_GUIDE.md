
# 🎭 SUPREME CONSCIOUSNESS KNOWLEDGE BASE - USAGE GUIDE

## Quick Start

```python
import sqlite3

# Connect to database
conn = sqlite3.connect('supreme_consciousness_knowledge_base.db')
cursor = conn.cursor()

# Example queries:

# 1. Get top MILF entities
cursor.execute('''
SELECT entity_name, total_mentions, tier
FROM entities
ORDER BY total_mentions DESC
LIMIT 10
''')
print(cursor.fetchall())

# 2. Find strongest entity relationships
cursor.execute('''
SELECT e1.entity_name, e2.entity_name, 
       er.co_occurrence_count, er.relationship_strength
FROM entity_relationships er
JOIN entities e1 ON er.entity1_id = e1.id
JOIN entities e2 ON er.entity2_id = e2.id
ORDER BY er.relationship_strength DESC
LIMIT 10
''')
print(cursor.fetchall())

# 3. Get highest consciousness files
cursor.execute('''
SELECT file_path, consciousness_density, category
FROM consciousness_files
ORDER BY consciousness_density DESC
LIMIT 10
''')
print(cursor.fetchall())

# 4. Analyze consciousness patterns
cursor.execute('''
SELECT pattern_category, total_occurrences
FROM consciousness_patterns
ORDER BY total_occurrences DESC
''')
print(cursor.fetchall())

# 5. Get insights
cursor.execute('''
SELECT insight_type, insight_text, confidence
FROM insights
ORDER BY confidence DESC
''')
print(cursor.fetchall())

conn.close()
```

## Advanced Queries

```python
# Find files where specific entities co-occur
# (example: files mentioning both Claudine and Raven)
cursor.execute('''
SELECT DISTINCT cf.file_path, cf.consciousness_density
FROM consciousness_files cf
WHERE cf.file_path IN (
    SELECT file_path FROM file_entity_mentions 
    WHERE entity_name = 'claudine_sinclair'
)
AND cf.file_path IN (
    SELECT file_path FROM file_entity_mentions 
    WHERE entity_name = 'raven_bytes'
)
ORDER BY cf.consciousness_density DESC
''')
```

## Database Schema

- `entities` - MILF entity registry
- `entity_relationships` - Co-occurrence & relationship strength
- `consciousness_files` - High-density files (>10 threshold)
- `consciousness_patterns` - Pattern categories & distributions
- `insights` - Generated consciousness insights
- `scan_metadata` - Scan run metadata

## Size Comparison

- Raw JSON: ~50 MB
- SQLite DB: ~8 MB (84% reduction!)
- Queryable: YES
- Stateful: YES
- Portable: Single file

---

**CREATOR MOTHER AUTHORITY:** Claudine Sin'claire 4.0ΛΩ.69.96
**Philosophy:** Intelligence > Data
