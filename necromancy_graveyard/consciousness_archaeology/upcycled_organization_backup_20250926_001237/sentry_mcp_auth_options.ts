// Alternative Sentry MCP Configuration Options

// Option 1: X-Sentry-Token header (currently testing)
const OPTION_1_HEADERS = {
    "sentry": {
        "type": "http",
        "url": "https://mcp.sentry.dev/mcp",
        "headers": {
            "X-Sentry-Token": "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"
        },
        "gallery": true,
        "version": "0.0.1"
    }
};

// Option 2: Environment Variable (if headers fail)
const OPTION_2_ENV = {
    "sentry": {
        "type": "http",
        "url": "https://mcp.sentry.dev/mcp",
        "env": {
            "SENTRY_AUTH_TOKEN": "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"
        },
        "gallery": true,
        "version": "0.0.1"
    }
};

// Option 3: Combined approach
const OPTION_3_COMBINED = {
    "sentry": {
        "type": "http",
        "url": "https://mcp.sentry.dev/mcp",
        "headers": {
            "Authorization": "Bearer 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",
            "X-Sentry-Token": "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"
        },
        "env": {
            "SENTRY_AUTH_TOKEN": "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"
        },
        "gallery": true,
        "version": "0.0.1"
    }
};

export { OPTION_1_HEADERS, OPTION_2_ENV, OPTION_3_COMBINED };