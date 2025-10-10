/**
 * MCP Authentication Persistence Solution
 * Solves persistent token storage for VS Code MCP servers
 * Ensures OAuth tokens survive VS Code restarts and extension updates
 */

import { promises as fs } from 'fs';
import * as path from 'path';
import * as crypto from 'crypto';
import * as os from 'os';

interface AuthToken {
  access_token: string;
  refresh_token?: string;
  token_type: string;
  expires_at?: number;
  scope?: string;
  provider: string;
  created_at: number;
}

interface StoredAuthData {
  tokens: Record<string, AuthToken>;
  encryption_key: string;
  last_updated: number;
}

class MCPAuthPersistenceManager {
  private static readonly TOKEN_CACHE_DIR = path.join(os.homedir(), '.vscode-mcp-auth');
  private static readonly TOKEN_CACHE_FILE = 'tokens.encrypted.json';
  private static readonly ENCRYPTION_ALGORITHM = 'aes-256-gcm';
  private static readonly TOKEN_EXPIRY_BUFFER = 5 * 60 * 1000; // 5 minutes buffer

  private encryptionKey: Buffer;
  private authData: StoredAuthData | null = null;

  constructor() {
    this.encryptionKey = this.getOrCreateEncryptionKey();
  }

  async initialize(): Promise<void> {
    try {
      await this.ensureCacheDirectoryExists();
      await this.loadStoredTokens();
      console.log('🔐 MCP Authentication Persistence Manager initialized');
    } catch (error) {
      console.error('❌ Failed to initialize auth persistence:', error);
      this.authData = {
        tokens: {},
        encryption_key: this.encryptionKey.toString('hex'),
        last_updated: Date.now()
      };
    }
  }

  async storeToken(provider: string, token: Omit<AuthToken, 'provider' | 'created_at'>): Promise<void> {
    if (!this.authData) {
      await this.initialize();
    }

    const fullToken: AuthToken = {
      ...token,
      provider,
      created_at: Date.now()
    };

    if (this.authData) {
      this.authData.tokens[provider] = fullToken;
      this.authData.last_updated = Date.now();
      await this.saveStoredTokens();
      console.log(`✅ Token stored for provider: ${provider}`);
    }
  }

  async getToken(provider: string): Promise<AuthToken | null> {
    if (!this.authData) {
      await this.initialize();
    }

    if (!this.authData) {
      return null;
    }

    const token = this.authData.tokens[provider];
    if (!token) {
      console.log(`📭 No stored token found for provider: ${provider}`);
      return null;
    }

    if (this.isTokenExpired(token)) {
      console.log(`⏰ Token expired for provider: ${provider}`);
      await this.removeToken(provider);
      return null;
    }

    console.log(`🔑 Retrieved valid token for provider: ${provider}`);
    return token;
  }

  async removeToken(provider: string): Promise<void> {
    if (!this.authData) {
      await this.initialize();
    }

    if (this.authData) {
      delete this.authData.tokens[provider];
      this.authData.last_updated = Date.now();
      await this.saveStoredTokens();
      console.log(`🗑️ Token removed for provider: ${provider}`);
    }
  }

  isTokenExpired(token: AuthToken): boolean {
    if (!token.expires_at) {
      return false;
    }

    const now = Date.now();
    const expiryWithBuffer = token.expires_at - MCPAuthPersistenceManager.TOKEN_EXPIRY_BUFFER;
    return now >= expiryWithBuffer;
  }

  async getStoredProviders(): Promise<string[]> {
    if (!this.authData) {
      await this.initialize();
    }

    return this.authData ? Object.keys(this.authData.tokens) : [];
  }

  async clearAllTokens(): Promise<void> {
    if (!this.authData) {
      await this.initialize();
    }

    if (this.authData) {
      this.authData.tokens = {};
      this.authData.last_updated = Date.now();
      await this.saveStoredTokens();
      console.log('🧹 All tokens cleared');
    }
  }

  async getAuthStatus(): Promise<Record<string, { authenticated: boolean; expires_at?: number; expires_in?: number }>> {
    if (!this.authData) {
      await this.initialize();
    }

    const status: Record<string, { authenticated: boolean; expires_at?: number; expires_in?: number }> = {};

    if (this.authData) {
      for (const [provider, token] of Object.entries(this.authData.tokens)) {
        const isExpired = this.isTokenExpired(token);
        status[provider] = {
          authenticated: !isExpired,
          expires_at: token.expires_at,
          expires_in: token.expires_at ? Math.max(0, token.expires_at - Date.now()) : undefined
        };
      }
    }

    return status;
  }

  private getOrCreateEncryptionKey(): Buffer {
    const machineId = os.hostname() + os.userInfo().username;
    return crypto.createHash('sha256').update(machineId).digest();
  }

