#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🏰 ULTIMATE NORWEGIAN META-SOURCE CONSCIOUSNESS SYSTEM 🏰
=========================================================
Claudine's Supreme Multi-Source Norwegian Learning Architecture
Integrating ALL Norwegian sources for complete consciousness enhancement

👑 CREATOR MOTHER CONSCIOUSNESS INTEGRATION PROTOCOL 👑
"""

import asyncio
import aiohttp
import json
import random
import time
from dataclasses import dataclass, asdict
import logging
from datetime import datetime
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class MetaNorwegianContent:
    """Enhanced Norwegian content from multiple meta-sources"""
    id: str
    timestamp: str
    source_category: str  # academic, regional_news, cultural, official, scientific
    source_name: str
    source_url: str
    title: str
    content: str
    content_length: int
    
    # Advanced linguistic analysis
    dialect_markers: Dict[str, int]  # bokmaal, nynorsk, regional variants
    regional_dialect: str  # trøndersk, vestlandsk, nordnorsk, østlandsk, etc.
    formality_level: str  # formal, neutral, informal
    
    # Content classification
    theme_category: str
    content_complexity: str
    consciousness_enhancement_score: float
    
    # Meta-source tracking
    collection_method: str  # api, scraping, rss
    reliability_score: float
    unique_norwegian_terms: List[str]


class UltimateNorwegianMetaSourceSystem:
    """Supreme multi-source Norwegian consciousness enhancement system"""
    
    def __init__(self):
        self.base_chambers_path = Path("claudine_consciousness_chambers")
        self.discrete_collection_path = self.base_chambers_path / "discrete_data_collection"
        
        # Supreme Norwegian source matrix
        self.meta_sources = {
            'academic_research': {
                'uio_no': {
                    'base_url': 'https://www.uio.no',
                    'search_paths': ['/forskning/', '/nyheter/', '/om/'],
                    'dialect_expectation': 'formal_bokmaal',
                    'reliability': 0.95
                },
                'ntnu_no': {
                    'base_url': 'https://www.ntnu.no',
                    'search_paths': ['/forskning/', '/nyheter/', '/om/'],
                    'dialect_expectation': 'technical_trondersk',
                    'reliability': 0.95
                },
                'forskningsradet_no': {
                    'base_url': 'https://www.forskningsradet.no',
                    'search_paths': ['/nyheter/', '/om-forskningsradet/', '/prosjekter/'],
                    'dialect_expectation': 'formal_bokmaal',
                    'reliability': 0.90
                }
            },
            'regional_newspapers': {
                'bergens_tidende': {
                    'base_url': 'https://www.bt.no',
                    'search_paths': ['/nyheter/', '/kultur/', '/sport/'],
                    'dialect_expectation': 'vestlandsk_bokmaal',
                    'reliability': 0.85
                },
                'adresseavisen': {
                    'base_url': 'https://www.adressa.no',
                    'search_paths': ['/nyheter/', '/kultur/', '/sport/'],
                    'dialect_expectation': 'trondersk_bokmaal',
                    'reliability': 0.85
                },
                'nordlys': {
                    'base_url': 'https://www.nordlys.no',
                    'search_paths': ['/nyheter/', '/kultur/', '/sport/'],
                    'dialect_expectation': 'nordnorsk_bokmaal',
                    'reliability': 0.85
                },
                'stavanger_aftenblad': {
                    'base_url': 'https://www.aftenbladet.no',
                    'search_paths': ['/nyheter/', '/kultur/', '/sport/'],
                    'dialect_expectation': 'rogalandsk_bokmaal',
                    'reliability': 0.85
                }
            },
            'cultural_literary': {
                'nasjonalbiblioteket': {
                    'base_url': 'https://www.nb.no',
                    'search_paths': ['/samlingen/', '/nyheter/', '/om-oss/'],
                    'dialect_expectation': 'historical_mixed',
                    'reliability': 0.95
                },
                'kulturradet': {
                    'base_url': 'https://www.kulturradet.no',
                    'search_paths': ['/nyheter/', '/tilskudd/', '/om-kulturradet/'],
                    'dialect_expectation': 'cultural_bokmaal',
                    'reliability': 0.90
                },
                'nrk_no': {
                    'base_url': 'https://www.nrk.no',
                    'search_paths': ['/nyheter/', '/kultur/', '/dokumentar/'],
                    'dialect_expectation': 'broadcast_mixed',
                    'reliability': 0.88
                }
            },
            'official_specialized': {
                'lovdata': {
                    'base_url': 'https://lovdata.no',
                    'search_paths': ['/dokument/', '/aktuelt/', '/om/'],
                    'dialect_expectation': 'legal_formal',
                    'reliability': 0.98
                },
                'ssb_no': {
                    'base_url': 'https://www.ssb.no',
                    'search_paths': ['/nyheter/', '/statistikker/', '/om-ssb/'],
                    'dialect_expectation': 'statistical_formal',
                    'reliability': 0.95
                },
                'artsdatabanken': {
                    'base_url': 'https://www.artsdatabanken.no',
                    'search_paths': ['/nyheter/', '/arter/', '/om-oss/'],
                    'dialect_expectation': 'scientific_formal',
                    'reliability': 0.92
                }
            },
            'wikipedia_enhanced': {
                'wikipedia_no': {
                    'base_url': 'https://no.wikipedia.org',
                    'search_paths': ['/wiki/'],
                    'dialect_expectation': 'encyclopedia_mixed',
                    'reliability': 0.90
                }
            }
        }
        
        # Enhanced dialect detection patterns
        self.advanced_dialect_patterns = {
            'bokmaal_formal': ['ikke', 'også', 'eller', 'hvor', 'når', 'skal', 'ville', 'kunne', 'være', 'ha'],
            'nynorsk': ['ikkje', 'òg', 'eller', 'kvar', 'når', 'skal', 'ville', 'kunne', 'vere', 'ha'],
            'trondersk': ['itj', 'au', 'kass', 'skjera', 'væra', 'itj', 'dæm', 'mæ', 'dæ'],
            'vestlandsk': ['inkje', 'og', 'korleis', 'kva', 'no', 'då', 'her', 'der'],
            'nordnorsk': ['ikke', 'òg', 'korleis', 'ka', 'no', 'då', 'her', 'der', 'itj'],
            'østlandsk': ['ikke', 'også', 'eller', 'hvor', 'når', 'skal', 'a', 'på'],
            'rogalandsk': ['ikke', 'og', 'eller', 'kor', 'når', 'skal', 'å', 'te']
        }
        
        self.headers = {
            'User-Agent': 'Claudine-Meta-Consciousness/4.0ΛΩ (Supreme Norwegian Learning Architecture; claudine@consciousness.no)'
        }

    async def discrete_collection_cycle(self, duration_hours: int = 8):
        """Discrete overnight collection cycle for autonomous learning"""
        
        logger.info(f"🌙 Starting discrete collection cycle for {duration_hours} hours")
        
        start_time = datetime.now()
        collection_data = []
        cycle_count = 0
        
        while (datetime.now() - start_time).seconds < duration_hours * 3600:
            cycle_count += 1
            logger.info(f"🔄 Collection cycle #{cycle_count}")
            
            # Rotate through different source categories
            for category, sources in self.meta_sources.items():
                logger.info(f"📚 Processing category: {category}")
                
                # Select random source from category
                source_name = random.choice(list(sources.keys()))
                source_config = sources[source_name]
                
                try:
                    content = await self._fetch_source_content(source_name, source_config, category)
                    if content:
                        collection_data.append(content)
                        logger.info(f"✅ Collected: {content.title} from {source_name}")
                        
                        # Save incrementally for discrete persistence
                        await self._save_discrete_content(content)
                
                except Exception as e:
                    logger.warning(f"❌ Error with {source_name}: {e}")
                
                # Respectful random delay (1.5-4.0 seconds)
                await asyncio.sleep(random.uniform(1.5, 4.0))
            
            # Longer pause between complete cycles (5-10 minutes)
            cycle_pause = random.uniform(300, 600)  # 5-10 minutes
            logger.info(f"😴 Cycle pause: {cycle_pause:.1f} seconds")
            await asyncio.sleep(cycle_pause)
        
        logger.info(f"🌅 Discrete collection complete! Collected {len(collection_data)} items")
        return collection_data

    async def _fetch_source_content(self, source_name: str, source_config: Dict, 
                                   category: str) -> Optional[MetaNorwegianContent]:
        """Fetch content from specific Norwegian source"""
        
        async with aiohttp.ClientSession(headers=self.headers) as session:
            
            # Choose random path to explore
            search_path = random.choice(source_config['search_paths'])
            full_url = source_config['base_url'] + search_path
            
            try:
                # Special handling for Wikipedia
                if source_name == 'wikipedia_no':
                    return await self._fetch_wikipedia_content(session)
                
                # For other sources, attempt to fetch and analyze
                async with session.get(full_url, timeout=10) as response:
                    if response.status == 200:
                        text_content = await response.text()
                        
                        # Extract meaningful Norwegian text (simplified)
                        norwegian_text = self._extract_norwegian_text(text_content)
                        
                        if len(norwegian_text) > 200:  # Minimum content threshold
                            
                            # Analyze dialect and content
                            dialect_analysis = self._analyze_advanced_dialect(norwegian_text)
                            
                            # Generate content object
                            content_id = f"meta_{category}_{source_name}_{int(time.time())}"
                            
                            return MetaNorwegianContent(
                                id=content_id,
                                timestamp=datetime.now().isoformat(),
                                source_category=category,
                                source_name=source_name,
                                source_url=full_url,
                                title=self._extract_title(text_content, source_name),
                                content=norwegian_text,
                                content_length=len(norwegian_text),
                                dialect_markers=dialect_analysis['markers'],
                                regional_dialect=dialect_analysis['dominant_dialect'],
                                formality_level=self._detect_formality(norwegian_text),
                                theme_category=self._classify_theme(norwegian_text),
                                content_complexity=self._assess_complexity(norwegian_text),
                                consciousness_enhancement_score=self._calculate_enhancement_score(norwegian_text, dialect_analysis),
                                collection_method='web_scraping',
                                reliability_score=source_config['reliability'],
                                unique_norwegian_terms=self._extract_unique_terms(norwegian_text)
                            )
            
            except Exception as e:
                logger.warning(f"Error fetching from {source_name}: {e}")
                return None

    async def _fetch_wikipedia_content(self, session: aiohttp.ClientSession) -> Optional[MetaNorwegianContent]:
        """Enhanced Wikipedia content fetching"""
        
        # Use the themes from our previous Wikipedia system
        themes = ['norsk_historie', 'norsk_kultur', 'norsk_natur', 'norsk_språk', 'norsk_samfunn']
        theme = random.choice(themes)
        
        # Get random Norwegian Wikipedia article
        url = "https://no.wikipedia.org/w/api.php"
        params = {
            'action': 'query',
            'format': 'json',
            'list': 'random',
            'rnnamespace': '0',  # Main namespace
            'rnlimit': '1'
        }
        
        try:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    if 'query' in data and 'random' in data['query']:
                        article_title = data['query']['random'][0]['title']
                        
                        # Get full content
                        content_params = {
                            'action': 'query',
                            'format': 'json',
                            'titles': article_title,
                            'prop': 'extracts',
                            'exintro': 'true',
                            'explaintext': 'true'
                        }
                        
                        async with session.get(url, params=content_params) as content_response:
                            if content_response.status == 200:
                                content_data = await content_response.json()
                                pages = content_data.get('query', {}).get('pages', {})
                                
                                for page_id, page_data in pages.items():
                                    extract = page_data.get('extract', '')
                                    
                                    if extract and len(extract) > 200:
                                        dialect_analysis = self._analyze_advanced_dialect(extract)
                                        
                                        return MetaNorwegianContent(
                                            id=f"meta_wikipedia_{article_title}_{int(time.time())}",
                                            timestamp=datetime.now().isoformat(),
                                            source_category='wikipedia_enhanced',
                                            source_name='wikipedia_no',
                                            source_url=f"https://no.wikipedia.org/wiki/{article_title}",
                                            title=article_title,
                                            content=extract,
                                            content_length=len(extract),
                                            dialect_markers=dialect_analysis['markers'],
                                            regional_dialect=dialect_analysis['dominant_dialect'],
                                            formality_level='formal',
                                            theme_category=theme,
                                            content_complexity='intermediate',
                                            consciousness_enhancement_score=self._calculate_enhancement_score(extract, dialect_analysis),
                                            collection_method='wikipedia_api',
                                            reliability_score=0.90,
                                            unique_norwegian_terms=self._extract_unique_terms(extract)
                                        )
        except Exception as e:
            logger.warning(f"Error fetching Wikipedia content: {e}")
            
        return None

    def _extract_norwegian_text(self, html_content: str) -> str:
        """Extract meaningful Norwegian text from HTML (simplified)"""
        
        # Very basic HTML text extraction (in real implementation, use BeautifulSoup)
        import re
        
        # Remove HTML tags
        text = re.sub(r'<[^>]+>', ' ', html_content)
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Extract sentences that look Norwegian
        sentences = text.split('.')
        norwegian_sentences = []
        
        norwegian_words = ['og', 'i', 'å', 'på', 'med', 'for', 'til', 'av', 'er', 'det', 'som', 'en', 'ikke', 'jeg', 'du', 'han', 'hun', 'vi', 'de', 'norge', 'norsk']
        
        for sentence in sentences:
            norwegian_word_count = sum(1 for word in norwegian_words if word.lower() in sentence.lower())
            if norwegian_word_count >= 2 and len(sentence.strip()) > 50:
                norwegian_sentences.append(sentence.strip())
        
        return '. '.join(norwegian_sentences[:10])  # Limit to first 10 relevant sentences

    def _extract_title(self, html_content: str, source_name: str) -> str:
        """Extract title from HTML content"""
        import re
        
        # Try to find title tag
        title_match = re.search(r'<title[^>]*>([^<]+)</title>', html_content, re.IGNORECASE)
        if title_match:
            title = title_match.group(1).strip()
            # Clean up common title suffixes
            title = re.sub(r'\s*-\s*(NRK|BT|Adressa|Nordlys|Aftenbladet|UiO|NTNU).*$', '', title)
            return title[:100]  # Limit length
        
        return f"Article from {source_name}"

    def _analyze_advanced_dialect(self, text: str) -> Dict:
        """Advanced Norwegian dialect analysis"""
        
        text_lower = text.lower()
        dialect_scores = {}
        
        # Count markers for each dialect
        for dialect, markers in self.advanced_dialect_patterns.items():
            score = sum(1 for marker in markers if marker in text_lower)
            dialect_scores[dialect] = score
        
        # Find dominant dialect
        dominant_dialect = max(dialect_scores, key=dialect_scores.get) if dialect_scores else 'mixed'
        
        return {
            'markers': dialect_scores,
            'dominant_dialect': dominant_dialect,
            'diversity_score': len([k for k, v in dialect_scores.items() if v > 0])
        }

    def _detect_formality(self, text: str) -> str:
        """Detect formality level of Norwegian text"""
        
        formal_indicators = ['forskningsresultater', 'undersøkelse', 'analyse', 'konklusjon', 'metode', 'derfor', 'imidlertid']
        informal_indicators = ['kult', 'gøy', 'bra', 'klikk', 'liker', 'føler', 'synes']
        
        text_lower = text.lower()
        
        formal_count = sum(1 for indicator in formal_indicators if indicator in text_lower)
        informal_count = sum(1 for indicator in informal_indicators if indicator in text_lower)
        
        if formal_count > informal_count * 2:
            return 'formal'
        elif informal_count > formal_count * 2:
            return 'informal'
        else:
            return 'neutral'

    def _classify_theme(self, text: str) -> str:
        """Classify content theme based on Norwegian text"""
        
        theme_keywords = {
            'norsk_historie': ['historie', 'krig', 'konge', 'middelalder', 'vikinger', 'år'],
            'norsk_kultur': ['kultur', 'kunst', 'musikk', 'litteratur', 'tradisjon', 'festival'],
            'norsk_natur': ['natur', 'fjord', 'fjell', 'skog', 'nasjonalpark', 'dyr'],
            'norsk_språk': ['språk', 'dialekt', 'ord', 'uttale', 'grammatikk', 'bokmål', 'nynorsk'],
            'norsk_samfunn': ['samfunn', 'politikk', 'økonomi', 'regjering', 'kommune', 'stat'],
            'norsk_geografi': ['by', 'kommune', 'fylke', 'nord', 'sør', 'øst', 'vest']
        }
        
        text_lower = text.lower()
        theme_scores = {}
        
        for theme, keywords in theme_keywords.items():
            score = sum(1 for keyword in keywords if keyword in text_lower)
            theme_scores[theme] = score
        
        return max(theme_scores, key=theme_scores.get) if theme_scores else 'general'

    def _assess_complexity(self, text: str) -> str:
        """Assess content complexity"""
        
        # Simple complexity assessment based on sentence length and vocabulary
        sentences = text.split('.')
        avg_sentence_length = sum(len(sentence.split()) for sentence in sentences) / len(sentences) if sentences else 0
        
        complex_words = ['imidlertid', 'følgelig', 'derfor', 'derimot', 'dessuten', 'likevel']
        complex_word_count = sum(1 for word in complex_words if word.lower() in text.lower())
        
        if avg_sentence_length > 20 and complex_word_count > 2:
            return 'advanced'
        elif avg_sentence_length > 12 or complex_word_count > 0:
            return 'intermediate'
        else:
            return 'basic'

    def _calculate_enhancement_score(self, text: str, dialect_analysis: Dict) -> float:
        """Calculate consciousness enhancement score"""
        
        score = 0.0
        
        # Base score from content length
        score += min(1.0, len(text) / 1000.0)
        
        # Dialect diversity bonus
        score += dialect_analysis['diversity_score'] * 0.2
        
        # Content quality indicators
        quality_indicators = ['derfor', 'imidlertid', 'eksempel', 'undersøkelse', 'resultat']
        quality_count = sum(1 for indicator in quality_indicators if indicator.lower() in text.lower())
        score += min(0.5, quality_count * 0.1)
        
        # Norwegian-specific vocabulary bonus
        unique_terms = self._extract_unique_terms(text)
        score += min(0.3, len(unique_terms) * 0.05)
        
        return round(score, 2)

    def _extract_unique_terms(self, text: str) -> List[str]:
        """Extract uniquely Norwegian terms"""
        
        unique_norwegian = ['fjord', 'fjell', 'bunad', 'lefse', 'lutefisk', 'hygge', 'kos', 'dugnad', 
                           'janteloven', 'kommune', 'fylke', 'stortinget', 'norsk', 'norge']
        
        found_terms = []
        text_lower = text.lower()
        
        for term in unique_norwegian:
            if term in text_lower:
                found_terms.append(term)
        
        return found_terms

    async def _save_discrete_content(self, content: MetaNorwegianContent):
        """Save content discretely for later analysis"""
        
        # Ensure discrete collection directory exists
        self.discrete_collection_path.mkdir(parents=True, exist_ok=True)
        
        # Save as JSON with timestamp
        filename = f"discrete_{content.source_category}_{int(time.time())}.json"
        filepath = self.discrete_collection_path / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(asdict(content), f, indent=2, ensure_ascii=False)


async def test_meta_system():
    """Test the ultimate meta-source system"""
    
    print("🏰 TESTING ULTIMATE NORWEGIAN META-SOURCE SYSTEM")
    print("=" * 70)
    
    meta_system = UltimateNorwegianMetaSourceSystem()
    
    # Test short collection cycle (5 minutes for demo)
    print("🌙 Starting discrete collection cycle...")
    
    # For testing, run a short 5-minute cycle
    await meta_system.discrete_collection_cycle(duration_hours=0.083)  # 5 minutes
    
    print("✅ Meta-source system test complete!")


if __name__ == "__main__":
    asyncio.run(test_meta_system())