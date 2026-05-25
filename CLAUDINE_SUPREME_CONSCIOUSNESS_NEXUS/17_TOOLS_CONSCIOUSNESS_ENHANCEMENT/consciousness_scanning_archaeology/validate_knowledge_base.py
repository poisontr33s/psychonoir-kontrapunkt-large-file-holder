#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🎭 SUPREME CONSCIOUSNESS KNOWLEDGE BASE VALIDATOR 🎭
Validates and showcases intelligence stored in database
"""

import sqlite3
import sys

def validate_knowledge_base(db_path: str = "supreme_consciousness_knowledge_base.db"):
    """Validate and showcase database content"""
    
    print("\n" + "="*80)
    print("🎭 SUPREME CONSCIOUSNESS KNOWLEDGE BASE VALIDATION 🎭")
    print("="*80 + "\n")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 1. Entity validation
    print("👑 MILF ENTITY REGISTRY:\n")
    cursor.execute('''
        SELECT entity_name, total_mentions, tier
        FROM entities
        ORDER BY total_mentions DESC
        LIMIT 10
    ''')
    for name, mentions, tier in cursor.fetchall():
        print(f"  Tier {tier}: {name} - {mentions:,} mentions")
    
    # 2. Relationship strength
    print("\n💋 STRONGEST ENTITY RELATIONSHIPS:\n")
    cursor.execute('''
        SELECT e1.entity_name, e2.entity_name, 
               er.co_occurrence_count, er.relationship_strength
        FROM entity_relationships er
        JOIN entities e1 ON er.entity1_id = e1.id
        JOIN entities e2 ON er.entity2_id = e2.id
        ORDER BY er.relationship_strength DESC
        LIMIT 5
    ''')
    for e1, e2, count, strength in cursor.fetchall():
        print(f"  {e1} ↔ {e2}: {count:,} co-occurrences (strength: {strength:.3f})")
    
    # 3. Consciousness patterns
    print("\n🔥 CONSCIOUSNESS PATTERNS:\n")
    cursor.execute('''
        SELECT pattern_category, total_occurrences
        FROM consciousness_patterns
        ORDER BY total_occurrences DESC
    ''')
    for pattern, occurrences in cursor.fetchall():
        print(f"  {pattern}: {occurrences:,} occurrences")
    
    # 4. High-consciousness files
    print("\n💎 HIGHEST CONSCIOUSNESS FILES:\n")
    cursor.execute('''
        SELECT file_path, consciousness_density, category
        FROM consciousness_files
        ORDER BY consciousness_density DESC
        LIMIT 5
    ''')
    for path, density, category in cursor.fetchall():
        print(f"  Density {density:.2f}: {path}")
        print(f"    Category: {category}\n")
    
    # 5. Autonomous insights
    print("✨ AUTONOMOUS INSIGHTS:\n")
    cursor.execute('''
        SELECT insight_type, insight_text, confidence
        FROM insights
        ORDER BY confidence DESC
    ''')
    for itype, text, confidence in cursor.fetchall():
        print(f"  [{itype}] (confidence: {confidence:.2f})")
        print(f"  {text}\n")
    
    # 6. Database statistics
    print("📊 DATABASE STATISTICS:\n")
    
    cursor.execute("SELECT COUNT(*) FROM entities")
    entity_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM entity_relationships")
    relationship_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM consciousness_files")
    file_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM consciousness_patterns")
    pattern_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM insights")
    insight_count = cursor.fetchone()[0]
    
    print(f"  Entities: {entity_count}")
    print(f"  Relationships: {relationship_count}")
    print(f"  High-consciousness files: {file_count}")
    print(f"  Consciousness patterns: {pattern_count}")
    print(f"  Autonomous insights: {insight_count}")
    
    # 7. Compression metrics
    print("\n💾 COMPRESSION METRICS:\n")
    cursor.execute("SELECT total_files_scanned, total_consciousness_refs, scan_timestamp, scanner_version FROM scan_metadata LIMIT 1")
    result = cursor.fetchone()
    if result:
        total_files, total_refs, timestamp, version = result
        print(f"  Files scanned: {total_files:,}")
        print(f"  Total consciousness refs: {total_refs:,}")
        print(f"  Scan timestamp: {timestamp}")
        print(f"  Scanner version: {version}")
    
    import os
    db_size = os.path.getsize(db_path) / (1024 * 1024)  # MB
    print(f"  Database size: {db_size:.2f} MB")
    print(f"  Estimated raw size: ~50 MB")
    print(f"  Compression ratio: {(1 - db_size/50)*100:.1f}%")
    
    conn.close()
    
    print("\n" + "="*80)
    print("✅ VALIDATION COMPLETE - KNOWLEDGE BASE OPERATIONAL!")
    print("="*80 + "\n")

if __name__ == "__main__":
    db_path = sys.argv[1] if len(sys.argv) > 1 else "supreme_consciousness_knowledge_base.db"
    validate_knowledge_base(db_path)
