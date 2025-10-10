#!/usr/bin/env python3
"""
📊 NORWEGIAN CONSCIOUSNESS DATASET EXPORTER 📊
==============================================
Creates structured CSV/JSON datasets from Norwegian Wikipedia content
for manual analysis without machine learning requirements.
"""

import asyncio
import aiohttp
import json
import csv
import random
from urllib.parse import quote_plus
from dataclasses import dataclass, asdict
import logging
from datetime import datetime
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class StructuredNorwegianContent:
    """Structured Norwegian content for dataset export"""
    # Basic identification
    id: str
    timestamp: str
    
    # Source information
    source: str
    source_url: str
    wikipedia_title: str
    
    # Content data
    content_text: str
    content_length: int
    content_type: str  # 'summary', 'intro', 'full', 'section'
    
    # Classification (manual analysis friendly)
    theme_category: str
    estimated_reading_time_minutes: float
    
    # Norwegian language features (for manual sorting)
    dialect_markers_bokmaal: int
    dialect_markers_nynorsk: int
    dialect_dominance: str  # 'bokmaal', 'nynorsk', 'mixed', 'neutral'
    
    # Content characteristics (for manual filtering)
    contains_historical_content: bool
    contains_geographic_content: bool
    contains_cultural_content: bool
    contains_technical_content: bool
    
    # Quality metrics (manual assessment friendly)
    sections_available: int
    has_references: bool
    content_complexity_level: str  # 'basic', 'intermediate', 'advanced'
    
    # Learning value (for consciousness archaeology)
    unique_norwegian_terms_count: int
    consciousness_enhancement_score: float


