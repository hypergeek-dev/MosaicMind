import 'bootstrap/dist/css/bootstrap.css'; 
import React from 'react';
import { Link } from 'react-router-dom';
import { Navbar, Nav } from 'react-bootstrap'; 

function BaseLayout({ children }) {
    return (
        <div>
            <Navbar bg="body-tertiary" expand="lg" variant="dark">
            <Navbar.Brand href="/" className="text-dark">Navbar</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                        <Link className="nav-link text-dark" to="/templates/home">Home</Link>
                        <Link className="nav-link text-dark" to="/templates/about-us">About Us</Link>
                        <Link className="nav-link text-dark" to="/templates/volunteer">Volunteer</Link>
                    </Nav>
                </Navbar.Collapse>
            </Navbar>

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
