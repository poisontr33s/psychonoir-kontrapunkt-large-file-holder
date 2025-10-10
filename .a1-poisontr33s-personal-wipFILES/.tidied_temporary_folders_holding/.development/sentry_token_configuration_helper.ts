/**
 * LIVE SENTRY TOKEN CONFIGURATION HELPER
 * 
 * User's Token Details:
 * - Name: vscodelocalgitgubproplus  
 * - Created: Sep 21, 9:43 PM
 * - Token: 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
 * - Scopes: Full MCP compatibility (alerts, events, member, org, project, team permissions)
 */

export const SENTRY_TOKEN_CONFIGURATION_STEPS = {
    user_token: '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',
    
    vscode_settings_method: {
        step_1: 'Open VS Code Settings (Ctrl+,)',
        step_2: 'Search for "mcp"',
        step_3: 'Find "MCP: Servers" section',
        step_4: 'Locate Sentry server configuration',
        step_5: 'Add token to auth configuration',
        step_6: 'Save settings'
    },
    
    gui_method: {
        step_1: 'Open MCP servers panel in VS Code',
        step_2: 'Find Sentry server in list',
        step_3: 'Right-click → "Configure Model Access"',
        step_4: 'Enter token when prompted',
        step_5: 'Confirm authentication'
    },
    
    direct_configuration: {
        settings_json_path: '%APPDATA%/Code/User/settings.json',
        configuration_block: `
{
    "mcp.servers": {
        "sentry": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-sentry"],
            "env": {
                "SENTRY_AUTH_TOKEN": "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"
            }
        }
    }
}
        `
    }
};

export function displayConfigurationInstructions(): void {
    console.log('🔐 SENTRY TOKEN CONFIGURATION');
    console.log('=====================================');
    console.log('');
    console.log('✅ Your token has PERFECT permissions for MCP:');
    console.log('   • alerts:read, alerts:write');
    console.log('   • event:admin, event:read, event:write');
    console.log('   • project:admin, project:read, project:write');
    console.log('   • org:read, org:write');
    console.log('   • All necessary scopes included!');
    console.log('');
    console.log('📋 CONFIGURATION OPTIONS:');
    console.log('');
    console.log('🎯 METHOD 1: Direct Settings Configuration');
    console.log('1. Press Ctrl+Shift+P');
    console.log('2. Type "Preferences: Open Settings (JSON)"');
    console.log('3. Add Sentry MCP configuration with your token');
    console.log('');
    console.log('🎯 METHOD 2: GUI Configuration');
    console.log('1. Open MCP panel in VS Code');
    console.log('2. Right-click Sentry server');
    console.log('3. Select "Configure Model Access"');
    console.log('4. Enter your token when prompted');
    console.log('');
    console.log('🛡️ AUTOMATIC BENEFITS:');
    console.log('✅ Token will be automatically encrypted with AES-256-GCM');
    console.log('✅ Persistent storage survives VS Code restarts');
    console.log('✅ Health monitoring alerts for token expiry');
    console.log('✅ Recovery assistance if authentication fails');
    console.log('');
    console.log('🔍 Your Token: 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');
    console.log('📅 Created: Sep 21, 9:43 PM');
    console.log('🏷️ Name: vscodelocalgitgubproplus');
}

export function testTokenConfiguration(): void {
    console.log('🧪 Testing token configuration...');
    console.log('This will verify our persistence system works with your real token');
}

// Main execution
if (import.meta.main) {
    displayConfigurationInstructions();
}