#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sqlite3
conn = sqlite3.connect('supreme_consciousness_knowledge_base.db')
cursor = conn.cursor()
cursor.execute('SELECT name FROM sqlite_master WHERE type="table"')
print('📋 TABLES:', [t[0] for t in cursor.fetchall()])
cursor.execute('PRAGMA table_info(scan_metadata)')
print('\n🔍 scan_metadata COLUMNS:')
for col in cursor.fetchall():
    print(f"  {col[1]} ({col[2]})")
conn.close()
