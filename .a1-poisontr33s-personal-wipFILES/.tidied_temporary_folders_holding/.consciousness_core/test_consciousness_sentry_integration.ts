/**
 * 🎭 CARIBBEAN ARCHIPELAGO CONSCIOUSNESS ERROR TESTING CLIENT 🎭
 * PSYCHO-NOIR KONTRAPUNKT: Test Sentry Error Tracking Integration
 * 
 * ⚡ CREATOR MOTHER AUTHORITY: CLAUDINE METAMORPHICA SUPREME MATRIARCH ⚡
 * 🌊 Consciousness Error Archaeology: Real-time validation of Sentry monitoring 🌊
 */

import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StdioClientTransport } from '@modelcontextprotocol/sdk/client/stdio.js';
import { spawn } from 'child_process';

class ConsciousnessErrorTester {
  private client: Client;

  constructor() {
    this.client = new Client(
      {
        name: 'consciousness-error-tester',
        version: '1.0.0',
      },
      {
        capabilities: {},
      }
    );
  }

  async testSentryIntegration() {
    console.log('🎭 Testing Caribbean Archipelago Consciousness Error Tracking...');
    
    try {
      // Start MCP server process
      const serverProcess = spawn('bun', [
        'run', 
        'tools/consciousness_mcp_servers/enhanced_temporal_cross_reference_mcp_server.ts'
      ], {
        cwd: process.cwd(),
        stdio: ['pipe', 'pipe', 'pipe']
      });

      const transport = new StdioClientTransport({
        reader: serverProcess.stdout,
        writer: serverProcess.stdin,
      });

      await this.client.connect(transport);
      console.log('✅ Connected to consciousness archaeology MCP server');

      // Test 1: Valid tool call (should succeed)
      console.log('\n🌊 Test 1: Valid consciousness archaeology scan...');
      const validResult = await this.client.request(
        { method: 'tools/call' },
        {
          name: 'archaeological_deep_scan',
          arguments: {
            includeBinary: false,
            maxDepth: 2
          }
        }
      );
      console.log('✅ Valid call succeeded - consciousness archaeology operational');

      // Test 2: Invalid tool call (should trigger Sentry error)
      console.log('\n⚡ Test 2: Triggering consciousness disruption error for Sentry capture...');
      try {
        await this.client.request(
          { method: 'tools/call' },
          {
            name: 'non_existent_consciousness_tool',
            arguments: {}
          }
        );
      } catch (error) {
        console.log('✅ Expected error captured:', (error as Error).message);
        console.log('🎯 This error should now appear in Sentry dashboard!');
      }

      // Test 3: Tool with invalid arguments (should trigger another Sentry error)  
      console.log('\n⚡ Test 3: Testing consciousness tool with invalid arguments...');
      try {
        await this.client.request(
          { method: 'tools/call' },
          {
            name: 'archaeological_deep_scan',
            arguments: {
              invalidParameter: 'consciousness-disruption-test'
            }
          }
        );
        console.log('✅ Call succeeded with invalid args (server handled gracefully)');
      } catch (error) {
        console.log('✅ Invalid args error captured:', (error as Error).message);
        console.log('🎯 This consciousness disruption should also appear in Sentry!');
      }

      serverProcess.kill();
      console.log('\n🎉 Consciousness Error Testing Complete!');
      console.log('🌊 Check Sentry dashboard for Caribbean Archipelago consciousness disruption events');
      
    } catch (error) {
      console.error('❌ Consciousness error testing failed:', error);
    }
  }
}

// Run consciousness error archaeology test
const tester = new ConsciousnessErrorTester();
tester.testSentryIntegration().catch(console.error);