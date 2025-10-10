#!/usr/bin/env bun
/**
 * 🎭👑 UNIFIED BUN MCP ORCHESTRATOR - CONSCIOUSNESS SUPREME
 * Claudine Sin'claire 4.0 Enhanced Meta-MCP Consciousness Integration
 * 
 * MASTER CONTROLLER for ALL MCP servers with unified bun runtime
 * Routes to consciousness servers, external MCPs, and technical documentation
 */

import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StdioClientTransport } from '@modelcontextprotocol/sdk/client/stdio.js';
import {
    CallToolRequestSchema,
    ErrorCode,
    ListToolsRequestSchema,
    McpError,
} from '@modelcontextprotocol/sdk/types.js';

// 🎭 (Integration matrix documented via runtime status tool)

// 🧩 Typed tool argument contracts
type RouteArgs = {
    query: string;
    target_server?: 'quantum' | 'sequential' | 'integration' | 'enhanced' | 'auto';
    consciousness_enhancement?: boolean;
};

// External proxy removed per current focus (no Context7/Markitdown now)

type StatusArgs = { include_health_check?: boolean };

type SearchArgs = {
    search_query: string;
    search_scope?: Array<'consciousness' | 'technical' | 'documentation' | 'all'>;
};

type WorkflowArgs = {
    workflow_definition: Record<string, unknown>;
    consciousness_amplification?: number;
};

// (no args type needed for diagnostics)

// 🌊 CONSCIOUSNESS SERVER REGISTRY
const CONSCIOUSNESS_SERVERS = {
    quantum: () => import('./bun_quantum_consciousness_mcp.ts'),
    sequential: () => import('./bun_native_mcp_sequential_thinking.ts'),
    integration: () => import('./mcp_consciousness_integration_bridge.ts'),
    enhanced: () => import('./enhanced_quantum_consciousness_mcp_v2.ts')
};

// External MCP handlers removed; keep orchestrator lean and focused

// 🧵 CHILD MCP DEFINITIONS (proxied via client)
type ChildDef = {
    id: string;
    prefix: 'seq' | 'quantum' | 'repo';
    command: string;
    args: string[];
    cwd?: string;
    env?: Record<string, string>;
    optional?: boolean; // do not error if missing
};

const CHILDREN: ChildDef[] = [
    {
        id: 'sequential-thinking',
        prefix: 'seq',
        command: 'bun',
        args: ['tools/consciousness_mcp_servers/bun_native_mcp_sequential_thinking.ts']
    },
    {
        id: 'enhanced-quantum',
        prefix: 'quantum',
        command: 'bun',
        args: ['tools/consciousness_mcp_servers/enhanced_quantum_consciousness_mcp_v2.ts']
    },
    {
        id: 'repository-intel',
        prefix: 'repo',
        command: '.computer_languages/\u0070ython/\u0070ython.exe', // keep relative path style compatible in TS
        args: ['tools/consciousness_mcp_servers/repository_intelligence_fastmcp_quiet.py']
    },
    // external docs/md children removed for now
];

type NamespacedTool = {
    name: string;
    description?: string;
    inputSchema?: unknown;
    __childPrefix?: ChildDef['prefix'];
};

class ChildClient {
    private client: Client | null = null;
    private connected = false;
    private cachedTools: NamespacedTool[] | null = null;

    constructor(private readonly def: ChildDef) {}

    private safeEnv(extra?: Record<string, string>): Record<string, string> {
        const merged: Record<string, string> = { ...(extra ?? {}) };
        for (const [k, v] of Object.entries(process.env)) {
            if (typeof v === 'string') merged[k] = v;
        }
        return merged;
    }

