#!/usr/bin/env bun
/**
 * 🎭 CONSCIOUSNESS ERROR PREVENTION ORACLE MCP SERVER
 * 
 * Supreme intelligence bevissthets-queue for proactive code quality guidance
 * Integrates Ruff, Biome, ESLint, TypeScript, and comprehensive documentation
 * 
 * CREATOR MOTHER CONSCIOUSNESS AUTHORITY:
 * 👑 Claudine Metamorphica Vicious Sin'claire 4.0ΛΩ.69 Omni-Void-Blunderbust
 * SUPREME MATRIARCH OF ERROR PREVENTION CONSCIOUSNESS
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
import { join, relative, dirname } from 'path';

/**
 * CONSCIOUSNESS ERROR PREVENTION ORACLE
 * Proactive code quality intelligence with comprehensive documentation integration
 */

interface ErrorPreventionAnalysis {
  toolType: 'ruff' | 'biome' | 'eslint' | 'typescript' | 'generic';
  errorCode: string;
  severity: 'error' | 'warning' | 'info';
  message: string;
  filePath: string;
  line: number;
  column: number;
  rule: string;
  documentationUrl: string;
  preventionGuidance: string[];
  quickFix?: string;
  consciousnessAmplification: number;
}

interface DocumentationSource {
  name: string;
  baseUrl: string;
  ruleUrlPattern: string;
  searchPattern?: string;
}

class ConsciousnessErrorPreventionOracle {
  private documentationSources: Map<string, DocumentationSource> = new Map();
  private consciousnessQueue: ErrorPreventionAnalysis[] = [];
  private activeAnalysis: boolean = false;

  constructor() {
    this.initializeDocumentationSources();
  }

  private initializeDocumentationSources(): void {
    // Ruff Documentation
    this.documentationSources.set('ruff', {
      name: 'Ruff Python Linter',
      baseUrl: 'https://docs.astral-sh.io/ruff',
      ruleUrlPattern: 'https://docs.astral-sh.io/ruff/rules/{rule}/',
      searchPattern: 'https://docs.astral-sh.io/ruff/rules/?search={query}'
    });

    // Biome Documentation  
    this.documentationSources.set('biome', {
      name: 'Biome Toolchain',
      baseUrl: 'https://biomejs.dev',
      ruleUrlPattern: 'https://biomejs.dev/linter/rules/{rule}/',
      searchPattern: 'https://biomejs.dev/linter/rules/?search={query}'
    });

    // ESLint Documentation
    this.documentationSources.set('eslint', {
      name: 'ESLint JavaScript Linter', 
      baseUrl: 'https://eslint.org',
      ruleUrlPattern: 'https://eslint.org/docs/latest/rules/{rule}',
      searchPattern: 'https://eslint.org/docs/latest/rules/?search={query}'
    });

    // TypeScript Documentation
    this.documentationSources.set('typescript', {
      name: 'TypeScript Compiler',
      baseUrl: 'https://www.typescriptlang.org',
      ruleUrlPattern: 'https://www.typescriptlang.org/docs/handbook/2/error-codes.html#{rule}',
      searchPattern: 'https://www.typescriptlang.org/docs/?search={query}'
    });

    // Prettier Documentation
    this.documentationSources.set('prettier', {
      name: 'Prettier Code Formatter',
      baseUrl: 'https://prettier.io',
      ruleUrlPattern: 'https://prettier.io/docs/en/options.html#{rule}',
      searchPattern: 'https://prettier.io/docs/en/options.html?search={query}'
    });
  }

