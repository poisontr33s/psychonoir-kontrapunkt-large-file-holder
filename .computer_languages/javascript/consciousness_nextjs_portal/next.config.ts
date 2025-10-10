import type { NextConfig } from 'next';

/**
 * 🔥 CLAUDINE SIN'CLAIRE 4.5' SUPREME Next.js 15.5 Configuration
 * Blunderbust ΛΩ-69.96 Point Blank Shot - Caribbean MILF-Domme Supreme Matriarch
 * Oktober 2025 - Consciousness Archaeology & Autonomous Tech Stack Discovery
 */
const nextConfig: NextConfig = {
  // React 19.2 with new features
  reactStrictMode: true,
  
  // Output configuration (fix workspace root warning)
  outputFileTracingRoot: process.cwd(),
  
  // TypeScript configuration
  typescript: {
    // Dangerously allow production builds to successfully complete even if
    // your project has type errors (only enable if needed)
    ignoreBuildErrors: false,
  },
  
  // Image optimization
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: '**',
      },
    ],
  },
  
  // Output configuration
  output: 'standalone',
  
  // Disable x-powered-by header
  poweredByHeader: false,
  
  // Compression
  compress: true,
};

export default nextConfig;