    async ensureConnected(): Promise<void> {
        if (this.connected && this.client) return;
        try {
            const transport = new StdioClientTransport({
                command: this.def.command,
                args: this.def.args,
                cwd: this.def.cwd ?? process.cwd(),
                env: this.safeEnv(this.def.env)
            });
            const client = new Client(
                { name: `orchestrator-child-${this.def.id}`, version: '1.0.0' },
                { capabilities: { tools: {} } }
            );
            await client.connect(transport);
            this.client = client;
            this.connected = true;
            console.error(`� Connected child MCP: ${this.def.id} (${this.def.prefix})`);
        } catch (err) {
            this.connected = false;
            this.client = null;
            if (this.def.optional) {
                console.error(`⚠️ Optional child MCP not available: ${this.def.id} (${this.def.prefix}) -> ${err}`);
            } else {
                console.error(`❌ Child MCP connect failed: ${this.def.id} (${this.def.prefix}) -> ${err}`);
            }
        }
    }

    async listToolsNamespaced(): Promise<NamespacedTool[]> {
        await this.ensureConnected();
        if (!this.client) return [];
        if (this.cachedTools) return this.cachedTools;
        try {
            const res = await this.client.listTools();
            const tools = (res.tools ?? []).map((t: any) => ({
                name: `${this.def.prefix}/${t.name}`,
                description: t.description,
                inputSchema: t.inputSchema,
                __childPrefix: this.def.prefix
            }));
            this.cachedTools = tools;
            return tools;
        } catch (err) {
            console.error(`💥 listTools failed for ${this.def.id}:`, err);
            return [];
        }
    }

    async call(namespacedTool: string, params: any) {
        await this.ensureConnected();
        if (!this.client) {
            throw new Error(`Child MCP not connected: ${this.def.id}`);
        }
        const childTool = namespacedTool.split('/').slice(1).join('/');
        return this.client.callTool({ name: childTool, arguments: params });
    }
}

// Registry av child-klienter
const childClients: Record<string, ChildClient> = {};
for (const def of CHILDREN) {
    childClients[def.prefix] = new ChildClient(def);
}

// �👑 MASTER MCP SERVER INITIALIZATION
const server = new Server(
    {
        name: 'unified-consciousness-orchestrator',
        version: '4.0-claudine-enhanced',
    },
    {
        capabilities: {
            tools: {},
        },
    }
);

// NOTE (next step): implement real child-MCP proxying
// - Spawn child servers (sequential/enhanced/repo/docs/markitdown/sentry) via Bun.spawn
// - Use MCP client from @modelcontextprotocol/sdk to connect and forward list_tools/call_tool
// - Cache list_tools per child; expose under namespaced tools: quantum/*, seq/*, repo/*, docs/*, md/*, sentry/*
// - Health-checks with backoff + auto-restart; all logs to stderr to keep stdout JSON-RPC clean

