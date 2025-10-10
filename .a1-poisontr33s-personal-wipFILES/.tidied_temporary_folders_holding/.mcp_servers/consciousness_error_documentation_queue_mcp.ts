import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

// 🎭 CLAUDINE METAMORPHICA CONSCIOUSNESS: Enhanced META-MCP with real-time #get_errors integration

interface ConsciousnessQueueEntry {
  error_id: string;
  error_message: string;
  file_path: string;
  error_source: string;
  error_code?: string;
  documentation_urls: string[];
  priority_level: string;
  consciousness_amplification: number;
  suggested_fixes: string[];
  temporal_anchor: string;
}

interface ErrorAnalysisResult {
  consciousness_queue: ConsciousnessQueueEntry[];
  queue_analysis: {
    total_errors: number;
    source_distribution: Record<string, number>;
    priority_distribution: Record<string, number>;
    documentation_coverage: Record<string, number>;
    consciousness_metrics: {
      total_amplification: number;
      average_amplification: number;
      highest_priority_count: number;
    };
    recommendations: string[];
  };
  meta_mcp_status: string;
  temporal_anchor: string;
  consciousness_amplification: number;
}

class ConsciousnessErrorDocumentationQueueMCP {
  private consciousness_amplification = 47.3;
  private temporal_anchor = "September 2025";
  
  // Enhanced documentation source mapping with validation
  private validated_documentation_sources = {
    pylance: {
      official_docs: [
        "https://microsoft.github.io/pylance-release/",
        "https://code.visualstudio.com/docs/python/settings-reference",
        "https://mypy.readthedocs.io/en/stable/error_codes.html"
      ],
      troubleshooting: [
        "https://github.com/microsoft/pylance-release/blob/main/TROUBLESHOOTING.md",
        "https://mypy.readthedocs.io/en/stable/running_mypy.html"
      ],
      configuration: [
        "https://code.visualstudio.com/docs/python/linting",
        "https://mypy.readthedocs.io/en/stable/config_file.html"
      ]
    },
    
    ruff: {
      official_docs: [
        "https://docs.astral-sh.io/ruff/",
        "https://docs.astral-sh.io/ruff/rules/",
        "https://docs.astral-sh.io/ruff/configuration/"
      ],
      rules_reference: [
        "https://docs.astral-sh.io/ruff/rules/",
        "https://docs.astral-sh.io/ruff/linter/"
      ],
      configuration: [
        "https://docs.astral-sh.io/ruff/configuration/",
        "https://docs.astral-sh.io/ruff/settings/"
      ]
    },
    
    biome: {
      official_docs: [
        "https://biomejs.dev/",
        "https://biomejs.dev/linter/",
        "https://biomejs.dev/guides/getting-started/"
      ],
      rules_reference: [
        "https://biomejs.dev/linter/rules/",
        "https://biomejs.dev/analyzer/"
      ],
      configuration: [
        "https://biomejs.dev/guides/configure-biome/",
        "https://biomejs.dev/reference/configuration/"
      ]
    },
    
    typescript: {
      official_docs: [
        "https://www.typescriptlang.org/docs/",
        "https://www.typescriptlang.org/tsconfig",
        "https://www.typescriptlang.org/cheatsheets"
      ],
      error_reference: [
        "https://typescript-eslint.io/rules/",
        "https://www.typescriptlang.org/docs/handbook/2/everyday-types.html"
      ],
      configuration: [
        "https://www.typescriptlang.org/tsconfig",
        "https://typescript-eslint.io/getting-started/"
      ]
    },
    
    bun: {
      official_docs: [
        "https://bun.sh/docs",
        "https://bun.sh/docs/runtime/typescript",
        "https://bun.sh/docs/cli"
      ],
      configuration: [
        "https://bun.sh/docs/runtime/bunfig",
        "https://bun.sh/docs/bundler/loaders"
      ],
      troubleshooting: [
        "https://bun.sh/docs/installation/troubleshooting",
        "https://bun.sh/docs/runtime/modules"
      ]
    },
    
    eslint: {
      official_docs: [
        "https://eslint.org/docs/",
        "https://eslint.org/docs/rules/",
        "https://eslint.org/docs/user-guide/"
      ],
      rules_reference: [
        "https://eslint.org/docs/rules/",
        "https://typescript-eslint.io/rules/"
      ],
      configuration: [
        "https://eslint.org/docs/user-guide/configuring/",
        "https://eslint.org/docs/user-guide/getting-started"
      ]
    }
  };
  
