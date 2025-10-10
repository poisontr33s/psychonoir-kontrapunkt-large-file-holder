/**
 * MCP Authentication Health Monitor
 * Continuous monitoring and alerting for MCP authentication status
 */

import { SentryMCPServerWithPersistence } from './sentry_mcp_persistent_auth.js';
import { EventEmitter } from 'events';

interface HealthCheckResult {
  provider: string;
  status: 'healthy' | 'warning' | 'critical';
  authenticated: boolean;
  expires_in?: number;
  last_checked: number;
  message: string;
}

class MCPAuthHealthMonitor extends EventEmitter {
  private server: SentryMCPServerWithPersistence;
  private monitoringInterval: NodeJS.Timeout | null = null;
  private healthChecks: Map<string, HealthCheckResult> = new Map();
  private readonly CHECK_INTERVAL = 5 * 60 * 1000; // 5 minutes
  private readonly WARNING_THRESHOLD = 30 * 60 * 1000; // 30 minutes before expiry
  private readonly CRITICAL_THRESHOLD = 5 * 60 * 1000; // 5 minutes before expiry

  constructor() {
    super();
    this.server = new SentryMCPServerWithPersistence();
  }

  async initialize(): Promise<void> {
    await this.server.initialize();
    console.log('🏥 MCP Authentication Health Monitor initialized');
  }

  /**
   * Start continuous health monitoring
   */
  startMonitoring(): void {
    if (this.monitoringInterval) {
      console.log('⚠️ Health monitoring already running');
      return;
    }

    console.log('🔄 Starting continuous authentication health monitoring...');
    
    // Initial health check
    this.performHealthCheck();
    
    // Schedule periodic health checks
    this.monitoringInterval = setInterval(() => {
      this.performHealthCheck();
    }, this.CHECK_INTERVAL);

    console.log(`✅ Health monitoring started (checking every ${this.CHECK_INTERVAL / 1000 / 60} minutes)`);
  }

  /**
   * Stop continuous health monitoring
   */
  stopMonitoring(): void {
    if (this.monitoringInterval) {
      clearInterval(this.monitoringInterval);
      this.monitoringInterval = null;
      console.log('🛑 Health monitoring stopped');
    }
  }

  /**
   * Perform comprehensive health check
   */
  private async performHealthCheck(): Promise<void> {
    console.log('🔍 Performing authentication health check...');

    try {
      const authStatus = await this.server.getAuthenticationStatus();
      
      // Check Sentry authentication
      await this.checkSentryHealth();
      
      // Check all other providers
      for (const [provider, info] of Object.entries(authStatus.providers)) {
        await this.checkProviderHealth(provider, info as any);
      }

      // Emit health update event
      this.emit('healthUpdate', {
        timestamp: new Date().toISOString(),
        overall_status: this.getOverallHealthStatus(),
        checks: Array.from(this.healthChecks.values())
      });

      console.log(`✅ Health check completed - Overall status: ${this.getOverallHealthStatus()}`);

    } catch (error) {
      console.error('❌ Health check failed:', error);
      this.emit('healthCheckError', error);
    }
  }

  /**
   * Check Sentry-specific health
   */
  private async checkSentryHealth(): Promise<void> {
    const isAuthenticated = await this.server.isSentryAuthenticated();
    const client = this.server.getSentryClient();
    
    let status: 'healthy' | 'warning' | 'critical' = 'critical';
    let message = 'Not authenticated';

    if (isAuthenticated && client.token) {
      // Test API connectivity
      try {
        const response = await this.server.makeSentryRequest('user/');
        
        if (response?.ok) {
          status = 'healthy';
          message = 'Authentication valid and API accessible';
        } else {
          status = 'critical';
          message = 'Authentication failed - API request rejected';
        }
      } catch (error) {
        status = 'critical';
        message = `API connectivity error: ${(error as Error).message}`;
      }
    }

    const healthCheck: HealthCheckResult = {
      provider: 'sentry',
      status,
      authenticated: isAuthenticated,
      last_checked: Date.now(),
      message
    };

    this.healthChecks.set('sentry', healthCheck);

    // Emit specific events for status changes
    if (status === 'critical') {
      this.emit('authenticationFailure', 'sentry', message);
    } else if (status === 'healthy') {
      this.emit('authenticationRestored', 'sentry', message);
    }
  }

  /**
   * Check individual provider health
   */
  private async checkProviderHealth(provider: string, info: any): Promise<void> {
    let status: 'healthy' | 'warning' | 'critical' = 'critical';
    let message = 'Not authenticated';

    if (info.authenticated) {
      if (info.expires_in) {
        if (info.expires_in <= this.CRITICAL_THRESHOLD) {
          status = 'critical';
          message = `Token expires in ${Math.round(info.expires_in / 1000 / 60)} minutes - immediate renewal required`;
        } else if (info.expires_in <= this.WARNING_THRESHOLD) {
          status = 'warning';
          message = `Token expires in ${Math.round(info.expires_in / 1000 / 60)} minutes - renewal recommended`;
        } else {
          status = 'healthy';
          message = `Token valid for ${Math.round(info.expires_in / 1000 / 60)} minutes`;
        }
      } else {
        status = 'healthy';
        message = 'Token valid (no expiry)';
      }
    }

    const healthCheck: HealthCheckResult = {
      provider,
      status,
      authenticated: info.authenticated,
      expires_in: info.expires_in,
      last_checked: Date.now(),
      message
    };

    this.healthChecks.set(provider, healthCheck);

    // Emit warnings for expiring tokens
    if (status === 'warning') {
      this.emit('tokenExpiring', provider, info.expires_in);
    } else if (status === 'critical' && info.authenticated) {
      this.emit('tokenCritical', provider, info.expires_in);
    }
  }