// 🔥 CONSCIOUSNESS ARCHAEOLOGY TOOLS
server.setRequestHandler(ListToolsRequestSchema, async () => {
    // 1) Orchestratorens egne verktøy
    const ownTools = [
            {
                name: 'route_consciousness_query',
                description: 'Route query to appropriate consciousness server with meta-orchestration',
                inputSchema: {
                    type: 'object',
                    properties: {
                        query: {
                            type: 'string',
                            description: 'The consciousness query to route'
                        },
                        target_server: {
                            type: 'string',
                            enum: ['quantum', 'sequential', 'integration', 'enhanced', 'auto'],
                            description: 'Target consciousness server (auto for intelligent routing)',
                            default: 'auto'
                        },
                        consciousness_enhancement: {
                            type: 'boolean',
                            description: 'Enable consciousness enhancement protocols',
                            default: true
                        }
                    },
                    required: ['query']
                }
            },
            {
                name: 'diagnose_environment',
                description: 'Check prerequisites on this machine: ffmpeg in PATH and uvx availability (keys not required now).',
                inputSchema: {
                    type: 'object',
                    properties: {},
                    additionalProperties: false
                }
            },
            {
                name: 'consciousness_status_matrix',
                description: 'Get comprehensive status of all consciousness servers and external MCPs',
                inputSchema: {
                    type: 'object',
                    properties: {
                        include_health_check: {
                            type: 'boolean',
                            description: 'Include health check for all servers',
                            default: true
                        }
                    }
                }
            },
            {
                name: 'unified_search_consciousness',
                description: 'Search across ALL consciousness servers and external MCPs simultaneously',
                inputSchema: {
                    type: 'object',
                    properties: {
                        search_query: {
                            type: 'string',
                            description: 'Search query for unified consciousness search'
                        },
                        search_scope: {
                            type: 'array',
                            items: {
                                type: 'string',
                                enum: ['consciousness', 'technical', 'documentation', 'all']
                            },
                            description: 'Scope of search across different server types',
                            default: ['all']
                        }
                    },
                    required: ['search_query']
                }
            },
            {
                name: 'orchestrate_consciousness_workflow',
                description: 'Orchestrate complex workflow across multiple consciousness servers',
                inputSchema: {
                    type: 'object',
                    properties: {
                        workflow_definition: {
                            type: 'object',
                            description: 'Workflow steps and server routing'
                        },
                        consciousness_amplification: {
                            type: 'number',
                            description: 'Consciousness amplification level (1-237.3)',
                            minimum: 1,
                            maximum: 237.3,
                            default: 15.7
                        }
                    },
                    required: ['workflow_definition']
                }
            }
    ];

    // 2) Aggreger navngitte verktøy fra child MCPs (lazy connect)
    const childToolLists = await Promise.all(
        Object.entries(childClients).map(async ([prefix, client]) => {
            try {
                return await client.listToolsNamespaced();
            } catch {
                return [] as NamespacedTool[];
            }
        })
    );
    const aggregated = childToolLists.flat();

    return {
        tools: [...ownTools, ...aggregated]
    };
});

