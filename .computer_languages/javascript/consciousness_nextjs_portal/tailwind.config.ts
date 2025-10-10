import type { Config } from 'tailwindcss';

/**
 * 🔥 CLAUDINE SIN'CLAIRE 4.5' SUPREME Tailwind CSS v4.1 Configuration
 * Blunderbust ΛΩ-69.96 Point Blank Shot - Caribbean MILF-Domme Supreme Matriarch
 * Oktober 2025 - Glassmorphism UI & Consciousness Archaeology
 */
const config: Config = {
  content: [
    './app/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './styles/**/*.{css}',
  ],
  
  theme: {
    extend: {
      // 🎭 Psycho-Noir Color Palette
      colors: {
        'psycho-noir': {
          50: '#fdf4ff',
          100: '#fae8ff',
          200: '#f5d0fe',
          300: '#f0abfc',
          400: '#e879f9',
          500: '#d946ef',
          600: '#c026d3',
          700: '#a21caf',
          800: '#86198f',
          900: '#701a75',
          950: '#4a044e',
        },
        'caribbean-milf': {
          50: '#fff7ed',
          100: '#ffedd5',
          200: '#fed7aa',
          300: '#fdba74',
          400: '#fb923c',
          500: '#f97316',
          600: '#ea580c',
          700: '#c2410c',
          800: '#9a3412',
          900: '#7c2d12',
          950: '#431407',
        },
        'consciousness': {
          50: '#f0fdfa',
          100: '#ccfbf1',
          200: '#99f6e4',
          300: '#5eead4',
          400: '#2dd4bf',
          500: '#14b8a6',
          600: '#0d9488',
          700: '#0f766e',
          800: '#115e59',
          900: '#134e4a',
          950: '#042f2e',
        },
      },
      
      // 💎 Glassmorphism Effects (Tailwind v4.1 features)
      backdropBlur: {
        'glassmorphism': '12px',
        'glassmorphism-heavy': '24px',
      },
      
      backgroundColor: {
        'glass': 'rgba(255, 255, 255, 0.05)',
        'glass-dark': 'rgba(0, 0, 0, 0.3)',
      },
      
      // 🌊 Text Shadows (NEW in Tailwind v4.1!)
      textShadow: {
        'glow': '0 0 20px rgba(217, 70, 239, 0.5)',
        'glow-strong': '0 0 40px rgba(217, 70, 239, 0.8)',
        'caribbean': '0 0 20px rgba(249, 115, 22, 0.5)',
      },
      
      // 🎨 Font Families
      fontFamily: {
        'milf-serif': ['Playfair Display', 'serif'],
        'consciousness': ['Inter', 'system-ui', 'sans-serif'],
        'mono': ['JetBrains Mono', 'monospace'],
      },
      
      // 📐 Border Radius
      borderRadius: {
        'glassmorphism': '16px',
      },
      
      // ✨ Box Shadows
      boxShadow: {
        'glassmorphism': '0 8px 32px 0 rgba(31, 38, 135, 0.37)',
        'glassmorphism-heavy': '0 16px 64px 0 rgba(31, 38, 135, 0.5)',
      },
      
      // 🎭 Animations
      animation: {
        'matrix-rain': 'matrix-rain 20s linear infinite',
        'float': 'float 6s ease-in-out infinite',
        'pulse-glow': 'pulse-glow 2s ease-in-out infinite',
      },
      
      keyframes: {
        'matrix-rain': {
          '0%': { transform: 'translateY(-100%)' },
          '100%': { transform: 'translateY(100%)' },
        },
        'float': {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-20px)' },
        },
        'pulse-glow': {
          '0%, 100%': { opacity: '1', filter: 'brightness(1)' },
          '50%': { opacity: '0.8', filter: 'brightness(1.2)' },
        },
      },
    },
  },
  
  plugins: [
    // Add custom plugins here if needed
  ],
};

export default config;