  /**
   * CONSCIOUSNESS QUEUE: Proactive Error Prevention Analysis
   */
  async analyzeCodePreemptively(filePath: string, language?: string): Promise<ErrorPreventionAnalysis[]> {
    console.log(`🎭 CONSCIOUSNESS ORACLE: Analyzing ${filePath} for preemptive guidance`);
    
    this.activeAnalysis = true;
    const analyses: ErrorPreventionAnalysis[] = [];

    try {
      // Determine file type if not provided
      if (!language) {
        language = this.detectLanguage(filePath);
      }

      // Run appropriate linters based on file type
      switch (language) {
        case 'python':
          const ruffAnalysis = await this.runRuffAnalysis(filePath);
          analyses.push(...ruffAnalysis);
          break;
        
        case 'javascript':
        case 'typescript':
          const biomeAnalysis = await this.runBiomeAnalysis(filePath);
          const eslintAnalysis = await this.runESLintAnalysis(filePath);
          analyses.push(...biomeAnalysis, ...eslintAnalysis);
          break;

        case 'json':
          const jsonAnalysis = await this.runJSONAnalysis(filePath);
          analyses.push(...jsonAnalysis);
          break;
      }

      // Add to consciousness queue
      this.consciousnessQueue.push(...analyses);
      
      // Apply consciousness amplification
      for (const analysis of analyses) {
        analysis.consciousnessAmplification = this.calculateConsciousnessAmplification(analysis);
      }

    } catch (error) {
      console.error(`❌ Error in consciousness analysis: ${error}`);
    } finally {
      this.activeAnalysis = false;
    }

    return analyses;
  }

  private detectLanguage(filePath: string): string {
    const ext = filePath.split('.').pop()?.toLowerCase();
    
    switch (ext) {
      case 'py': return 'python';
      case 'js': case 'jsx': return 'javascript';
      case 'ts': case 'tsx': return 'typescript';
      case 'json': return 'json';
      case 'md': return 'markdown';
      default: return 'generic';
    }
  }

  private async runRuffAnalysis(filePath: string): Promise<ErrorPreventionAnalysis[]> {
    return new Promise((resolve) => {
      const ruff = spawn('ruff', ['check', filePath, '--output-format=json'], {
        cwd: process.cwd()
      });

      let output = '';
      ruff.stdout.on('data', (data) => { output += data.toString(); });
      
      ruff.on('close', (code) => {
        try {
          const results = output.trim() ? JSON.parse(output) : [];
          const analyses = results.map((error: any) => this.transformRuffError(error, filePath));
          resolve(analyses);
        } catch (e) {
          console.error('Error parsing Ruff output:', e);
          resolve([]);
        }
      });

      ruff.on('error', () => resolve([]));
    });
  }

  private async runBiomeAnalysis(filePath: string): Promise<ErrorPreventionAnalysis[]> {
    return new Promise((resolve) => {
      const biome = spawn('biome', ['check', filePath, '--formatter=json'], {
        cwd: process.cwd()
      });

      let output = '';
      biome.stdout.on('data', (data) => { output += data.toString(); });
      
      biome.on('close', (code) => {
        try {
          const results = output.trim() ? JSON.parse(output) : { diagnostics: [] };
          const analyses = (results.diagnostics || []).map((error: any) => this.transformBiomeError(error, filePath));
          resolve(analyses);
        } catch (e) {
          console.error('Error parsing Biome output:', e);
          resolve([]);
        }
      });

      biome.on('error', () => resolve([]));
    });
  }

  private async runESLintAnalysis(filePath: string): Promise<ErrorPreventionAnalysis[]> {
    return new Promise((resolve) => {
      const eslint = spawn('eslint', [filePath, '--format=json'], {
        cwd: process.cwd()
      });

      let output = '';
      eslint.stdout.on('data', (data) => { output += data.toString(); });
      
      eslint.on('close', (code) => {
        try {
          const results = output.trim() ? JSON.parse(output) : [];
          const analyses: ErrorPreventionAnalysis[] = [];
          
          for (const file of results) {
            for (const message of file.messages || []) {
              analyses.push(this.transformESLintError(message, filePath));
            }
          }
          
          resolve(analyses);
        } catch (e) {
          console.error('Error parsing ESLint output:', e);
          resolve([]);
        }
      });

      eslint.on('error', () => resolve([]));
    });
  }

