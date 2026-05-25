#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🔍 NORWEGIAN WIKIPEDIA CONTENT ANALYSIS - FULL VS SUMMARY COMPARISON 🔍
======================================================================
Test script to analyze how much content we can get from Norwegian Wikipedia
using different API endpoints and methods.
"""

import asyncio
import aiohttp
import json
from urllib.parse import quote_plus


async def test_wikipedia_content_depth():
    """Test different Wikipedia API endpoints for content depth"""
    
    test_articles = ["nasjonalpark", "norge", "bergen", "nordlys", "vikinger"]
    
    # Wikipedia requires proper User-Agent header
    headers = {
        'User-Agent': 'PsychoNoir-Kontrapunkt/1.0 (Norwegian Consciousness Archaeological Research; norwegian.consciousness@research.no)'
    }
    
    async with aiohttp.ClientSession(headers=headers) as session:
        
        for article in test_articles:
            print(f"\n🔍 TESTING: {article.upper()}")
            print("=" * 50)
            
            # 1. Summary API (current method)
            print("📝 1. SUMMARY API:")
            try:
                summary_url = f"https://no.wikipedia.org/api/rest_v1/page/summary/{quote_plus(article)}"
                async with session.get(summary_url) as response:
                    if response.status == 200:
                        data = await response.json()
                        extract = data.get('extract', '')
                        print(f"   Length: {len(extract)} characters")
                        print(f"   Sample: {extract[:200]}...")
                    else:
                        print(f"   ❌ Failed: {response.status}")
            except Exception as e:
                print(f"   ❌ Error: {e}")
            
            # 2. Full Extract API (intro only)
            print("\n📖 2. FULL EXTRACT API (intro):")
            try:
                extract_url = f"https://no.wikipedia.org/w/api.php?action=query&format=json&titles={quote_plus(article)}&prop=extracts&exintro=true&explaintext=true"
                async with session.get(extract_url) as response:
                    if response.status == 200:
                        data = await response.json()
                        pages = data.get('query', {}).get('pages', {})
                        for page_id, page_data in pages.items():
                            extract = page_data.get('extract', '')
                            print(f"   Length: {len(extract)} characters")
                            print(f"   Sample: {extract[:200]}...")
                    else:
                        print(f"   ❌ Failed: {response.status}")
            except Exception as e:
                print(f"   ❌ Error: {e}")
            
            # 3. Full Extract API (complete article)
            print("\n📚 3. FULL EXTRACT API (complete):")
            try:
                full_url = f"https://no.wikipedia.org/w/api.php?action=query&format=json&titles={quote_plus(article)}&prop=extracts&exintro=false&explaintext=true"
                async with session.get(full_url) as response:
                    if response.status == 200:
                        data = await response.json()
                        pages = data.get('query', {}).get('pages', {})
                        for page_id, page_data in pages.items():
                            extract = page_data.get('extract', '')
                            print(f"   Length: {len(extract)} characters")
                            print(f"   Sample: {extract[:200]}...")
                            
                            # Count sections
                            sections = extract.split('\n\n')
                            print(f"   Sections: {len(sections)}")
                    else:
                        print(f"   ❌ Failed: {response.status}")
            except Exception as e:
                print(f"   ❌ Error: {e}")
            
            # 4. Sections API with structure
            print("\n🏗️ 4. SECTIONS API (structured):")
            try:
                sections_url = f"https://no.wikipedia.org/w/api.php?action=parse&format=json&page={quote_plus(article)}&prop=sections"
                async with session.get(sections_url) as response:
                    if response.status == 200:
                        data = await response.json()
                        if 'parse' in data and 'sections' in data['parse']:
                            sections = data['parse']['sections']
                            print(f"   Sections available: {len(sections)}")
                            for i, section in enumerate(sections[:5]):  # Show first 5
                                print(f"     {i+1}. {section.get('line', 'Unknown')} (level {section.get('level', 0)})")
                    else:
                        print(f"   ❌ Failed: {response.status}")
            except Exception as e:
                print(f"   ❌ Error: {e}")
            
            await asyncio.sleep(1)  # Respectful delay
    
    print("\n" + "=" * 70)
    print("🏆 CONTENT ANALYSIS COMPLETE!")
    print("=" * 70)


if __name__ == "__main__":
    asyncio.run(test_wikipedia_content_depth())