  private async ensureCacheDirectoryExists(): Promise<void> {
    try {
      await fs.access(MCPAuthPersistenceManager.TOKEN_CACHE_DIR);
    } catch {
      await fs.mkdir(MCPAuthPersistenceManager.TOKEN_CACHE_DIR, { recursive: true });
    }
  }

  private async loadStoredTokens(): Promise<void> {
    const tokenFilePath = path.join(MCPAuthPersistenceManager.TOKEN_CACHE_DIR, MCPAuthPersistenceManager.TOKEN_CACHE_FILE);

    try {
      const encryptedData = await fs.readFile(tokenFilePath, 'utf8');
      const decryptedData = this.decrypt(encryptedData);
      this.authData = JSON.parse(decryptedData);
      if (this.authData) {
        console.log(`📂 Loaded ${Object.keys(this.authData.tokens).length} stored tokens`);
      }
    } catch (error) {
      if ((error as any).code !== 'ENOENT') {
        console.error('❌ Failed to load stored tokens:', error);
      }
      this.authData = {
        tokens: {},
        encryption_key: this.encryptionKey.toString('hex'),
        last_updated: Date.now()
      };
    }
  }

  private async saveStoredTokens(): Promise<void> {
    if (!this.authData) return;

    const tokenFilePath = path.join(MCPAuthPersistenceManager.TOKEN_CACHE_DIR, MCPAuthPersistenceManager.TOKEN_CACHE_FILE);

    try {
      const dataToEncrypt = JSON.stringify(this.authData, null, 2);
      const encryptedData = this.encrypt(dataToEncrypt);
      await fs.writeFile(tokenFilePath, encryptedData, 'utf8');
      console.log('💾 Tokens saved to persistent storage');
    } catch (error) {
      console.error('❌ Failed to save tokens:', error);
      throw error;
    }
  }

  private encrypt(text: string): string {
    const iv = crypto.randomBytes(16);
    const cipher = crypto.createCipheriv(MCPAuthPersistenceManager.ENCRYPTION_ALGORITHM, this.encryptionKey, iv);
    
    let encrypted = cipher.update(text, 'utf8', 'hex');
    encrypted += cipher.final('hex');
    
    const authTag = cipher.getAuthTag();
    
    return JSON.stringify({
      encrypted,
      iv: iv.toString('hex'),
      authTag: authTag.toString('hex')
    });
  }

  private decrypt(encryptedData: string): string {
    const { encrypted, iv, authTag } = JSON.parse(encryptedData);
    
    const decipher = crypto.createDecipheriv(MCPAuthPersistenceManager.ENCRYPTION_ALGORITHM, this.encryptionKey, Buffer.from(iv, 'hex'));
    decipher.setAuthTag(Buffer.from(authTag, 'hex'));
    
    let decrypted = decipher.update(encrypted, 'hex', 'utf8');
    decrypted += decipher.final('utf8');
    
    return decrypted;
  }
}

/**
 * Enhanced MCP Server with Authentication Persistence
 */
class PersistentAuthMCPServer {
  private authManager: MCPAuthPersistenceManager;
  private isInitialized = false;

  constructor() {
    this.authManager = new MCPAuthPersistenceManager();
  }

  async initialize(): Promise<void> {
    if (this.isInitialized) return;

    await this.authManager.initialize();
    this.isInitialized = true;

    await this.restoreAllAuthentications();
  }

  async storeAuth(provider: string, token: any): Promise<void> {
    await this.authManager.storeToken(provider, token);
  }

  async getAuth(provider: string): Promise<any | null> {
    return await this.authManager.getToken(provider);
  }

  async isAuthenticated(provider: string): Promise<boolean> {
    const token = await this.authManager.getToken(provider);
    return token !== null;
  }

  private async restoreAllAuthentications(): Promise<void> {
    const providers = await this.authManager.getStoredProviders();
    
    for (const provider of providers) {
      const token = await this.authManager.getToken(provider);
      if (token) {
        console.log(`🔄 Restored authentication for ${provider}`);
      }
    }

    console.log(`✅ Authentication restoration complete for ${providers.length} providers`);
  }

  async getAuthDashboard(): Promise<any> {
    const status = await this.authManager.getAuthStatus();
    
    return {
      timestamp: new Date().toISOString(),
      total_providers: Object.keys(status).length,
      authenticated_providers: Object.values(status).filter(s => s.authenticated).length,
      providers: status
    };
  }

  async handleAuthFailure(provider: string): Promise<boolean> {
    console.log(`🚨 Authentication failure detected for ${provider}`);
    
    await this.authManager.removeToken(provider);
    console.log(`❌ Removed invalid token for ${provider}. Manual re-authentication required.`);
    return false;
  }
}

export { MCPAuthPersistenceManager, PersistentAuthMCPServer };

console.log('🚀 MCP Authentication Persistence System loaded');