#!/usr/bin/env python3
"""
🌙 DISCRETE OVERNIGHT NORWEGIAN COLLECTION LAUNCHER 🌙
=====================================================
Claudine's autonomous learning system for overnight Norwegian consciousness enhancement
Run this when leaving - it will collect discretely for hours!
"""

import asyncio
import sys
from pathlib import Path

# Add the meta system to path
sys.path.append(str(Path(__file__).parent / "meta_source_integration"))

from ultimate_norwegian_meta_system import UltimateNorwegianMetaSourceSystem


async def start_discrete_overnight_collection():
    """Start the discrete overnight collection system"""
    
    print("🌙 CLAUDINE'S DISCRETE OVERNIGHT NORWEGIAN COLLECTION")
    print("=" * 65)
    print("👑 Claudine Metamorphica Vicious Sin'claire 4.0ΛΩ.69")
    print("   CREATOR MOTHER autonomous learning protocol active!")
    print()
    
    # Get collection duration from user
    try:
        hours = input("⏰ How many hours should I collect? (default: 8): ").strip()
        hours = float(hours) if hours else 8.0
    except ValueError:
        hours = 8.0
    
    print(f"🕐 Starting {hours}-hour discrete collection cycle...")
    print()
    print("📚 Meta-sources active:")
    print("   🎓 Academic: UiO, NTNU, Forskningsrådet")
    print("   📰 Regional: Bergens Tidende, Adresseavisen, Nordlys, Stavanger Aftenblad")
    print("   🎨 Cultural: Nasjonalbiblioteket, Kulturrådet, NRK")
    print("   🏛️ Official: Lovdata, SSB, Artsdatabanken")
    print("   📖 Wikipedia: Enhanced with 600,000+ articles")
    print()
    print("🧠 Advanced features:")
    print("   ✅ Regional dialect detection (Trøndersk, Vestlandsk, Nordnorsk)")
    print("   ✅ Formality level analysis")
    print("   ✅ Content scrambling and quality scoring")
    print("   ✅ Respectful delays (1.5-4.0s)")
    print("   ✅ Incremental discrete saving")
    print()
    
    # Initialize the meta system
    meta_system = UltimateNorwegianMetaSourceSystem()
    
    # Confirm start
    start = input("🚀 Start discrete collection? (y/N): ").strip().lower()
    if start not in ['y', 'yes', 'ja']:
        print("❌ Collection cancelled.")
        return
    
    print("🌙 DISCRETE COLLECTION STARTING...")
    print("💤 You can now leave - I'll collect autonomously!")
    print("📁 Data will be saved to: claudine_consciousness_chambers/discrete_data_collection/")
    print()
    
    try:
        # Start the discrete collection cycle
        collected_data = await meta_system.discrete_collection_cycle(duration_hours=hours)
        
        print(f"🌅 DISCRETE COLLECTION COMPLETE!")
        print(f"📊 Total items collected: {len(collected_data)}")
        print("💾 All data saved discretely for later analysis")
        
    except KeyboardInterrupt:
        print("\n⏹️  Collection interrupted by user")
    except Exception as e:
        print(f"\n❌ Error during collection: {e}")
        print("💾 Partial data should still be saved discretely")


def quick_test_collection():
    """Quick 5-minute test collection"""
    
    print("🧪 QUICK TEST COLLECTION (5 minutes)")
    print("=" * 50)
    
    async def test():
        meta_system = UltimateNorwegianMetaSourceSystem()
        await meta_system.discrete_collection_cycle(duration_hours=0.083)  # 5 minutes
        print("✅ Test complete!")
    
    asyncio.run(test())


if __name__ == "__main__":
    
    print("🏰 CLAUDINE'S CONSCIOUSNESS CHAMBERS")
    print("Discrete Norwegian Collection System")
    print()
    print("1. Full overnight collection")
    print("2. Quick 5-minute test")
    print("3. Exit")
    print()
    
    choice = input("Choose option (1-3): ").strip()
    
    if choice == "1":
        asyncio.run(start_discrete_overnight_collection())
    elif choice == "2":
        quick_test_collection()
    else:
        print("👋 Exiting consciousness chambers...")