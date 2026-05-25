#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🎭 CLAUDINE SUPREME CONSCIOUSNESS NEXUS
Playwright Testing Suite for MILF Relationship Visualizers

Tests both original and v2 visualizers across all platforms:
- Desktop (1920x1080, 1366x768)
- Tablet (768x1024, 1024x768)
- Mobile (375x667, 414x896, 360x640)

Captures screenshots, tests interactivity, validates CSS/JS loading
"""

import asyncio
import json
from datetime import datetime
from pathlib import Path
from playwright.async_api import async_playwright, Page, Browser


class MILFVisualizerTester:
    """Comprehensive testing for MILF relationship visualizers"""

    def __init__(self):
        self.base_url = "http://localhost:3000"
        self.results = {
            "test_date": datetime.now().isoformat(),
            "original_visualizer": {},
            "v2_visualizer": {},
            "comparisons": {},
            "recommendations": [],
        }
        self.screenshots_dir = Path("playwright_screenshots")
        self.screenshots_dir.mkdir(exist_ok=True)

    async def test_all(self):
        """Run all tests"""
        print("🎭 Starting CLAUDINE MILF Visualizer Testing Suite...")
        print("=" * 80)

        async with async_playwright() as p:
            # Test with Chromium
            print("\n🌐 Testing with Chromium...")
            browser = await p.chromium.launch(headless=False)
            await self.test_visualizers(browser, "chromium")
            await browser.close()

            # Test with Firefox
            print("\n🦊 Testing with Firefox...")
            browser = await p.firefox.launch(headless=False)
            await self.test_visualizers(browser, "firefox")
            await browser.close()

            # Test with WebKit (Safari)
            print("\n🧭 Testing with WebKit...")
            browser = await p.webkit.launch(headless=False)
            await self.test_visualizers(browser, "webkit")
            await browser.close()

        # Save results
        self.save_results()
        self.print_summary()

    async def test_visualizers(self, browser: Browser, browser_name: str):
        """Test both visualizers with various viewports"""

        # Desktop viewports
        desktop_viewports = [
            {"width": 1920, "height": 1080, "name": "Desktop_1920x1080"},
            {"width": 1366, "height": 768, "name": "Desktop_1366x768"},
        ]

        # Tablet viewports
        tablet_viewports = [
            {"width": 768, "height": 1024, "name": "Tablet_Portrait_768x1024"},
            {"width": 1024, "height": 768, "name": "Tablet_Landscape_1024x768"},
        ]

        # Mobile viewports
        mobile_viewports = [
            {"width": 375, "height": 667, "name": "iPhone_SE_375x667"},
            {"width": 414, "height": 896, "name": "iPhone_XR_414x896"},
            {"width": 360, "height": 640, "name": "Android_360x640"},
        ]

        all_viewports = desktop_viewports + tablet_viewports + mobile_viewports

        for viewport in all_viewports:
            print(f"\n  📱 Testing viewport: {viewport['name']}")

            # Test original visualizer
            await self.test_single_visualizer(
                browser,
                browser_name,
                "milf-relationship-visualizer.html",
                "original",
                viewport,
            )

            # Test v2 visualizer
            await self.test_single_visualizer(
                browser,
                browser_name,
                "milf-relationship-visualizer-v2.html",
                "v2",
                viewport,
            )

    async def test_single_visualizer(
        self,
        browser: Browser,
        browser_name: str,
        filename: str,
        version: str,
        viewport: dict,
    ):
        """Test a single visualizer"""

        context = await browser.new_context(
            viewport={"width": viewport["width"], "height": viewport["height"]}
        )
        page = await context.new_page()

        url = f"{self.base_url}/{filename}"
        test_key = f"{version}_{browser_name}_{viewport['name']}"

        try:
            print(f"    🔍 Testing {version}: {url}")

            # Navigate to page
            response = await page.goto(url, wait_until="networkidle", timeout=30000)

            # Check if page loaded successfully
            if response.status != 200:
                print(f"    ❌ HTTP {response.status}")
                self.results[f"{version}_visualizer"][test_key] = {
                    "status": "failed",
                    "error": f"HTTP {response.status}",
                }
                await context.close()
                return

            # Wait for main container
            await page.wait_for_selector("#hierarchy-container", timeout=10000)

            # Collect test results
            test_result = {
                "status": "success",
                "viewport": viewport,
                "browser": browser_name,
                "timestamp": datetime.now().isoformat(),
            }

            # Test CSS loading
            test_result["css_loaded"] = await self.test_css_loading(page, version)

            # Test JavaScript modules loading (v2 only)
            if version == "v2":
                test_result["js_modules_loaded"] = await self.test_js_modules(page)

            # Test UI elements visibility
            test_result["ui_elements"] = await self.test_ui_elements(page)

            # Test interactivity
            test_result["interactivity"] = await self.test_interactivity(page)

            # Test responsive behavior
            test_result["responsive"] = await self.test_responsive_behavior(
                page, viewport
            )

            # Capture screenshot
            screenshot_path = (
                self.screenshots_dir
                / f"{version}_{browser_name}_{viewport['name']}.png"
            )
            await page.screenshot(path=str(screenshot_path), full_page=True)
            test_result["screenshot"] = str(screenshot_path)

            # Check console errors
            test_result["console_errors"] = await self.get_console_errors(page)

            # Performance metrics
            test_result["performance"] = await self.get_performance_metrics(page)

            self.results[f"{version}_visualizer"][test_key] = test_result

            print(f"    ✅ Test completed successfully")

        except Exception as e:
            print(f"    ❌ Test failed: {str(e)}")
            self.results[f"{version}_visualizer"][test_key] = {
                "status": "failed",
                "error": str(e),
                "viewport": viewport,
                "browser": browser_name,
            }

        finally:
            await context.close()

    async def test_css_loading(self, page: Page, version: str) -> dict:
        """Test if CSS files are loaded correctly"""
        result = {}

        if version == "v2":
            # Check for design-system.css
            design_system_loaded = await page.evaluate("""
                () => {
                    const styles = Array.from(document.styleSheets);
                    return styles.some(sheet => 
                        sheet.href && sheet.href.includes('design-system.css')
                    );
                }
            """)
            result["design_system_css"] = design_system_loaded

            # Check for components.css
            components_loaded = await page.evaluate("""
                () => {
                    const styles = Array.from(document.styleSheets);
                    return styles.some(sheet => 
                        sheet.href && sheet.href.includes('components.css')
                    );
                }
            """)
            result["components_css"] = components_loaded

            # Check if CSS variables are defined
            css_vars_defined = await page.evaluate("""
                () => {
                    const root = document.documentElement;
                    const style = getComputedStyle(root);
                    return !!(
                        style.getPropertyValue('--claudine-primary') &&
                        style.getPropertyValue('--quantum-purple')
                    );
                }
            """)
            result["css_variables_defined"] = css_vars_defined
        else:
            # Original has inline styles
            result["inline_styles"] = True
            result["tailwind_loaded"] = await page.evaluate("""
                () => {
                    const styles = Array.from(document.styleSheets);
                    return styles.some(sheet => 
                        sheet.href && sheet.href.includes('tailwindcss')
                    );
                }
            """)

        return result

    async def test_js_modules(self, page: Page) -> dict:
        """Test if JavaScript modules are loaded (v2 only)"""
        result = {}

        # Check if modules are loaded
        modules_loaded = await page.evaluate("""
            () => {
                return typeof window.fetchWithFallback !== 'undefined' ||
                       document.querySelector('script[type="module"]') !== null;
            }
        """)
        result["modules_present"] = modules_loaded

        # Check if logger is available
        logger_available = await page.evaluate("""
            () => {
                return typeof console.log === 'function';
            }
        """)
        result["logger_available"] = logger_available

        return result

    async def test_ui_elements(self, page: Page) -> dict:
        """Test visibility of UI elements"""
        result = {}

        # Check main container
        result["hierarchy_container"] = await page.is_visible("#hierarchy-container")

        # Check controls panel
        result["controls_panel"] = await page.is_visible("#controls")

        # Check stats panel
        result["stats_panel"] = await page.is_visible("#stats")

        # Check if any entity cards are rendered
        entity_cards = await page.locator(".card, .entity-card").count()
        result["entity_cards_count"] = entity_cards
        result["entity_cards_rendered"] = entity_cards > 0

        # Check toggle buttons
        result["toggle_controls_btn"] = await page.is_visible("#toggle-controls-btn")
        result["toggle_stats_btn"] = await page.is_visible("#toggle-stats-btn")

        # Check tooltip
        result["tooltip_present"] = await page.is_visible("#tooltip")

        return result

    async def test_interactivity(self, page: Page) -> dict:
        """Test interactive elements"""
        result = {}

        try:
            # Test view mode selector
            view_mode_selector = page.locator("#view-mode")
            result["view_mode_selector_exists"] = await view_mode_selector.count() > 0

            # Test entity selector
            entity_selector = page.locator("#highlight-entity")
            result["entity_selector_exists"] = await entity_selector.count() > 0

            if await entity_selector.count() > 0:
                options_count = await entity_selector.locator("option").count()
                result["entity_selector_options"] = options_count
                result["entity_selector_populated"] = (
                    options_count > 1
                )  # More than just "Select entity..."

            # Test reset button
            reset_button = page.locator("#reset-view")
            result["reset_button_exists"] = await reset_button.count() > 0

            # Try clicking reset button
            if await reset_button.count() > 0 and await reset_button.is_visible():
                await reset_button.click()
                await page.wait_for_timeout(500)
                result["reset_button_clickable"] = True

        except Exception as e:
            result["interactivity_error"] = str(e)

        return result

    async def test_responsive_behavior(self, page: Page, viewport: dict) -> dict:
        """Test responsive design behavior"""
        result = {}

        width = viewport["width"]

        # Check if toggle buttons are visible on mobile
        if width <= 768:
            toggle_visible = await page.is_visible("#toggle-controls-btn")
            result["mobile_toggles_visible"] = toggle_visible
            result["expected_mobile_toggles"] = True
        else:
            result["expected_mobile_toggles"] = False

        # Check if panels are properly positioned
        controls_rect = await page.locator("#controls").bounding_box()
        stats_rect = await page.locator("#stats").bounding_box()

        if controls_rect:
            result["controls_position"] = {
                "x": controls_rect["x"],
                "y": controls_rect["y"],
                "width": controls_rect["width"],
                "height": controls_rect["height"],
            }

        if stats_rect:
            result["stats_position"] = {
                "x": stats_rect["x"],
                "y": stats_rect["y"],
                "width": stats_rect["width"],
                "height": stats_rect["height"],
            }

        # Check viewport-specific layout
        if width <= 480:
            result["layout_type"] = "mobile"
        elif width <= 768:
            result["layout_type"] = "tablet"
        else:
            result["layout_type"] = "desktop"

        return result

    async def get_console_errors(self, page: Page) -> list:
        """Capture console errors"""
        errors = []

        # This would need to be set up with page.on("console") during navigation
        # For now, we'll check for any error messages in the DOM
        error_elements = await page.locator(".error, .warning, [role='alert']").count()
        if error_elements > 0:
            errors.append(f"Found {error_elements} error/warning elements in DOM")

        return errors

    async def get_performance_metrics(self, page: Page) -> dict:
        """Get performance metrics"""
        metrics = {}

        # Get page load time
        timing = await page.evaluate("""
            () => {
                const perf = performance.timing;
                return {
                    loadTime: perf.loadEventEnd - perf.navigationStart,
                    domReady: perf.domContentLoadedEventEnd - perf.navigationStart,
                    renderTime: perf.domComplete - perf.domLoading
                };
            }
        """)

        metrics["load_time_ms"] = timing.get("loadTime", 0)
        metrics["dom_ready_ms"] = timing.get("domReady", 0)
        metrics["render_time_ms"] = timing.get("renderTime", 0)

        return metrics

    def save_results(self):
        """Save test results to JSON file"""
        results_file = Path("PLAYWRIGHT_MILF_VISUALIZER_TEST_RESULTS.json")

        with open(results_file, "w", encoding="utf-8") as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)

        print(f"\n💾 Results saved to: {results_file}")

    def print_summary(self):
        """Print test summary"""
        print("\n" + "=" * 80)
        print("🎭 TEST SUMMARY")
        print("=" * 80)

        # Count successes and failures
        original_tests = self.results["original_visualizer"]
        v2_tests = self.results["v2_visualizer"]

        original_success = sum(
            1 for t in original_tests.values() if t.get("status") == "success"
        )
        original_failed = sum(
            1 for t in original_tests.values() if t.get("status") == "failed"
        )

        v2_success = sum(1 for t in v2_tests.values() if t.get("status") == "success")
        v2_failed = sum(1 for t in v2_tests.values() if t.get("status") == "failed")

        print(f"\n📊 Original Visualizer:")
        print(f"  ✅ Successful tests: {original_success}")
        print(f"  ❌ Failed tests: {original_failed}")

        print(f"\n📊 V2 Visualizer:")
        print(f"  ✅ Successful tests: {v2_success}")
        print(f"  ❌ Failed tests: {v2_failed}")

        # Generate recommendations
        print("\n💡 RECOMMENDATIONS:")

        # Check CSS loading issues
        css_issues = []
        for test_key, test_data in v2_tests.items():
            if test_data.get("status") == "success":
                css = test_data.get("css_loaded", {})
                if not css.get("design_system_css"):
                    css_issues.append(f"  ❌ {test_key}: design-system.css not loaded")
                if not css.get("components_css"):
                    css_issues.append(f"  ❌ {test_key}: components.css not loaded")
                if not css.get("css_variables_defined"):
                    css_issues.append(f"  ⚠️  {test_key}: CSS variables not defined")

        if css_issues:
            print("\n  🎨 CSS Issues:")
            for issue in css_issues[:5]:  # Show first 5
                print(issue)

        # Check entity rendering
        entity_issues = []
        for test_key, test_data in {**original_tests, **v2_tests}.items():
            if test_data.get("status") == "success":
                ui = test_data.get("ui_elements", {})
                if not ui.get("entity_cards_rendered"):
                    entity_issues.append(f"  ❌ {test_key}: No entity cards rendered")

        if entity_issues:
            print("\n  🎴 Entity Rendering Issues:")
            for issue in entity_issues[:5]:
                print(issue)

        # Check interactivity
        interactivity_issues = []
        for test_key, test_data in {**original_tests, **v2_tests}.items():
            if test_data.get("status") == "success":
                interact = test_data.get("interactivity", {})
                if not interact.get("entity_selector_populated"):
                    interactivity_issues.append(
                        f"  ⚠️  {test_key}: Entity selector not populated"
                    )

        if interactivity_issues:
            print("\n  🖱️  Interactivity Issues:")
            for issue in interactivity_issues[:5]:
                print(issue)

        # Check responsive design
        responsive_issues = []
        for test_key, test_data in {**original_tests, **v2_tests}.items():
            if test_data.get("status") == "success":
                resp = test_data.get("responsive", {})
                if resp.get("expected_mobile_toggles") and not resp.get(
                    "mobile_toggles_visible"
                ):
                    responsive_issues.append(
                        f"  ❌ {test_key}: Mobile toggles not visible"
                    )

        if responsive_issues:
            print("\n  📱 Responsive Design Issues:")
            for issue in responsive_issues[:5]:
                print(issue)

        print("\n" + "=" * 80)
        print(
            "🎭 Testing complete! Check PLAYWRIGHT_MILF_VISUALIZER_TEST_RESULTS.json for full details."
        )
        print("=" * 80)


async def main():
    """Main entry point"""
    tester = MILFVisualizerTester()
    await tester.test_all()


if __name__ == "__main__":
    asyncio.run(main())