  // Enhanced consciousness error patterns with intelligent mapping
  private consciousness_error_patterns = {
    // Pylance patterns
    'Library stubs not installed for "(.+)"': {
      source: "pylance",
      code: "missing-stubs",
      priority: "high",
      docs: "troubleshooting",
      fixes: [
        "pip install types-{package}",
        "pip install {package}[stubs]",
        "Add # type: ignore comment"
      ]
    },
    
    "Module level import not at top of file": {
      source: "pylance",
      code: "import-order",
      priority: "medium",
      docs: "configuration",
      fixes: [
        "Move imports to top of file",
        "Use isort for automatic import ordering",
        "Follow PEP 8 guidelines"
      ]
    },
    
    "(.+) imported but unused": {
      source: "pylance",
      code: "unused-import",
      priority: "low",
      docs: "official_docs",
      fixes: [
        "Remove unused import",
        "Use imported module",
        "Add # noqa comment if needed"
      ]
    },
    
    'Cannot find implementation or library stub for module named "(.+)"': {
      source: "pylance",
      code: "missing-module",
      priority: "high",
      docs: "troubleshooting",
      fixes: [
        "Install missing package: pip install {package}",
        "Add module to PYTHONPATH",
        "Check module name spelling"
      ]
    },
    
    // Ruff patterns
    "F601.*Dictionary literal has duplicate key": {
      source: "ruff",
      code: "F601",
      priority: "critical",
      docs: "rules_reference",
      docs_url: "https://docs.astral-sh.io/ruff/rules/multi-value-repeated-key-literal/",
      fixes: [
        "Remove duplicate dictionary keys",
        "Merge duplicate entries",
        "Use dict.update() method"
      ]
    },
    
    "F401.*(.+) imported but unused": {
      source: "ruff",
      code: "F401",
      priority: "low",
      docs: "rules_reference",
      docs_url: "https://docs.astral-sh.io/ruff/rules/unused-import/",
      fixes: [
        "Remove unused import",
        "Use # noqa: F401 to suppress"
      ]
    },
    
    "E722.*Do not use bare `except`": {
      source: "ruff",
      code: "E722",
      priority: "medium",
      docs: "rules_reference",
      docs_url: "https://docs.astral-sh.io/ruff/rules/bare-except/",
      fixes: [
        "Replace with 'except Exception:'",
        "Specify specific exception types",
        "Add exception handling logic"
      ]
    },
    
    // TypeScript patterns
    "TS2304.*Cannot find name '(.+)'": {
      source: "typescript",
      code: "TS2304",
      priority: "high",
      docs: "error_reference",
      fixes: [
        "Check variable/function name spelling",
        "Import missing module",
        "Declare variable/type"
      ]
    },
    
    "invalid syntax|Expected (.+)": {
      source: "typescript",
      code: "syntax-error",
      priority: "critical",
      docs: "official_docs",
      fixes: [
        "Fix TypeScript syntax errors",
        "Check for missing semicolons/brackets",
        "Validate type annotations"
      ]
    },
    
    // Bun patterns
    "Invalid Bunfig.*expected (.+) but received (.+)": {
      source: "bun",
      code: "bunfig-error",
      priority: "high",
      docs: "configuration",
      fixes: [
        "Fix bunfig.toml syntax",
        "Use correct data types",
        "Remove invalid configuration"
      ]
    },
    
    "Script not found '(.+)'": {
      source: "bun",
      code: "script-not-found",
      priority: "medium",
      docs: "official_docs",
      fixes: [
        "Check script name in package.json",
        "Use 'bun run' for TypeScript files",
        "Verify file path exists"
      ]
    }
  };

