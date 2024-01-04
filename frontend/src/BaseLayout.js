import 'bootstrap/dist/css/bootstrap.css';
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
            const response = await axios.post('http://localhost:8000/login/', {
                username: username,
                password: password
            });
            console.log(response.data);
    
      
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

<Navbar bg="body-tertiary" expand="lg" variant="dark">
                <Navbar.Brand href="/" className="text-dark">Navbar</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                        <Link className="nav-link text-dark" to="/">Home</Link>
                        <Link className="nav-link text-dark" to="/meeting_list_all">Meetings</Link>
                        <Link className="nav-link text-dark" to="/aboutus">About Us</Link>
                        <Link className="nav-link text-dark" to="/feedback">Feedback</Link>
                        <Link className="nav-link text-dark" to="/volunteer">Volunteer</Link>
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

            <main>
                {children}
            </main>

            {/* ... Footer ... */}
        </div>
    );
}

export default BaseLayout;
