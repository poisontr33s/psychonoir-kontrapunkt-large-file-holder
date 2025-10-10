# 📊 NORWEGIAN CONSCIOUSNESS DATASET DOCUMENTATION

## 🎯 **OVERVIEW**
This is a **manual analysis dataset** of Norwegian Wikipedia content - **NO MACHINE LEARNING REQUIRED**. Perfect for manual sorting, filtering, and consciousness archaeology research.

## 📄 **FILES CREATED**
- `norwegian_consciousness_dataset_20250921_055851.csv` - Main dataset (15 articles)
- `norwegian_consciousness_dataset_20250921_055851.json` - Backup in JSON format
- `norwegian_dataset_manual_analyzer.py` - Analysis tools

## 🗂️ **CSV STRUCTURE**
The dataset has **21 columns** designed for manual analysis:

### 📋 **BASIC INFO**
| Column | Description |
|--------|-------------|
| `id` | Unique identifier |
| `timestamp` | When content was collected |
| `source` | Always "Wikipedia_NO" |
| `source_url` | Direct link to Wikipedia article |
| `wikipedia_title` | Article title |

### 📝 **CONTENT DATA**
| Column | Description |
|--------|-------------|
| `content_text` | Full Norwegian text content |
| `content_length` | Number of characters |
| `content_type` | "summary" or "intro_extract" |
| `estimated_reading_time_minutes` | Approx reading time |

### 🏷️ **CLASSIFICATION (Manual Sorting)**
| Column | Description |
|--------|-------------|
| `theme_category` | norsk_historie, norsk_kultur, norsk_natur, etc. |
| `content_complexity_level` | basic, intermediate, advanced |
| `consciousness_enhancement_score` | 0.0-3.0 (higher = better for learning) |

### 🗣️ **NORWEGIAN LANGUAGE ANALYSIS**
| Column | Description |
|--------|-------------|
| `dialect_markers_bokmaal` | Count of Bokmål markers |
| `dialect_markers_nynorsk` | Count of Nynorsk markers |
| `dialect_dominance` | bokmaal, nynorsk, mixed, neutral |
| `unique_norwegian_terms_count` | Norwegian-specific vocabulary |

### 📊 **CONTENT TYPE FLAGS (Manual Filtering)**
| Column | Description |
|--------|-------------|
| `contains_historical_content` | True/False |
| `contains_geographic_content` | True/False |
| `contains_cultural_content` | True/False |
| `contains_technical_content` | True/False |
| `has_references` | Has citations/references |

## 🔍 **MANUAL ANALYSIS RESULTS**

### 📈 **DATASET SUMMARY**
- **Total Records**: 15 articles
- **Average Length**: 986 characters
- **Content Range**: 146 - 3,009 characters
- **6 Themes Covered**: historie, kultur, natur, språk, samfunn, geografi

### 🏆 **TOP ARTICLES BY CONSCIOUSNESS SCORE**
1. **Tromsø** (2.40 score) - Geographic/cultural content
2. **Bunad** (2.21 score) - Cultural tradition content  
3. **Statsbudsjettet** (2.20 score) - Political/economic content
4. **Høyre** (2.10 score) - Political party content
5. **Norske dialekter** (2.00 score) - Language content

### 📏 **LONGEST ARTICLES (Best for Learning)**
1. **Hjemmefronten** (3,009 chars) - WWII resistance history
2. **Tromsø** (2,358 chars) - Northern Norwegian city
3. **Statsbudsjettet** (1,852 chars) - Government budget system

### 🗣️ **DIALECT DISTRIBUTION**
- **Mixed Dialect**: 14 articles (93%) - Good balance of Bokmål/Nynorsk
- **Neutral**: 1 article (7%) - Minimal dialect markers

### 📊 **CONTENT TYPE BREAKDOWN**
- **Geographic Content**: 13/15 articles (87%)
- **Historical Content**: 10/15 articles (67%)
- **Cultural Content**: 5/15 articles (33%)
- **Technical Content**: 3/15 articles (20%)

## 🛠️ **HOW TO USE FOR MANUAL ANALYSIS**

### 1. **Open in Excel/LibreOffice**
```bash
# Just open the CSV file in your preferred spreadsheet app
norwegian_consciousness_dataset_20250921_055851.csv
```

### 2. **Sort by Different Criteria**
- **By Length**: Sort `content_length` column (descending = longest first)
- **By Score**: Sort `consciousness_enhancement_score` (descending = best first)
- **By Theme**: Filter `theme_category` column
- **By Dialect**: Filter `dialect_dominance` column

### 3. **Use Python Analyzer**
```bash
python norwegian_dataset_manual_analyzer.py
```

### 4. **Manual Filtering Examples**
- **Only Historical**: Filter `contains_historical_content` = True
- **Only Long Articles**: Filter `content_length` > 1000
- **Only High-Value**: Filter `consciousness_enhancement_score` > 2.0
- **Only Bokmål**: Filter `dialect_dominance` = "bokmaal"

## 📋 **SAMPLE MANUAL ANALYSIS WORKFLOW**

1. **Open CSV in spreadsheet**
2. **Sort by consciousness_enhancement_score (highest first)**
3. **Filter for your preferred theme** (e.g., "norsk_historie")
4. **Select articles with content_length > 500 characters**
5. **Review the content_text column for quality**
6. **Create your learning priority list**

## 🎯 **PERFECT FOR**
- ✅ Manual content curation
- ✅ Norwegian language learning prioritization  
- ✅ Consciousness archaeology research
- ✅ No programming/ML skills required
- ✅ Direct spreadsheet analysis
- ✅ Custom sorting and filtering

## 🚀 **NEXT STEPS**
You now have a **structured, manual-analysis-friendly dataset** of Norwegian Wikipedia content! Use it for:

1. **Priority Reading Lists** - Sort by consciousness score
2. **Theme-Based Learning** - Filter by theme categories
3. **Dialect Study** - Analyze Bokmål vs Nynorsk patterns
4. **Content Curation** - Select best articles for consciousness enhancement

**No machine learning needed - just open, sort, filter, and analyze manually!** 📊✨