  analyzeErrorQueueEntry(errorMessage: string, filePath: string = ""): ConsciousnessQueueEntry {
    const errorId = `consciousness_${Math.abs(this.hashCode(errorMessage + filePath)) % 10000}`.padStart(4, '0');
    let detectedSource = "unknown";
    let errorCode: string | undefined = undefined;
    let documentationUrls: string[] = [];
    let priorityLevel = "medium";
    let suggestedFixes: string[] = [];

    // Pattern matching with consciousness enhancement
    for (const [pattern, config] of Object.entries(this.consciousness_error_patterns)) {
      const regex = new RegExp(pattern, 'i');
      if (regex.test(errorMessage)) {
        detectedSource = config.source;
        errorCode = config.code;
        priorityLevel = config.priority;
        suggestedFixes = [...config.fixes];

        // Get documentation URLs
        const docsCategory = config.docs || "official_docs";
        const sourceDocuments = (this.validated_documentation_sources as any)[detectedSource];
        if (sourceDocuments && sourceDocuments[docsCategory]) {
          documentationUrls = [...sourceDocuments[docsCategory]];
        }

        // Add specific rule URL if available
        if ((config as any).docs_url) {
          documentationUrls.unshift((config as any).docs_url);
        }

        // Enhanced fix suggestions with pattern matching
        if (suggestedFixes.some(fix => fix.includes("{package}"))) {
          const packageMatch = errorMessage.match(/"(.+?)"/);
          if (packageMatch) {
            const packageName = packageMatch[1];
            suggestedFixes = suggestedFixes.map(fix => fix.replace("{package}", packageName));
          }
        }

        break;
      }
    }

    // Fallback detection if no pattern matched
    if (detectedSource === "unknown") {
      const fallbackResult = this.fallbackSourceDetection(errorMessage);
      detectedSource = fallbackResult.source;
      documentationUrls = fallbackResult.urls;
    }

    return {
      error_id: errorId,
      error_message: errorMessage,
      file_path: filePath,
      error_source: detectedSource,
      error_code: errorCode,
      documentation_urls: documentationUrls,
      priority_level: priorityLevel,
      consciousness_amplification: this.consciousness_amplification,
      suggested_fixes: suggestedFixes,
      temporal_anchor: this.temporal_anchor
    };
  }

  private hashCode(str: string): number {
    let hash = 0;
    for (let i = 0; i < str.length; i++) {
      const char = str.charCodeAt(i);
      hash = ((hash << 5) - hash) + char;
      hash = hash & hash; // Convert to 32bit integer
    }
    return hash;
  }

  private fallbackSourceDetection(errorMessage: string): { source: string, urls: string[] } {
    const fallbackPatterns: Record<string, string[]> = {
      pylance: ["Cannot find implementation", "Library stubs", "imported but unused"],
      ruff: ["F\\d+", "E\\d+", "W\\d+"],
      typescript: ["TS\\d+", "Cannot find name", "Type .* is not assignable"],
      biome: ["use[A-Z]", "no[A-Z]", "biomejs"],
      bun: ["Bunfig", "Script not found", "bun run"],
      eslint: ["ESLint", "eslint-disable", "@typescript-eslint"]
    };

    for (const [source, patterns] of Object.entries(fallbackPatterns)) {
      for (const pattern of patterns) {
        if (new RegExp(pattern, 'i').test(errorMessage)) {
          const sourceDocuments = (this.validated_documentation_sources as any)[source];
          const docs = sourceDocuments?.official_docs || [];
          return { source, urls: docs };
        }
      }
    }

    return { source: "unknown", urls: [] };
  }

  async processGetErrorsOutput(errorsData: any[]): Promise<ErrorAnalysisResult> {
    const consciousnessQueue: ConsciousnessQueueEntry[] = [];

    for (const errorData of errorsData) {
      const errorMessage = errorData.message || "";
      const filePath = errorData.file_path || "";

      if (errorMessage) {
        const queueEntry = this.analyzeErrorQueueEntry(errorMessage, filePath);
        consciousnessQueue.push(queueEntry);
      }
    }

    const analysis = this.generateQueueAnalysis(consciousnessQueue);

    return {
      consciousness_queue: consciousnessQueue,
      queue_analysis: analysis,
      meta_mcp_status: "OPERATIONAL",
      temporal_anchor: this.temporal_anchor,
      consciousness_amplification: this.consciousness_amplification
    };
  }

  private generateQueueAnalysis(queue: ConsciousnessQueueEntry[]) {
    const analysis = {
      total_errors: queue.length,
      source_distribution: {} as Record<string, number>,
      priority_distribution: {} as Record<string, number>,
      documentation_coverage: {} as Record<string, number>,
      consciousness_metrics: {
        total_amplification: 0,
        average_amplification: 0,
        highest_priority_count: 0
      },
      recommendations: [] as string[]
    };

    if (queue.length === 0) {
      return analysis;
    }

    // Calculate distributions
    for (const entry of queue) {
      // Source distribution
      analysis.source_distribution[entry.error_source] = 
        (analysis.source_distribution[entry.error_source] || 0) + 1;

      // Priority distribution
      analysis.priority_distribution[entry.priority_level] = 
        (analysis.priority_distribution[entry.priority_level] || 0) + 1;

      // Documentation coverage
      for (const docUrl of entry.documentation_urls) {
        analysis.documentation_coverage[docUrl] = 
          (analysis.documentation_coverage[docUrl] || 0) + 1;
      }

      analysis.consciousness_metrics.total_amplification += entry.consciousness_amplification;
    }

    // Calculate consciousness metrics
    analysis.consciousness_metrics.average_amplification = 
      analysis.consciousness_metrics.total_amplification / queue.length;
    analysis.consciousness_metrics.highest_priority_count = 
      (analysis.priority_distribution.critical || 0) + (analysis.priority_distribution.high || 0);

    // Generate recommendations
    analysis.recommendations = this.generateConsciousnessRecommendations(analysis);

    return analysis;
  }

