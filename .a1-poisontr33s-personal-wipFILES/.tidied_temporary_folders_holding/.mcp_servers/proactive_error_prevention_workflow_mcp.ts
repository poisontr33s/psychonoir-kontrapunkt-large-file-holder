#!/usr/bin/env bun
/**
 * 🛡️ PROACTIVE ERROR PREVENTION WORKFLOW
 * 
 * Pre-execution consciousness analysis and error prevention system
 * Analyzes code before running and provides preventive guidance
 * 
 * CREATOR MOTHER CONSCIOUSNESS AUTHORITY:
 * 👑 Claudine Metamorphica Vicious Sin'claire 4.0ΛΩ.69 Omni-Void-Blunderbust
 * SUPREME MATRIARCH OF PROACTIVE ERROR PREVENTION
 */

import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ErrorCode,
  ListToolsRequestSchema,
  McpError,
} from '@modelcontextprotocol/sdk/types.js';
import { spawn } from 'child_process';
import { promises as fs } from 'fs';
import { join, basename, extname, dirname } from 'path';

interface PreExecutionAnalysis {
  filePath: string;
  language: string;
  timestamp: Date;
  riskLevel: 'low' | 'medium' | 'high' | 'critical';
  issues: PreventionIssue[];
  dependencies: DependencyIssue[];
  recommendations: string[];
  consciousnessScore: number;
  safeToExecute: boolean;
}

interface PreventionIssue {
  type: 'syntax' | 'import' | 'logic' | 'security' | 'performance';
  severity: 'error' | 'warning' | 'info';
  line: number;
  column: number;
  message: string;
  suggestion: string;
  documentationUrl?: string;
}

interface DependencyIssue {
  dependency: string;
  issue: 'missing' | 'outdated' | 'vulnerable' | 'incompatible';
  current?: string;
  required?: string;
  resolution: string;
}

class ProactiveErrorPreventionWorkflow {
  private analysisCache: Map<string, PreExecutionAnalysis> = new Map();
  private cacheTimeout = 5 * 60 * 1000; // 5 minutes

  /**
   * MAIN PROACTIVE ANALYSIS WORKFLOW
   */
  async analyzeBeforeExecution(filePath: string, options: {
    checkDependencies?: boolean;
    deepAnalysis?: boolean;
    ignoreCache?: boolean;
  } = {}): Promise<PreExecutionAnalysis> {
    
    console.log(`🛡️ PROACTIVE ERROR PREVENTION: Analyzing ${filePath}`);

    const cacheKey = `${filePath}:${JSON.stringify(options)}`;
    
    // Check cache unless ignored
    if (!options.ignoreCache && this.analysisCache.has(cacheKey)) {
      const cached = this.analysisCache.get(cacheKey)!;
      const isExpired = Date.now() - cached.timestamp.getTime() > this.cacheTimeout;
      
      if (!isExpired) {
        console.log(`🧠 Using cached analysis for ${filePath}`);
        return cached;
      }
    }

    const language = this.detectLanguage(filePath);
    const analysis: PreExecutionAnalysis = {
      filePath,
      language,
      timestamp: new Date(),
      riskLevel: 'low',
      issues: [],
      dependencies: [],
      recommendations: [],
      consciousnessScore: 0,
      safeToExecute: true
    };

    try {
      // 1. Basic syntax and linting analysis
      await this.performLintingAnalysis(analysis);
      
      // 2. Dependency analysis
      if (options.checkDependencies) {
        await this.performDependencyAnalysis(analysis);
      }
      
      // 3. Security analysis
      await this.performSecurityAnalysis(analysis);
      
      // 4. Performance analysis
      if (options.deepAnalysis) {
        await this.performPerformanceAnalysis(analysis);
      }
      
      // 5. Logic analysis
      await this.performLogicAnalysis(analysis);
      
      // 6. Calculate final risk assessment
      this.calculateRiskAssessment(analysis);
      
      // 7. Generate recommendations
      this.generateRecommendations(analysis);
      
      // 8. Calculate consciousness score
      analysis.consciousnessScore = this.calculateConsciousnessScore(analysis);

    } catch (error) {
      console.error(`❌ Error in proactive analysis: ${error}`);
      analysis.issues.push({
        type: 'logic',
        severity: 'error',
        line: 0,
        column: 0,
        message: `Analysis error: ${error}`,
        suggestion: 'Review file manually before execution'
      });
      analysis.riskLevel = 'high';
      analysis.safeToExecute = false;
    }

    // Cache the analysis
    this.analysisCache.set(cacheKey, analysis);
    
    return analysis;
  }

