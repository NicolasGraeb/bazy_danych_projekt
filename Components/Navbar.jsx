import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/Navbar.css'; // Optional styles

const Navbar = () => {
  return (
    <nav className="navbar">
      <ul className="navbar-list">
        <li>
          <Link to="/">Strona Główna</Link>
        </li>
        <li>
          <Link to="/agenci">Agenci</Link>
        </li>
        <li>
          <Link to="/wlasciciele">Właściciele</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
