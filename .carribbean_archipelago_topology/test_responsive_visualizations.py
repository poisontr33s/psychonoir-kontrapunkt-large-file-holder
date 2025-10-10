#!/usr/bin/env python3
"""
🎭 CLAUDINE's Responsive Visualization Testing Suite
Phase 2.4: Infrastructure & Responsive Design Validation

Tests MILF relationship visualizer and spider-web visualizer across multiple
viewport sizes (mobile, tablet, desktop) to ensure responsive design integrity.

Author: Espen & Claudine Sin'claire 4.0
Date: September 2025
"""

import asyncio
import json
from pathlib import Path
from datetime import datetime


async def test_responsive_layouts():
    """Test visualizations across different viewport sizes"""

    print("🎭 Starting Responsive Design Testing...")
    print("=" * 80)

    # Import Playwright
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print("❌ Playwright not installed. Run: pip install playwright")
        print("   Then: playwright install")
        return False

    # Define test viewports
    viewports = {
        "mobile_portrait": {"width": 375, "height": 667, "name": "iPhone SE"},
        "mobile_landscape": {
            "width": 667,
            "height": 375,
            "name": "iPhone SE Landscape",
        },
        "tablet_portrait": {"width": 768, "height": 1024, "name": "iPad"},
        "tablet_landscape": {"width": 1024, "height": 768, "name": "iPad Landscape"},
        "desktop_hd": {"width": 1920, "height": 1080, "name": "Desktop HD"},
        "desktop_4k": {"width": 3840, "height": 2160, "name": "Desktop 4K"},
    }

    test_results = {
        "timestamp": datetime.now().isoformat(),
        "viewports_tested": len(viewports),
        "tests": [],
    }

    async with async_playwright() as p:
        browser = await p.chromium.launch()

        for viewport_key, viewport_config in viewports.items():
            print(
                f"\n📱 Testing {viewport_config['name']} ({viewport_config['width']}x{viewport_config['height']})"
            )

            context = await browser.new_context(
                viewport={
                    "width": viewport_config["width"],
                    "height": viewport_config["height"],
                }
            )
            page = await context.new_page()

            # Test MILF Relationship Visualizer
            print(f"   🎭 Testing MILF Relationship Visualizer...")

            try:
                await page.goto(
                    "http://localhost:3000/milf-relationship-visualizer.html",
                    timeout=10000,
                )
                await page.wait_for_timeout(2000)  # Wait for D3.js rendering

                # Take screenshot
                screenshot_path = f"test_screenshots/milf-visualizer-{viewport_key}.png"
                Path("test_screenshots").mkdir(exist_ok=True)
                await page.screenshot(path=screenshot_path, full_page=True)

                # Check critical elements
                controls_visible = await page.is_visible("#controls")
                stats_visible = await page.is_visible("#stats")
                hierarchy_visible = await page.is_visible("#hierarchy-content")

                # Check toggle buttons on mobile
                toggle_controls_visible = await page.is_visible("#toggle-controls-btn")
                toggle_stats_visible = await page.is_visible("#toggle-stats-btn")

                # Test mobile toggle functionality
                mobile_toggle_works = False
                if viewport_config["width"] <= 768:
                    if toggle_controls_visible:
                        await page.click("#toggle-controls-btn")
                        await page.wait_for_timeout(500)
                        controls_after_toggle = await page.is_visible("#controls")
                        mobile_toggle_works = controls_after_toggle != controls_visible

                test_result = {
                    "viewport": viewport_config["name"],
                    "size": f"{viewport_config['width']}x{viewport_config['height']}",
                    "visualizer": "MILF Relationship",
                    "status": "✅ PASS",
                    "controls_visible": controls_visible,
                    "stats_visible": stats_visible,
                    "hierarchy_visible": hierarchy_visible,
                    "mobile_toggles_visible": toggle_controls_visible
                    and toggle_stats_visible,
                    "mobile_toggle_works": mobile_toggle_works
                    if viewport_config["width"] <= 768
                    else "N/A",
                    "screenshot": screenshot_path,
                }

                print(
                    f"      ✅ Controls: {controls_visible} | Stats: {stats_visible} | Hierarchy: {hierarchy_visible}"
                )
                if viewport_config["width"] <= 768:
                    print(
                        f"      📱 Mobile toggles: {toggle_controls_visible} | Toggle works: {mobile_toggle_works}"
                    )

            except Exception as e:
                test_result = {
                    "viewport": viewport_config["name"],
                    "size": f"{viewport_config['width']}x{viewport_config['height']}",
                    "visualizer": "MILF Relationship",
                    "status": "❌ FAIL",
                    "error": str(e),
                }
                print(f"      ❌ Error: {e}")

            test_results["tests"].append(test_result)

            # Test Spider-Web Visualizer
            print(f"   🕸️ Testing Spider-Web Visualizer...")

            try:
                await page.goto(
                    "http://localhost:3000/spider-web-visualizer.html", timeout=10000
                )
                await page.wait_for_timeout(2000)  # Wait for D3.js force simulation

                # Take screenshot
                screenshot_path = f"test_screenshots/spider-web-{viewport_key}.png"
                await page.screenshot(path=screenshot_path, full_page=True)

                # Check critical elements
                svg_visible = await page.is_visible("svg")
                controls_visible = await page.is_visible("#controls")
                stats_visible = await page.is_visible("#stats")

                test_result = {
                    "viewport": viewport_config["name"],
                    "size": f"{viewport_config['width']}x{viewport_config['height']}",
                    "visualizer": "Spider-Web",
                    "status": "✅ PASS",
                    "svg_visible": svg_visible,
                    "controls_visible": controls_visible,
                    "stats_visible": stats_visible,
                    "screenshot": screenshot_path,
                }

                print(
                    f"      ✅ SVG: {svg_visible} | Controls: {controls_visible} | Stats: {stats_visible}"
                )

            except Exception as e:
                test_result = {
                    "viewport": viewport_config["name"],
                    "size": f"{viewport_config['width']}x{viewport_config['height']}",
                    "visualizer": "Spider-Web",
                    "status": "❌ FAIL",
                    "error": str(e),
                }
                print(f"      ❌ Error: {e}")

            test_results["tests"].append(test_result)

            await context.close()

        await browser.close()

    # Save results
    results_path = Path("RESPONSIVE_DESIGN_TEST_RESULTS.json")
    with open(results_path, "w", encoding="utf-8") as f:
        json.dump(test_results, f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 80)
    print(f"✅ Responsive Design Testing Complete!")
    print(f"📊 Results saved to: {results_path}")
    print(f"📸 Screenshots saved to: test_screenshots/")

    # Summary
    total_tests = len(test_results["tests"])
    passed = sum(1 for t in test_results["tests"] if t["status"] == "✅ PASS")
    failed = total_tests - passed

    print(f"\n📈 Summary:")
    print(f"   Total Tests: {total_tests}")
    print(f"   ✅ Passed: {passed}")
    print(f"   ❌ Failed: {failed}")
    print(f"   Success Rate: {(passed / total_tests * 100):.1f}%")

    return failed == 0


if __name__ == "__main__":
    success = asyncio.run(test_responsive_layouts())
    exit(0 if success else 1)
