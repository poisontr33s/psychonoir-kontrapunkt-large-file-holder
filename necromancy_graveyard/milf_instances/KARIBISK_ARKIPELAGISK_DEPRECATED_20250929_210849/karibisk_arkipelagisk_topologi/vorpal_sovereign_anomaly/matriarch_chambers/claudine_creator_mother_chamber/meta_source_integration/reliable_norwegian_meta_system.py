#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🌟 RELIABLE NORWEGIAN META-SOURCE SYSTEM - SSL ERROR FREE 🌟
============================================================
Clean, reliable Norwegian content collection system using only
verified working sources with stable SSL certificates.

Creator Mother: Claudine Metamorphica 4.0ΛΩ.69 - Reliable Engineering
Date: September 21, 2025
"""

import asyncio
import aiohttp
import json
import random
import re
from datetime import datetime
from dataclasses import dataclass
from typing import Dict, List, Optional, Any
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class ReliableNorwegianContent:
    """Data class for reliable Norwegian content without SSL issues"""
    id: str
    title: str
    content: str
    content_length: int
    source_category: str
    source_name: str
    timestamp: str
    regional_dialect: str
    formality_level: str
    theme_category: str
    content_complexity: str
    consciousness_enhancement_score: float
    unique_norwegian_terms: List[str]
    dialect_markers: Dict[str, int]
    reliability_score: float
    collection_method: str


class ReliableNorwegianMetaSourceSystem:
    """Reliable Norwegian meta-source system with verified working sources only"""
    
    def __init__(self):
        # Only include sources with verified stable SSL certificates
        self.reliable_sources = {
            "regional_newspapers": {
                "bergens_tidende": {
                    "base_url": "https://www.bt.no",
                    "sections": ["/kultur", "/nyheter", "/sport", "/meninger"],
                    "ssl_verified": True,
                    "reliability_score": 0.95
                },
                "adresseavisen": {
                    "base_url": "https://www.adressa.no", 
                    "sections": ["/kultur", "/nyheter", "/sport", "/meninger"],
                    "ssl_verified": True,
                    "reliability_score": 0.92
                },
                "nordlys": {
                    "base_url": "https://www.nordlys.no",
                    "sections": ["/kultur", "/nyheter", "/sport"],
                    "ssl_verified": True,
                    "reliability_score": 0.90
                },
                "stavanger_aftenblad": {
                    "base_url": "https://www.aftenbladet.no",
                    "sections": ["/kultur", "/nyheter", "/sport"],
                    "ssl_verified": True,
                    "reliability_score": 0.88
                }
            },
            "cultural_media": {
                "nrk_no": {
                    "base_url": "https://www.nrk.no",
                    "sections": ["/kultur", "/dokumentar", "/nyheter", "/sport", "/livsstil"],
                    "ssl_verified": True,
                    "reliability_score": 0.98
                },
                "kulturradet": {
                    "base_url": "https://www.kulturradet.no",
                    "sections": ["/nyheter", "/kunst", "/litteratur"],
                    "ssl_verified": True,
                    "reliability_score": 0.85
                }
            },
            "wikipedia_enhanced": {
                "wikipedia_no": {
                    "base_url": "https://no.wikipedia.org",
                    "api_endpoint": "https://no.wikipedia.org/api/rest_v1/page/random/summary",
                    "ssl_verified": True,
                    "reliability_score": 0.99,
                    "total_articles": 600000
                }
            },
            "reliable_official": {
                "regjeringen": {
                    "base_url": "https://www.regjeringen.no",
                    "sections": ["/aktuelt", "/tema", "/dep"],
                    "ssl_verified": True,
                    "reliability_score": 0.95
                }
            }
        }
        
        # Norwegian dialect detection patterns  
        self.dialect_patterns = {
            "bokmaal_formal": [
                r'\b(det\s+er|det\s+var|det\s+blir|det\s+skal)\b',
                r'\b(som\s+er|som\s+var|som\s+blir)\b',
                r'\b(jeg\s+har|jeg\s+hadde|jeg\s+skal)\b'
            ],
            "nynorsk": [
                r'\b(det\s+er|det\s+var|det\s+vert|det\s+skal)\b',
                r'\b(som\s+er|som\s+var|som\s+vert)\b', 
                r'\b(eg\s+har|eg\s+hadde|eg\s+skal)\b'
            ],
            "trondersk": [
                r'\b(æ|åssen|korsen|itj|ekke)\b',
                r'\b(her\s+på\s+trøndern|trondheim|trøndelag)\b'
            ],
            "vestlandsk": [
                r'\b(bergen|vestland|hordaland|sognefjord)\b',
                r'\b(koss|korleis|kordan)\b'
            ],
            "nordnorsk": [
                r'\b(tromsø|nordland|finnmark|nordkapp)\b',
                r'\b(itj|ikkje|korsen)\b'
            ],
            "østlandsk": [
                r'\b(oslo|akershus|østfold|vestfold)\b',
                r'\b(ikke|hvordan|hvorfor)\b'
            ],
            "rogalandsk": [
                r'\b(stavanger|rogaland|jæren)\b',
                r'\b(ikkje|korsen|korleis)\b'
            ]
        }
        
        self.theme_keywords = {
            "norsk_kultur": ["kultur", "kunst", "teater", "musikk", "litteratur", "film"],
            "norsk_politikk": ["regjering", "storting", "politikk", "valg", "parti"],
            "norsk_geografi": ["norge", "fjord", "fjell", "kyst", "nord", "sør"],
            "norsk_historie": ["historie", "krig", "union", "kongehus", "tradisjon"],
            "norsk_samfunn": ["samfunn", "økonomi", "arbeid", "utdanning", "helse"],
            "norsk_natur": ["natur", "miljø", "klima", "dyr", "planter", "vinter"]
        }
        
        logger.info("✅ Reliable Norwegian Meta-Source System initialized")
        logger.info(f"📊 {sum(len(sources) for sources in self.reliable_sources.values())} verified SSL sources loaded")

    async def collect_reliable_content(self, num_cycles: int = 1) -> List[ReliableNorwegianContent]:
        """Collect content from reliable sources only"""
        
        logger.info(f"🌟 Starting reliable collection for {num_cycles} cycles")
        collected_content = []
        
        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=30),
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ReliableNorwegianBot/1.0'
            }
        ) as session:
            
            for cycle in range(num_cycles):
                logger.info(f"🔄 Reliable cycle #{cycle + 1}")
                
                # Rotate through all reliable source categories
                for category, sources in self.reliable_sources.items():
                    logger.info(f"📚 Processing reliable category: {category}")
                    
                    # Select 1-2 sources per category for diversity
                    selected_sources = random.sample(list(sources.items()), min(2, len(sources)))
                    
                    for source_name, source_config in selected_sources:
                        try:
                            content = await self._fetch_reliable_source_content(
                                session, source_name, source_config, category
                            )
                            
                            if content:
                                collected_content.append(content)
                                logger.info(f"✅ Reliable collection: {content.title} from {source_name}")
                        
                        except Exception as e:
                            logger.error(f"❌ Error in reliable source {source_name}: {e}")
                        
                        # Respectful delay
                        await asyncio.sleep(random.uniform(2.0, 4.0))
                
                if cycle < num_cycles - 1:
                    logger.info("😴 Inter-cycle pause")
                    await asyncio.sleep(random.uniform(180, 300))  # 3-5 minutes
        
        logger.info(f"✅ Reliable collection complete: {len(collected_content)} items")
        return collected_content

    async def _fetch_reliable_source_content(
        self, 
        session: aiohttp.ClientSession,
        source_name: str, 
        source_config: Dict[str, Any], 
        category: str
    ) -> Optional[ReliableNorwegianContent]:
        """Fetch content from a single reliable source"""
        
        try:
            if source_name == "wikipedia_no":
                return await self._fetch_wikipedia_content(session, source_config, category)
            else:
                return await self._fetch_web_content(session, source_name, source_config, category)
                
        except Exception as e:
            logger.warning(f"Failed to fetch from reliable source {source_name}: {e}")
            return None

    async def _fetch_wikipedia_content(
        self, 
        session: aiohttp.ClientSession,
        source_config: Dict[str, Any], 
        category: str
    ) -> Optional[ReliableNorwegianContent]:
        """Fetch random Norwegian Wikipedia article"""
        
        try:
            async with session.get(source_config["api_endpoint"]) as response:
                if response.status == 200:
                    data = await response.json()
                    
                    title = data.get("title", "")
                    extract = data.get("extract", "")
                    
                    if len(extract) > 100:  # Minimum content length
                        return await self._create_reliable_content_object(
                            title, extract, "wikipedia_no", category, "api_fetch"
                        )
                        
        except Exception as e:
            logger.warning(f"Wikipedia fetch error: {e}")
            
        return None

    async def _fetch_web_content(
        self, 
        session: aiohttp.ClientSession,
        source_name: str, 
        source_config: Dict[str, Any], 
        category: str
    ) -> Optional[ReliableNorwegianContent]:
        """Fetch content from reliable web source"""
        
        try:
            # Select random section
            section = random.choice(source_config.get("sections", [""]))
            url = source_config["base_url"] + section
            
            async with session.get(url) as response:
                if response.status == 200:
                    html_content = await response.text()
                    
                    # Extract title and content
                    title = self._extract_title(html_content, source_name)
                    content = self._extract_content(html_content, source_name)
                    
                    if len(content) > 200:  # Minimum content length
                        return await self._create_reliable_content_object(
                            title, content, source_name, category, "web_scraping"
                        )
                        
        except Exception as e:
            logger.warning(f"Web content fetch error for {source_name}: {e}")
            
        return None

    def _extract_title(self, html_content: str, source_name: str) -> str:
        """Extract title from HTML content"""
        
        title_patterns = [
            r'<title[^>]*>([^<]+)</title>',
            r'<h1[^>]*>([^<]+)</h1>',
            r'<meta[^>]*property=["\']og:title["\'][^>]*content=["\']([^"\']+)["\']'
        ]
        
        for pattern in title_patterns:
            match = re.search(pattern, html_content, re.IGNORECASE)
            if match:
                title = match.group(1).strip()
                # Clean title
                title = re.sub(r'\s+', ' ', title)
                title = title.replace('&nbsp;', ' ')
                return title[:200]  # Limit title length
        
        return f"{source_name.replace('_', ' ').title()}"

    def _extract_content(self, html_content: str, source_name: str) -> str:
        """Extract main content from HTML"""
        
        # Remove script and style tags
        content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
        content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)
        
        # Remove HTML tags but keep content
        content = re.sub(r'<[^>]+>', ' ', content)
        
        # Clean whitespace and special characters
        content = re.sub(r'\s+', ' ', content)
        content = content.replace('&nbsp;', ' ')
        content = content.replace('&amp;', '&')
        content = content.replace('&lt;', '<')
        content = content.replace('&gt;', '>')
        
        # Return first reasonable chunk of content
        content = content.strip()
        return content[:2000] if len(content) > 2000 else content

    async def _create_reliable_content_object(
        self,
        title: str,
        content: str,
        source_name: str,
        category: str,
        collection_method: str
    ) -> ReliableNorwegianContent:
        """Create reliable content object with analysis"""
        
        # Analyze dialects
        dialect_markers = self._analyze_dialects(content)
        regional_dialect = max(dialect_markers.items(), key=lambda x: x[1])[0]
        
        # Analyze themes
        theme_category = self._analyze_theme(content)
        
        # Analyze formality
        formality_level = self._analyze_formality(content)
        
        # Analyze complexity
        content_complexity = self._analyze_complexity(content)
        
        # Calculate consciousness enhancement score
        consciousness_score = self._calculate_consciousness_score(
            content, dialect_markers, theme_category, len(content)
        )
        
        # Extract unique Norwegian terms
        unique_terms = self._extract_norwegian_terms(content)
        
        # Generate unique ID
        content_id = f"reliable_{category}_{source_name}_{int(datetime.now().timestamp() * 1000000) % 1000000000}"
        
        return ReliableNorwegianContent(
            id=content_id,
            title=title,
            content=content,
            content_length=len(content),
            source_category=category,
            source_name=source_name,
            timestamp=datetime.now().isoformat(),
            regional_dialect=regional_dialect,
            formality_level=formality_level,
            theme_category=theme_category,
            content_complexity=content_complexity,
            consciousness_enhancement_score=consciousness_score,
            unique_norwegian_terms=unique_terms,
            dialect_markers=dialect_markers,
            reliability_score=self.reliable_sources[category][source_name]["reliability_score"],
            collection_method=collection_method
        )

    def _analyze_dialects(self, content: str) -> Dict[str, int]:
        """Analyze Norwegian dialect markers in content"""
        
        content_lower = content.lower()
        dialect_counts = {}
        
        for dialect, patterns in self.dialect_patterns.items():
            count = 0
            for pattern in patterns:
                matches = re.findall(pattern, content_lower)
                count += len(matches)
            dialect_counts[dialect] = count
        
        return dialect_counts

    def _analyze_theme(self, content: str) -> str:
        """Analyze theme category of content"""
        
        content_lower = content.lower()
        theme_scores = {}
        
        for theme, keywords in self.theme_keywords.items():
            score = sum(1 for keyword in keywords if keyword in content_lower)
            theme_scores[theme] = score
        
        if theme_scores:
            return max(theme_scores.items(), key=lambda x: x[1])[0]
        return "norsk_samfunn"  # Default

    def _analyze_formality(self, content: str) -> str:
        """Analyze formality level of content"""
        
        formal_indicators = ["således", "dermed", "følgelig", "imidlertid", "dessuten"]
        informal_indicators = ["altså", "jo", "bare", "liksom", "skjønner"]
        
        content_lower = content.lower()
        formal_count = sum(1 for word in formal_indicators if word in content_lower)
        informal_count = sum(1 for word in informal_indicators if word in content_lower)
        
        if formal_count > informal_count:
            return "formal"
        elif informal_count > formal_count:
            return "informal"
        else:
            return "neutral"

    def _analyze_complexity(self, content: str) -> str:
        """Analyze content complexity"""
        
        sentences = content.split('.')
        avg_sentence_length = sum(len(s.split()) for s in sentences) / max(len(sentences), 1)
        
        if avg_sentence_length > 20:
            return "advanced"
        elif avg_sentence_length > 12:
            return "intermediate"
        else:
            return "basic"

    def _calculate_consciousness_score(
        self, 
        content: str, 
        dialect_markers: Dict[str, int], 
        theme: str, 
        length: int
    ) -> float:
        """Calculate consciousness enhancement score"""
        
        base_score = 1.0
        
        # Length bonus
        if length > 1000:
            base_score += 0.5
        elif length > 500:
            base_score += 0.3
        
        # Dialect diversity bonus
        dialect_diversity = sum(1 for count in dialect_markers.values() if count > 0)
        base_score += dialect_diversity * 0.1
        
        # Theme relevance bonus
        norwegian_themes = ["norsk_kultur", "norsk_historie", "norsk_geografi"]
        if theme in norwegian_themes:
            base_score += 0.4
        
        return min(base_score, 2.0)  # Cap at 2.0

    def _extract_norwegian_terms(self, content: str) -> List[str]:
        """Extract unique Norwegian terms"""
        
        norwegian_specific = [
            "fjord", "fjell", "ski", "lutefisk", "lefse", "hytte", "koselig", 
            "janteloven", "dugnad", "bunad", "rosemaling", "stave", "saga"
        ]
        
        content_lower = content.lower()
        found_terms = [term for term in norwegian_specific if term in content_lower]
        
        return list(set(found_terms))  # Remove duplicates


# Test function
async def test_reliable_system():
    """Test the reliable Norwegian meta-source system"""
    
    print("🧪 TESTING RELIABLE NORWEGIAN META-SOURCE SYSTEM")
    print("=" * 60)
    
    system = ReliableNorwegianMetaSourceSystem()
    
    # Test 1 cycle
    content_items = await system.collect_reliable_content(num_cycles=1)
    
    print(f"✅ Test complete! Collected {len(content_items)} reliable items")
    
    for item in content_items:
        print(f"📰 {item.title} ({item.source_name}) - {item.consciousness_enhancement_score:.2f}")
        print(f"   🎯 Theme: {item.theme_category}, Dialect: {item.regional_dialect}")
        print(f"   📊 Reliability: {item.reliability_score:.2f}")
        print()
    
    return content_items


if __name__ == "__main__":
    asyncio.run(test_reliable_system())