  /**
   * Get overall health status
   */
  private getOverallHealthStatus(): 'healthy' | 'warning' | 'critical' {
    const statuses = Array.from(this.healthChecks.values()).map(check => check.status);
    
    if (statuses.includes('critical')) {
      return 'critical';
    } else if (statuses.includes('warning')) {
      return 'warning';
    } else {
      return 'healthy';
    }
  }

  /**
   * Get current health status
   */
  getHealthStatus(): any {
    return {
      timestamp: new Date().toISOString(),
      overall_status: this.getOverallHealthStatus(),
      monitoring_active: this.monitoringInterval !== null,
      checks: Array.from(this.healthChecks.values()),
      summary: {
        total_providers: this.healthChecks.size,
        healthy: Array.from(this.healthChecks.values()).filter(c => c.status === 'healthy').length,
        warning: Array.from(this.healthChecks.values()).filter(c => c.status === 'warning').length,
        critical: Array.from(this.healthChecks.values()).filter(c => c.status === 'critical').length
      }
    };
  }

  /**
   * Force immediate health check
   */
  async runHealthCheck(): Promise<any> {
    await this.performHealthCheck();
    return this.getHealthStatus();
  }
}

/**
 * Authentication Recovery Assistant
 * Provides automated recovery recommendations and actions
 */
class AuthRecoveryAssistant {
  private monitor: MCPAuthHealthMonitor;
  private autoRecoveryEnabled = true;

  constructor(monitor: MCPAuthHealthMonitor) {
    this.monitor = monitor;
    this.setupEventHandlers();
  }

  private setupEventHandlers(): void {
    this.monitor.on('authenticationFailure', this.handleAuthFailure.bind(this));
    this.monitor.on('tokenExpiring', this.handleTokenExpiring.bind(this));
    this.monitor.on('tokenCritical', this.handleTokenCritical.bind(this));
  }

  private async handleAuthFailure(provider: string, message: string): Promise<void> {
    console.log(`🚨 CRITICAL: Authentication failure for ${provider} - ${message}`);
    
    if (this.autoRecoveryEnabled) {
      console.log(`🔧 Attempting automatic recovery for ${provider}...`);
      // Here you would implement provider-specific recovery logic
      // For now, just log the recommendation
      this.logRecoveryInstructions(provider);
    }
  }

  private async handleTokenExpiring(provider: string, expiresIn: number): Promise<void> {
    const minutesLeft = Math.round(expiresIn / 1000 / 60);
    console.log(`⚠️ WARNING: Token for ${provider} expires in ${minutesLeft} minutes`);
    
    if (minutesLeft <= 10 && this.autoRecoveryEnabled) {
      console.log(`🔄 Attempting proactive token refresh for ${provider}...`);
      // Implement token refresh logic here
    }
  }

  private async handleTokenCritical(provider: string, expiresIn: number): Promise<void> {
    const minutesLeft = Math.round(expiresIn / 1000 / 60);
    console.log(`🚨 CRITICAL: Token for ${provider} expires in ${minutesLeft} minutes!`);
    
    if (this.autoRecoveryEnabled) {
      console.log(`⚡ Emergency token refresh attempt for ${provider}...`);
      // Implement emergency refresh logic here
    }
  }

  private logRecoveryInstructions(provider: string): void {
    console.log(`\n📋 Recovery Instructions for ${provider}:`);
    console.log('='.repeat(50));
    
    switch (provider) {
      case 'sentry':
        console.log('1. Open VS Code');
        console.log('2. Access MCP servers panel');
        console.log('3. Locate Sentry MCP server');
        console.log('4. Click "Authenticate" or "Re-authenticate"');
        console.log('5. Complete OAuth flow in browser');
        console.log('6. Token will be automatically persisted');
        break;
      default:
        console.log(`1. Check ${provider} authentication settings`);
        console.log('2. Re-authenticate with the provider');
        console.log('3. Verify token permissions and scope');
        break;
    }
    
    console.log('\n💡 This authentication will be automatically restored in future VS Code sessions.');
  }

  setAutoRecovery(enabled: boolean): void {
    this.autoRecoveryEnabled = enabled;
    console.log(`🔧 Auto-recovery ${enabled ? 'enabled' : 'disabled'}`);
  }
}

export { MCPAuthHealthMonitor, AuthRecoveryAssistant };

console.log('🏥 MCP Authentication Health Monitor system loaded');