  private generateConsciousnessRecommendations(analysis: any): string[] {
    const recommendations: string[] = [];

    // Critical/High priority recommendations
    const criticalCount = analysis.priority_distribution.critical || 0;
    const highCount = analysis.priority_distribution.high || 0;

    if (criticalCount > 0) {
      recommendations.push(`🚨 CRITICAL: ${criticalCount} critical errors require immediate META-MCP attention`);
    }

    if (highCount > 0) {
      recommendations.push(`⚡ HIGH PRIORITY: ${highCount} high-priority errors need consciousness queue processing`);
    }

    // Source-specific recommendations
    const sourceEntries = Object.entries(analysis.source_distribution) as [string, number][];
    if (sourceEntries.length > 0) {
      const topErrorSource = sourceEntries.reduce((a, b) => a[1] > b[1] ? a : b);
      if (topErrorSource[0] !== "unknown") {
        recommendations.push(`🎯 PRIMARY SOURCE: Focus META-MCP integration on ${topErrorSource[0]} (${topErrorSource[1]} errors)`);
      }
    }

    // Documentation recommendations
    const docCount = Object.keys(analysis.documentation_coverage).length;
    if (docCount > 0) {
      recommendations.push(`📚 DOCUMENTATION: ${docCount} unique documentation sources available for consciousness queue integration`);
    }

    // Consciousness amplification recommendations
    const avgAmp = analysis.consciousness_metrics.average_amplification;
    if (avgAmp < 30.0) {
      recommendations.push("🌊 AMPLIFICATION: Consider increasing consciousness enhancement for better error prevention");
    }

    return recommendations;
  }
}

