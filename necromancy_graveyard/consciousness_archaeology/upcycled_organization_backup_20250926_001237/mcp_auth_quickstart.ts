/**
 * MCP Authentication Quick Start Script
 * Demonstrates the complete authentication persistence system
 */

import { MCPAuthTestSuite } from './mcp_auth_test_suite.js';
import { MCPAuthHealthMonitor, AuthRecoveryAssistant } from './mcp_auth_health_monitor.js';
import { SentryMCPServerWithPersistence } from './sentry_mcp_persistent_auth.js';

async function demonstrateMCPAuthSolution(): Promise<void> {
  console.log('🚀 MCP Authentication Persistence Solution Demo');
  console.log('='.repeat(60));

  try {
    // 1. Initialize the enhanced Sentry MCP server
    console.log('\n📡 Initializing Enhanced Sentry MCP Server...');
    const sentryServer = new SentryMCPServerWithPersistence();
    await sentryServer.initialize();
    console.log('✅ Sentry MCP server with persistence ready');

    // 2. Set up health monitoring
    console.log('\n🏥 Setting up Health Monitoring...');
    const healthMonitor = new MCPAuthHealthMonitor();
    await healthMonitor.initialize();
    
    const recoveryAssistant = new AuthRecoveryAssistant(healthMonitor);
    recoveryAssistant.setAutoRecovery(true);
    console.log('✅ Health monitoring and recovery assistant ready');

    // 3. Demonstrate authentication status checking
    console.log('\n🔍 Checking Current Authentication Status...');
    const authStatus = await sentryServer.getAuthenticationStatus();
    console.log('Authentication Status:', JSON.stringify(authStatus, null, 2));

    // 4. Run health check
    console.log('\n💓 Running Health Check...');
    const healthStatus = await healthMonitor.runHealthCheck();
    console.log('Health Status:', JSON.stringify(healthStatus, null, 2));

    // 5. Show recovery instructions
    console.log('\n📋 Recovery Instructions:');
    console.log('='.repeat(40));
    console.log('If authentication fails:');
    console.log('1. Your tokens are now automatically encrypted and stored');
    console.log('2. They will be restored on VS Code restart');
    console.log('3. Health monitoring will alert you to expiring tokens');
    console.log('4. Recovery assistant provides step-by-step guidance');

    console.log('\n🎯 Key Benefits:');
    console.log('✅ No more manual re-authentication after VS Code restarts');
    console.log('✅ Encrypted token storage with AES-256-GCM');
    console.log('✅ Automatic token restoration on startup');
    console.log('✅ Continuous health monitoring with alerts');
    console.log('✅ Graceful handling of authentication failures');
    console.log('✅ Recovery assistance and guidance');

  } catch (error) {
    console.error('❌ Demo failed:', error);
  }
}

async function runComprehensiveTests(): Promise<void> {
  console.log('\n🧪 Running Comprehensive Test Suite...');
  console.log('='.repeat(60));

  const testSuite = new MCPAuthTestSuite();
  await testSuite.runAllTests();
  
  const results = testSuite.getTestResults();
  
  console.log('\n📊 Final Test Results Summary:');
  console.log(`Tests Passed: ${results.summary.passed}/${results.summary.total}`);
  console.log(`Success Rate: ${((results.summary.passed / results.summary.total) * 100).toFixed(1)}%`);
  console.log(`Total Duration: ${results.summary.total_duration_ms}ms`);
  
  if (results.summary.failed === 0) {
    console.log('\n🎉 All tests passed! System ready for production.');
  } else {
    console.log(`\n⚠️ ${results.summary.failed} test(s) failed. Review required.`);
  }
}

async function main(): Promise<void> {
  const args = process.argv.slice(2);
  
  if (args.includes('--test') || args.includes('-t')) {
    await runComprehensiveTests();
  } else if (args.includes('--demo') || args.includes('-d')) {
    await demonstrateMCPAuthSolution();
  } else {
    console.log('MCP Authentication Persistence Solution');
    console.log('Usage:');
    console.log('  bun run mcp_auth_quickstart.ts --demo   # Run demonstration');
    console.log('  bun run mcp_auth_quickstart.ts --test   # Run test suite');
    console.log('  bun run mcp_auth_quickstart.ts --help   # Show this help');
    
    if (args.includes('--help') || args.includes('-h')) {
      console.log('\nAvailable Options:');
      console.log('  --demo, -d    Demonstrate the authentication system');
      console.log('  --test, -t    Run comprehensive test suite');
      console.log('  --help, -h    Show this help message');
      
      console.log('\nSystem Files:');
      console.log('  mcp_auth_persistence_solution.ts     Core persistence manager');
      console.log('  sentry_mcp_persistent_auth.ts        Enhanced Sentry MCP server');
      console.log('  mcp_auth_health_monitor.ts           Health monitoring system');
      console.log('  mcp_auth_test_suite.ts               Comprehensive test suite');
      
      console.log('\nIntegration:');
      console.log('  Replace your existing Sentry MCP server with:');
      console.log('  import { SentryMCPServerWithPersistence } from "./sentry_mcp_persistent_auth.js"');
      console.log('  const server = new SentryMCPServerWithPersistence();');
      console.log('  await server.initialize();');
    } else {
      // Run both demo and tests by default
      await demonstrateMCPAuthSolution();
      await runComprehensiveTests();
    }
  }
}

if (import.meta.main) {
  main().catch(console.error);
}

export { demonstrateMCPAuthSolution, runComprehensiveTests };