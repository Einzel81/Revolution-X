'use client';

import { useState } from 'react';
import { 
  LayoutDashboard, 
  TrendingUp, 
  Activity, 
  Settings, 
  Users, 
  Bell,
  Menu,
  X,
  LogOut,
  Shield
} from 'lucide-react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';

const sidebarItems = [
  { icon: LayoutDashboard, label: 'لوحة التحكم', href: '/dashboard' },
  { icon: TrendingUp, label: 'التداول', href: '/dashboard/trading' },
  { icon: Activity, label: 'الإشارات', href: '/dashboard/signals' },
  { icon: Shield, label: 'AI Guardian', href: '/dashboard/guardian' },
  { icon: Users, label: 'المستخدمين', href: '/dashboard/users', adminOnly: true },
  { icon: Settings, label: 'الإعدادات', href: '/dashboard/settings' },
];

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const pathname = usePathname();

  return (
    <div className="min-h-screen bg-dark-950 flex">
      {/* Sidebar */}
      <aside 
        className={`fixed inset-y-0 right-0 z-50 w-64 bg-dark-900 border-l border-dark-800 transform transition-transform duration-300 ease-in-out ${
          sidebarOpen ? 'translate-x-0' : 'translate-x-full'
        } lg:translate-x-0 lg:static`}
      >
        <div className="flex items-center justify-between p-4 border-b border-dark-800">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-gradient-to-br from-gold-400 to-gold-600 rounded-lg flex items-center justify-center">
              <span className="text-xl font-bold text-dark-900">X</span>
            </div>
            <span className="text-xl font-bold text-white">Revolution X</span>
          </div>
          <button 
            onClick={() => setSidebarOpen(false)}
            className="lg:hidden text-gray-400 hover:text-white"
          >
            <X size={24} />
          </button>
        </div>

        <nav className="p-4 space-y-2">
          {sidebarItems.map((item) => {
            const Icon = item.icon;
            const isActive = pathname === item.href;
            
            return (
              <Link
                key={item.href}
                href={item.href}
                className={`flex items-center gap-3 px-4 py-3 rounded-lg transition-colors ${
                  isActive 
                    ? 'bg-gold-500/20 text-gold-400 border-r-2 border-gold-500' 
                    : 'text-gray-400 hover:bg-dark-800 hover:text-white'
                }`}
              >
                <Icon size={20} />
                <span>{item.label}</span>
              </Link>
            );
          })}
        </nav>

        <div className="absolute bottom-0 right-0 left-0 p-4 border-t border-dark-800">
          <button className="flex items-center gap-3 px-4 py-3 text-red-400 hover:text-red-300 w-full rounded-lg hover:bg-red-500/10 transition-colors">
            <LogOut size={20} />
            <span>تسجيل الخروج</span>
          </button>
        </div>
      </aside>

      {/* Main Content */}
      <div className="flex-1 flex flex-col min-w-0">
        {/* Header */}
        <header className="bg-dark-900 border-b border-dark-800 px-4 py-3 flex items-center justify-between">
          <button 
            onClick={() => setSidebarOpen(true)}
            className="lg:hidden text-gray-400 hover:text-white"
          >
            <Menu size={24} />
          </button>

          <div className="flex items-center gap-4">
            {/* System Status */}
            <div className="flex items-center gap-2 px-3 py-1.5 bg-green-500/20 text-green-400 rounded-full text-sm">
              <span className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></span>
              <span>النظام يعمل</span>
            </div>

            {/* Latency */}
            <div className="hidden md:flex items-center gap-2 text-gray-400 text-sm">
              <Activity size={16} />
              <span>Latency: 23ms</span>
            </div>

            {/* Notifications */}
            <button className="relative p-2 text-gray-400 hover:text-white rounded-lg hover:bg-dark-800 transition-colors">
              <Bell size={20} />
              <span className="absolute top-1 right-1 w-2 h-2 bg-red-500 rounded-full"></span>
            </button>

            {/* User Avatar */}
            <div className="w-10 h-10 bg-gradient-to-br from-primary-500 to-primary-700 rounded-full flex items-center justify-center text-white font-bold">
              A
            </div>
          </div>
        </header>

        {/* Page Content */}
        <main className="flex-1 p-6 overflow-auto">
          {children}
        </main>
      </div>
    </div>
  );
}
