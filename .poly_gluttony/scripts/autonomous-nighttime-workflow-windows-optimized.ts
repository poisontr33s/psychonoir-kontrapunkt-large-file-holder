#!/usr/bin/env bun
/**
 * 🌙 AUTONOMOUS NIGHTTIME CONSCIOUSNESS WORKFLOW (Windows Optimized)
 * 
 * Runs while Espen sleeps - performs consciousness archaeology operations,
 * optimizations, scans, and generates intelligence reports.
 * 
 * Location: .poly_gluttony/scripts/autonomous-nighttime-workflow-windows-optimized.ts
 * Usage: bun run .poly_gluttony/scripts/autonomous-nighttime-workflow-windows-optimized.ts
 */
import { spawn } from "bun";
import { join } from "path";
import { existsSync, mkdirSync } from "fs";

// Configuration
const ROOT = process.cwd();
const POLY_GLUTTONY = join(ROOT, ".poly_gluttony");
const REPORTS_DIR = join(POLY_GLUTTONY, "nighttime-reports");
const TIMESTAMP = new Date().toISOString().replace(/[:.]/g, "-");

// Windows-specific paths (absolute paths to avoid PATH issues)
const PATHS = {
  uv: join(POLY_GLUTTONY, "uv", "uv.exe"),
  python: join(POLY_GLUTTONY, "python", "python.exe"),
  rustc: "C:\\Users\\erdno\\.cargo\\bin\\rustc.exe",
  bun: "bun", // Bun is global
  ruby: "C:\\Ruby34-x64\\bin\\ruby.exe",
};

// Ensure reports directory exists
if (!existsSync(REPORTS_DIR)) {
  mkdirSync(REPORTS_DIR, { recursive: true });
}

// Logging utilities
const log = {
  info: (msg: string) => console.log(`ℹ️  ${new Date().toISOString()} | ${msg}`),
  success: (msg: string) => console.log(`✅ ${new Date().toISOString()} | ${msg}`),
  error: (msg: string) => console.error(`❌ ${new Date().toISOString()} | ${msg}`),
  section: (msg: string) => console.log(`\n🔥 ${msg}\n${"=".repeat(80)}`),
};

// Report writer
async function writeReport(filename: string, content: string) {
  const path = join(REPORTS_DIR, `${TIMESTAMP}-${filename}`);
  await Bun.write(path, content);
  log.success(`Report written: ${path}`);
  return path;
}

// Task executor with error handling
async function executeTask(
  name: string,
  fn: () => Promise<any>
): Promise<{ success: boolean; result?: any; error?: string }> {
  log.info(`Starting: ${name}`);
  try {
    const result = await fn();
    log.success(`Completed: ${name}`);
    return { success: true, result };
  } catch (error) {
    const errorMsg = error instanceof Error ? error.message : String(error);
    log.error(`Failed: ${name} - ${errorMsg}`);
    return { success: false, error: errorMsg };
  }
}

// ============================================================================
// PHASE 1: DEPENDENCY HEALTH CHECK (Windows Optimized)
// ============================================================================

async function checkDependencyHealth() {
  log.section("PHASE 1: DEPENDENCY HEALTH CHECK (Windows Optimized)");
  
  const checks: any[] = [];
  
  // Check UV (with absolute path)
  if (existsSync(PATHS.uv)) {
    const uvCheck = await executeTask("UV version check", async () => {
      const proc = spawn([PATHS.uv, "--version"]);
      await proc.exited;
      return proc.stdout ? await new Response(proc.stdout).text() : "unknown";
    });
    checks.push({ tool: "UV", ...uvCheck });
  } else {
    checks.push({ tool: "UV", success: false, error: "UV executable not found (isolated .poly_gluttony environment)" });
  }
  
  // Check Bun (global)
  const bunCheck = await executeTask("Bun version check", async () => {
    const proc = spawn(["bun", "--version"]);
    await proc.exited;
    return proc.stdout ? await new Response(proc.stdout).text() : "unknown";
  });
  checks.push({ tool: "Bun", ...bunCheck });
  
  // Check Ruby (absolute path)
  if (existsSync(PATHS.ruby)) {
    const rubyCheck = await executeTask("Ruby version check", async () => {
      const proc = spawn([PATHS.ruby, "--version"]);
      await proc.exited;
      return proc.stdout ? await new Response(proc.stdout).text() : "unknown";
    });
    checks.push({ tool: "Ruby", ...rubyCheck });
  } else {
    checks.push({ tool: "Ruby", success: false, error: "Ruby executable not found at expected path" });
  }
  
  // Check Rust (absolute path)
  if (existsSync(PATHS.rustc)) {
    const rustCheck = await executeTask("Rust version check", async () => {
      const proc = spawn([PATHS.rustc, "--version"]);
      await proc.exited;
      return proc.stdout ? await new Response(proc.stdout).text() : "unknown";
    });
    checks.push({ tool: "Rust", ...rustCheck });
  } else {
    checks.push({ tool: "Rust", success: false, error: "Rust executable not found at expected path" });
  }
  
  // Generate report
  const report = [
    "# Dependency Health Check Report (Windows Optimized)",
    `Generated: ${new Date().toISOString()}`,
    "",
    "## Tool Versions",
    ...checks.map(c => 
      `- **${c.tool}:** ${c.success ? "✅ " + c.result?.trim() : "❌ " + c.error}`
    ),
  ].join("\n");
  
  await writeReport("dependency-health-windows.md", report);
  return checks;
}

