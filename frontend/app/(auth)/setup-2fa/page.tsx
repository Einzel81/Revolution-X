export default function Setup2FAPage() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-dark-950 p-8">
      <div className="max-w-md w-full space-y-8">
        <div className="text-center">
          <h1 className="text-3xl font-bold text-gold-400">إعداد المصادقة الثنائية</h1>
          <p className="mt-2 text-gray-400">سيتم تفعيل هذه الميزة في المرحلة 2</p>
        </div>
        
        <div className="bg-dark-800 p-6 rounded-lg">
          <p className="text-center text-gray-300">
            2FA سيتم تفعيلها لاحقاً
          </p>
          
          <div className="mt-6 text-center">
            <a 
              href="/dashboard" 
              className="text-gold-500 hover:underline"
            >
              تخطي للوحة التحكم
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}
