import React, { useEffect, useState } from 'react';
import { Container, Row, Col, Card } from 'react-bootstrap';
import axios from 'axios';

const MeetingListAll = () => {
    const [meetings, setMeetings] = useState([]);
    const [error, setError] = useState(null);  // New state for error

    useEffect(() => {
        axios.get('/meeting_list_all/')
            .then(response => {
                setMeetings(response.data);
            })
            .catch(error => {
                console.error('Error fetching meetings:', error);
                setError(error);  
            });
    }, []);
   
    if (error) {
        return (
            <Container className="mt-4">
                <Row>
                    <Col>
                        <p>There was an error fetching the meetings. Please try again later.</p>
                    </Col>
                </Row>
            </Container>
        );
    }

    return (
        <Container className="mt-4">
            <Row>
                {meetings.length > 0 ? (
                    meetings.map((meeting, index) => (
                        <Col key={index} md={4} className="mb-3">
                            <Card>
                                <Card.Body>
                                    <Card.Title>{meeting.name}</Card.Title>
                                    <Card.Subtitle className="mb-2 text-muted">
                                        {meeting.area}
                                    </Card.Subtitle>
                                    <Card.Text>
                                        {meeting.description}
                                    </Card.Text>
                                    <Card.Link href={meeting.moreInfoUrl}>
                                        More Info
                                    </Card.Link>
                                    <Card.Link href={meeting.onlineMeetingUrl}>
                                        Online Meeting Link
                                    </Card.Link>
                                </Card.Body>
                            </Card>
                        </Col>
                    ))
                ) : (
                    <Col>
                        <p>No meetings available.</p>
                    </Col>
                )}
            </Row>
        </Container>
    );
};

export default MeetingListAll;