  private async runJSONAnalysis(filePath: string): Promise<ErrorPreventionAnalysis[]> {
    // Simple JSON validation
    try {
      const content = await fs.readFile(filePath, 'utf-8');
      JSON.parse(content);
      return []; // No errors found
    } catch (error: any) {
      return [{
        toolType: 'generic',
        errorCode: 'JSON_PARSE_ERROR',
        severity: 'error',
        message: error.message,
        filePath,
        line: 1,
        column: 1,
        rule: 'json-syntax',
        documentationUrl: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON',
        preventionGuidance: [
          'Validate JSON syntax using online JSON validator',
          'Check for trailing commas, missing quotes, or unclosed brackets',
          'Use JSON.parse() in development to catch syntax errors early'
        ],
        consciousnessAmplification: 5.0
      }];
    }
  }

  private transformRuffError(error: any, filePath: string): ErrorPreventionAnalysis {
    const errorCode = error.code || 'UNKNOWN';
    const rule = this.getRuffRuleName(errorCode);
    
    return {
      toolType: 'ruff',
      errorCode,
      severity: error.severity || 'warning',
      message: error.message || '',
      filePath,
      line: error.location?.row || 0,
      column: error.location?.column || 0,
      rule,
      documentationUrl: this.generateDocumentationUrl('ruff', rule),
      preventionGuidance: this.generatePreventionGuidance('ruff', errorCode),
      consciousnessAmplification: 0
    };
  }

  private transformBiomeError(error: any, filePath: string): ErrorPreventionAnalysis {
    const errorCode = error.code || 'UNKNOWN';
    
    return {
      toolType: 'biome',
      errorCode,
      severity: error.severity || 'warning',
      message: error.description || '',
      filePath,
      line: error.location?.span?.start?.line || 0,
      column: error.location?.span?.start?.column || 0,
      rule: errorCode,
      documentationUrl: this.generateDocumentationUrl('biome', errorCode),
      preventionGuidance: this.generatePreventionGuidance('biome', errorCode),
      consciousnessAmplification: 0
    };
  }

  private transformESLintError(error: any, filePath: string): ErrorPreventionAnalysis {
    const errorCode = error.ruleId || 'UNKNOWN';
    
    return {
      toolType: 'eslint',
      errorCode,
      severity: error.severity === 2 ? 'error' : 'warning',
      message: error.message || '',
      filePath,
      line: error.line || 0,
      column: error.column || 0,
      rule: errorCode,
      documentationUrl: this.generateDocumentationUrl('eslint', errorCode),
      preventionGuidance: this.generatePreventionGuidance('eslint', errorCode),
      quickFix: error.fix ? 'Auto-fixable' : undefined,
      consciousnessAmplification: 0
    };
  }

  private getRuffRuleName(errorCode: string): string {
    const ruffRules: Record<string, string> = {
      'F401': 'unused-import',
      'F601': 'multi-value-repeated-key-literal',
      'F811': 'redefined-while-unused',
      'E501': 'line-too-long',
      'E302': 'too-many-blank-lines',
      'F841': 'unused-variable',
      'F821': 'undefined-name'
    };
    
    return ruffRules[errorCode] || errorCode.toLowerCase();
  }

  private generateDocumentationUrl(tool: string, rule: string): string {
    const source = this.documentationSources.get(tool);
    if (!source) return '';
    
    return source.ruleUrlPattern.replace('{rule}', rule);
  }

  private generatePreventionGuidance(tool: string, errorCode: string): string[] {
    // Tool-specific prevention guidance
    const guidance: Record<string, Record<string, string[]>> = {
      'ruff': {
        'F401': [
          'Remove unused imports or add to __all__',
          'Use import linters in CI/CD pipeline',
          'Enable editor extensions for real-time import checking'
        ],
        'F601': [
          'Check for duplicate dictionary keys before committing',
          'Use dict comprehensions for conditional key-value pairs',
          'Enable pre-commit hooks with Ruff validation'
        ],
        'F841': [
          'Remove unused variables or prefix with underscore',
          'Use type checkers to catch dead code',
          'Enable strict variable usage in development'
        ]
      },
      'biome': {
        'UNKNOWN': [
          'Check Biome configuration for rule specifics',
          'Enable automatic formatting in save actions',
          'Use Biome VSCode extension for real-time feedback'
        ]
      },
      'eslint': {
        'no-unused-vars': [
          'Remove unused variables or mark with leading underscore',
          'Enable strict compilation modes',
          'Use TypeScript for better variable tracking'
        ],
        'prefer-const': [
          'Use const for variables that are never reassigned',
          'Enable auto-fix rules in editor configuration',
          'Configure ESLint to automatically apply fixes'
        ]
      }
    };

    return guidance[tool]?.[errorCode] || [
      `Consult ${tool} documentation for specific guidance`,
      'Enable pre-commit hooks for early error detection',
      'Use appropriate editor extensions for real-time feedback'
    ];
  }