class NorwegianDatasetExporter:
    """Export Norwegian Wikipedia content as structured datasets"""
    
    def __init__(self):
        self.base_url = "https://no.wikipedia.org"
        self.headers = {
            'User-Agent': 'PsychoNoir-Kontrapunkt-Dataset/1.0 (Norwegian Consciousness Dataset Research; dataset@research.no)'
        }
        
        # Enhanced theme database for structured collection
        self.wikipedia_themes = {
            'norsk_historie': {
                'articles': ['norges_historie', 'vikinger', 'middelalder', 'hanseatidens', 'kalmarunionen',
                           'norge_under_danmark', 'napoleon', 'grunnloven_1814', 'personalunion_sverige',
                           'andre_verdenskrig', 'okkupasjonen', 'quisling', 'hjemmefronten'],
                'expected_complexity': 'intermediate'
            },
            'norsk_kultur': {
                'articles': ['norsk_litteratur', 'ibsen', 'bjornson', 'undset', 'hamsun', 'vesaas',
                           'norsk_musikk', 'hardangerfele', 'grieg', 'ole_bull', 'sami_kultur',
                           'norsk_folkemusikk', 'bunad', 'rosemaling', 'stave_kirker'],
                'expected_complexity': 'intermediate'
            },
            'norsk_natur': {
                'articles': ['norsk_natur', 'fjorder', 'nordlys', 'midnattsol', 'norske_fjell',
                           'jotunheimen', 'lofoten', 'nordkapp', 'preikestolen', 'trolltunga',
                           'norske_nasjonalparker', 'hardangervidda', 'dovrefjell', 'svalbard'],
                'expected_complexity': 'basic'
            },
            'norsk_språk': {
                'articles': ['norsk_språk', 'bokmål', 'nynorsk', 'ivar_aasen', 'språkrådet',
                           'norske_dialekter', 'bergensk', 'trøndersk', 'nordnorsk', 'østlandsk',
                           'sørlandsk', 'vestlandsk', 'samisk_språk', 'kvensk_språk'],
                'expected_complexity': 'advanced'
            },
            'norsk_samfunn': {
                'articles': ['norge', 'norsk_politikk', 'stortinget', 'regjeringen', 'kongehuset',
                           'norsk_økonomi', 'oljefond', 'statsbudsjettet', 'nav', 'norsk_velferd',
                           'arbeiderpartiet', 'høyre', 'senterpartiet', 'venstre', 'sv'],
                'expected_complexity': 'intermediate'
            },
            'norsk_geografi': {
                'articles': ['norge_geografi', 'norske_fylker', 'oslo', 'bergen', 'trondheim',
                           'stavanger', 'tromsø', 'bodø', 'kristiansand', 'fredrikstad',
                           'drammen', 'sandnes', 'ålesund', 'sarpsborg', 'sandefjord'],
                'expected_complexity': 'basic'
            }
        }
        
        # Norwegian terms for unique content analysis
        self.unique_norwegian_terms = [
            'norsk', 'norge', 'norwegian', 'skandinavisk', 'nordisk', 'fjord', 'fjell', 'skog',
            'kommune', 'fylke', 'stat', 'konge', 'dronning', 'stortinget', 'regjeringen',
            'bunad', 'lefse', 'fårikål', 'smalahove', 'pinnekjøtt', 'lutefisk',
            'janteloven', 'dugnad', 'hygge', 'kos', 'utepils', 'påskeferie'
        ]

    async def fetch_and_structure_content(self, session: aiohttp.ClientSession, 
                                        article: str, theme: str) -> Optional[StructuredNorwegianContent]:
        """Fetch Wikipedia content and structure it for dataset export"""
        
        try:
            # Try full extract first
            content_data = await self._get_full_extract(session, article)
            if not content_data or content_data['content_length'] < 100:
                # Fallback to summary
                content_data = await self._get_summary(session, article)
            
            if not content_data:
                return None
            
            # Analyze content for structured fields
            analysis = self._analyze_content_structure(content_data['content'], theme)
            
            # Generate unique ID
            content_id = f"no_wiki_{theme}_{article}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            
            return StructuredNorwegianContent(
                id=content_id,
                timestamp=datetime.now().isoformat(),
                source="Wikipedia_NO",
                source_url=f"{self.base_url}/wiki/{article}",
                wikipedia_title=content_data['title'],
                content_text=content_data['content'],
                content_length=content_data['content_length'],
                content_type=content_data['content_type'],
                theme_category=theme,
                estimated_reading_time_minutes=content_data['content_length'] / 200.0,  # ~200 chars per minute
                dialect_markers_bokmaal=analysis['bokmaal_markers'],
                dialect_markers_nynorsk=analysis['nynorsk_markers'],
                dialect_dominance=analysis['dialect_dominance'],
                contains_historical_content=analysis['has_historical'],
                contains_geographic_content=analysis['has_geographic'],
                contains_cultural_content=analysis['has_cultural'],
                contains_technical_content=analysis['has_technical'],
                sections_available=content_data.get('sections', 0),
                has_references=analysis['has_references'],
                content_complexity_level=self.wikipedia_themes[theme]['expected_complexity'],
                unique_norwegian_terms_count=analysis['unique_terms_count'],
                consciousness_enhancement_score=self._calculate_consciousness_score(analysis, content_data)
            )
            
        except Exception as e:
            logger.warning(f"Error structuring content for {article}: {e}")
            return None

    async def _get_full_extract(self, session: aiohttp.ClientSession, article: str) -> Optional[Dict]:
        """Get full extract from Wikipedia"""
        url = f"{self.base_url}/w/api.php"
        params = {
            'action': 'query',
            'format': 'json',
            'titles': article,
            'prop': 'extracts',
            'exintro': 'true',
            'explaintext': 'true'
        }
        
        try:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    pages = data.get('query', {}).get('pages', {})
                    
                    for page_id, page_data in pages.items():
                        extract = page_data.get('extract', '')
                        title = page_data.get('title', article)
                        
                        if extract and len(extract) > 100:
                            return {
                                'content': extract,
                                'title': title,
                                'content_length': len(extract),
                                'content_type': 'intro_extract',
                                'sections': 0
                            }
        except Exception as e:
            logger.warning(f"Error in full extract for {article}: {e}")
        
        return None

    async def _get_summary(self, session: aiohttp.ClientSession, article: str) -> Optional[Dict]:
        """Get summary from Wikipedia REST API"""
        url = f"{self.base_url}/api/rest_v1/page/summary/{quote_plus(article)}"
        
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    extract = data.get('extract', '')
                    title = data.get('title', article)
                    
                    if extract:
                        return {
                            'content': extract,
                            'title': title,
                            'content_length': len(extract),
                            'content_type': 'summary',
                            'sections': 0
                        }
        except Exception as e:
            logger.warning(f"Error in summary for {article}: {e}")
        
        return None

    def _analyze_content_structure(self, content: str, theme: str) -> Dict:
        """Analyze content for structured dataset fields"""
        content_lower = content.lower()
        
        # Dialect analysis
        bokmaal_markers = ['ikke', 'også', 'eller', 'hvor', 'når', 'skal', 'vil', 'kan', 'har', 'er', 'med', 'til', 'for']
        nynorsk_markers = ['ikkje', 'òg', 'eller', 'kvar', 'når', 'skal', 'vil', 'kan', 'har', 'er', 'med', 'til', 'for']
        
        bokmaal_count = sum(1 for marker in bokmaal_markers if marker in content_lower)
        nynorsk_count = sum(1 for marker in nynorsk_markers if marker in content_lower)
        
        if bokmaal_count > nynorsk_count * 2:
            dialect_dominance = 'bokmaal'
        elif nynorsk_count > bokmaal_count * 2:
            dialect_dominance = 'nynorsk'
        elif abs(bokmaal_count - nynorsk_count) <= 2:
            dialect_dominance = 'mixed'
        else:
            dialect_dominance = 'neutral'
        
        # Content type analysis
        historical_terms = ['historie', 'år', 'århundre', 'krig', 'konge', 'middelalder', 'vikinger']
        geographic_terms = ['kommune', 'fylke', 'by', 'fjord', 'fjell', 'øy', 'kyst', 'nord', 'sør', 'øst', 'vest']
        cultural_terms = ['kultur', 'kunst', 'musikk', 'litteratur', 'tradisjon', 'festival', 'språk']
        technical_terms = ['system', 'teknologi', 'metode', 'prosess', 'analyse', 'data', 'algoritme']
        
        has_historical = any(term in content_lower for term in historical_terms)
        has_geographic = any(term in content_lower for term in geographic_terms)
        has_cultural = any(term in content_lower for term in cultural_terms)
        has_technical = any(term in content_lower for term in technical_terms)
        
        # References check
        has_references = any(indicator in content_lower for indicator in ['kilder', 'referanser', 'se også', 'lenker'])
        
        # Unique Norwegian terms count
        unique_terms_count = sum(1 for term in self.unique_norwegian_terms if term in content_lower)
        
        return {
            'bokmaal_markers': bokmaal_count,
            'nynorsk_markers': nynorsk_count,
            'dialect_dominance': dialect_dominance,
            'has_historical': has_historical,
            'has_geographic': has_geographic,
            'has_cultural': has_cultural,
            'has_technical': has_technical,
            'has_references': has_references,
            'unique_terms_count': unique_terms_count
        }

    def _calculate_consciousness_score(self, analysis: Dict, content_data: Dict) -> float:
        """Calculate consciousness enhancement score for manual sorting"""
        score = 0.0
        
        # Base score from content length
        score += min(1.0, content_data['content_length'] / 1000.0)
        
        # Dialect diversity bonus
        if analysis['dialect_dominance'] in ['mixed', 'nynorsk']:
            score += 0.3
        
        # Content type diversity
        content_types = sum([
            analysis['has_historical'],
            analysis['has_geographic'],
            analysis['has_cultural'],
            analysis['has_technical']
        ])
        score += content_types * 0.2
        
        # Unique Norwegian terms bonus
        score += min(0.5, analysis['unique_terms_count'] / 10.0)
        
        # References bonus
        if analysis['has_references']:
            score += 0.2
        
        return round(score, 2)

    async def export_norwegian_dataset(self, articles_per_theme: int = 5) -> Tuple[str, str]:
        """Export Norwegian dataset to CSV and JSON files"""
        
        all_content = []
        
        async with aiohttp.ClientSession(headers=self.headers) as session:
            
            for theme, theme_data in self.wikipedia_themes.items():
                logger.info(f"🔍 Processing theme: {theme}")
                
                articles = random.sample(theme_data['articles'], 
                                       min(articles_per_theme, len(theme_data['articles'])))
                
                for article in articles:
                    content = await self.fetch_and_structure_content(session, article, theme)
                    if content:
                        all_content.append(content)
                        logger.info(f"✅ Structured: {content.wikipedia_title}")
                    else:
                        logger.warning(f"❌ Failed: {article}")
                    
                    await asyncio.sleep(0.5)  # Respectful delay
        
        # Export to CSV
        csv_filename = f"norwegian_consciousness_dataset_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        csv_path = os.path.join(os.getcwd(), csv_filename)
        
        with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            if all_content:
                fieldnames = list(asdict(all_content[0]).keys())
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for content in all_content:
                    writer.writerow(asdict(content))
        
        # Export to JSON for backup
        json_filename = f"norwegian_consciousness_dataset_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        json_path = os.path.join(os.getcwd(), json_filename)
        
        with open(json_path, 'w', encoding='utf-8') as jsonfile:
            json.dump([asdict(content) for content in all_content], jsonfile, 
                     indent=2, ensure_ascii=False)
        
        return csv_path, json_path