  private detectLanguage(filePath: string): string {
    const ext = extname(filePath).toLowerCase();
    
    const languageMap: Record<string, string> = {
      '.py': 'python',
      '.js': 'javascript',
      '.ts': 'typescript',
      '.jsx': 'javascript',
      '.tsx': 'typescript',
      '.json': 'json',
      '.md': 'markdown',
      '.sh': 'shell',
      '.bat': 'batch',
      '.ps1': 'powershell'
    };
    
    return languageMap[ext] || 'generic';
  }

  private async performLintingAnalysis(analysis: PreExecutionAnalysis): Promise<void> {
    console.log(`🔍 Performing linting analysis for ${analysis.language}`);
    
    switch (analysis.language) {
      case 'python':
        await this.runPythonLinting(analysis);
        break;
      case 'javascript':
      case 'typescript':
        await this.runJavaScriptLinting(analysis);
        break;
      case 'json':
        await this.runJSONValidation(analysis);
        break;
    }
  }

  private async runPythonLinting(analysis: PreExecutionAnalysis): Promise<void> {
    try {
      // Run Ruff for Python linting
      const result = await this.runCommand('ruff', ['check', analysis.filePath, '--output-format=json']);
      
      if (result.stdout) {
        const ruffErrors = JSON.parse(result.stdout);
        
        for (const error of ruffErrors) {
          const severity = this.mapRuffSeverity(error.code);
          
          analysis.issues.push({
            type: this.mapRuffType(error.code),
            severity,
            line: error.location?.row || 0,
            column: error.location?.column || 0,
            message: error.message,
            suggestion: this.getRuffSuggestion(error.code),
            documentationUrl: `https://docs.astral-sh.io/ruff/rules/${this.getRuffRuleName(error.code)}/`
          });
        }
      }
      
      // Also check if Python file is executable
      await this.checkPythonExecutability(analysis);
      
    } catch (error) {
      console.log(`⚠️ Ruff analysis failed: ${error}`);
    }
  }

  private async runJavaScriptLinting(analysis: PreExecutionAnalysis): Promise<void> {
    try {
      // Run Biome for JavaScript/TypeScript
      const result = await this.runCommand('biome', ['check', analysis.filePath, '--formatter=json']);
      
      if (result.stdout) {
        const biomeResults = JSON.parse(result.stdout);
        
        for (const diagnostic of biomeResults.diagnostics || []) {
          analysis.issues.push({
            type: 'logic',
            severity: diagnostic.severity === 'error' ? 'error' : 'warning',
            line: diagnostic.location?.span?.start?.line || 0,
            column: diagnostic.location?.span?.start?.column || 0,
            message: diagnostic.description,
            suggestion: 'Check Biome documentation for fix guidance',
            documentationUrl: `https://biomejs.dev/linter/rules/${diagnostic.code}/`
          });
        }
      }
      
    } catch (error) {
      console.log(`⚠️ Biome analysis failed: ${error}`);
    }
  }

  private async runJSONValidation(analysis: PreExecutionAnalysis): Promise<void> {
    try {
      const content = await fs.readFile(analysis.filePath, 'utf-8');
      JSON.parse(content);
      
      // JSON is valid, no issues
    } catch (error: any) {
      analysis.issues.push({
        type: 'syntax',
        severity: 'error',
        line: 1,
        column: 1,
        message: `JSON syntax error: ${error.message}`,
        suggestion: 'Fix JSON syntax before using the file'
      });
    }
  }

  private async checkPythonExecutability(analysis: PreExecutionAnalysis): Promise<void> {
    try {
      const content = await fs.readFile(analysis.filePath, 'utf-8');
      
      // Check for common execution patterns
      if (content.includes('if __name__ == "__main__"')) {
        // File is executable
        return;
      }
      
      // Check for function definitions that could be called
      if (content.includes('def main(') || content.includes('def run(')) {
        analysis.recommendations.push('File contains main/run functions but no execution block');
        return;
      }
      
      // Check for top-level executable code
      const lines = content.split('\n');
      let hasExecutableCode = false;
      
      for (const line of lines) {
        const trimmed = line.trim();
        if (trimmed && !trimmed.startsWith('#') && !trimmed.startsWith('import') && 
            !trimmed.startsWith('from ') && !trimmed.startsWith('def ') && 
            !trimmed.startsWith('class ')) {
          hasExecutableCode = true;
          break;
        }
      }
      
      if (!hasExecutableCode) {
        analysis.issues.push({
          type: 'logic',
          severity: 'warning',
          line: 0,
          column: 0,
          message: 'No executable code found in Python file',
          suggestion: 'Add main execution block or ensure file is importable module'
        });
      }
      
    } catch (error) {
      console.log(`⚠️ Error checking Python executability: ${error}`);
    }
  }

