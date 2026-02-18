export default function RegisterPage() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-dark-950 p-8">
      <div className="max-w-md w-full space-y-8">
        <div className="text-center">
          <h1 className="text-3xl font-bold text-gold-400">إنشاء حساب</h1>
          <p className="mt-2 text-gray-400">سيتم تفعيل هذه الميزة في المرحلة 2</p>
        </div>
        
        <div className="bg-dark-800 p-6 rounded-lg">
          <p className="text-center text-gray-300">
            التسجيل متاح فقط من خلال لوحة الأدمن
          </p>
          
          <div className="mt-6 text-center">
            <a 
              href="/login" 
              className="text-gold-500 hover:underline"
            >
              لديك حساب؟ سجل الدخول
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}