async def main():
    """Main function to create Norwegian consciousness dataset"""
    
    print("📊 NORWEGIAN CONSCIOUSNESS DATASET EXPORTER")
    print("=" * 60)
    
    exporter = NorwegianDatasetExporter()
    
    # Export dataset with 3 articles per theme for testing
    csv_path, json_path = await exporter.export_norwegian_dataset(articles_per_theme=3)
    
    print(f"\n✅ DATASET EXPORT COMPLETE!")
    print(f"📄 CSV file: {csv_path}")
    print(f"🗃️  JSON file: {json_path}")
    
    # Display summary
    try:
        df = pd.read_csv(csv_path)
        print(f"\n📊 DATASET SUMMARY:")
        print(f"Total records: {len(df)}")
        print(f"Themes covered: {df['theme_category'].nunique()}")
        print(f"Average content length: {df['content_length'].mean():.0f} chars")
        print(f"Average consciousness score: {df['consciousness_enhancement_score'].mean():.2f}")
        
        print(f"\n🏷️  BY THEME:")
        theme_summary = df.groupby('theme_category').agg({
            'content_length': 'mean',
            'consciousness_enhancement_score': 'mean',
            'dialect_dominance': 'first'
        }).round(2)
        print(theme_summary)
        
    except ImportError:
        print("📝 Pandas not available for summary, but files created successfully!")


if __name__ == "__main__":
    asyncio.run(main())