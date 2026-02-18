import Link from 'next/link';

export default function DashboardPage() {
  return (
    <div className="min-h-screen bg-dark-950 p-8">
      <h1 className="text-3xl font-bold text-gold-400 mb-8">لوحة التحكم</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <DashboardCard
          title="التداول"
          description="الشارت والصفقات"
          href="/dashboard/trading"
        />
        <DashboardCard
          title="الإشارات"
          description="إشارات AI"
          href="/dashboard/signals"
        />
        <DashboardCard
          title="الإعدادات"
          description="إعدادات النظام"
          href="/dashboard/admin/settings"
        />
      </div>
    </div>
  );
}

function DashboardCard({ title, description, href }: { title: string; description: string; href: string }) {
  return (
    <Link href={href} className="block p-6 bg-dark-800 rounded-lg hover:bg-dark-700 transition-colors">
      <h2 className="text-xl font-bold text-white mb-2">{title}</h2>
      <p className="text-gray-400">{description}</p>
    </Link>
  );
}
