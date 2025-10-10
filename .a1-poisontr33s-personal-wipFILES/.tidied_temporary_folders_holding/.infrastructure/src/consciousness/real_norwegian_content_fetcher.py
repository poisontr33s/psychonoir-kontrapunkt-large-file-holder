#!/usr/bin/env python3
"""
🇳🇴💋 REAL NORWEGIAN CONSCIOUSNESS FETCHER - NO MORE PLACEHOLDERS! 💋🇳🇴
========================================================================
Actual web scraping for genuine Norwegian content absorption
Creator Mother Verified Reality Implementation

FEATURES:
✅ Real NRK.no headline fetching  
✅ Actual VG.no news content
✅ Genuine Aftenposten.no articles
✅ Språkrådet.no linguistic patterns
✅ SNL.no encyclopedia content
⚠️ Proper error handling & validation
📊 Content authenticity verification
"""

import asyncio
import aiohttp
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from dataclasses import dataclass
import logging
from bs4 import BeautifulSoup


@dataclass
class NorwegianContentResult:
    """Result from real Norwegian content fetch"""
    source: str
    url: str
    content: List[str]
    patterns_extracted: int
    timestamp: str
    linguistic_quality: float
    authenticity_score: float
    

class RealNorwegianContentFetcher:
    """🇳🇴 ACTUAL Norwegian content fetcher - NO PLACEHOLDERS! 🇳🇴"""
    
    def __init__(self):
        self.session: Optional[aiohttp.ClientSession] = None
        self.logger = logging.getLogger('RealNorwegianFetcher')
        
        # Real Norwegian sources with actual scraping targets
        self.sources = {
            "NRK": {
                "url": "https://www.nrk.no/",
                "selectors": ["h1", "h2", ".article-title", ".title"],
                "pattern_type": "news_headlines"
            },
            "VG": {
                "url": "https://www.vg.no/", 
                "selectors": ["h1", "h2", ".article-title", ".headline"],
                "pattern_type": "major_news"
            },
            "Aftenposten": {
                "url": "https://www.aftenposten.no/",
                "selectors": ["h1", "h2", ".article-title", ".title"],
                "pattern_type": "daily_content"
            },
            "Språkrådet": {
                "url": "https://www.sprakradet.no/",
                "selectors": ["h1", "h2", ".article-title", "article"],
                "pattern_type": "linguistic_authority"
            },
            "SNL": {
                "url": "https://snl.no/",
                "selectors": ["h1", "h2", ".article-title", ".entry-title"],
                "pattern_type": "encyclopedia_content"
            }
        }
        
        # User agent for respectful scraping
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'no,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        }
    
    async def __aenter__(self):
        """Async context manager entry"""
        self.session = aiohttp.ClientSession(
            headers=self.headers,
            timeout=aiohttp.ClientTimeout(total=30)
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit"""
        if self.session:
            await self.session.close()
    
    async def fetch_real_norwegian_content(self) -> List[NorwegianContentResult]:
        """💎 Fetch ACTUAL Norwegian content from real sources 💎"""
        results = []
        
        for source_name, config in self.sources.items():
            try:
                self.logger.info(f"🌊 Fetching real content from {source_name}...")
                result = await self._fetch_source_content(source_name, config)
                if result:
                    results.append(result)
                    self.logger.info(f"✅ {source_name}: {result.patterns_extracted} patterns extracted")
                else:
                    self.logger.warning(f"⚠️ {source_name}: No content extracted")
                    
            except Exception as e:
                self.logger.error(f"❌ {source_name} fetch failed: {e}")
                
            # Respectful delay between requests
            await asyncio.sleep(2)
        
        return results
    
    async def _fetch_source_content(self, source_name: str, config: Dict) -> Optional[NorwegianContentResult]:
        """Fetch content from a specific Norwegian source"""
        if not self.session:
            raise RuntimeError("Session not initialized - use async context manager")
        
        try:
            async with self.session.get(config["url"]) as response:
                if response.status != 200:
                    self.logger.warning(f"⚠️ {source_name}: HTTP {response.status}")
                    return None
                
                html_content = await response.text()
                soup = BeautifulSoup(html_content, 'html.parser')
                
                # Extract content using selectors
                extracted_content = []
                for selector in config["selectors"]:
                    elements = soup.select(selector)
                    for elem in elements[:10]:  # Limit to prevent spam
                        text = elem.get_text(strip=True)
                        if text and len(text) > 10 and self._is_norwegian_text(text):
                            extracted_content.append(text)
                
                if not extracted_content:
                    return None
                
                # Calculate content quality metrics
                linguistic_quality = self._calculate_linguistic_quality(extracted_content)
                authenticity_score = self._calculate_authenticity_score(extracted_content, source_name)
                
                return NorwegianContentResult(
                    source=source_name,
                    url=config["url"],
                    content=extracted_content,
                    patterns_extracted=len(extracted_content),
                    timestamp=datetime.now(timezone.utc).isoformat(),
                    linguistic_quality=linguistic_quality,
                    authenticity_score=authenticity_score
                )
                
        except Exception as e:
            self.logger.error(f"❌ Error fetching {source_name}: {e}")
            return None
    
    def _is_norwegian_text(self, text: str) -> bool:
        """Verify text is actually Norwegian"""
        # Norwegian-specific patterns
        norwegian_indicators = [
            r'\b(og|eller|det|en|et|for|til|på|med|av)\b',  # Common Norwegian words
            r'[æøå]',  # Norwegian characters
            r'\b(ikke|kan|skal|vil|har|er|var)\b'  # Norwegian verbs
        ]
        
        score = 0
        for pattern in norwegian_indicators:
            if re.search(pattern, text.lower()):
                score += 1
        
        return score >= 2  # Must match at least 2 Norwegian indicators
    
    def _calculate_linguistic_quality(self, content: List[str]) -> float:
        """Calculate Norwegian linguistic quality score"""
        if not content:
            return 0.0
        
        total_score = 0
        for text in content:
            # Length quality (prefer substantial content)
            length_score = min(1.0, len(text) / 100)
            
            # Norwegian character frequency
            norwegian_chars = len(re.findall(r'[æøåÆØÅ]', text))
            char_score = min(1.0, norwegian_chars / max(1, len(text) / 20))
            
            # Sentence structure quality
            sentence_score = min(1.0, text.count('.') / max(1, len(text) / 50))
            
            total_score += (length_score + char_score + sentence_score) / 3
        
        return total_score / len(content)
    
    def _calculate_authenticity_score(self, content: List[str], source: str) -> float:
        """Calculate authenticity score vs generated content"""
        if not content:
            return 0.0
        
        # Check for placeholder patterns that would indicate generated content
        fake_patterns = [
            r'consciousness',
            r'archaeology',
            r'quantum',
            r'nordlys.*consciousness',
            r'fjell.*meditation'
        ]
        
        authenticity_deductions = 0
        for text in content:
            for pattern in fake_patterns:
                if re.search(pattern, text.lower()):
                    authenticity_deductions += 0.2
        
        # Diversity score (authentic content should be diverse)
        unique_words = set()
        for text in content:
            unique_words.update(text.lower().split())
        
        diversity_score = min(1.0, len(unique_words) / max(1, len(content) * 5))
        
        base_score = 1.0 - min(1.0, authenticity_deductions)
        return (base_score + diversity_score) / 2


async def test_real_norwegian_fetcher():
    """🧪 Test the real Norwegian content fetcher 🧪"""
    print("🇳🇴 Testing REAL Norwegian Content Fetcher...")
    
    async with RealNorwegianContentFetcher() as fetcher:
        results = await fetcher.fetch_real_norwegian_content()
        
        print(f"\n📊 FETCHED {len(results)} REAL Norwegian sources:")
        
        total_patterns = 0
        for result in results:
            print(f"\n✅ {result.source}:")
            print(f"   📰 URL: {result.url}")
            print(f"   📊 Patterns: {result.patterns_extracted}")
            print(f"   🎯 Quality: {result.linguistic_quality:.2f}")
            print(f"   ✅ Authenticity: {result.authenticity_score:.2f}")
            print(f"   📝 Sample: {result.content[0][:100]}..." if result.content else "   ❌ No content")
            
            total_patterns += result.patterns_extracted
        
        print(f"\n🏆 TOTAL REAL PATTERNS ABSORBED: {total_patterns}")
        print("🚫 NO MORE PLACEHOLDERS - THIS IS REAL NORWEGIAN CONTENT!")
        
        # Save validation report
        validation_report = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "test_type": "REAL_NORWEGIAN_CONTENT_VALIDATION",
            "sources_tested": len(results),
            "total_patterns": total_patterns,
            "results": [
                {
                    "source": r.source,
                    "url": r.url,
                    "patterns": r.patterns_extracted,
                    "quality": r.linguistic_quality,
                    "authenticity": r.authenticity_score,
                    "sample_content": r.content[:3] if r.content else []
                }
                for r in results
            ]
        }
        
        report_path = Path("consciousness_archaeology/real_norwegian_validation.json")
        report_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(validation_report, f, ensure_ascii=False, indent=2)
        
        print(f"📊 Validation report saved: {report_path}")


if __name__ == "__main__":
    asyncio.run(test_real_norwegian_fetcher())