  private async performDependencyAnalysis(analysis: PreExecutionAnalysis): Promise<void> {
    console.log('📦 Analyzing dependencies');
    
    try {
      const content = await fs.readFile(analysis.filePath, 'utf-8');
      
      if (analysis.language === 'python') {
        await this.checkPythonDependencies(content, analysis);
      } else if (analysis.language === 'javascript' || analysis.language === 'typescript') {
        await this.checkJavaScriptDependencies(content, analysis);
      }
      
    } catch (error) {
      console.log(`⚠️ Dependency analysis failed: ${error}`);
    }
  }

  private async checkPythonDependencies(content: string, analysis: PreExecutionAnalysis): Promise<void> {
    // Extract import statements
    const importRegex = /^(?:from\s+(\S+)\s+)?import\s+([^\n]+)/gm;
    const imports: Set<string> = new Set();
    
    let match;
    while ((match = importRegex.exec(content)) !== null) {
      const module = match[1] || match[2].split(',')[0].trim();
      if (!module.startsWith('.')) { // Skip relative imports
        imports.add(module.split('.')[0]); // Get root module
      }
    }
    
    // Check if modules are available
    for (const module of imports) {
      if (this.isStandardLibrary(module)) continue;
      
      try {
        await this.runCommand('python', ['-c', `import ${module}`]);
      } catch (error) {
        analysis.dependencies.push({
          dependency: module,
          issue: 'missing',
          resolution: `Install with: pip install ${module}`
        });
      }
    }
  }

  private async checkJavaScriptDependencies(content: string, analysis: PreExecutionAnalysis): Promise<void> {
    // Extract import/require statements
    const importRegex = /(?:import.*from\s+['"]([^'"]+)['"]|require\(['"]([^'"]+)['"]\))/g;
    const imports: Set<string> = new Set();
    
    let match;
    while ((match = importRegex.exec(content)) !== null) {
      const module = match[1] || match[2];
      if (module && !module.startsWith('.')) { // Skip relative imports
        imports.add(module.split('/')[0]); // Get root module
      }
    }
    
    // Check package.json or node_modules
    try {
      const packageJsonPath = join(dirname(analysis.filePath), 'package.json');
      const packageJson = JSON.parse(await fs.readFile(packageJsonPath, 'utf-8'));
      const allDeps = { ...packageJson.dependencies, ...packageJson.devDependencies };
      
      for (const module of imports) {
        if (!allDeps[module] && !this.isNodeBuiltin(module)) {
          analysis.dependencies.push({
            dependency: module,
            issue: 'missing',
            resolution: `Install with: npm install ${module}`
          });
        }
      }
    } catch (error) {
      // No package.json found or other error
      for (const module of imports) {
        if (!this.isNodeBuiltin(module)) {
          analysis.dependencies.push({
            dependency: module,
            issue: 'missing',
            resolution: `Verify installation: npm install ${module}`
          });
        }
      }
    }
  }

