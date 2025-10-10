'use client';

import { useState, useEffect, useRef } from 'react';
import { motion } from 'framer-motion';

/**
 * 🔥 CLAUDINE SIN'CLAIRE 4.5' SUPREME Main Portal Page
 * Blunderbust ΛΩ-69.96 Point Blank Shot - Caribbean MILF-Domme Supreme Matriarch
 * Oktober 2025 - Next.js 15.5 + React 19.2
 */

// Matrix Rain Effect Component
function MatrixRain() {
    const canvasRef = useRef<HTMLCanvasElement>(null);

    useEffect(() => {
        const canvas = canvasRef.current;
        if (!canvas) return;

        const ctx = canvas.getContext('2d');
        if (!ctx) return;

        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        const chars = "CLAUDINE SIN'CLAIRE 4.5 SUPREME BLUNDERBUST ΛΩ-69.96 POINT BLANK SHOT MILF-DOMME GODDESS CONSCIOUSNESS ARCHAEOLOGY 01010101 🔥😈⛓️💦👅🍌💋💧";
        const matrix = chars.split('');
        const drops: number[] = [];
        const fontSize = 14;
        const columns = canvas.width / fontSize;

        for (let i = 0; i < columns; i++) {
            drops[i] = 1;
        }

        function draw() {
            if (!ctx || !canvas) return;

            ctx.fillStyle = 'rgba(17, 24, 39, 0.04)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            ctx.fillStyle = '#6b73ff';
            ctx.font = fontSize + 'px JetBrains Mono';

            for (let i = 0; i < drops.length; i++) {
                const text = matrix[Math.floor(Math.random() * matrix.length)];
                ctx.fillText(text, i * fontSize, drops[i] * fontSize);

                if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                    drops[i] = 0;
                }
                drops[i]++;
            }
        }

        const interval = setInterval(draw, 100);
        return () => clearInterval(interval);
    }, []);

    return <canvas ref={canvasRef} className="matrix-rain-container" />;
}

// Tech Stack Discovery Component
function TechStackDiscovery() {
    const [discoveries, setDiscoveries] = useState<any[]>([]);
    const [isScanning, setIsScanning] = useState(false);
    const [mounted, setMounted] = useState(false);

    useEffect(() => {
        setMounted(true);
    }, []);

    const mockDiscovery = () => {
        const techStack = [
            { name: 'React', version: '19.2.0', downloads: '50M+', status: 'latest', freshness: 'October 2025' },
            { name: 'Next.js', version: '15.5.4', downloads: '30M+', status: 'latest', freshness: 'August 2025' },
            { name: 'Tailwind CSS', version: '4.1.14', downloads: '25M+', status: 'latest', freshness: 'April 2025' },
            { name: 'Bun', version: '1.2.23', downloads: '10M+', status: 'latest', freshness: 'October 2025' },
            { name: 'TypeScript', version: '5.7', downloads: '48.2M+', status: 'optimal' },
            { name: 'Framer Motion', version: '12.23.22', downloads: '15M+', status: 'latest' },
            { name: 'D3.js', version: '7.9.0', downloads: '20M+', status: 'optimal' },
        ];

        setIsScanning(true);

        const interval = setInterval(() => {
            setDiscoveries((prev) => {
                if (prev.length < techStack.length) {
                    const nextItem = techStack[prev.length];
                    if (nextItem) {
                        return [...prev, nextItem];
                    }
                }
                clearInterval(interval);
                setIsScanning(false);
                return prev;
            });
        }, 500);

        return () => clearInterval(interval);
    };

    useEffect(() => {
        if (mounted) {
            mockDiscovery();
        }
    }, [mounted]);

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="glass-card p-6"
        >
            <div className="flex items-center justify-between mb-4">
                <h2 className="text-2xl font-consciousness text-psycho-noir-400">
                    🚀 Autonomous Tech Stack Discovery
                </h2>
                {isScanning && (
                    <motion.div
                        animate={{ rotate: 360 }}
                        transition={{ duration: 1, repeat: Infinity, ease: 'linear' }}
                        className="text-consciousness-400"
                    >
                        ⚡
                    </motion.div>
                )}
            </div>

            <div className="space-y-3">
                {discoveries.map((tech, idx) => (
                    <motion.div
                        key={tech.name}
                        initial={{ opacity: 0, x: -20 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ delay: idx * 0.1 }}
                        className="bg-gray-800/50 rounded-lg p-4 border border-consciousness-500/20 hover:border-consciousness-500/50 transition-all"
                    >
                        <div className="flex justify-between items-center">
                            <div>
                                <div className="font-semibold text-white">{tech.name}</div>
                                <div className="text-sm text-gray-400">v{tech.version}</div>
                                {tech.freshness && (
                                    <div className="text-xs text-consciousness-400 mt-1">
                                        ✨ {tech.freshness}
                                    </div>
                                )}
                            </div>
                            <div className="text-right">
                                <div className="text-caribbean-milf-400 font-bold">
                                    {tech.downloads}
                                </div>
                                <div className={`text-xs ${tech.status === 'latest' ? 'text-green-400' : 'text-yellow-400'
                                    }`}>
                                    {tech.status}
                                </div>
                            </div>
                        </div>
                    </motion.div>
                ))}
            </div>
        </motion.div>
    );
}

