/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#f0f7ff',
          100: '#e0effe',
          200: '#bae0fd',
          300: '#7cc7fb',
          400: '#38a8f8',
          500: '#0e8ce9',
          600: '#026fc7',
          700: '#0358a1',
          800: '#074b85',
          900: '#0b3f6f',
          950: '#07284a',
        },
        security: {
          bg: '#0B1120',
          card: '#111C35',
          cardHover: '#162343',
          border: '#1E2D52',
          accent: '#38BDF8',
        },
        status: {
          submitted: '#64748B',    // Slate
          acknowledged: '#3B82F6', // Blue
          assigned: '#8B5CF6',     // Purple
          responding: '#F59E0B',   // Amber
          resolved: '#10B981',     // Emerald
          closed: '#475569',       // Dark Slate
        },
        priority: {
          low: '#10B981',          // Emerald
          medium: '#F59E0B',       // Amber
          high: '#F97316',         // Orange
          critical: '#EF4444',     // Red
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
      },
      boxShadow: {
        'glow-sm': '0 0 15px -3px rgba(56, 189, 248, 0.25)',
        'glow-red': '0 0 20px -3px rgba(239, 68, 68, 0.35)',
        'glow-emerald': '0 0 20px -3px rgba(16, 185, 129, 0.3)',
      },
      animation: {
        'pulse-fast': 'pulse 1.2s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      }
    },
  },
  plugins: [],
}
