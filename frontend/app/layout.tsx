import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'Revolution X - AI Trading System',
  description: 'Advanced AI-powered trading system for Gold and Metals',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="ar" dir="rtl">
      <body className={inter.className}>
        <main className="min-h-screen bg-dark-950 text-white">
          {children}
        </main>
      </body>
    </html>
  );
}
