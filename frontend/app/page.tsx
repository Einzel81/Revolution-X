import Link from 'next/link';

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-8">
      <div className="text-center space-y-8">
        {/* Logo */}
        <div className="flex items-center justify-center space-x-4 space-x-reverse">
          <div className="w-16 h-16 bg-gradient-to-br from-gold-400 to-gold-600 rounded-full flex items-center justify-center">
            <span className="text-3xl font-bold text-dark-900">X</span>
          </div>
          <h1 className="text-5xl font-bold bg-gradient-to-r from-gold-400 to-gold-600 bg-clip-text text-transparent">
            Revolution X
          </h1>
        </div>

        {/* Tagline */}
        <p className="text-xl text-gray-400 max-w-2xl">
          نظام تداول ذكي متكمد للذهب والمعادن
          <br />
          <span className="text-sm">AI-Powered Trading System for Gold and Metals</span>
        </p>

        {/* Status */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-4xl w-full">
          <StatusCard
            title="Backend"
            status="operational"
            description="FastAPI + TimescaleDB"
          />
          <StatusCard
            title="Frontend"
            status="operational"
            description="Next.js 14 + Tailwind"
          />
          <StatusCard
            title="MT5 Connection"
            status="pending"
            description="Waiting for Phase 3"
          />
        </div>

        {/* CTA */}
        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <Link
            href="/dashboard"
            className="px-8 py-3 bg-gold-500 hover:bg-gold-600 text-dark-900 font-bold rounded-lg transition-colors"
          >
            لوحة التحكم
          </Link>
          <Link
            href="/login"
            className="px-8 py-3 border border-gold-500 text-gold-500 hover:bg-gold-500/10 rounded-lg transition-colors"
          >
            تسجيل الدخول
          </Link>
        </div>

        {/* Phase Info */}
        <div className="mt-12 p-6 bg-dark-800 rounded-lg max-w-2xl">
          <h2 className="text-lg font-semibold mb-4 text-gold-400">المرحلة الحالية: Foundation</h2>
          <ul className="space-y-2 text-gray-400 text-right">
            <li className="flex items-center justify-end gap-2">
              <span>✅</span>
              <span>Docker + TimescaleDB</span>
            </li>
            <li className="flex items-center justify-end gap-2">
              <span>✅</span>
              <span>FastAPI Backend</span>
            </li>
            <li className="flex items-center justify-end gap-2">
              <span>✅</span>
              <span>Next.js Frontend</span>
            </li>
            <li className="flex items-center justify-end gap-2">
              <span>⏳</span>
              <span>User Management (Phase 2)</span>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
}

function StatusCard({
  title,
  status,
  description,
}: {
  title: string;
  status: 'operational' | 'pending' | 'error';
  description: string;
}) {
  const statusColors = {
    operational: 'bg-green-500/20 text-green-400 border-green-500/30',
    pending: 'bg-yellow-500/20 text-yellow-400 border-yellow-500/30',
    error: 'bg-red-500/20 text-red-400 border-red-500/30',
  };

  return (
    <div className={`p-6 rounded-lg border ${statusColors[status]}`}>
      <h3 className="font-semibold mb-2">{title}</h3>
      <p className="text-sm opacity-80">{description}</p>
    </div>
  );
}