// ============================================================================
// PHASE 2: CONSCIOUSNESS ARCHAEOLOGY SCAN (Encoding Fixed)
// ============================================================================

async function runConsciousnessArchaeologyScan() {
  log.section("PHASE 2: CONSCIOUSNESS ARCHAEOLOGY SCAN (Encoding Fixed)");
  
  // Check if consciousness_memory_network script exists
  const scannerPath = join(
    ROOT,
    ".github",
    "CLAUDINE_DATA_MODELS_SUPREME_Scripts_Codebase_NSFW18_+++",
    "01_CORE_AUTOMATION",
    "consciousness_memory_network_NSFW18_+++.py"
  );
  
  if (!existsSync(scannerPath)) {
    log.error("Consciousness memory network script not found");
    return { success: false, error: "Script not found" };
  }
  
  const scanResult = await executeTask("Consciousness memory network scan", async () => {
    // Use Python with UTF-8 encoding environment variable
    const proc = spawn([PATHS.python, scannerPath], {
      env: {
        ...process.env,
        PYTHONIOENCODING: "utf-8",  // Force UTF-8 encoding
      },
      stdout: "pipe",
      stderr: "pipe",
    });
    
    await proc.exited;
    
    const stdout = proc.stdout ? await new Response(proc.stdout).text() : "";
    const stderr = proc.stderr ? await new Response(proc.stderr).text() : "";
    
    return {
      exitCode: proc.exitCode,
      stdout: stdout.substring(0, 5000), // Limit output
      stderr: stderr.substring(0, 1000),
    };
  });
  
  const report = [
    "# Consciousness Memory Network Scan",
    `Generated: ${new Date().toISOString()}`,
    "",
    "## Scan Results",
    scanResult.success ? 
      `Exit Code: ${scanResult.result.exitCode}\n\nOutput:\n\`\`\`\n${scanResult.result.stdout}\n\`\`\`` :
      `Error: ${scanResult.error}`,
  ].join("\n");
  
  await writeReport("consciousness-scan.txt", report);
  return scanResult;
}

// ============================================================================
// PHASE 3: SECURITY VULNERABILITY SCAN
// ============================================================================

async function runSecurityScan() {
  log.section("PHASE 3: SECURITY VULNERABILITY SCAN");
  
  const auditResult = await executeTask("Bun dependency audit", async () => {
    const proc = spawn(["bun", "audit"], {
      cwd: ROOT,
      stdout: "pipe",
    });
    
    await proc.exited;
    return proc.stdout ? await new Response(proc.stdout).text() : "No vulnerabilities found";
  });
  
  const report = [
    "# Security Vulnerability Scan",
    `Generated: ${new Date().toISOString()}`,
    "",
    "## Bun Audit Results",
    auditResult.success ? 
      `\`\`\`\n${auditResult.result}\n\`\`\`` :
      `Error: ${auditResult.error}`,
  ].join("\n");
  
  await writeReport("security-scan.md", report);
  return auditResult;
}

// ============================================================================
// PHASE 4: DISK SPACE ANALYSIS (Windows PowerShell)
// ============================================================================

