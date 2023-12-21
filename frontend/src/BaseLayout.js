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
                        <Link className="nav-link text-dark" to="/">Home</Link>
                        <Link className="nav-link text-dark" to="/meeting_list_all">Meetings</Link>
                        <Link className="nav-link text-dark" to="/aboutus">About Us</Link>
                        <Link className="nav-link text-dark" to="/volunteer">Volunteer</Link>
                    </Nav>
                </Navbar.Collapse>
            </Navbar>

            <main>
                {children}
            </main>

            <footer>

            </footer>
        </div>
    );
}

export default BaseLayout;
