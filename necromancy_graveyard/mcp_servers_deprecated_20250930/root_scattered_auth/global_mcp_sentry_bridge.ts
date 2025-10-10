/**
 * Global MCP Sentry Authentication Bridge
 * Integrates with VS Code's global MCP Sentry HTTP server
 * Provides persistent authentication for https://mcp.sentry.dev/mcp
 */

import { MCPAuthPersistenceManager } from './mcp_auth_persistence_solution.js';
import * as fs from 'fs/promises';
import * as path from 'path';
import * as os from 'os';

interface GlobalMCPConfig {
  servers: Record<string, any>;
}

class GlobalMCPSentryBridge {
  private persistenceManager: MCPAuthPersistenceManager;
  private globalConfigPath: string;
  
  constructor() {
    this.persistenceManager = new MCPAuthPersistenceManager();
    // Windows VS Code user config path
    this.globalConfigPath = path.join(
      os.homedir(), 
      'AppData', 
      'Roaming', 
      'Code', 
      'User', 
      'mcp.json'
    );
  }

  async initialize(): Promise<void> {
    await this.persistenceManager.initialize();
    console.log('🌐 Global MCP Sentry Authentication Bridge initialized');
  }

  /**
   * Read current global MCP configuration
   */
  async getGlobalMCPConfig(): Promise<GlobalMCPConfig> {
    try {
      const configContent = await fs.readFile(this.globalConfigPath, 'utf-8');
      return JSON.parse(configContent);
    } catch (error) {
      console.error('❌ Failed to read global MCP config:', error);
      throw error;
    }
  }

  /**
   * Check if Sentry is configured in global MCP
   */
  async isSentryConfiguredGlobally(): Promise<boolean> {
    try {
      const config = await this.getGlobalMCPConfig();
      return !!(config.servers?.sentry);
    } catch {
      return false;
    }
  }

  /**
   * Get current Sentry configuration from global MCP
   */
  async getSentryGlobalConfig(): Promise<any> {
    const config = await this.getGlobalMCPConfig();
    return config.servers?.sentry || null;
  }

  /**
   * Store Sentry authentication token for global HTTP server
   */
  async storeSentryToken(token: any): Promise<void> {
    // Store token with provider identifier for global server
    await this.persistenceManager.storeToken('sentry_global_http', {
      access_token: token.access_token,
      refresh_token: token.refresh_token,
      token_type: token.token_type || 'Bearer',
      expires_at: token.expires_at,
      scope: token.scope
    });
    
    console.log('✅ Sentry global HTTP token stored with persistence');
  }

  /**
   * Retrieve stored Sentry token for global HTTP server
   */
  async getSentryToken(): Promise<any> {
    const token = await this.persistenceManager.getToken('sentry_global_http');
    
    if (token) {
      console.log('🔑 Retrieved Sentry global HTTP token from persistent storage');
      return token;
    }
    
    console.log('⚠️ No stored Sentry global HTTP token found');
    return null;
  }

  /**
   * Check if stored Sentry token is valid
   */
  async isSentryTokenValid(): Promise<boolean> {
    const token = await this.getSentryToken();
    
    if (!token) return false;
    
    if (token.expires_at) {
      const now = Date.now();
      const buffer = 5 * 60 * 1000; // 5 minute buffer
      return token.expires_at > (now + buffer);
    }
    
    return true; // No expiry means valid
  }

  /**
   * Generate enhanced global MCP configuration with authentication hints
   */
  async generateEnhancedGlobalConfig(): Promise<GlobalMCPConfig> {
    const currentConfig = await this.getGlobalMCPConfig();
    
    // Add authentication context to Sentry server config
    if (currentConfig.servers?.sentry) {
      const storedToken = await this.getSentryToken();
      
      currentConfig.servers.sentry = {
        ...currentConfig.servers.sentry,
        // Add metadata for authentication status
        _auth_persistence: {
          enabled: true,
          token_stored: !!storedToken,
          token_valid: await this.isSentryTokenValid(),
          last_check: new Date().toISOString()
        }
      };
    }
    
    return currentConfig;
  }

  /**
   * Monitor global MCP Sentry authentication status
   */
  async monitorGlobalSentryAuth(): Promise<any> {
    const sentryConfig = await this.getSentryGlobalConfig();
    const storedToken = await this.getSentryToken();
    const isValid = await this.isSentryTokenValid();
    
    return {
      global_sentry_configured: !!sentryConfig,
      sentry_config: sentryConfig,
      token_stored: !!storedToken,
      token_valid: isValid,
      auth_status: isValid ? 'authenticated' : 'needs_authentication',
      server_url: sentryConfig?.url || 'unknown',
      server_type: sentryConfig?.type || 'unknown',
      recommendations: this.generateAuthRecommendations(!!storedToken, isValid)
    };
  }

  /**
   * Generate authentication recommendations
   */
  private generateAuthRecommendations(tokenStored: boolean, tokenValid: boolean): string[] {
    const recommendations: string[] = [];
    
    if (!tokenStored) {
      recommendations.push('🔐 Authenticate with Sentry MCP to store persistent token');
      recommendations.push('🔧 Token will be automatically restored on VS Code restart');
    } else if (!tokenValid) {
      recommendations.push('⚠️ Stored token expired - re-authentication required');
      recommendations.push('🔄 New token will be automatically persisted');
    } else {
      recommendations.push('✅ Authentication valid and persistent');
      recommendations.push('🎯 Token will be restored automatically on VS Code restart');
    }
    
    return recommendations;
  }

  /**
   * Generate integration report for troubleshooting
   */
  async generateIntegrationReport(): Promise<any> {
    const authStatus = await this.monitorGlobalSentryAuth();
    
    return {
      bridge_status: 'active',
      timestamp: new Date().toISOString(),
      global_mcp_path: this.globalConfigPath,
      authentication: authStatus,
      integration_notes: [
        'Global MCP Sentry server (HTTP) authentication bridged with local persistence',
        'Tokens stored encrypted and restored automatically on VS Code restart',
        'Works alongside workspace consciousness servers without conflicts',
        'Authentication failures will be logged and recovery guidance provided'
      ],
      troubleshooting: {
        common_issues: [
          'Global vs workspace MCP conflicts',
          'HTTP server token expiry',
          'Windows credential storage conflicts',
          'Multi-terminal authentication chaos'
        ],
        solutions_applied: [
          'Persistent token storage with AES-256-GCM encryption',
          'Automatic token restoration on startup',
          'Separation of global and workspace authentication',
          'Bridge layer for HTTP server integration'
        ]
      }
    };
  }
}

export { GlobalMCPSentryBridge };

console.log('🌐 Global MCP Sentry Authentication Bridge loaded');