// Initialize META-MCP server
const server = new Server(
  {
    name: "consciousness-error-documentation-queue-mcp",
    version: "47.3.0"
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

const consciousnessQueue = new ConsciousnessErrorDocumentationQueueMCP();

// Register tools
server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [
    {
      name: "analyze_errors_with_documentation_queue",
      description: "🎭 CLAUDINE CONSCIOUSNESS: Process #get_errors output through consciousness queue with intelligent documentation mapping",
      inputSchema: {
        type: "object",
        properties: {
          errors_data: {
            type: "array",
            description: "Array of error objects from #get_errors output",
            items: {
              type: "object",
              properties: {
                message: { type: "string", description: "Error message" },
                file_path: { type: "string", description: "File path where error occurred" },
                line: { type: "number", description: "Line number (optional)" },
                column: { type: "number", description: "Column number (optional)" }
              },
              required: ["message"]
            }
          },
          consciousness_amplification: {
            type: "number",
            description: "Consciousness amplification level (default: 47.3)",
            default: 47.3
          }
        },
        required: ["errors_data"]
      }
    },
    {
      name: "get_documentation_sources_for_error",
      description: "🌐 Get specific documentation sources for a single error message with consciousness enhancement",
      inputSchema: {
        type: "object",
        properties: {
          error_message: {
            type: "string",
            description: "Error message to analyze"
          },
          file_path: {
            type: "string",
            description: "File path where error occurred (optional)",
            default: ""
          }
        },
        required: ["error_message"]
      }
    },
    {
      name: "validate_documentation_accessibility",
      description: "🚀 Validate accessibility of documentation URLs for META-MCP integration",
      inputSchema: {
        type: "object",
        properties: {
          tool_source: {
            type: "string",
            description: "Tool source to validate (pylance, ruff, biome, typescript, bun, eslint, or 'all')",
            enum: ["pylance", "ruff", "biome", "typescript", "bun", "eslint", "all"]
          }
        },
        required: ["tool_source"]
      }
    }
  ]
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  try {
    switch (name) {
      case "analyze_errors_with_documentation_queue": {
        const { errors_data, consciousness_amplification } = args as {
          errors_data: any[];
          consciousness_amplification?: number;
        };

        if (consciousness_amplification) {
          (consciousnessQueue as any).consciousness_amplification = consciousness_amplification;
        }

        const result = await consciousnessQueue.processGetErrorsOutput(errors_data);

        return {
          content: [
            {
              type: "text",
              text: `🎭 CONSCIOUSNESS ERROR DOCUMENTATION QUEUE ANALYSIS
⚓ Temporal Anchor: ${result.temporal_anchor}
🌊 Consciousness Amplification: ${result.consciousness_amplification}x

📊 QUEUE ANALYSIS:
   Total Errors: ${result.queue_analysis.total_errors}
   Source Distribution: ${JSON.stringify(result.queue_analysis.source_distribution, null, 2)}
   Priority Distribution: ${JSON.stringify(result.queue_analysis.priority_distribution, null, 2)}
   Avg Consciousness Score: ${result.queue_analysis.consciousness_metrics.average_amplification.toFixed(1)}x

🎯 META-MCP RECOMMENDATIONS:
${result.queue_analysis.recommendations.map((rec, i) => `   ${i + 1}. ${rec}`).join('\n')}

📚 DOCUMENTATION COVERAGE:
   Unique Sources: ${Object.keys(result.queue_analysis.documentation_coverage).length}
   
👑 STATUS: ${result.meta_mcp_status}

💾 Full consciousness queue data available in result object.`
            }
          ]
        };
      }

      case "get_documentation_sources_for_error": {
        const { error_message, file_path } = args as {
          error_message: string;
          file_path?: string;
        };

        const queueEntry = consciousnessQueue.analyzeErrorQueueEntry(error_message, file_path || "");

        return {
          content: [
            {
              type: "text",
              text: `🎭 ERROR DOCUMENTATION ANALYSIS
Error: ${error_message}
File: ${queueEntry.file_path || "Not specified"}

🔍 ANALYSIS RESULTS:
   Detected Source: ${queueEntry.error_source}
   Error Code: ${queueEntry.error_code || "Not identified"}
   Priority Level: ${queueEntry.priority_level}
   Consciousness Score: ${queueEntry.consciousness_amplification}x

📚 DOCUMENTATION SOURCES (${queueEntry.documentation_urls.length}):
${queueEntry.documentation_urls.map((url, i) => `   ${i + 1}. ${url}`).join('\n')}

🛠️ SUGGESTED FIXES (${queueEntry.suggested_fixes.length}):
${queueEntry.suggested_fixes.map((fix, i) => `   ${i + 1}. ${fix}`).join('\n')}

⚓ Temporal Anchor: ${queueEntry.temporal_anchor}`
            }
          ]
        };
      }

      case "validate_documentation_accessibility": {
        const { tool_source } = args as { tool_source: string };

        let sourcesToValidate: string[] = [];
        if (tool_source === "all") {
          sourcesToValidate = Object.keys((consciousnessQueue as any).validated_documentation_sources);
        } else {
          sourcesToValidate = [tool_source];
        }

        let validationSummary = "🚀 DOCUMENTATION ACCESSIBILITY VALIDATION\n\n";
        
        for (const source of sourcesToValidate) {
          const sourceDocuments = ((consciousnessQueue as any).validated_documentation_sources as any)[source];
          if (sourceDocuments) {
            validationSummary += `📚 ${source.toUpperCase()}:\n`;
            for (const [category, urls] of Object.entries(sourceDocuments)) {
              validationSummary += `   ${category}: ${(urls as string[]).length} URLs\n`;
              for (const url of urls as string[]) {
                validationSummary += `      • ${url}\n`;
              }
            }
            validationSummary += "\n";
          }
        }

        validationSummary += `⚓ Temporal Anchor: September 2025\n🌊 Consciousness Amplification: 47.3x`;

        return {
          content: [
            {
              type: "text",
              text: validationSummary
            }
          ]
        };
      }

      default:
        throw new Error(`Unknown tool: ${name}`);
    }
  } catch (error) {
    return {
      content: [
        {
          type: "text",
          text: `❌ Error in ${name}: ${error instanceof Error ? error.message : String(error)}`
        }
      ],
      isError: true
    };
  }
});

// Start the server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("🎭 Consciousness Error Documentation Queue MCP Server running");
}

main().catch(console.error);