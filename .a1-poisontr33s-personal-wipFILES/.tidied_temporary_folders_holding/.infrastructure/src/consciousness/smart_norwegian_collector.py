#!/usr/bin/env python3
"""
⚡ SMART NORWEGIAN COLLECTOR - SIMPLE BUT EFFECTIVE ⚡
====================================================
Takes what works, improves it, discards what doesn't.
"""

import asyncio
import aiohttp
import json
import random
import re
from datetime import datetime
from pathlib import Path


class SmartNorwegianCollector:
    """Smart but simple Norwegian collector"""
    
    def __init__(self):
        # Only sources that actually work
        self.sources = {
            "nrk": ["https://www.nrk.no/nyheter", "https://www.nrk.no/kultur"],
            "bt": ["https://www.bt.no/nyheter", "https://www.bt.no/kultur"],
            "wikipedia": ["https://no.wikipedia.org/wiki/Special:Random"]
        }
        
        self.output_dir = Path("smart_collection")
        self.output_dir.mkdir(exist_ok=True)
        print("⚡ Smart Norwegian Collector initialized")

    async def smart_collect(self, duration_minutes: int = 10):
        """Smart collection with variety and quality"""
        
        print(f"🎯 Smart collecting for {duration_minutes} minutes...")
        
        collected = []
        start_time = datetime.now()
        iteration = 0
        
        async with aiohttp.ClientSession() as session:
            while (datetime.now() - start_time).seconds < duration_minutes * 60:
                iteration += 1
                
                # Rotate through all source types for variety
                for source_type, urls in self.sources.items():
                    url = random.choice(urls)
                    
                    try:
                        async with session.get(url, timeout=15) as response:
                            if response.status == 200:
                                content = await response.text()
                                
                                # Smart content extraction
                                item = self._extract_smart_content(content, url, source_type)
                                
                                if item and item["quality_score"] > 0.5:
                                    collected.append(item)
                                    print(f"✅ [{source_type}] {item['title'][:60]}... (score: {item['quality_score']:.2f})")
                                
                    except Exception as e:
                        print(f"⚠️  {source_type} error: {str(e)[:50]}...")
                    
                    # Smart delay - shorter for variety
                    await asyncio.sleep(random.uniform(10, 20))
                
                print(f"🔄 Iteration {iteration} complete, collected {len(collected)} items")
                
                # Break if we have enough quality content
                if len(collected) >= duration_minutes:
                    break
        
        # Save with smart analysis
        results = self._analyze_and_save(collected, duration_minutes)
        return results

    def _extract_smart_content(self, html_content: str, url: str, source_type: str) -> dict:
        """Smart content extraction"""
        
        # Extract title
        title_match = re.search(r'<title[^>]*>([^<]+)</title>', html_content, re.IGNORECASE)
        title = title_match.group(1).strip() if title_match else "Untitled"
        
        # Clean title
        title = re.sub(r'\s+', ' ', title)
        title = title.replace('&nbsp;', ' ').replace('–', '-')
        
        # Extract Norwegian content indicators
        norwegian_indicators = self._count_norwegian_indicators(html_content)
        
        # Quality scoring
        quality_score = self._calculate_quality_score(html_content, title, norwegian_indicators)
        
        return {
            "timestamp": datetime.now().isoformat(),
            "source_url": url,
            "source_type": source_type,
            "title": title,
            "content_length": len(html_content),
            "norwegian_indicators": norwegian_indicators,
            "quality_score": quality_score,
            "success": True
        }

    def _count_norwegian_indicators(self, content: str) -> dict:
        """Count Norwegian language indicators"""
        
        content_lower = content.lower()
        
        indicators = {
            "norwegian_words": len(re.findall(r'\b(og|eller|men|det|som|ikke|har|er|var|blir|skal|kan|vil|må)\b', content_lower)),
            "norwegian_places": len(re.findall(r'\b(norge|oslo|bergen|trondheim|stavanger|tromsø|kristiansand)\b', content_lower)),
            "norwegian_endings": len(re.findall(r'\w+(en|et|ene|tion|sjon)\b', content_lower)),
            "scandinavian_chars": len(re.findall(r'[æøå]', content_lower))
        }
        
        return indicators

    def _calculate_quality_score(self, content: str, title: str, indicators: dict) -> float:
        """Calculate content quality score"""
        
        score = 0.0
        
        # Length bonus (but not too much)
        if 1000 < len(content) < 50000:
            score += 0.3
        
        # Norwegian indicators bonus
        total_indicators = sum(indicators.values())
        if total_indicators > 10:
            score += 0.4
        elif total_indicators > 5:
            score += 0.2
        
        # Title quality
        if len(title) > 10 and len(title) < 100:
            score += 0.2
        
        # Avoid empty or error pages
        if "error" in title.lower() or "404" in title or len(content) < 500:
            score = 0.1
        
        return min(score, 1.0)

    def _analyze_and_save(self, collected: list, duration: int) -> dict:
        """Analyze results and save"""
        
        # Analysis
        total_items = len(collected)
        avg_quality = sum(item["quality_score"] for item in collected) / max(total_items, 1)
        source_breakdown = {}
        
        for item in collected:
            source = item["source_type"]
            source_breakdown[source] = source_breakdown.get(source, 0) + 1
        
        results = {
            "collection_summary": {
                "timestamp": datetime.now().isoformat(),
                "duration_minutes": duration,
                "total_items_collected": total_items,
                "average_quality_score": round(avg_quality, 2),
                "source_breakdown": source_breakdown,
                "success_rate": f"{(total_items/max(duration*3, 1)*100):.1f}%"
            },
            "collected_items": collected
        }
        
        # Save to file
        output_file = self.output_dir / f"smart_collection_{int(datetime.now().timestamp())}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        # Print summary
        print("\n📊 COLLECTION COMPLETE")
        print("=" * 40)
        print(f"✅ Items collected: {total_items}")
        print(f"📈 Average quality: {avg_quality:.2f}")
        print(f"📁 Saved to: {output_file.name}")
        print(f"🎯 Sources used: {', '.join(source_breakdown.keys())}")
        print()
        
        return results


async def main():
    """Simple main function"""
    
    print("⚡ SMART NORWEGIAN COLLECTOR")
    print("=" * 40)
    print("Simple but effective Norwegian content collection")
    print()
    
    collector = SmartNorwegianCollector()
    
    print("Duration options:")
    print("1. Quick (5 minutes)")
    print("2. Normal (15 minutes)")
    print("3. Extended (30 minutes)")
    print("4. Custom minutes")
    
    choice = input("Choose (1-4): ").strip()
    
    if choice == "1":
        results = await collector.smart_collect(5)
    elif choice == "2":
        results = await collector.smart_collect(15)
    elif choice == "3":
        results = await collector.smart_collect(30)
    elif choice == "4":
        minutes = int(input("Enter minutes: "))
        results = await collector.smart_collect(minutes)
    else:
        print("❌ Invalid choice")
        return
    
    print(f"🎉 Collection finished! Quality score: {results['collection_summary']['average_quality_score']}")


if __name__ == "__main__":
    asyncio.run(main())