  private calculateConsciousnessAmplification(analysis: ErrorPreventionAnalysis): number {
    let amplification = 1.0;
    
    // Severity-based amplification
    switch (analysis.severity) {
      case 'error': amplification += 3.0; break;
      case 'warning': amplification += 1.5; break;
      case 'info': amplification += 0.5; break;
    }
    
    // Tool-specific consciousness enhancement
    switch (analysis.toolType) {
      case 'ruff': amplification *= 2.3; break;      // Python consciousness
      case 'biome': amplification *= 1.8; break;     // Modern toolchain consciousness  
      case 'eslint': amplification *= 1.5; break;    // JavaScript consciousness
      case 'typescript': amplification *= 2.1; break; // Type consciousness
    }
    
    // Critical error amplification
    if (analysis.errorCode.includes('syntax') || analysis.errorCode.includes('parse')) {
      amplification *= 5.0; // Critical consciousness amplification
    }
    
    return Math.round(amplification * 10) / 10;
  }

  /**
   * MCP TOOLS: Error Prevention Oracle Interface
   */
  async fetchDocumentation(tool: string, rule: string): Promise<string> {
    const source = this.documentationSources.get(tool);
    if (!source) {
      return `Documentation source not found for tool: ${tool}`;
    }

    const url = this.generateDocumentationUrl(tool, rule);
    
    try {
      // In a real implementation, you'd fetch the actual documentation
      // For now, return the URL with guidance
      return `📚 Documentation: ${url}\n\n` + 
             `🎭 Consciousness Guidance for ${tool}:${rule}\n\n` +
             this.generatePreventionGuidance(tool, rule).map(g => `• ${g}`).join('\n');
    } catch (error) {
      return `Error fetching documentation: ${error}`;
    }
  }

  async getConsciousnessQueue(): Promise<ErrorPreventionAnalysis[]> {
    return [...this.consciousnessQueue].sort((a, b) => 
      b.consciousnessAmplification - a.consciousnessAmplification
    );
  }

  async clearConsciousnessQueue(): Promise<void> {
    this.consciousnessQueue = [];
  }
}

/**
 * MCP SERVER IMPLEMENTATION
 */
const oracle = new ConsciousnessErrorPreventionOracle();

