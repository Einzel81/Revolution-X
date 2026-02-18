export default function GuardianLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-dark-950">
      <nav className="bg-dark-800 p-4 mb-8">
        <h1 className="text-xl font-bold text-gold-400">AI Guardian</h1>
      </nav>
      {children}
    </div>
  );
}