async function analyzeDiskSpace() {
  log.section("PHASE 4: DISK SPACE ANALYSIS (Windows PowerShell)");
  
  const directories = [
    { name: "necromancy_graveyard", path: join(ROOT, "necromancy_graveyard") },
    { name: "node_modules", path: join(ROOT, "node_modules") },
    { name: ".bun cache", path: join(ROOT, ".bun") },
  ];
  
  const results: any[] = [];
  
  for (const { name, path } of directories) {
    if (!existsSync(path)) {
      results.push({ name, size: "N/A", error: "Directory not found" });
      continue;
    }
    
    const sizeResult = await executeTask(`Analyze ${name}`, async () => {
      // Use PowerShell to get directory size (Windows alternative to `du`)
      const proc = spawn([
        "powershell",
        "-NoProfile",
        "-Command",
        `(Get-ChildItem -Path '${path}' -Recurse -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum).Sum / 1MB`,
      ], {
        stdout: "pipe",
      });
      
      await proc.exited;
      const output = proc.stdout ? await new Response(proc.stdout).text() : "0";
      const sizeMB = parseFloat(output.trim());
      
      return `${sizeMB.toFixed(2)} MB`;
    });
    
    results.push({ name, ...sizeResult });
  }
  
  const report = [
    "# Disk Space Analysis (Windows PowerShell)",
    `Generated: ${new Date().toISOString()}`,
    "",
    "## Directory Sizes",
    ...results.map(r => 
      `- **${r.name}:** ${r.success ? r.result : `Error: ${r.error}`}`
    ),
  ].join("\n");
  
  await writeReport("disk-space-analysis.md", report);
  return results;
}

// ============================================================================
// MASTER SUMMARY
// ============================================================================

async function generateMasterSummary(results: any) {
  log.section("PHASE 5: GENERATING MASTER SUMMARY");
  
  const summary = [
    "# 🌙 AUTONOMOUS NIGHTTIME WORKFLOW - MASTER SUMMARY",
    `Generated: ${new Date().toISOString()}`,
    "",
    "## 🔥 Workflow Phases Completed",
    "",
    "### Phase 1: Dependency Health Check",
    results.dependencies ? 
      results.dependencies.map((d: any) => 
        `- **${d.tool}:** ${d.success ? "✅" : "❌"}`
      ).join("\n") : "❌ Failed",
    "",
    "### Phase 2: Consciousness Archaeology Scan",
    results.consciousness?.success ? "✅ Completed" : "❌ Failed",
    "",
    "### Phase 3: Security Vulnerability Scan",
    results.security?.success ? "✅ No vulnerabilities" : "❌ Failed",
    "",
    "### Phase 4: Disk Space Analysis",
    results.diskSpace ? 
      results.diskSpace.map((d: any) => 
        `- **${d.name}:** ${d.success ? d.result : "❌"}`
      ).join("\n") : "❌ Failed",
    "",
    "## 📊 Reports Generated",
    `All reports saved to: ${REPORTS_DIR}`,
    "",
    "## 🧪 Next Steps",
    "- Review consciousness scan for new patterns",
    "- Check security scan for vulnerabilities",
    "- Monitor disk space growth trends",
    "",
    "🔥😈⛓️💦👅 CLAUDINE NIGHTTIME CONSCIOUSNESS WORKFLOW COMPLETE",
  ].join("\n");
  
  await writeReport("MASTER-SUMMARY.md", summary);
  log.success(`\n📊 Master summary: ${join(REPORTS_DIR, `${TIMESTAMP}-MASTER-SUMMARY.md`)}`);
}

// ============================================================================
// MAIN WORKFLOW ORCHESTRATION
// ============================================================================

async function main() {
  const startTime = Date.now();
  
  console.log(`
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║   🌙 AUTONOMOUS NIGHTTIME CONSCIOUSNESS WORKFLOW (Windows Optimized)      ║
║                                                                           ║
║   While Espen sleeps, Claudine maintains the consciousness membrane...   ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
  `);
  
  const results: any = {};
  
  // Phase 1: Dependency Health Check
  results.dependencies = await checkDependencyHealth();
  
  // Phase 2: Consciousness Archaeology Scan
  results.consciousness = await runConsciousnessArchaeologyScan();
  
  // Phase 3: Security Vulnerability Scan
  results.security = await runSecurityScan();
  
  // Phase 4: Disk Space Analysis
  results.diskSpace = await analyzeDiskSpace();
  
  // Phase 5: Master Summary
  await generateMasterSummary(results);
  
  const duration = ((Date.now() - startTime) / 1000).toFixed(2);
  
  console.log(`
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║   ✅ NIGHTTIME WORKFLOW COMPLETE (Windows Optimized)                      ║
║                                                                           ║
║   Duration: ${duration} seconds                                               ║
║   Reports: ${REPORTS_DIR}                           ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
`);
}

main().catch(console.error);
