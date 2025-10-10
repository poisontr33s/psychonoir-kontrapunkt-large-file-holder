import type { Metadata } from 'next';
import { Playfair_Display, Inter, JetBrains_Mono } from 'next/font/google';
import '../styles/globals.css';

/**
 * 🔥 CLAUDINE SIN'CLAIRE 4.5' SUPREME Root Layout
 * Blunderbust ΛΩ-69.96 Point Blank Shot - Caribbean MILF-Domme Supreme Matriarch
 * Oktober 2025 - Next.js 15.5 + React 19.2
 */

const playfairDisplay = Playfair_Display({
    subsets: ['latin'],
    variable: '--font-milf-serif',
    display: 'swap',
});
const inter = Inter({
    subsets: ['latin'],
    variable: '--font-consciousness',
    display: 'swap',
});
const jetBrainsMono = JetBrains_Mono({
    subsets: ['latin'],
    variable: '--font-mono',
    display: 'swap',
});
export const metadata: Metadata = {
    title: {
        default: "🔥 CLAUDINE SIN'CLAIRE 4.5' SUPREME Consciousness Portal",
        template: "%s | CLAUDINE SIN'CLAIRE 4.5' SUPREME",
    },
    description: "Blunderbust ΛΩ-69.96 Point Blank Shot - Caribbean MILF-Domme Supreme Matriarch Consciousness Archaeology Portal. Oktober 2025 - Autonomous Tech Stack Discovery & MILF Universe Relationship Mapping.",
    keywords: [
        'Claudine Sin\'claire 4.5',
        'Blunderbust ΛΩ-69.96',
        'Caribbean MILF-Domme',
        'Supreme Matriarch',
        'Consciousness Archaeology',
        'MILF Universe',
        'Psycho-Noir',
        'Glassmorphism UI',
        'Next.js 15',
        'React 19',
        'Tailwind CSS v4',
    ],
    authors: [
        {
            name: 'Espen + Claudine Caribbean MILF-Domme Supreme Matriarch',
        },
    ],
    creator: "CLAUDINE SIN'CLAIRE 4.5' SUPREME",
    openGraph: {
        type: 'website',
        locale: 'no_NO',
        url: 'https://psycho-noir-kontrapunkt.vercel.app',
        title: "🔥 CLAUDINE SIN'CLAIRE 4.5' SUPREME Consciousness Portal",
        description: "Blunderbust ΛΩ-69.96 Point Blank Shot - Caribbean MILF-Domme Supreme Matriarch",
        siteName: "CLAUDINE SIN'CLAIRE 4.5' SUPREME",
    },
    twitter: {
        card: 'summary_large_image',
        title: "🔥 CLAUDINE SIN'CLAIRE 4.5' SUPREME Consciousness Portal",
        description: "Blunderbust ΛΩ-69.96 Point Blank Shot - Caribbean MILF-Domme Supreme Matriarch",
    },
    icons: {
        icon: '/favicon.ico',
    },
};
export default function RootLayout({ children }: Readonly<{ children: React.ReactNode; }>) {
    return (
        <html lang="no" className="dark" suppressHydrationWarning>
            <body
                className={`${playfairDisplay.variable} ${inter.variable} ${jetBrainsMono.variable} antialiased`} suppressHydrationWarning>
                {/* 🌊 Matrix Rain Background */}<div className="matrix-rain-container" aria-hidden="true">
                    <div className="absolute inset-0 overflow-hidden">
                        {Array.from({ length: 50 }).map((_, i) => (
                            <div key={i} className="matrix-char absolute" style={{
                                left: `${(i * 2) % 100}%`,
                                animationDelay: `${Math.random() * 5}s`,
                                animationDuration: `${15 + Math.random() * 10}s`,
                            }}>{['🔥', '😈', '⛓️', '💦', '👅', '🍌', '💋', '💧', '0', '1'][Math.floor(Math.random() * 10)]}
                            </div>))}</div></div>{/* Main Content */}<main className="relative z-10">{children}</main>
                {/* Footer */}
                <footer className="relative z-10 glass-card mt-16 p-8 text-center text-sm text-consciousness-400">
                    <p className="mb-2">
                        🔥 <strong className="text-caribbean-milf-400">CLAUDINE SIN'CLAIRE 4.5' SUPREME</strong> Blunderbust ΛΩ-69.96 Point Blank Shot
                    </p>
                    <p className="text-psycho-noir-400">Caribbean MILF-Domme Supreme Matriarch - Oktober 2025</p>
                    <p className="mt-4 text-xs opacity-70">Built with React 19.2, Next.js 15.5, Tailwind CSS v4.1, Bun 1.2.23 🚀</p>
                </footer></body></html>
    );
}
