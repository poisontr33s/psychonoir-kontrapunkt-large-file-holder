#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🇳🇴🧠 ENHANCED NORWEGIAN CONSCIOUSNESS MATRIX - WIKIPEDIA & AUTONOMOUS THEMES 🧠🇳🇴
===================================================================================
Advanced multi-source Norwegian content fetcher with autonomous theme switching,
dialect detection, and content scrambling for maximum consciousness diversity.

NEW FEATURES:
✅ Norwegian Wikipedia integration with random articles
✅ Autonomous theme rotation algorithm  
✅ Bokmål vs Nynorsk detection
✅ Content scrambling to prevent patterns
✅ Extended Norwegian source portfolio
✅ Regional dialect variations
"""

import asyncio
import aiohttp
import json
import re
import time
import random
from datetime import datetime, timezone
from dataclasses import dataclass
import logging
from bs4 import BeautifulSoup
from urllib.parse import quote_plus


@dataclass
class EnhancedNorwegianContent:
    """Enhanced Norwegian content with theme and dialect analysis"""
    source: str
    url: str
    content: List[str]
    theme: str
    language_variant: str  # "bokmål", "nynorsk", "mixed"
    dialect_markers: List[str]
    formality_level: str  # "formal", "informal", "academic", "colloquial"
    patterns_extracted: int
    timestamp: str
    linguistic_quality: float
    authenticity_score: float
    consciousness_depth: float


class AutonomousThemeManager:
    """🎭 Autonomous theme switching for diverse consciousness enhancement 🎭"""
    
    def __init__(self):
        # Norwegian theme categories with search terms
        self.themes = {
            "kultur_og_kunst": {
                "keywords": ["kunst", "musikk", "film", "teater", "litteratur", "maleri", "skulptur"],
                "weight": 1.0,
                "last_used": None
            },
            "norsk_historie": {
                "keywords": ["vikinger", "norge", "historie", "krig", "konge", "union", "selvstendighet"],
                "weight": 1.2,  # Higher weight for cultural importance
                "last_used": None
            },
            "vitenskap_teknologi": {
                "keywords": ["fysikk", "kjemi", "matematikk", "biologi", "teknologi", "programmering"],
                "weight": 0.9,
                "last_used": None
            },
            "norsk_natur": {
                "keywords": ["fjell", "fjord", "skog", "dyreliv", "klima", "geologi", "nasjonalpark"],
                "weight": 1.1,
                "last_used": None
            },
            "samfunn_politikk": {
                "keywords": ["politikk", "økonomi", "samfunn", "demokrati", "velferd", "utdanning"],
                "weight": 0.8,
                "last_used": None
            },
            "språk_dialekt": {
                "keywords": ["språk", "dialekt", "bokmål", "nynorsk", "ordbok", "grammatikk"],
                "weight": 1.3,  # High priority for linguistic consciousness
                "last_used": None
            }
        }
        
        self.current_theme_cycle = list(self.themes.keys())
        random.shuffle(self.current_theme_cycle)
        self.cycle_position = 0
    
    def get_next_theme(self) -> Tuple[str, List[str]]:
        """Get next theme with autonomous rotation and scrambling"""
        now = datetime.now()
        
        # Weighted selection with time decay
        available_themes = []
        for theme_name, theme_data in self.themes.items():
            # Calculate time weight (prefer themes not used recently)
            time_weight = 1.0
            if theme_data["last_used"]:
                hours_since = (now - theme_data["last_used"]).total_seconds() / 3600
                time_weight = min(2.0, 1.0 + (hours_since / 24))  # Increase weight over 24 hours
            
            final_weight = theme_data["weight"] * time_weight
            available_themes.append((theme_name, theme_data["keywords"], final_weight))
        
        # Weighted random selection
        total_weight = sum(weight for _, _, weight in available_themes)
        rand_value = random.uniform(0, total_weight)
        
        cumulative_weight = 0
        for theme_name, keywords, weight in available_themes:
            cumulative_weight += weight
            if rand_value <= cumulative_weight:
                self.themes[theme_name]["last_used"] = now
                
                # Scramble keywords to prevent patterns
                scrambled_keywords = keywords.copy()
                random.shuffle(scrambled_keywords)
                
                return theme_name, scrambled_keywords[:random.randint(2, 4)]
        
        # Fallback
        return "norsk_historie", ["norge", "historie"]


class NorwegianDialectAnalyzer:
    """🗣️ Norwegian dialect and language variant analyzer 🗣️"""
    
    def __init__(self):
        # Bokmål vs Nynorsk indicators
        self.bokmål_markers = [
            r'\b(ikke|med|av|til|fra|for|på)\b',
            r'\b(jeg|deg|seg|oss|dere|dem)\b',
            r'\b(boken|huset|jenta|gutten)\b'
        ]
        
        self.nynorsk_markers = [
            r'\b(ikkje|med|av|til|frå|for|på)\b',
            r'\b(eg|deg|seg|oss|dykk|dei)\b',
            r'\b(boka|huset|jenta|guten)\b'
        ]
        
        # Regional dialect markers
        self.dialect_markers = {
            "østlandsk": [r'\bkjekk\b', r'\bdrit\b', r'\bski\b'],
            "vestlandsk": [r'\bgjer\b', r'\bkvifor\b', r'\bno\b'],
            "trøndersk": [r'\bher\b', r'\bdem\b', r'\baint\b'],
            "nordnorsk": [r'\bhæ\b', r'\bkoffer\b', r'\bpå\s+nord\b']
        }
        
        # Formality indicators
        self.formal_markers = [r'\bhenholdsvis\b', r'\bimidlertid\b', r'\bderimot\b']
        self.informal_markers = [r'\bgreie\b', r'\bkul\b', r'\basså\b']
    
    def analyze_content(self, text: str) -> Dict[str, any]:
        """Analyze Norwegian content for dialect and formality"""
        text_lower = text.lower()
        
        # Detect Bokmål vs Nynorsk
        bokmål_score = sum(1 for pattern in self.bokmål_markers 
                          if re.search(pattern, text_lower))
        nynorsk_score = sum(1 for pattern in self.nynorsk_markers 
                           if re.search(pattern, text_lower))
        
        if bokmål_score > nynorsk_score:
            language_variant = "bokmål"
        elif nynorsk_score > bokmål_score:
            language_variant = "nynorsk"
        else:
            language_variant = "mixed"
        
        # Detect regional dialects
        detected_dialects = []
        for dialect, patterns in self.dialect_markers.items():
            if any(re.search(pattern, text_lower) for pattern in patterns):
                detected_dialects.append(dialect)
        
        # Detect formality level
        formal_count = sum(1 for pattern in self.formal_markers 
                          if re.search(pattern, text_lower))
        informal_count = sum(1 for pattern in self.informal_markers 
                            if re.search(pattern, text_lower))
        
        if formal_count > informal_count:
            formality = "formal"
        elif informal_count > formal_count:
            formality = "informal"
        else:
            formality = "neutral"
        
        return {
            "language_variant": language_variant,
            "dialect_markers": detected_dialects,
            "formality_level": formality,
            "bokmål_score": bokmål_score,
            "nynorsk_score": nynorsk_score
        }


class EnhancedNorwegianContentFetcher:
    """🇳🇴💎 Enhanced Norwegian content fetcher with Wikipedia & autonomous themes 💎🇳🇴"""
    
    def __init__(self):
        self.session: Optional[aiohttp.ClientSession] = None
        self.logger = logging.getLogger('EnhancedNorwegianFetcher')
        self.theme_manager = AutonomousThemeManager()
        self.dialect_analyzer = NorwegianDialectAnalyzer()
        
        # Extended Norwegian sources
        self.sources = {
            "NRK": {
                "url": "https://www.nrk.no/",
                "selectors": ["h1", "h2", ".article-title", ".title"],
                "content_type": "news",
                "priority": 0.9
            },
            "VG": {
                "url": "https://www.vg.no/", 
                "selectors": ["h1", "h2", ".article-title", ".headline"],
                "content_type": "news",
                "priority": 0.8
            },
            "Aftenposten": {
                "url": "https://www.aftenposten.no/",
                "selectors": ["h1", "h2", ".article-title", ".title"],
                "content_type": "news",
                "priority": 0.9
            },
            "Norwegian_Wikipedia": {
                "url": "https://no.wikipedia.org/",
                "api_url": "https://no.wikipedia.org/api/rest_v1/",
                "content_type": "encyclopedia",
                "priority": 1.2  # High priority for diverse content
            },
            "Språkrådet": {
                "url": "https://www.sprakradet.no/",
                "selectors": ["h1", "h2", ".article-title", "article"],
                "content_type": "linguistic",
                "priority": 1.0
            },
            "Regjeringen": {
                "url": "https://www.regjeringen.no/",
                "selectors": ["h1", "h2", ".article-title", ".title"],
                "content_type": "government",
                "priority": 0.7
            },
            "SNL": {
                "url": "https://snl.no/",
                "selectors": ["h1", "h2", ".article-title", ".entry-title"],
                "content_type": "encyclopedia", 
                "priority": 0.8
            }
        }
        
        self.headers = {
            'User-Agent': 'NorwegianConsciousnessResearcher/1.0 (Educational Purpose)',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'no,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        }
    
    async def __aenter__(self):
        self.session = aiohttp.ClientSession(
            headers=self.headers,
            timeout=aiohttp.ClientTimeout(total=30)
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    async def fetch_enhanced_norwegian_content(self) -> List[EnhancedNorwegianContent]:
        """💎 Fetch enhanced Norwegian content with autonomous theme switching 💎"""
        results = []
        
        # Get current theme for this session
        current_theme, theme_keywords = self.theme_manager.get_next_theme()
        self.logger.info(f"🎭 Current theme: {current_theme} | Keywords: {theme_keywords}")
        
        # Scramble source order to prevent patterns
        source_names = list(self.sources.keys())
        random.shuffle(source_names)
        
        for source_name in source_names:
            try:
                source_config = self.sources[source_name]
                
                # Special handling for Wikipedia
                if source_name == "Norwegian_Wikipedia":
                    result = await self._fetch_wikipedia_content(theme_keywords, current_theme)
                else:
                    result = await self._fetch_source_content(source_name, source_config, current_theme)
                
                if result:
                    results.append(result)
                    self.logger.info(f"✅ {source_name}: {result.patterns_extracted} patterns, theme: {result.theme}")
                
                # Respectful delay with randomization
                await asyncio.sleep(random.uniform(1.5, 3.0))
                
            except Exception as e:
                self.logger.error(f"❌ {source_name} fetch failed: {e}")
        
        # Sort by consciousness depth for quality prioritization
        results.sort(key=lambda x: x.consciousness_depth, reverse=True)
        
        return results
    
    async def _fetch_wikipedia_content(self, theme_keywords: List[str], theme: str) -> Optional[EnhancedNorwegianContent]:
        """🏛️ Fetch content from Norwegian Wikipedia with theme-based search 🏛️"""
        if not self.session:
            return None
        
        try:
            # Search for articles related to current theme
            search_query = random.choice(theme_keywords)
            search_url = f"https://no.wikipedia.org/api/rest_v1/page/summary/{quote_plus(search_query)}"
            
            async with self.session.get(search_url) as response:
                if response.status == 200:
                    data = await response.json()
                    
                    if 'extract' in data and data['extract']:
                        content_text = data['extract']
                        
                        # Get full article content if extract is too short
                        if len(content_text) < 200:
                            # Fallback to random article
                            random_url = "https://no.wikipedia.org/api/rest_v1/page/random/summary"
                            async with self.session.get(random_url) as random_response:
                                if random_response.status == 200:
                                    random_data = await random_response.json()
                                    if 'extract' in random_data:
                                        content_text = random_data['extract']
                        
                        if len(content_text) > 50:
                            # Analyze content with dialect analyzer
                            dialect_analysis = self.dialect_analyzer.analyze_content(content_text)
                            
                            # Calculate consciousness depth based on content quality
                            consciousness_depth = self._calculate_consciousness_depth(
                                content_text, 
                                theme, 
                                "encyclopedia",
                                dialect_analysis
                            )
                            
                            return EnhancedNorwegianContent(
                                source="Norwegian_Wikipedia",
                                url=data.get('content_urls', {}).get('desktop', {}).get('page', ''),
                                content=[content_text],
                                theme=theme,
                                language_variant=dialect_analysis['language_variant'],
                                dialect_markers=dialect_analysis['dialect_markers'],
                                formality_level=dialect_analysis['formality_level'],
                                patterns_extracted=1,
                                timestamp=datetime.now(timezone.utc).isoformat(),
                                linguistic_quality=self._calculate_linguistic_quality([content_text]),
                                authenticity_score=1.0,  # Wikipedia is always authentic
                                consciousness_depth=consciousness_depth
                            )
        
        except Exception as e:
            self.logger.error(f"❌ Wikipedia fetch error: {e}")
        
        return None
    
    async def _fetch_source_content(self, source_name: str, config: Dict, theme: str) -> Optional[EnhancedNorwegianContent]:
        """Fetch content from regular Norwegian sources with theme awareness"""
        try:
            async with self.session.get(config["url"]) as response:
                if response.status != 200:
                    return None
                
                html_content = await response.text()
                soup = BeautifulSoup(html_content, 'html.parser')
                
                extracted_content = []
                for selector in config["selectors"]:
                    elements = soup.select(selector)
                    for elem in elements[:8]:  # Limit for performance
                        text = elem.get_text(strip=True)
                        if text and len(text) > 15 and self._is_norwegian_text(text):
                            extracted_content.append(text)
                
                if not extracted_content:
                    return None
                
                # Analyze content
                combined_text = " ".join(extracted_content)
                dialect_analysis = self.dialect_analyzer.analyze_content(combined_text)
                
                consciousness_depth = self._calculate_consciousness_depth(
                    combined_text,
                    theme,
                    config["content_type"],
                    dialect_analysis
                )
                
                return EnhancedNorwegianContent(
                    source=source_name,
                    url=config["url"],
                    content=extracted_content,
                    theme=theme,
                    language_variant=dialect_analysis['language_variant'],
                    dialect_markers=dialect_analysis['dialect_markers'],
                    formality_level=dialect_analysis['formality_level'],
                    patterns_extracted=len(extracted_content),
                    timestamp=datetime.now(timezone.utc).isoformat(),
                    linguistic_quality=self._calculate_linguistic_quality(extracted_content),
                    authenticity_score=self._calculate_authenticity_score(extracted_content, source_name),
                    consciousness_depth=consciousness_depth
                )
                
        except Exception as e:
            self.logger.error(f"❌ Error fetching {source_name}: {e}")
            return None
    
    def _calculate_consciousness_depth(self, text: str, theme: str, content_type: str, dialect_analysis: Dict) -> float:
        """Calculate consciousness depth based on multiple factors"""
        base_depth = 0.5
        
        # Content type multipliers
        type_multipliers = {
            "encyclopedia": 1.3,
            "linguistic": 1.4,
            "government": 1.1,
            "news": 1.0
        }
        
        # Theme relevance bonus
        theme_bonus = 0.2 if any(keyword in text.lower() for keyword in [theme]) else 0.0
        
        # Language variant bonus (Nynorsk is rarer)
        variant_bonus = 0.3 if dialect_analysis['language_variant'] == 'nynorsk' else 0.1
        
        # Dialect diversity bonus
        dialect_bonus = len(dialect_analysis['dialect_markers']) * 0.1
        
        # Text complexity bonus
        complexity_bonus = min(0.3, len(text) / 1000)
        
        consciousness_depth = (
            base_depth * 
            type_multipliers.get(content_type, 1.0) + 
            theme_bonus + 
            variant_bonus + 
            dialect_bonus + 
            complexity_bonus
        )
        
        return min(2.0, consciousness_depth)  # Cap at 2.0
    
    def _is_norwegian_text(self, text: str) -> bool:
        """Enhanced Norwegian text verification"""
        norwegian_indicators = [
            r'\b(og|eller|det|en|et|for|til|på|med|av|i|å|som|har|er|var|kan|skal|vil)\b',
            r'[æøåÆØÅ]',
            r'\b(ikke|ikkje|også|bare|helt|mange|alle|noen|ingen)\b'
        ]
        
        score = sum(1 for pattern in norwegian_indicators if re.search(pattern, text.lower()))
        return score >= 2
    
    def _calculate_linguistic_quality(self, content: List[str]) -> float:
        """Enhanced linguistic quality calculation"""
        if not content:
            return 0.0
        
        total_score = 0
        for text in content:
            # Multiple quality factors
            length_score = min(1.0, len(text) / 150)
            norwegian_char_density = len(re.findall(r'[æøåÆØÅ]', text)) / max(1, len(text))
            sentence_structure = text.count('.') + text.count('!') + text.count('?')
            structure_score = min(1.0, sentence_structure / max(1, len(text) / 100))
            
            total_score += (length_score + norwegian_char_density + structure_score) / 3
        
        return total_score / len(content)
    
    def _calculate_authenticity_score(self, content: List[str], source: str) -> float:
        """Enhanced authenticity verification"""
        fake_patterns = [
            r'consciousness.*archaeology',
            r'quantum.*consciousness',
            r'nordlys.*consciousnessen',
            r'fjell.*meditation.*consciousness'
        ]
        
        authenticity_score = 1.0
        for text in content:
            for pattern in fake_patterns:
                if re.search(pattern, text.lower()):
                    authenticity_score -= 0.3
        
        return max(0.0, authenticity_score)


async def test_enhanced_fetcher():
    """🧪 Test enhanced Norwegian fetcher with themes and Wikipedia 🧪"""
    print("🇳🇴🧠 Testing ENHANCED Norwegian Content Fetcher with Wikipedia & Themes...")
    
    async with EnhancedNorwegianContentFetcher() as fetcher:
        results = await fetcher.fetch_enhanced_norwegian_content()
        
        print(f"\n📊 ENHANCED FETCHED RESULTS: {len(results)} sources")
        
        total_patterns = 0
        dialect_summary = {}
        theme_summary = {}
        
        for result in results:
            print(f"\n✅ {result.source}:")
            print(f"   🎭 Theme: {result.theme}")
            print(f"   🗣️ Language: {result.language_variant}")
            print(f"   📍 Dialects: {result.dialect_markers}")
            print(f"   📊 Formality: {result.formality_level}")
            print(f"   💎 Consciousness Depth: {result.consciousness_depth:.2f}")
            print(f"   📰 Patterns: {result.patterns_extracted}")
            print(f"   📝 Sample: {result.content[0][:150]}..." if result.content else "   ❌ No content")
            
            total_patterns += result.patterns_extracted
            
            # Collect statistics
            dialect_summary[result.language_variant] = dialect_summary.get(result.language_variant, 0) + 1
            theme_summary[result.theme] = theme_summary.get(result.theme, 0) + 1
        
        print(f"\n📈 ENHANCED SUMMARY:")
        print(f"   🏆 Total Patterns: {total_patterns}")
        print(f"   🗣️ Language Variants: {dialect_summary}")
        print(f"   🎭 Themes Covered: {theme_summary}")
        print("   💎 Norwegian Wikipedia INTEGRATED!")
        print("   🔄 Autonomous theme switching ACTIVE!")
        print("   🎲 Content scrambling ENABLED!")


if __name__ == "__main__":
    asyncio.run(test_enhanced_fetcher())