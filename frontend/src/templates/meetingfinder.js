import React, { useState } from 'react';
import { Form, Button, Row, Col, Container } from 'react-bootstrap';

const MeetingSearchForm = ({ onSearch }) => {
    const [searchCriteria, setSearchCriteria] = useState({
        day: '',
        time: '',
        type: ''
    });

    const handleChange = (e) => {
        setSearchCriteria({ ...searchCriteria, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onSearch(searchCriteria);
    };

    return (
        <Container>
            <Form onSubmit={handleSubmit}>
                <Row>
                    <Col md={4}>
                        <Form.Group controlId="formDay">
                            <Form.Label>Day</Form.Label>
                            <Form.Control 
                                as="select" 
                                name="day" 
                                value={searchCriteria.day} 
                                onChange={handleChange}
                            >
                                <option value="">Select a Day</option>
                                {/* Add day options here */}
                            </Form.Control>
                        </Form.Group>
                    </Col>

                    <Col md={4}>
                        <Form.Group controlId="formTime">
                            <Form.Label>Time</Form.Label>
                            <Form.Control 
                                as="select" 
                                name="time" 
                                value={searchCriteria.time} 
                                onChange={handleChange}
                            >
                                <option value="">Select Time</option>
                                {/* Add time options here */}
                            </Form.Control>
                        </Form.Group>
                    </Col>

                    <Col md={4}>
                        <Form.Group controlId="formType">
                            <Form.Label>Type</Form.Label>
                            <Form.Control 
                                as="select" 
                                name="type" 
                                value={searchCriteria.type} 
                                onChange={handleChange}
                            >
                                <option value="">Select Type</option>
                                {/* Add type options here */}
                            </Form.Control>
                        </Form.Group>
                    </Col>
                </Row>

                <Button variant="primary" type="submit">
                    Search
                </Button>
            </Form>
        </Container>
    );
};

export default MeetingSearchForm;
