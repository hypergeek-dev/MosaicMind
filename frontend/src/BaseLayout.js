import 'bootstrap/dist/css/bootstrap.css';
import React from 'react';
import { Link } from 'react-router-dom';
import { Navbar, Nav, Form, FormControl, Button, Row, Col } from 'react-bootstrap';

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

            <footer className="mt-3">
                <div className="d-flex justify-content-end">
                    <Form inline>
                        <Row>
                            <Col xs="auto">
                                <Form.Label className="mb-2 align-self-center">
                                    ADMIN
                                </Form.Label>
                            </Col>
                            <Col xs="auto">
                                <FormControl
                                    type="text"
                                    placeholder="Username"
                                    className="mb-2"
                                />
                            </Col>
                            <Col xs="auto">
                                <FormControl
                                    type="password"
                                    placeholder="Password"
                                    className="mb-2"
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
            </footer>
        </div>
    );
}

export default BaseLayout;
