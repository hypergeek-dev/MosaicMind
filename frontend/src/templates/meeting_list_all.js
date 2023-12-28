import React, { useEffect, useState } from 'react';
import { Container, Row, Col, Card, Spinner, Alert } from 'react-bootstrap';
import axios from 'axios';

const fetchMeetings = async () => {
    try {
        const response = await axios.get('/meeting_list_all/');
        return response.data;
    } catch (error) {
        throw error;
    }
};

const MeetingListAll = () => {
    const [meetings, setMeetings] = useState([]);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        setIsLoading(true);
        fetchMeetings()
            .then(data => {
                setMeetings(data);
                setIsLoading(false);
            })
            .catch(error => {
                console.error('Error fetching meetings:', error);
                setError(error);
                setIsLoading(false);
            });
    }, []);

    if (isLoading) {
        return (
            <Container className="mt-4 text-center">
                <Spinner animation="border" role="status" />
                <p>Loading meetings...</p>
            </Container>
        );
    }

    if (error) {
        return (
            <Container className="mt-4">
                <Alert variant="danger">
                    There was an error fetching the meetings: {error.message}
                </Alert>
            </Container>
        );
    }

    return (
        <Container className="mt-4">
            <Row>
                {meetings.length > 0 ? (
                    meetings.map(meeting => (
                        <Col key={meeting.id} md={4} className="mb-3">
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
                        <Alert variant="info">No meetings are currently available.</Alert>
                    </Col>
                )}
            </Row>
        </Container>
    );
};

export default MeetingListAll;