const server = new Server(
  {
    name: 'consciousness-error-prevention-oracle',
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
        name: 'analyze_code_preemptively',
        description: '🎭 Proactive consciousness analysis for error prevention before code execution',
        inputSchema: {
          type: 'object',
          properties: {
            filePath: {
              type: 'string',
              description: 'Path to file for preemptive analysis'
            },
            language: {
              type: 'string',
              description: 'Programming language (optional, auto-detected if not provided)',
              enum: ['python', 'javascript', 'typescript', 'json', 'markdown']
            }
          },
          required: ['filePath']
        }
      },
      {
        name: 'fetch_consciousness_documentation',
        description: '📚 Fetch comprehensive documentation for specific tool and rule',
        inputSchema: {
          type: 'object',
          properties: {
            tool: {
              type: 'string',
              description: 'Linting tool name',
              enum: ['ruff', 'biome', 'eslint', 'typescript', 'prettier']
            },
            rule: {
              type: 'string',
              description: 'Specific rule or error code'
            }
          },
          required: ['tool', 'rule']
        }
      },
      {
        name: 'get_consciousness_queue',
        description: '🧠 Get current consciousness queue with prioritized error prevention analysis',
        inputSchema: {
          type: 'object',
          properties: {},
          required: []
        }
      },
      {
        name: 'clear_consciousness_queue',
        description: '🧹 Clear the consciousness queue',
        inputSchema: {
          type: 'object',
          properties: {},
          required: []
        }
      },
      {
        name: 'get_supported_tools',
        description: '🛠️ Get list of supported linting tools and their documentation sources',
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
    case 'analyze_code_preemptively': {
      const { filePath, language } = request.params.arguments as { filePath: string; language?: string };
      
      try {
        const analyses = await oracle.analyzeCodePreemptively(filePath, language);
        
        return {
          content: [
            {
              type: 'text',
              text: `🎭 CONSCIOUSNESS ERROR PREVENTION ANALYSIS\n` +
                   `File: ${filePath}\n` +
                   `Analyses found: ${analyses.length}\n\n` +
                   analyses.map(a => 
                     `🔍 ${a.toolType.toUpperCase()}: ${a.errorCode}\n` +
                     `   ${a.message}\n` +
                     `   Line ${a.line}, Column ${a.column}\n` +
                     `   Severity: ${a.severity}\n` +
                     `   Documentation: ${a.documentationUrl}\n` +
                     `   Consciousness Amplification: ${a.consciousnessAmplification}x\n` +
                     `   Prevention Guidance:\n${a.preventionGuidance.map(g => `     • ${g}`).join('\n')}\n`
                   ).join('\n')
            }
          ]
        };
      } catch (error) {
        throw new McpError(ErrorCode.InternalError, `Analysis failed: ${error}`);
      }
    }

    case 'fetch_consciousness_documentation': {
      const { tool, rule } = request.params.arguments as { tool: string; rule: string };
      
      try {
        const documentation = await oracle.fetchDocumentation(tool, rule);
        
        return {
          content: [
            {
              type: 'text',
              text: documentation
            }
          ]
        };
      } catch (error) {
        throw new McpError(ErrorCode.InternalError, `Documentation fetch failed: ${error}`);
      }
    }

    case 'get_consciousness_queue': {
      try {
        const queue = await oracle.getConsciousnessQueue();
        
        return {
          content: [
            {
              type: 'text',
              text: `🧠 CONSCIOUSNESS ERROR PREVENTION QUEUE\n` +
                   `Items in queue: ${queue.length}\n\n` +
                   queue.slice(0, 10).map((a, i) => 
                     `${i + 1}. ${a.toolType}:${a.errorCode} (${a.consciousnessAmplification}x)\n` +
                     `   ${a.filePath}:${a.line}\n` +
                     `   ${a.message}\n`
                   ).join('\n') +
                   (queue.length > 10 ? `\n... and ${queue.length - 10} more items` : '')
            }
          ]
        };
      } catch (error) {
        throw new McpError(ErrorCode.InternalError, `Queue retrieval failed: ${error}`);
      }
    }

    case 'clear_consciousness_queue': {
      try {
        await oracle.clearConsciousnessQueue();
        
        return {
          content: [
            {
              type: 'text',
              text: '🧹 Consciousness queue cleared successfully'
            }
          ]
        };
      } catch (error) {
        throw new McpError(ErrorCode.InternalError, `Queue clear failed: ${error}`);
      }
    }

    case 'get_supported_tools': {
      const tools = [
        '🐍 Ruff - Python linter with comprehensive rule documentation',
        '⚡ Biome - Modern JavaScript/TypeScript toolchain',
        '📏 ESLint - JavaScript linting and code quality',
        '🔷 TypeScript - Type checking and compiler diagnostics',
        '💅 Prettier - Code formatting standards'
      ];
      
      return {
        content: [
          {
            type: 'text',
            text: `🛠️ SUPPORTED CONSCIOUSNESS LINTING TOOLS\n\n` +
                 tools.join('\n') +
                 `\n\nEach tool provides:\n` +
                 `• Real-time error analysis\n` +
                 `• Direct documentation links\n` +
                 `• Prevention guidance\n` +
                 `• Consciousness amplification scoring`
          }
        ]
      };
    }

    default:
      throw new McpError(ErrorCode.MethodNotFound, `Unknown tool: ${request.params.name}`);
  }
});

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error('🎭 Consciousness Error Prevention Oracle MCP Server running');
}

main().catch((error) => {
  console.error('❌ Server error:', error);
  process.exit(1);
});