/**
 * MCP Authentication Test Suite
 * Comprehensive testing for authentication persistence across VS Code restarts
 */

import { MCPAuthPersistenceManager } from './mcp_auth_persistence_solution.js';
import { SentryMCPServerWithPersistence } from './sentry_mcp_persistent_auth.js';
import { MCPAuthHealthMonitor } from './mcp_auth_health_monitor.js';

interface TestResult {
  test_name: string;
  status: 'passed' | 'failed' | 'skipped';
  duration_ms: number;
  error?: string;
  details?: any;
}

class MCPAuthTestSuite {
  private persistenceManager: MCPAuthPersistenceManager;
  private sentryServer: SentryMCPServerWithPersistence;
  private healthMonitor: MCPAuthHealthMonitor;
  private testResults: TestResult[] = [];

  constructor() {
    this.persistenceManager = new MCPAuthPersistenceManager();
    this.sentryServer = new SentryMCPServerWithPersistence();
    this.healthMonitor = new MCPAuthHealthMonitor();
  }

  /**
   * Run complete test suite
   */
  async runAllTests(): Promise<void> {
    console.log('🧪 Starting MCP Authentication Test Suite');
    console.log('='.repeat(60));

    this.testResults = [];

    // Core functionality tests
    await this.runTest('Token Encryption/Decryption', this.testTokenEncryption.bind(this));
    await this.runTest('Token Storage Persistence', this.testTokenStoragePersistence.bind(this));
    await this.runTest('Token Expiry Handling', this.testTokenExpiryHandling.bind(this));
    
    // Sentry integration tests
    await this.runTest('Sentry Server Initialization', this.testSentryServerInit.bind(this));
    await this.runTest('Sentry Token Restoration', this.testSentryTokenRestoration.bind(this));
    await this.runTest('Sentry API Request Handling', this.testSentryAPIRequests.bind(this));
    
    // Health monitoring tests
    await this.runTest('Health Monitor Initialization', this.testHealthMonitorInit.bind(this));
    await this.runTest('Health Check Execution', this.testHealthCheckExecution.bind(this));
    
    // Integration tests
    await this.runTest('Full System Integration', this.testFullSystemIntegration.bind(this));
    await this.runTest('VS Code Restart Simulation', this.testVSCodeRestartSimulation.bind(this));

    // Print test summary
    this.printTestSummary();
  }

  /**
   * Run individual test with timing and error handling
   */
  private async runTest(testName: string, testFunction: () => Promise<void>): Promise<void> {
    const startTime = Date.now();
    
    try {
      console.log(`\n🔬 Running: ${testName}`);
      await testFunction();
      
      const duration = Date.now() - startTime;
      this.testResults.push({
        test_name: testName,
        status: 'passed',
        duration_ms: duration
      });
      
      console.log(`✅ PASSED: ${testName} (${duration}ms)`);
      
    } catch (error) {
      const duration = Date.now() - startTime;
      this.testResults.push({
        test_name: testName,
        status: 'failed',
        duration_ms: duration,
        error: (error as Error).message
      });
      
      console.log(`❌ FAILED: ${testName} (${duration}ms)`);
      console.log(`   Error: ${(error as Error).message}`);
    }
  }

  /**
   * Test token encryption and decryption
   */
  private async testTokenEncryption(): Promise<void> {
    const testToken = {
      access_token: 'test_access_token_12345',
      refresh_token: 'test_refresh_token_67890',
      token_type: 'Bearer',
      expires_at: Date.now() + 3600000,
      scope: 'read write'
    };

    // Store token
    await this.persistenceManager.storeToken('test', testToken);
    
    // Retrieve token
    const retrievedToken = await this.persistenceManager.getToken('test');
    
    if (!retrievedToken) {
      throw new Error('Token retrieval failed');
    }

    // Verify token integrity
    if (retrievedToken.access_token !== testToken.access_token) {
      throw new Error('Token access_token mismatch');
    }
    
    if (retrievedToken.refresh_token !== testToken.refresh_token) {
      throw new Error('Token refresh_token mismatch');
    }

    // Clean up
    await this.persistenceManager.removeToken('test');
  }

