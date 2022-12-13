import React from 'react';
import Link from 'next/link';

const Navigation = () => {
  return (
    <nav className="bg-gray-900 text-white py-4">
      <div className="container mx-auto px-6">
        <Link href="/" className="text-lg font-semibold text-gray-100 no-underline">
          Your Website
        </Link>

        <div className="flex items-center ml-auto">
          <Link href="/about" className="px-3 py-2 rounded-lg text-sm font-medium hover:bg-gray-800 focus:outline-none focus:bg-gray-800">
            About
          </Link>
          <Link href="/custom" className="px-3 py-2 rounded-lg text-sm font-medium hover:bg-gray-800 focus:outline-none focus:bg-gray-800">
            Contact
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Navigation;
