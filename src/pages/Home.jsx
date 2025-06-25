import Logo from '../components/Logo';

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-50 p-8">
      <Logo />
      <h1 className="text-3xl font-bold mt-4">Welcome to Campus Assistant</h1>
      <p className="text-gray-600 mt-2">
        Get started by selecting an option from the menu above.
      </p>

      <div className="mt-10 text-3xl font-bold underline text-blue-500">
        Hello Tailwind!
      </div>
    </div>
  );
}
