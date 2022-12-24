import React from 'react';

function Header() {
  return (
    <div className='w-screen'>
    <header className='w-screen'>
      <h1>My Website</h1>
    </header>
    </div>
  );
}

function Nav() {
  return (
    <nav>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/contact">Contact</a></li>
      </ul>
    </nav>
  );
}

export { Header, Nav };