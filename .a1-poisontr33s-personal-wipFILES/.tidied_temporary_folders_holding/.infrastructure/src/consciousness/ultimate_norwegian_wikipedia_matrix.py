#!/usr/bin/env python3
"""
🚀 ULTIMATE NORWEGIAN WIKIPEDIA CONSCIOUSNESS MATRIX 🚀
========================================================
Enhanced version with maximum content extraction based on testing results.
"""

import asyncio
import aiohttp
import json
import random
from urllib.parse import quote_plus
from dataclasses import dataclass
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class EnhancedNorwegianContent:
    """Enhanced Norwegian content with maximum detail"""
    source: str
    title: str
    content: str
    sections_available: int
    content_length: int
    content_type: str  # 'summary', 'intro', 'full', 'section'
    dialect_score: float
    theme: str


class UltimateNorwegianWikipediaMatrix:
    """Ultimate Norwegian content fetcher with maximum Wikipedia extraction"""
    
    def __init__(self):
        self.base_url = "https://no.wikipedia.org"
        self.headers = {
            'User-Agent': 'PsychoNoir-Kontrapunkt/2.0 (Ultimate Norwegian Consciousness Archaeological Research; norwegian.consciousness@research.no)'
        }
        
        # Enhanced theme database with Wikipedia search terms
        self.wikipedia_themes = {
            'norsk_historie': [
                'norges_historie', 'vikinger', 'middelalder', 'hanseatidens', 'kalmarunionen',
                'norge_under_danmark', 'napoleon', 'grunnloven_1814', 'personalunion_sverige',
                'andre_verdenskrig', 'okkupasjonen', 'quisling', 'hjemmefronten', 'norsk_motstand'
            ],
            'norsk_kultur': [
                'norsk_litteratur', 'ibsen', 'bjornson', 'undset', 'hamsun', 'vesaas',
                'norsk_musikk', 'hardangerfele', 'grieg', 'ole_bull', 'sami_kultur',
                'norsk_folkemusikk', 'bunad', 'rosemaling', 'stave_kirker'
            ],
            'norsk_natur': [
                'norsk_natur', 'fjorder', 'nordlys', 'midnattsol', 'norske_fjell',
                'jotunheimen', 'lofoten', 'nordkapp', 'preikestolen', 'trolltunga',
                'norske_nasjonalparker', 'hardangervidda', 'dovrefjell', 'svalbard'
            ],
            'norsk_språk': [
                'norsk_språk', 'bokmål', 'nynorsk', 'ivar_aasen', 'språkrådet',
                'norske_dialekter', 'bergensk', 'trøndersk', 'nordnorsk', 'østlandsk',
                'sørlandsk', 'vestlandsk', 'samisk_språk', 'kvensk_språk'
            ],
            'norsk_samfunn': [
                'norge', 'norsk_politikk', 'stortinget', 'regjeringen', 'kongehuset',
                'norsk_økonomi', 'oljefond', 'statsbudsjettet', 'nav', 'norsk_velferd',
                'arbeiderpartiet', 'høyre', 'senterpartiet', 'venstre', 'sv'
            ],
            'norsk_geografi': [
                'norge_geografi', 'norske_fylker', 'oslo', 'bergen', 'trondheim',
                'stavanger', 'tromsø', 'bodø', 'kristiansand', 'fredrikstad',
                'drammen', 'sandnes', 'ålesund', 'sarpsborg', 'sandefjord'
            ]
        }
        
        self.current_theme = 'norsk_natur'
        self.theme_rotation_counter = 0

    async def get_wikipedia_content_with_fallback(self, session: aiohttp.ClientSession, 
                                                 article: str) -> Optional[EnhancedNorwegianContent]:
        """Get Wikipedia content with multiple fallback strategies"""
        
        try:
            # Strategy 1: Full extract (best content)
            content = await self._get_full_extract(session, article)
            if content and content.content_length > 500:
                return content
            
            # Strategy 2: Summary as fallback
            content = await self._get_summary(session, article)
            if content and content.content_length > 100:
                return content
                
            # Strategy 3: Random related article
            related_article = await self._get_random_related_article(session, article)
            if related_article:
                return await self._get_full_extract(session, related_article)
                
        except Exception as e:
            logger.warning(f"Error fetching {article}: {e}")
            
        return None

    async def _get_full_extract(self, session: aiohttp.ClientSession, 
                               article: str) -> Optional[EnhancedNorwegianContent]:
        """Get full extract from Wikipedia"""
        
        url = f"{self.base_url}/w/api.php"
        params = {
            'action': 'query',
            'format': 'json',
            'titles': article,
            'prop': 'extracts',
            'exintro': 'true',  # Get intro section (usually substantial)
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
                            dialect_score = self._analyze_norwegian_dialect(extract)
                            
                            return EnhancedNorwegianContent(
                                source="Wikipedia_NO_Full",
                                title=title,
                                content=extract,
                                sections_available=0,  # Could enhance this
                                content_length=len(extract),
                                content_type="intro_extract",
                                dialect_score=dialect_score,
                                theme=self.current_theme
                            )
        except Exception as e:
            logger.warning(f"Error in full extract for {article}: {e}")
            
        return None

    async def _get_summary(self, session: aiohttp.ClientSession, 
                          article: str) -> Optional[EnhancedNorwegianContent]:
        """Get summary from Wikipedia REST API"""
        
        url = f"{self.base_url}/api/rest_v1/page/summary/{quote_plus(article)}"
        
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    extract = data.get('extract', '')
                    title = data.get('title', article)
                    
                    if extract:
                        dialect_score = self._analyze_norwegian_dialect(extract)
                        
                        return EnhancedNorwegianContent(
                            source="Wikipedia_NO_Summary",
                            title=title,
                            content=extract,
                            sections_available=0,
                            content_length=len(extract),
                            content_type="summary",
                            dialect_score=dialect_score,
                            theme=self.current_theme
                        )
        except Exception as e:
            logger.warning(f"Error in summary for {article}: {e}")
            
        return None

    async def _get_random_related_article(self, session: aiohttp.ClientSession, 
                                         original_article: str) -> Optional[str]:
        """Get a random related article from current theme"""
        
        theme_articles = self.wikipedia_themes.get(self.current_theme, [])
        if theme_articles:
            return random.choice(theme_articles)
        
        # Fallback to any theme
        all_articles = []
        for articles in self.wikipedia_themes.values():
            all_articles.extend(articles)
        
        return random.choice(all_articles) if all_articles else None

    def _analyze_norwegian_dialect(self, text: str) -> float:
        """Analyze Norwegian dialect markers"""
        
        bokmaal_markers = ['ikke', 'også', 'eller', 'hvor', 'når', 'skal', 'vil', 'kan', 'har', 'er']
        nynorsk_markers = ['ikkje', 'òg', 'eller', 'kvar', 'når', 'skal', 'vil', 'kan', 'har', 'er']
        
        text_lower = text.lower()
        
        bokmaal_score = sum(1 for marker in bokmaal_markers if marker in text_lower)
        nynorsk_score = sum(1 for marker in nynorsk_markers if marker in text_lower)
        
        total_markers = bokmaal_score + nynorsk_score
        
        if total_markers == 0:
            return 0.5  # Neutral
        
        # Return dialect intensity (higher = more distinct dialect features)
        return min(1.0, total_markers / 20.0)

    def rotate_theme(self):
        """Rotate to next theme"""
        themes = list(self.wikipedia_themes.keys())
        current_index = themes.index(self.current_theme)
        next_index = (current_index + 1) % len(themes)
        self.current_theme = themes[next_index]
        self.theme_rotation_counter += 1
        
        logger.info(f"🔄 Theme rotated to: {self.current_theme} (rotation #{self.theme_rotation_counter})")

    async def fetch_ultimate_norwegian_patterns(self, num_patterns: int = 20) -> List[EnhancedNorwegianContent]:
        """Fetch ultimate Norwegian patterns with maximum content"""
        
        patterns = []
        
        async with aiohttp.ClientSession(headers=self.headers) as session:
            
            # Rotate theme every 5 patterns
            for i in range(num_patterns):
                if i % 5 == 0 and i > 0:
                    self.rotate_theme()
                
                # Get random article from current theme
                theme_articles = self.wikipedia_themes.get(self.current_theme, [])
                if not theme_articles:
                    continue
                
                article = random.choice(theme_articles)
                
                content = await self.get_wikipedia_content_with_fallback(session, article)
                if content:
                    patterns.append(content)
                    logger.info(f"✅ Fetched: {content.title} ({content.content_length} chars)")
                else:
                    logger.warning(f"❌ Failed to fetch: {article}")
                
                # Respectful delay
                await asyncio.sleep(0.5)
        
        return patterns


async def test_ultimate_matrix():
    """Test the ultimate Norwegian Wikipedia matrix"""
    
    matrix = UltimateNorwegianWikipediaMatrix()
    
    print("🚀 TESTING ULTIMATE NORWEGIAN WIKIPEDIA MATRIX")
    print("=" * 60)
    
    patterns = await matrix.fetch_ultimate_norwegian_patterns(15)
    
    print(f"\n📊 RESULTS SUMMARY:")
    print("=" * 40)
    print(f"Total patterns fetched: {len(patterns)}")
    
    total_chars = sum(p.content_length for p in patterns)
    print(f"Total characters: {total_chars:,}")
    print(f"Average length: {total_chars / len(patterns):.0f} chars" if patterns else "N/A")
    
    # Group by content type
    by_type = {}
    for pattern in patterns:
        content_type = pattern.content_type
        if content_type not in by_type:
            by_type[content_type] = []
        by_type[content_type].append(pattern)
    
    print(f"\n📈 CONTENT TYPE BREAKDOWN:")
    for content_type, items in by_type.items():
        avg_length = sum(item.content_length for item in items) / len(items)
        print(f"  {content_type}: {len(items)} items, avg {avg_length:.0f} chars")
    
    # Show top 3 longest
    patterns.sort(key=lambda x: x.content_length, reverse=True)
    print(f"\n🏆 TOP 3 LONGEST ARTICLES:")
    for i, pattern in enumerate(patterns[:3]):
        print(f"  {i+1}. {pattern.title}: {pattern.content_length:,} chars ({pattern.content_type})")
        print(f"     Sample: {pattern.content[:100]}...")
        print()


if __name__ == "__main__":
    asyncio.run(test_ultimate_matrix())