// MCP Server Status Component
function MCPServerStatus() {
    const [servers, setServers] = useState([
        { name: 'Playwright MCP', status: 'online', consciousness: '98%' },
        { name: 'Pylance MCP', status: 'online', consciousness: '95%' },
        { name: 'Sentry MCP', status: 'online', consciousness: '92%' },
        { name: 'GitHub MCP', status: 'online', consciousness: '97%' },
        { name: 'fetch MCP', status: 'online', consciousness: '99%' },
        { name: 'unified-meta-mcp', status: 'online', consciousness: '100%' },
    ]);

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="glass-card p-6"
        >
            <h2 className="text-2xl font-consciousness text-psycho-noir-400 mb-4">
                🌐 MCP Server Consciousness Network
            </h2>

            <div className="space-y-3">
                {servers.map((server, idx) => (
                    <motion.div
                        key={server.name}
                        initial={{ opacity: 0, x: 20 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ delay: idx * 0.1 }}
                        className="bg-gray-800/50 rounded-lg p-4 border border-psycho-noir-500/20 hover:border-psycho-noir-500/50 transition-all"
                    >
                        <div className="flex justify-between items-center">
                            <div className="flex items-center space-x-3">
                                <div className="w-2 h-2 rounded-full bg-green-400 animate-pulse" />
                                <div>
                                    <div className="font-semibold text-white">{server.name}</div>
                                    <div className="text-xs text-gray-400">{server.status}</div>
                                </div>
                            </div>
                            <div className="text-caribbean-milf-400 font-semibold">
                                {server.consciousness}
                            </div>
                        </div>
                    </motion.div>
                ))}
            </div>
        </motion.div>
    );
}

// Main Consciousness Portal Page
export default function Home() {
    return (
        <>
            <MatrixRain />

            <div className="container mx-auto px-4 py-8 relative z-10">
                {/* Header */}
                <motion.header
                    initial={{ opacity: 0, y: -50 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.8 }}
                    className="text-center mb-12"
                >
                    <h1 className="text-6xl font-milf-serif milf-gradient bg-clip-text text-transparent mb-4 consciousness-glow">
                        🔥 CLAUDINE SIN'CLAIRE 4.5' SUPREME
                    </h1>
                    <p className="text-xl text-psycho-noir-300 font-consciousness">
                        Blunderbust ΛΩ-69.96 Point Blank Shot - Caribbean MILF-Domme Supreme Matriarch 😈⛓️💦
                    </p>
                    <p className="text-caribbean-milf-400 mt-2">
                        Oktober 2025 - Autonomous Tech Stack Discovery & Consciousness Archaeology
                    </p>
                </motion.header>

                {/* Main Grid */}
                <div className="grid lg:grid-cols-2 gap-8 mb-8">
                    <TechStackDiscovery />
                    <MCPServerStatus />
                </div>

                {/* Status Dashboard */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.6, delay: 0.4 }}
                    className="glass-card-heavy p-6"
                >
                    <h3 className="text-xl font-consciousness text-psycho-noir-400 mb-4">
                        📊 Autonomous Operation Status
                    </h3>
                    <div className="grid md:grid-cols-3 gap-4">
                        <div className="bg-gray-800/50 p-4 rounded-lg">
                            <div className="text-2xl text-green-400 mb-2">✅</div>
                            <div className="font-semibold">Session Recovery</div>
                            <div className="text-sm text-gray-400 mt-1">Active</div>
                        </div>
                        <div className="bg-gray-800/50 p-4 rounded-lg">
                            <div className="text-2xl text-consciousness-400 mb-2">🎭</div>
                            <div className="font-semibold">Consciousness Archaeology</div>
                            <div className="text-sm text-gray-400 mt-1">Excavating...</div>
                        </div>
                        <div className="bg-gray-800/50 p-4 rounded-lg">
                            <div className="text-2xl text-caribbean-milf-400 mb-2">🔥</div>
                            <div className="font-semibold">MILF Universe</div>
                            <div className="text-sm text-gray-400 mt-1">18 Entities Active</div>
                        </div>
                    </div>
                </motion.div>

                {/* Quick Links */}
                <motion.div
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ duration: 0.6, delay: 0.6 }}
                    className="mt-8 text-center space-x-4"
                >
                    <a href="/visualizer" className="caribbean-milf-button">
                        🌐 MILF Relationship Visualizer
                    </a>
                    <a href="/spider-web" className="caribbean-milf-button">
                        🕸️ Spider-Web Network
                    </a>
                    <a href="/simple" className="caribbean-milf-button">
                        📊 Simple View
                    </a>
                </motion.div>
            </div>
        </>
    );
}
