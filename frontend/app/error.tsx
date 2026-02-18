'use client';

import { useEffect } from 'react';

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    // Log error to monitoring service
    console.error('Application error:', error);
  }, [error]);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-8 bg-dark-950">
      <div className="text-center space-y-6">
        {/* Error Icon */}
        <div className="w-20 h-20 bg-red-500/20 rounded-full flex items-center justify-center mx-auto">
          <svg 
            className="w-10 h-10 text-red-500" 
            fill="none" 
            stroke="currentColor" 
            viewBox="0 0 24 24"
          >
            <path 
              strokeLinecap="round" 
              strokeLinejoin="round" 
              strokeWidth={2} 
              d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" 
            />
          </svg>
        </div>

        {/* Error Message */}
        <h2 className="text-2xl font-bold text-white">
          عذراً، حدث خطأ ما
        </h2>
        <p className="text-gray-400 max-w-md">
          نعتذر عن الإزعاج. فريق Revolution X يعمل على حل المشكلة.
        </p>

        {/* Error Details (in development) */}
        {process.env.NODE_ENV === 'development' && (
          <div className="p-4 bg-dark-800 rounded-lg text-left max-w-2xl mx-auto">
            <p className="text-red-400 font-mono text-sm mb-2">Error Details:</p>
            <pre className="text-xs text-gray-400 overflow-auto">
              {error.message}
              {error.stack}
            </pre>
          </div>
        )}

        {/* Actions */}
        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <button
            onClick={() => reset()}
            className="px-6 py-3 bg-gold-500 hover:bg-gold-600 text-dark-900 font-bold rounded-lg transition-colors"
          >
            إعادة المحاولة
          </button>
          
          <button
            onClick={() => window.location.href = '/'}
            className="px-6 py-3 border border-gray-600 text-gray-300 hover:bg-gray-800 rounded-lg transition-colors"
          >
            العودة للرئيسية
          </button>
        </div>

        {/* Support Link */}
        <p className="text-sm text-gray-500">
          إذا استمرت المشكلة، يرجى{' '}
          <a href="mailto:support@revolution-x.com" className="text-gold-500 hover:underline">
            التواصل مع الدعم
          </a>
        </p>
      </div>
    </div>
  );
}
