import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';
import { Navbar, Nav, Form, FormControl, Button, Row, Col } from 'react-bootstrap';

function BaseLayout({ children }) {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            // Send a POST request to the login endpoint with username and password
            const response = await axios.post('https://2200-hypergeekdev-mosaicmind-ldowkfntf5v.ws-eu107.gitpod.io/login/', {
                username: username,
                password: password
            });
            console.log(response.data);

            // Redirect based on user type (assuming response.data contains isAdmin)
            if (response.data.isAdmin) {
                navigate('/admin_page');
            } else {
                navigate('/dashboard');
            }
        } catch (error) {
            console.error("There was an error logging in the user!", error);
        }
    };

    return (
        <div>
            {/* Navbar */}
            <Navbar bg="body-tertiary" expand="lg" variant="dark">
                <Navbar.Brand as={Link} to="/" className="text-dark">Navbar</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                        <Nav.Link as={Link} to="/" className="text-dark">Home</Nav.Link>
                        <Nav.Link as={Link} to="/meeting_list_all" className="text-dark">Meetings</Nav.Link>
                        <Nav.Link as={Link} to="/aboutus" className="text-dark">About Us</Nav.Link>
                        <Nav.Link as={Link} to="/feedback" className="text-dark">Feedback</Nav.Link>
                        <Nav.Link as={Link} to="/volunteer" className="text-dark">Volunteer</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
                <div className="d-flex justify-content-end">
                    <Form inline onSubmit={handleSubmit}>
                        <Row>
                            <Col xs="auto">
                                <FormControl
                                    type="text"
                                    placeholder="Username"
                                    className="mb-2"
                                    value={username}
                                    onChange={(e) => setUsername(e.target.value)}
                                />
                            </Col>
                            <Col xs="auto">
                                <FormControl
                                    type="password"
                                    placeholder="Password"
                                    className="mb-2"
                                    value={password}
                                    onChange={(e) => setPassword(e.target.value)}
                                />
                            </Col>
                            <Col xs="auto">
                                <Button type="submit" className="mb-2">
                                    Login
                                </Button>
                            </Col>
                        </Row>
                    </Form>
                </div>
            </Navbar>

            {/* Main Content */}
            <main>
                {children}
            </main>

            {/* Footer */}
            {/* Add your footer code here */}
        </div>
    );
}

export default BaseLayout;
