export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-dark-950 flex">
      <aside className="w-64 bg-dark-800 min-h-screen p-4">
        <h2 className="text-lg font-bold text-gold-400 mb-4">القائمة</h2>
        <nav className="space-y-2">
          <a href="/dashboard" className="block p-2 hover:bg-dark-700 rounded">الرئيسية</a>
          <a href="/dashboard/trading" className="block p-2 hover:bg-dark-700 rounded">التداول</a>
          <a href="/dashboard/signals" className="block p-2 hover:bg-dark-700 rounded">الإشارات</a>
          <a href="/dashboard/admin" className="block p-2 hover:bg-dark-700 rounded">الأدمن</a>
        </nav>
      </aside>
      <main className="flex-1 p-8">
        {children}
      </main>
    </div>
  );
}