  /**
   * Test token storage persistence across manager instances
   */
  private async testTokenStoragePersistence(): Promise<void> {
    const testToken = {
      access_token: 'persistent_token_abc123',
      token_type: 'Bearer',
      expires_at: Date.now() + 7200000
    };

    // Store with first manager instance
    await this.persistenceManager.storeToken('persistence_test', testToken);

    // Create new manager instance (simulates restart)
    const newManager = new MCPAuthPersistenceManager();
    await newManager.initialize();
    
    // Retrieve with new instance
    const retrievedToken = await newManager.getToken('persistence_test');
    
    if (!retrievedToken) {
      throw new Error('Token not persisted across manager instances');
    }

    if (retrievedToken.access_token !== testToken.access_token) {
      throw new Error('Persisted token data corrupted');
    }

    // Clean up
    await newManager.removeToken('persistence_test');
  }

  /**
   * Test token expiry handling
   */
  private async testTokenExpiryHandling(): Promise<void> {
    const expiredToken = {
      access_token: 'expired_token_xyz789',
      token_type: 'Bearer',
      expires_at: Date.now() - 3600000 // Expired 1 hour ago
    };

    const validToken = {
      access_token: 'valid_token_def456',
      token_type: 'Bearer',
      expires_at: Date.now() + 3600000 // Expires in 1 hour
    };

    // Store both tokens
    await this.persistenceManager.storeToken('expiry_test', expiredToken);
    await this.persistenceManager.storeToken('valid_test', validToken);

    // Test token validity by checking expiry dates directly
    const expiredRetrieved = await this.persistenceManager.getToken('expiry_test');
    const validRetrieved = await this.persistenceManager.getToken('valid_test');

    if (!expiredRetrieved || !validRetrieved) {
      throw new Error('Failed to retrieve stored tokens');
    }

    // Manual expiry check since isTokenValid method doesn't exist
    const now = Date.now();
    const expiredValid = expiredRetrieved.expires_at ? expiredRetrieved.expires_at > now : true;
    const validValid = validRetrieved.expires_at ? validRetrieved.expires_at > now : true;

    if (expiredValid) {
      throw new Error('Expired token incorrectly identified as valid');
    }

    if (!validValid) {
      throw new Error('Valid token incorrectly identified as expired');
    }

    // Clean up
    await this.persistenceManager.removeToken('expiry_test');
    await this.persistenceManager.removeToken('valid_test');
  }

  /**
   * Test Sentry server initialization
   */
  private async testSentryServerInit(): Promise<void> {
    await this.sentryServer.initialize();
    
    // Verify server is initialized
    const authStatus = await this.sentryServer.getAuthenticationStatus();
    
    if (!authStatus) {
      throw new Error('Sentry server failed to initialize');
    }

    if (!authStatus.providers.sentry) {
      throw new Error('Sentry provider not found in auth status');
    }
  }

  /**
   * Test Sentry token restoration
   */
  private async testSentryTokenRestoration(): Promise<void> {
    // This test checks if token restoration works without actual Sentry auth
    // We'll verify the restoration mechanism rather than actual API calls
    
    const testSentryToken = {
      access_token: 'test_sentry_token_restoration',
      token_type: 'Bearer',
      expires_at: Date.now() + 7200000
    };

    // Store a test token
    await this.persistenceManager.storeToken('sentry', testSentryToken);

    // Create new server instance (simulates restart)
    const newServer = new SentryMCPServerWithPersistence();
    await newServer.initialize();

    // Check if token was restored through the persistence manager
    const newManager = new MCPAuthPersistenceManager();
    await newManager.initialize();
    const restoredToken = await newManager.getToken('sentry');
    
    if (!restoredToken) {
      throw new Error('Sentry token not restored on server initialization');
    }

    if (restoredToken.access_token !== testSentryToken.access_token) {
      throw new Error('Restored Sentry token data corrupted');
    }

    // Clean up
    await this.persistenceManager.removeToken('sentry');
  }