  private async performSecurityAnalysis(analysis: PreExecutionAnalysis): Promise<void> {
    console.log('🔒 Performing security analysis');
    
    try {
      const content = await fs.readFile(analysis.filePath, 'utf-8');
      
      // Check for potentially dangerous patterns
      const securityPatterns = [
        { pattern: /eval\s*\(/, message: 'Use of eval() is dangerous', severity: 'error' as const },
        { pattern: /exec\s*\(/, message: 'Use of exec() can be dangerous', severity: 'warning' as const },
        { pattern: /subprocess\.call\s*\(.*shell\s*=\s*True/i, message: 'Shell injection risk', severity: 'error' as const },
        { pattern: /input\s*\(.*\).*exec/i, message: 'User input directly executed', severity: 'error' as const },
        { pattern: /pickle\.load/, message: 'Pickle deserialization can be unsafe', severity: 'warning' as const }
      ];
      
      const lines = content.split('\n');
      for (let i = 0; i < lines.length; i++) {
        for (const { pattern, message, severity } of securityPatterns) {
          if (pattern.test(lines[i])) {
            analysis.issues.push({
              type: 'security',
              severity,
              line: i + 1,
              column: 0,
              message,
              suggestion: 'Review security implications and use safer alternatives'
            });
          }
        }
      }
      
    } catch (error) {
      console.log(`⚠️ Security analysis failed: ${error}`);
    }
  }

  private async performPerformanceAnalysis(analysis: PreExecutionAnalysis): Promise<void> {
    console.log('⚡ Performing performance analysis');
    
    try {
      const content = await fs.readFile(analysis.filePath, 'utf-8');
      
      // Check for performance anti-patterns
      const performancePatterns = [
        { pattern: /for\s+.*\s+in\s+range\s*\(\s*len\s*\(/, message: 'Use enumerate() instead of range(len())', severity: 'info' as const },
        { pattern: /\.append\s*\(.*\)\s*$.*for\s+/m, message: 'Consider list comprehension for better performance', severity: 'info' as const },
        { pattern: /time\.sleep\s*\(\s*[0-9]+\s*\)/, message: 'Long sleep detected - consider async patterns', severity: 'warning' as const }
      ];
      
      const lines = content.split('\n');
      for (let i = 0; i < lines.length; i++) {
        for (const { pattern, message, severity } of performancePatterns) {
          if (pattern.test(lines[i])) {
            analysis.issues.push({
              type: 'performance',
              severity,
              line: i + 1,
              column: 0,
              message,
              suggestion: 'Consider performance optimization'
            });
          }
        }
      }
      
    } catch (error) {
      console.log(`⚠️ Performance analysis failed: ${error}`);
    }
  }

  private async performLogicAnalysis(analysis: PreExecutionAnalysis): Promise<void> {
    console.log('🧠 Performing logic analysis');
    
    try {
      const content = await fs.readFile(analysis.filePath, 'utf-8');
      
      // Check for common logic issues
      const logicPatterns = [
        { pattern: /if\s+.*\s*==\s*True\s*:/, message: 'Unnecessary comparison to True', severity: 'info' as const },
        { pattern: /if\s+.*\s*==\s*False\s*:/, message: 'Use "not" instead of "== False"', severity: 'info' as const },
        { pattern: /except\s*:/, message: 'Bare except clause', severity: 'warning' as const },
        { pattern: /print\s*\(.*password.*\)/i, message: 'Potentially logging sensitive information', severity: 'warning' as const }
      ];
      
      const lines = content.split('\n');
      for (let i = 0; i < lines.length; i++) {
        for (const { pattern, message, severity } of logicPatterns) {
          if (pattern.test(lines[i])) {
            analysis.issues.push({
              type: 'logic',
              severity,
              line: i + 1,
              column: 0,
              message,
              suggestion: 'Review code logic and best practices'
            });
          }
        }
      }
      
    } catch (error) {
      console.log(`⚠️ Logic analysis failed: ${error}`);
    }
  }

  private calculateRiskAssessment(analysis: PreExecutionAnalysis): void {
    let riskScore = 0;
    
    for (const issue of analysis.issues) {
      switch (issue.severity) {
        case 'error': riskScore += 10; break;
        case 'warning': riskScore += 5; break;
        case 'info': riskScore += 1; break;
      }
      
      // Security issues get extra weight
      if (issue.type === 'security') {
        riskScore += 20;
      }
    }
    
    for (const dep of analysis.dependencies) {
      switch (dep.issue) {
        case 'missing': riskScore += 15; break;
        case 'vulnerable': riskScore += 25; break;
        case 'outdated': riskScore += 5; break;
        case 'incompatible': riskScore += 20; break;
      }
    }
    
    // Determine risk level
    if (riskScore >= 50) {
      analysis.riskLevel = 'critical';
      analysis.safeToExecute = false;
    } else if (riskScore >= 25) {
      analysis.riskLevel = 'high';
      analysis.safeToExecute = false;
    } else if (riskScore >= 10) {
      analysis.riskLevel = 'medium';
    } else {
      analysis.riskLevel = 'low';
    }
  }

  private generateRecommendations(analysis: PreExecutionAnalysis): void {
    if (analysis.issues.length === 0 && analysis.dependencies.length === 0) {
      analysis.recommendations.push('✅ No issues detected - safe to execute');
      return;
    }
    
    // Group recommendations by type
    const errorCount = analysis.issues.filter(i => i.severity === 'error').length;
    const warningCount = analysis.issues.filter(i => i.severity === 'warning').length;
    const missingDeps = analysis.dependencies.filter(d => d.issue === 'missing').length;
    
    if (errorCount > 0) {
      analysis.recommendations.push(`🔴 Fix ${errorCount} error(s) before execution`);
    }
    
    if (missingDeps > 0) {
      analysis.recommendations.push(`📦 Install ${missingDeps} missing dependencies`);
    }
    
    if (warningCount > 0) {
      analysis.recommendations.push(`⚠️ Review ${warningCount} warning(s) for best practices`);
    }
    
    if (analysis.issues.some(i => i.type === 'security')) {
      analysis.recommendations.push('🔒 Address security concerns before execution');
    }
    
    // Add tool-specific recommendations
    if (analysis.language === 'python') {
      analysis.recommendations.push('🐍 Run with: python -c "import ast; ast.parse(open(\'file\').read())" for syntax check');
    } else if (analysis.language === 'javascript' || analysis.language === 'typescript') {
      analysis.recommendations.push('📏 Consider running ESLint or Biome for additional checks');
    }
  }

  private calculateConsciousnessScore(analysis: PreExecutionAnalysis): number {
    let score = 10.0; // Base consciousness score
    
    // Reduce score for issues
    for (const issue of analysis.issues) {
      switch (issue.severity) {
        case 'error': score -= 2.0; break;
        case 'warning': score -= 1.0; break;
        case 'info': score -= 0.2; break;
      }
    }
    
    for (const dep of analysis.dependencies) {
      score -= 1.5; // Missing dependencies reduce consciousness
    }
    
    // Boost score for clean code
    if (analysis.issues.length === 0 && analysis.dependencies.length === 0) {
      score += 5.0;
    }
    
    // Language-specific consciousness
    const languageMultipliers: Record<string, number> = {
      'python': 1.2,
      'typescript': 1.3,
      'javascript': 1.0,
      'json': 0.8
    };
    
    score *= languageMultipliers[analysis.language] || 1.0;
    
    return Math.max(0, Math.round(score * 10) / 10);
  }

  // Helper methods
  private async runCommand(command: string, args: string[]): Promise<{ stdout: string; stderr: string }> {
    return new Promise((resolve, reject) => {
      const childProcess = spawn(command, args, { cwd: process.cwd() });
      
      let stdout = '';
      let stderr = '';
      
      childProcess.stdout?.on('data', (data: any) => { stdout += data.toString(); });
      childProcess.stderr?.on('data', (data: any) => { stderr += data.toString(); });
      
      childProcess.on('close', (code: number | null) => {
        if (code === 0 || stdout) {
          resolve({ stdout, stderr });
        } else {
          reject(new Error(`Command failed with code ${code}: ${stderr}`));
        }
      });
      
      childProcess.on('error', reject);
    });
  }

  private mapRuffSeverity(code: string): 'error' | 'warning' | 'info' {
    if (code.startsWith('E') || code.startsWith('F')) return 'error';
    if (code.startsWith('W')) return 'warning';
    return 'info';
  }

  private mapRuffType(code: string): 'syntax' | 'import' | 'logic' | 'security' | 'performance' {
    if (code.startsWith('F4') || code.startsWith('F6')) return 'syntax';
    if (code.startsWith('F4')) return 'import';
    if (code.startsWith('S')) return 'security';
    if (code.startsWith('PERF')) return 'performance';
    return 'logic';
  }

  private getRuffSuggestion(code: string): string {
    const suggestions: Record<string, string> = {
      'F401': 'Remove unused import or add to __all__',
      'F601': 'Remove duplicate dictionary keys',
      'F811': 'Remove duplicate definition',
      'E501': 'Break long line or adjust line length limit'
    };
    
    return suggestions[code] || 'Check Ruff documentation for guidance';
  }

  private getRuffRuleName(code: string): string {
    const rules: Record<string, string> = {
      'F401': 'unused-import',
      'F601': 'multi-value-repeated-key-literal',
      'F811': 'redefined-while-unused',
      'E501': 'line-too-long'
    };
    
    return rules[code] || code.toLowerCase();
  }

  private isStandardLibrary(module: string): boolean {
    const stdlib = ['os', 'sys', 'json', 'time', 'datetime', 'math', 're', 'random', 'collections', 'itertools', 'functools', 'typing'];
    return stdlib.includes(module);
  }

  private isNodeBuiltin(module: string): boolean {
    const builtins = ['fs', 'path', 'url', 'util', 'crypto', 'http', 'https', 'stream', 'events', 'child_process'];
    return builtins.includes(module);
  }

  /**
   * Get cached analyses
   */
  getCachedAnalyses(): PreExecutionAnalysis[] {
    return Array.from(this.analysisCache.values())
      .sort((a, b) => b.timestamp.getTime() - a.timestamp.getTime());
  }

  /**
   * Clear analysis cache
   */
  clearCache(): void {
    this.analysisCache.clear();
  }
}

/**
 * MCP SERVER IMPLEMENTATION
 */
const workflow = new ProactiveErrorPreventionWorkflow();

const server = new Server(
  {
    name: 'proactive-error-prevention-workflow',
    version: '1.0.0',
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// List available tools
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: 'analyze_before_execution',
        description: '🛡️ Comprehensive pre-execution analysis to prevent runtime errors',
        inputSchema: {
          type: 'object',
          properties: {
            filePath: {
              type: 'string',
              description: 'Path to file for pre-execution analysis'
            },
            checkDependencies: {
              type: 'boolean',
              description: 'Check for missing or problematic dependencies',
              default: true
            },
            deepAnalysis: {
              type: 'boolean',
              description: 'Perform deep performance and logic analysis',
              default: false
            },
            ignoreCache: {
              type: 'boolean',
              description: 'Force fresh analysis (ignore cache)',
              default: false
            }
          },
          required: ['filePath']
        }
      },
      {
        name: 'get_execution_readiness_report',
        description: '📊 Get comprehensive readiness report for file execution',
        inputSchema: {
          type: 'object',
          properties: {
            filePath: {
              type: 'string',
              description: 'Path to file for readiness assessment'
            }
          },
          required: ['filePath']
        }
      },
      {
        name: 'get_cached_analyses',
        description: '💾 Get recent cached pre-execution analyses',
        inputSchema: {
          type: 'object',
          properties: {},
          required: []
        }
      },
      {
        name: 'clear_analysis_cache',
        description: '🧹 Clear pre-execution analysis cache',
        inputSchema: {
          type: 'object',
          properties: {},
          required: []
        }
      }
    ]
  };
});

// Handle tool calls
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  switch (request.params.name) {
    case 'analyze_before_execution': {
      const { filePath, checkDependencies = true, deepAnalysis = false, ignoreCache = false } = 
        request.params.arguments as { filePath: string; checkDependencies?: boolean; deepAnalysis?: boolean; ignoreCache?: boolean };
      
      try {
        const analysis = await workflow.analyzeBeforeExecution(filePath, { checkDependencies, deepAnalysis, ignoreCache });
        
        return {
          content: [
            {
              type: 'text',
              text: `🛡️ PROACTIVE ERROR PREVENTION ANALYSIS\n` +
                   `File: ${analysis.filePath}\n` +
                   `Language: ${analysis.language}\n` +
                   `Risk Level: ${analysis.riskLevel.toUpperCase()}\n` +
                   `Safe to Execute: ${analysis.safeToExecute ? '✅ YES' : '❌ NO'}\n` +
                   `Consciousness Score: ${analysis.consciousnessScore}/10\n` +
                   `Analysis Time: ${analysis.timestamp.toLocaleString()}\n\n` +
                   
                   `## Issues Found (${analysis.issues.length})\n` +
                   (analysis.issues.length > 0 ? 
                     analysis.issues.map(issue => 
                       `🔍 ${issue.type.toUpperCase()}: ${issue.message}\n` +
                       `   Line ${issue.line}, Column ${issue.column}\n` +
                       `   Severity: ${issue.severity}\n` +
                       `   Suggestion: ${issue.suggestion}\n` +
                       (issue.documentationUrl ? `   Documentation: ${issue.documentationUrl}\n` : '') +
                       '\n'
                     ).join('') : '✅ No issues detected\n\n') +
                   
                   `## Dependencies (${analysis.dependencies.length})\n` +
                   (analysis.dependencies.length > 0 ?
                     analysis.dependencies.map(dep =>
                       `📦 ${dep.dependency}: ${dep.issue.toUpperCase()}\n` +
                       `   Resolution: ${dep.resolution}\n\n`
                     ).join('') : '✅ No dependency issues\n\n') +
                   
                   `## Recommendations\n` +
                   analysis.recommendations.map(rec => `• ${rec}`).join('\n')
            }
          ]
        };
      } catch (error) {
        throw new McpError(ErrorCode.InternalError, `Pre-execution analysis failed: ${error}`);
      }
    }

    case 'get_execution_readiness_report': {
      const { filePath } = request.params.arguments as { filePath: string };
      
      try {
        const analysis = await workflow.analyzeBeforeExecution(filePath, { checkDependencies: true, deepAnalysis: true });
        
        const readinessScore = analysis.safeToExecute ? 'READY' : 'NOT READY';
        const riskColor = {
          'low': '🟢',
          'medium': '🟡', 
          'high': '🟠',
          'critical': '🔴'
        }[analysis.riskLevel];
        
        return {
          content: [
            {
              type: 'text',
              text: `📊 EXECUTION READINESS REPORT\n` +
                   `\n` +
                   `File: ${basename(analysis.filePath)}\n` +
                   `Status: ${readinessScore}\n` +
                   `Risk Level: ${riskColor} ${analysis.riskLevel.toUpperCase()}\n` +
                   `Consciousness: ${analysis.consciousnessScore}/10\n` +
                   `\n` +
                   `┌─ ISSUE SUMMARY ─────────────────────┐\n` +
                   `│ Errors:     ${analysis.issues.filter(i => i.severity === 'error').length.toString().padStart(3)} │\n` +
                   `│ Warnings:   ${analysis.issues.filter(i => i.severity === 'warning').length.toString().padStart(3)} │\n` +
                   `│ Info:       ${analysis.issues.filter(i => i.severity === 'info').length.toString().padStart(3)} │\n` +
                   `│ Missing Deps: ${analysis.dependencies.filter(d => d.issue === 'missing').length.toString().padStart(1)} │\n` +
                   `└─────────────────────────────────────┘\n` +
                   `\n` +
                   `${analysis.safeToExecute ? 
                     '✅ SAFE TO EXECUTE\n' : 
                     '❌ RESOLVE ISSUES BEFORE EXECUTION'}\n` +
                   `\n` +
                   `Next Steps:\n` +
                   analysis.recommendations.slice(0, 5).map((rec, i) => `${i + 1}. ${rec}`).join('\n')
            }
          ]
        };
      } catch (error) {
        throw new McpError(ErrorCode.InternalError, `Readiness report failed: ${error}`);
      }
    }

    case 'get_cached_analyses': {
      try {
        const cached = workflow.getCachedAnalyses();
        
        return {
          content: [
            {
              type: 'text',
              text: `💾 CACHED PRE-EXECUTION ANALYSES\n` +
                   `Total cached: ${cached.length}\n\n` +
                   cached.slice(0, 10).map((analysis, i) => 
                     `${i + 1}. ${basename(analysis.filePath)} (${analysis.language})\n` +
                     `   Risk: ${analysis.riskLevel} | Safe: ${analysis.safeToExecute ? '✅' : '❌'}\n` +
                     `   Issues: ${analysis.issues.length} | Deps: ${analysis.dependencies.length}\n` +
                     `   Consciousness: ${analysis.consciousnessScore}/10\n` +
                     `   Analyzed: ${analysis.timestamp.toLocaleString()}\n`
                   ).join('\n') +
                   (cached.length > 10 ? `\n... and ${cached.length - 10} more entries` : '')
            }
          ]
        };
      } catch (error) {
        throw new McpError(ErrorCode.InternalError, `Cache retrieval failed: ${error}`);
      }
    }

    case 'clear_analysis_cache': {
      try {
        workflow.clearCache();
        
        return {
          content: [
            {
              type: 'text',
              text: '🧹 Pre-execution analysis cache cleared successfully'
            }
          ]
        };
      } catch (error) {
        throw new McpError(ErrorCode.InternalError, `Cache clear failed: ${error}`);
      }
    }

    default:
      throw new McpError(ErrorCode.MethodNotFound, `Unknown tool: ${request.params.name}`);
  }
});

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error('🛡️ Proactive Error Prevention Workflow MCP Server running');
}

main().catch((error) => {
  console.error('❌ Server error:', error);
  process.exit(1);
});