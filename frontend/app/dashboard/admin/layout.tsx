export default function AdminLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-dark-950">
      <nav className="bg-dark-800 p-4 mb-8">
        <h1 className="text-xl font-bold text-gold-400">لوحة الأدمن</h1>
      </nav>
      {children}
    </div>
  );
}