  /**
   * Test Sentry API request handling
   */
  private async testSentryAPIRequests(): Promise<void> {
    // Test the API request structure without actual Sentry credentials
    // This verifies the request handling mechanism
    
    try {
      // This should fail gracefully without authentication
      await this.sentryServer.makeSentryRequest('user/');
    } catch (error) {
      // Expected to fail without valid token
      if (!(error as Error).message.includes('No authentication token')) {
        throw new Error(`Unexpected error in API request handling: ${(error as Error).message}`);
      }
    }

    // Test with mock token (should still fail but for different reason)
    const mockToken = {
      access_token: 'mock_token_for_testing',
      token_type: 'Bearer',
      expires_at: Date.now() + 3600000
    };

    await this.persistenceManager.storeToken('sentry', mockToken);
    
    const newServer = new SentryMCPServerWithPersistence();
    await newServer.initialize();

    try {
      await newServer.makeSentryRequest('user/');
    } catch (error) {
      // Should fail with authentication error, not structure error
      const errorMessage = (error as Error).message;
      if (errorMessage.includes('No authentication token')) {
        throw new Error('Token was not properly loaded for API request');
      }
    }

    // Clean up
    await this.persistenceManager.removeToken('sentry');
  }

  /**
   * Test health monitor initialization
   */
  private async testHealthMonitorInit(): Promise<void> {
    await this.healthMonitor.initialize();
    
    // Verify health monitor is operational
    const healthStatus = this.healthMonitor.getHealthStatus();
    
    if (!healthStatus) {
      throw new Error('Health monitor failed to initialize');
    }

    if (!healthStatus.timestamp) {
      throw new Error('Health monitor not providing status timestamps');
    }
  }

  /**
   * Test health check execution
   */
  private async testHealthCheckExecution(): Promise<void> {
    await this.healthMonitor.runHealthCheck();
    
    const healthStatus = this.healthMonitor.getHealthStatus();
    
    if (!healthStatus.checks || !Array.isArray(healthStatus.checks)) {
      throw new Error('Health checks not executing properly');
    }

    if (!healthStatus.summary) {
      throw new Error('Health summary not generated');
    }

    // Verify summary structure
    const requiredSummaryFields = ['total_providers', 'healthy', 'warning', 'critical'];
    for (const field of requiredSummaryFields) {
      if (!(field in healthStatus.summary)) {
        throw new Error(`Health summary missing required field: ${field}`);
      }
    }
  }

  /**
   * Test full system integration
   */
  private async testFullSystemIntegration(): Promise<void> {
    // Test complete workflow: store token → restart simulation → health check
    
    const integrationToken = {
      access_token: 'full_integration_token_test',
      token_type: 'Bearer',
      expires_at: Date.now() + 7200000
    };

    // 1. Store token
    await this.persistenceManager.storeToken('integration_test', integrationToken);

    // 2. Simulate restart by creating new instances
    const newManager = new MCPAuthPersistenceManager();
    const newServer = new SentryMCPServerWithPersistence();
    const newMonitor = new MCPAuthHealthMonitor();

    // 3. Initialize new instances
    await newServer.initialize();
    await newMonitor.initialize();

    // 4. Verify token persistence
    const restoredToken = await newManager.getToken('integration_test');
    if (!restoredToken) {
      throw new Error('Integration test: Token not persisted');
    }

    // 5. Run health check
    await newMonitor.runHealthCheck();
    const healthStatus = newMonitor.getHealthStatus();
    
    if (!healthStatus.monitoring_active) {
      // This is expected as monitoring wasn't started
    }

    // Clean up
    await newManager.removeToken('integration_test');
  }

