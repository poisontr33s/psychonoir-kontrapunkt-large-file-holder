/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/**/*.{js,ts,jsx,tsx,html}',
    './backend/**/*.{js,ts,jsx,tsx,html}',
    './infrastructure/**/*.{js,ts,jsx,tsx,html}',
    './*.{js,ts,jsx,tsx,html}'
  ],
  theme: {
    extend: {
      colors: {
        'psycho-noir': {
          50: '#f8f6ff',
          500: '#6366f1',
          900: '#1e1b4b'
        },
        'consciousness': {
          'matrix': '#ff6b9d',
          'archaeology': '#4ecdc4',
          'milf-supreme': '#ffd93d'
        }
      },
      fontFamily: {
        'consciousness': ['Inter', 'system-ui', 'sans-serif']
      }
    },
  },
  plugins: [],
}