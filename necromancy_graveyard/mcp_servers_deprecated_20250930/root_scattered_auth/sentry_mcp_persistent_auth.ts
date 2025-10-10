#!/usr/bin/env node

/**
 * Sentry MCP Server with Authentication Persistence
 * Enhanced version that automatically restores Sentry OAuth tokens after VS Code restarts
 */

import { PersistentAuthMCPServer } from './mcp_auth_persistence_solution.js';

class SentryMCPServerWithPersistence extends PersistentAuthMCPServer {
  private sentryToken: string | null = null;
  private sentryApiUrl: string = 'https://sentry.io/api/0/';
  
  constructor() {
    super();
  }

  async initialize(): Promise<void> {
    await super.initialize();
    
    // Try to restore Sentry authentication
    await this.restoreSentryAuth();
    
    console.log('🔮 Sentry MCP Server with Authentication Persistence initialized');
  }

  /**
   * Store Sentry authentication token
   */
  async storeSentryAuth(accessToken: string, refreshToken?: string, expiresIn?: number): Promise<void> {
    const tokenData = {
      access_token: accessToken,
      refresh_token: refreshToken,
      token_type: 'Bearer',
      expires_at: expiresIn ? Date.now() + (expiresIn * 1000) : undefined,
      scope: 'project:read org:read'
    };

    await this.storeAuth('sentry', tokenData);
    this.sentryToken = accessToken;
    
    console.log('✅ Sentry authentication stored successfully');
  }

  /**
   * Restore Sentry authentication from persistent storage
   */
  private async restoreSentryAuth(): Promise<boolean> {
    try {
      const token = await this.getAuth('sentry');
      
      if (token && token.access_token) {
        this.sentryToken = token.access_token;
        console.log('🔄 Sentry authentication restored from persistent storage');
        
        // Verify token is still valid by making a test API call
        const isValid = await this.verifySentryToken();
        
        if (isValid) {
          console.log('✅ Restored Sentry token is valid');
          return true;
        } else {
          console.log('❌ Restored Sentry token is invalid, removing...');
          await this.handleAuthFailure('sentry');
          return false;
        }
      }
      
      console.log('📭 No Sentry authentication found in persistent storage');
      return false;
    } catch (error) {
      console.error('❌ Failed to restore Sentry authentication:', error);
      return false;
    }
  }

  /**
   * Verify Sentry token by making a test API call
   */
  private async verifySentryToken(): Promise<boolean> {
    if (!this.sentryToken) {
      return false;
    }

    try {
      const response = await fetch(`${this.sentryApiUrl}user/`, {
        headers: {
          'Authorization': `Bearer ${this.sentryToken}`,
          'Content-Type': 'application/json'
        }
      });

      return response.ok;
    } catch (error) {
      console.error('❌ Token verification failed:', error);
      return false;
    }
  }

  /**
   * Get authenticated Sentry API client
   */
  getSentryClient(): { token: string | null; headers: Record<string, string> } {
    if (!this.sentryToken) {
      console.log('⚠️ No Sentry token available. Authentication required.');
      return { token: null, headers: {} };
    }

    return {
      token: this.sentryToken,
      headers: {
        'Authorization': `Bearer ${this.sentryToken}`,
        'Content-Type': 'application/json'
      }
    };
  }

  /**
   * Check if Sentry is authenticated
   */
  async isSentryAuthenticated(): Promise<boolean> {
    return await this.isAuthenticated('sentry');
  }

  /**
   * Handle Sentry API request with automatic token validation
   */
  async makeSentryRequest(endpoint: string, options: RequestInit = {}): Promise<Response | null> {
    const client = this.getSentryClient();
    
    if (!client.token) {
      console.log('❌ Sentry authentication required for API request');
      return null;
    }

    try {
      const response = await fetch(`${this.sentryApiUrl}${endpoint}`, {
        ...options,
        headers: {
          ...client.headers,
          ...options.headers
        }
      });

      // Handle authentication errors
      if (response.status === 401) {
        console.log('🚨 Sentry API returned 401 - token invalid');
        await this.handleAuthFailure('sentry');
        return null;
      }

      return response;
    } catch (error) {
      console.error('❌ Sentry API request failed:', error);
      return null;
    }
  }

  /**
   * Get authentication status dashboard including Sentry
   */
  async getAuthenticationStatus(): Promise<any> {
    const dashboard = await this.getAuthDashboard();
    
    return {
      ...dashboard,
      sentry_ready: await this.isSentryAuthenticated(),
      sentry_token_available: this.sentryToken !== null
    };
  }

  /**
   * Clear Sentry authentication
   */
  async clearSentryAuth(): Promise<void> {
    this.sentryToken = null;
    await this.handleAuthFailure('sentry');
    console.log('🧹 Sentry authentication cleared');
  }
}

/**
 * MCP Authentication Recovery Tool
 * Standalone tool to check and restore authentication status
 */
class MCPAuthRecoveryTool {
  private server: SentryMCPServerWithPersistence;

  constructor() {
    this.server = new SentryMCPServerWithPersistence();
  }

  async run(): Promise<void> {
    console.log('🔧 MCP Authentication Recovery Tool starting...');
    
    await this.server.initialize();
    
    // Get authentication status
    const status = await this.server.getAuthenticationStatus();
    
    console.log('\n📊 Authentication Status Report:');
    console.log('================================');
    console.log(`Timestamp: ${status.timestamp}`);
    console.log(`Total Providers: ${status.total_providers}`);
    console.log(`Authenticated Providers: ${status.authenticated_providers}`);
    console.log(`Sentry Ready: ${status.sentry_ready ? '✅ Yes' : '❌ No'}`);
    console.log(`Sentry Token Available: ${status.sentry_token_available ? '✅ Yes' : '❌ No'}`);
    
    if (Object.keys(status.providers).length > 0) {
      console.log('\nProvider Details:');
      for (const [provider, info] of Object.entries(status.providers)) {
        console.log(`  ${provider}: ${(info as any).authenticated ? '✅' : '❌'} ${(info as any).expires_in ? `(expires in ${Math.round((info as any).expires_in / 1000 / 60)} minutes)` : ''}`);
      }
    }

    // If Sentry is not authenticated, provide guidance
    if (!status.sentry_ready) {
      console.log('\n💡 Sentry Authentication Required:');
      console.log('To authenticate with Sentry:');
      console.log('1. Open VS Code with MCP servers enabled');
      console.log('2. Use the Sentry MCP server authentication flow');
      console.log('3. Your token will be automatically persisted for future sessions');
    }

    console.log('\n✅ Authentication recovery check complete');
  }
}

// Export for use in other modules
export { SentryMCPServerWithPersistence, MCPAuthRecoveryTool };

// Run recovery tool if this script is executed directly
if (import.meta.url === `file://${process.argv[1]}`) {
  const recoveryTool = new MCPAuthRecoveryTool();
  recoveryTool.run().catch(console.error);
}

console.log('🛡️ Sentry MCP Server with Authentication Persistence loaded');