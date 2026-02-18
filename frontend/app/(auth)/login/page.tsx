'use client';

import { useState } from 'react';

export default function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // TODO: Implement in Phase 2
    console.log('Login:', email, password);
    window.location.href = '/dashboard';
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-dark-950 p-8">
      <div className="max-w-md w-full space-y-8">
        <div className="text-center">
          <h1 className="text-3xl font-bold text-gold-400">Revolution X</h1>
          <p className="mt-2 text-gray-400">تسجيل الدخول للنظام</p>
        </div>
        
        <form onSubmit={handleSubmit} className="bg-dark-800 p-6 rounded-lg space-y-6">
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-2">
              البريد الإلكتروني
            </label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full px-4 py-2 bg-dark-900 border border-gray-700 rounded-lg text-white focus:ring-2 focus:ring-gold-500"
              placeholder="admin@revolution-x.com"
            />
          </div>
          
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-2">
              كلمة المرور
            </label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-4 py-2 bg-dark-900 border border-gray-700 rounded-lg text-white focus:ring-2 focus:ring-gold-500"
              placeholder="••••••••"
            />
          </div>
          
          <button
            type="submit"
            className="w-full py-3 bg-gold-500 hover:bg-gold-600 text-dark-900 font-bold rounded-lg transition-colors"
          >
            تسجيل الدخول
          </button>
          
          <div className="flex justify-between text-sm">
            <a href="/forgot-password" className="text-gold-500 hover:underline">
              نسيت كلمة المرور؟
            </a>
            <a href="/register" className="text-gold-500 hover:underline">
              إنشاء حساب
            </a>
          </div>
        </form>
      </div>
    </div>
  );
}