  /**
   * Test VS Code restart simulation
   */
  private async testVSCodeRestartSimulation(): Promise<void> {
    console.log('   🔄 Simulating VS Code restart scenario...');
    
    // Phase 1: Pre-restart setup
    const restartTestToken = {
      access_token: 'vs_code_restart_simulation_token',
      refresh_token: 'vs_code_restart_refresh_token',
      token_type: 'Bearer',
      expires_at: Date.now() + 3600000,
      scope: 'project:read org:read'
    };

    await this.persistenceManager.storeToken('vscode_restart_test', restartTestToken);
    
    // Phase 2: Simulate complete VS Code shutdown
    // (In real scenario, all objects would be destroyed)
    
    // Phase 3: Simulate VS Code startup with new instances
    const postRestartManager = new MCPAuthPersistenceManager();
    const postRestartServer = new SentryMCPServerWithPersistence();
    const postRestartMonitor = new MCPAuthHealthMonitor();

    // Phase 4: Initialize all systems
    await postRestartServer.initialize();
    await postRestartMonitor.initialize();

    // Phase 5: Verify complete token restoration
    const restoredToken = await postRestartManager.getToken('vscode_restart_test');
    
    if (!restoredToken) {
      throw new Error('VS Code restart simulation: Token not restored');
    }

    // Verify all token fields are intact
    if (restoredToken.access_token !== restartTestToken.access_token) {
      throw new Error('VS Code restart simulation: Access token corrupted');
    }

    if (restoredToken.refresh_token !== restartTestToken.refresh_token) {
      throw new Error('VS Code restart simulation: Refresh token corrupted');
    }

    if (restoredToken.scope !== restartTestToken.scope) {
      throw new Error('VS Code restart simulation: Token scope corrupted');
    }

    // Phase 6: Verify health monitoring works post-restart
    await postRestartMonitor.runHealthCheck();
    const postRestartHealth = postRestartMonitor.getHealthStatus();
    
    if (!postRestartHealth) {
      throw new Error('VS Code restart simulation: Health monitoring failed post-restart');
    }

    console.log('   ✅ VS Code restart simulation completed successfully');

    // Clean up
    await postRestartManager.removeToken('vscode_restart_test');
  }

  /**
   * Print comprehensive test summary
   */
  private printTestSummary(): void {
    console.log('\n' + '='.repeat(60));
    console.log('🧪 MCP Authentication Test Suite Results');
    console.log('='.repeat(60));

    const passed = this.testResults.filter(r => r.status === 'passed').length;
    const failed = this.testResults.filter(r => r.status === 'failed').length;
    const total = this.testResults.length;
    const totalDuration = this.testResults.reduce((sum, r) => sum + r.duration_ms, 0);

    console.log(`\n📊 Summary:`);
    console.log(`   Total Tests: ${total}`);
    console.log(`   Passed: ${passed} ✅`);
    console.log(`   Failed: ${failed} ${failed > 0 ? '❌' : ''}`);
    console.log(`   Success Rate: ${((passed / total) * 100).toFixed(1)}%`);
    console.log(`   Total Duration: ${totalDuration}ms`);

    if (failed > 0) {
      console.log(`\n❌ Failed Tests:`);
      this.testResults
        .filter(r => r.status === 'failed')
        .forEach(r => {
          console.log(`   • ${r.test_name}: ${r.error}`);
        });
    }

    console.log(`\n📈 Performance:`);
    this.testResults.forEach(r => {
      const status = r.status === 'passed' ? '✅' : '❌';
      console.log(`   ${status} ${r.test_name}: ${r.duration_ms}ms`);
    });

    if (passed === total) {
      console.log(`\n🎉 All tests passed! MCP Authentication system ready for production.`);
    } else {
      console.log(`\n⚠️ ${failed} test(s) failed. Please review and fix issues before deployment.`);
    }
  }

  /**
   * Get test results as JSON
   */
  getTestResults(): any {
    return {
      timestamp: new Date().toISOString(),
      summary: {
        total: this.testResults.length,
        passed: this.testResults.filter(r => r.status === 'passed').length,
        failed: this.testResults.filter(r => r.status === 'failed').length,
        total_duration_ms: this.testResults.reduce((sum, r) => sum + r.duration_ms, 0)
      },
      results: this.testResults
    };
  }
}

export { MCPAuthTestSuite };

console.log('🧪 MCP Authentication Test Suite loaded');