import React from 'react';
import { Link } from 'react-router-dom'; 

function BaseLayout({ children }) {
    return (
        <div>
            <header>
                <nav className="navbar navbar-expand-lg bg-body-tertiary container-fluid">
                    <Link className="navbar-brand" to="/">Navbar</Link>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                            <li className="nav-item">
                                <Link className="nav-link" to="/templates/index">Home</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" to="/templates/about-us">About Us</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" to="/templates/volunteer">Volunteer</Link>
                            </li>
                        </ul>
                    </div>
                </nav>
            </header>

            <main>
                {children}
            </main>

            <footer>
                {/* Footer content */}
            </footer>
        </div>
    );
}

export default BaseLayout;
