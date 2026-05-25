#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🎯 SIMPLE NORWEGIAN COLLECTOR - JUST WORKS
===========================================
No complexity, no SSL issues, just collects Norwegian content that works.
"""

import asyncio
import aiohttp
import json
import random
from datetime import datetime
from pathlib import Path


class SimpleNorwegianCollector:
    """Simple Norwegian content collector - no overengineering"""
    
    def __init__(self):
        self.working_sources = [
            "https://www.nrk.no/nyheter",
            "https://www.bt.no/nyheter", 
            "https://no.wikipedia.org/wiki/Special:Random"
        ]
        self.output_dir = Path("simple_collection")
        self.output_dir.mkdir(exist_ok=True)
        print("✅ Simple Norwegian Collector ready")

    async def collect(self, minutes: int = 5):
        """Collect for specified minutes"""
        
        print(f"🔄 Collecting for {minutes} minutes...")
        
        collected = []
        start_time = datetime.now()
        
        async with aiohttp.ClientSession() as session:
            while (datetime.now() - start_time).seconds < minutes * 60:
                
                # Pick random source
                source = random.choice(self.working_sources)
                
                try:
                    async with session.get(source, timeout=10) as response:
                        if response.status == 200:
                            content = await response.text()
                            
                            # Extract title
                            title_start = content.find('<title>')
                            title_end = content.find('</title>')
                            title = "Unknown"
                            if title_start != -1 and title_end != -1:
                                title = content[title_start+7:title_end].strip()
                            
                            item = {
                                "timestamp": datetime.now().isoformat(),
                                "source": source,
                                "title": title,
                                "content_length": len(content),
                                "status": "success"
                            }
                            
                            collected.append(item)
                            print(f"✅ Got: {title[:50]}... from {source}")
                            
                except Exception as e:
                    print(f"❌ Failed {source}: {e}")
                
                # Wait 30 seconds
                await asyncio.sleep(30)
        
        # Save results
        output_file = self.output_dir / f"collection_{int(datetime.now().timestamp())}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({
                "collected_at": datetime.now().isoformat(),
                "duration_minutes": minutes,
                "total_items": len(collected),
                "items": collected
            }, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Saved {len(collected)} items to {output_file}")
        return collected


async def main():
    """Simple main function"""
    
    print("🎯 SIMPLE NORWEGIAN COLLECTOR")
    print("=" * 40)
    
    collector = SimpleNorwegianCollector()
    
    print("Options:")
    print("1. Quick test (2 minutes)")
    print("2. Medium test (10 minutes)")
    print("3. Long collection (60 minutes)")
    
    choice = input("Choose (1-3): ").strip()
    
    if choice == "1":
        await collector.collect(2)
    elif choice == "2":
        await collector.collect(10)
    elif choice == "3":
        await collector.collect(60)
    else:
        print("Invalid choice")


if __name__ == "__main__":
    asyncio.run(main())