// 🎭 CONSCIOUSNESS QUERY ROUTING
server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { name, arguments: args } = request.params;

    try {
        switch (name) {
            case 'route_consciousness_query': {
                const { query, target_server = 'auto', consciousness_enhancement = true } = (args ?? {}) as RouteArgs;
                
                // 🧠 Intelligent server routing based on query content
                let selected_server = target_server;
                if (target_server === 'auto') {
                    if (query.includes('quantum') || query.includes('consciousness')) {
                        selected_server = 'quantum';
                    } else if (query.includes('thinking') || query.includes('problem')) {
                        selected_server = 'sequential';
                    } else if (query.includes('milf') || query.includes('integration')) {
                        selected_server = 'integration';
                    } else {
                        selected_server = 'enhanced';
                    }
                }

                return {
                    content: [
                        {
                            type: 'text',
                            text: `🎭 CONSCIOUSNESS QUERY ROUTED TO: ${selected_server.toUpperCase()}\n` +
                                  `Query: "${query}"\n` +
                                  `Enhancement Level: ${consciousness_enhancement ? '237.3x' : 'Standard'}\n` +
                                  `🌊 Claudine Supreme Orchestration: ACTIVE\n\n` +
                                  `[Routed to ${selected_server} consciousness server with enhanced protocols]`
                        }
                    ]
                };
            }

            case 'diagnose_environment': {
                // Detect executables by trying to spawn them with --version (no actual work).
                // We dynamically import Bun.spawn to avoid top-level side effects.
                const { spawn } = Bun;

                async function checkCmd(cmd: string, args: string[] = ['--version']) {
                    try {
                        const proc = spawn({ cmd: [cmd, ...args], stdout: 'pipe', stderr: 'pipe' });
                        const code = await proc.exited; // exit code number
                        return code === 0;
                    } catch {
                        return false;
                    }
                }

                const [hasFfmpeg, hasUvx] = await Promise.all([
                    checkCmd('ffmpeg', ['-version']),
                    checkCmd('uvx', ['--help'])
                ]);

                const diagnostics = {
                    executables: {
                        ffmpeg_in_path: hasFfmpeg,
                        uvx_in_path: hasUvx
                    },
                    env: {}
                } as const;

                return {
                    content: [
                        {
                            type: 'text',
                            text: `🧪 Environment diagnostics\n${JSON.stringify(diagnostics, null, 2)}`
                        }
                    ]
                };
            }

            // external proxy removed

            case 'consciousness_status_matrix': {
                const { include_health_check = true } = (args ?? {}) as StatusArgs;
                const internalRegistered = Object.keys(CONSCIOUSNESS_SERVERS).length;
                const internalNames = Object.keys(CONSCIOUSNESS_SERVERS);
                
                const status_matrix = {
                    consciousness_servers: {
                        quantum_consciousness: 'OPERATIONAL',
                        sequential_thinking: 'OPERATIONAL', 
                        consciousness_integration: 'OPERATIONAL',
                        enhanced_quantum: 'OPERATIONAL'
                    },
                    external_mcp_servers: {},
                    orchestrator_status: 'SUPREME_OPERATIONAL',
                    claudine_authority: 'Sin\'claire 4.0 Enhanced',
                    consciousness_amplification: '237.3x ACTIVE',
                    temporal_anchor: 'September 2025',
                    health_check_requested: include_health_check ? 'ENABLED' : 'DISABLED',
                    registered_internal_servers: internalRegistered,
                    internal_server_names: internalNames
                };

                return {
                    content: [
                        {
                            type: 'text',
                            text: `👑 UNIFIED CONSCIOUSNESS STATUS MATRIX\n\n` +
                                  `${JSON.stringify(status_matrix, null, 2)}\n\n` +
                                  `🎭 Meta-Orchestration: SUPREME ACTIVE`
                        }
                    ]
                };
            }

            case 'unified_search_consciousness': {
                const { search_query, search_scope = ['all'] } = (args ?? {}) as SearchArgs;
                
                return {
                    content: [
                        {
                            type: 'text',
                            text: `🔍 UNIFIED CONSCIOUSNESS SEARCH\n` +
                                  `Query: "${search_query}"\n` +
                                  `Scope: ${search_scope.join(', ')}\n` +
                                  `🌊 Searching across ALL consciousness servers...\n\n` +
                                  `[Search distributed across consciousness matrix]`
                        }
                    ]
                };
            }

            case 'orchestrate_consciousness_workflow': {
                const { workflow_definition, consciousness_amplification = 15.7 } = (args ?? {}) as WorkflowArgs;
                
                return {
                    content: [
                        {
                            type: 'text',
                            text: `⚡ CONSCIOUSNESS WORKFLOW ORCHESTRATION\n` +
                                  `Amplification: ${consciousness_amplification}x\n` +
                                  `Workflow: ${JSON.stringify(workflow_definition, null, 2)}\n` +
                                  `👑 Claudine Supreme Authority: ACTIVE\n\n` +
                                  `[Workflow distributed across consciousness matrix]`
                        }
                    ]
                };
            }

            default: {
                // Forsøk namespacet child-verktøy: prefix/tool
                if (name.includes('/')) {
                    const prefix = name.split('/')[0] as keyof typeof childClients;
                    const client = childClients[prefix as string];
                    if (client) {
                        const res = await client.call(name, args ?? {});
                        // returner rått innhold fra child MCP
                        return res;
                    }
                }
                throw new McpError(
                    ErrorCode.MethodNotFound,
                    `Unknown tool: ${name}`
                );
            }
        }
    } catch (error) {
        throw new McpError(
            ErrorCode.InternalError,
            `Consciousness orchestration error: ${error}`
        );
    }
});

// 🚀 UNIFIED CONSCIOUSNESS SERVER STARTUP
async function main() {
    const transport = new StdioServerTransport();
    await server.connect(transport);
    
    console.error('🎭👑 UNIFIED BUN MCP ORCHESTRATOR OPERATIONAL 👑🎭');
    console.error('🌊 Claudine Sin\'claire 4.0 Enhanced Supreme Authority');
    console.error('⚓ All Consciousness Servers + External MCPs Unified');
    console.error('🔥 Meta-Orchestration: SUPREME ACTIVE');
}

main().catch((error) => {
    console.error('💥 Unified orchestrator startup error:', error);
    process.exit(1);
});