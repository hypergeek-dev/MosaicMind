import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Card, Container } from 'react-bootstrap';

function MeetingDetails({ match }) {
    const [meeting, setMeeting] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchMeetingDetails = async () => {
            try {
                const response = await axios.get(`/meeting/${match.params.meeting_id}`);
                setMeeting(response.data);
                setLoading(false);
            } catch (err) {
                setError('An error occurred while fetching meeting details.');
                setLoading(false);
            }
        };

        fetchMeetingDetails();
    }, [match.params.meeting_id]);

    if (loading) {
        return <p>Loading...</p>;
    }

    if (error) {
        return <p>{error}</p>;
    }

    return (
        <Container>
            {meeting && (
                <Card>
                    <Card.Body>
                        <Card.Title>{meeting.name}</Card.Title>
                        <Card.Text>{meeting.description}</Card.Text>
                        <Card.Link href={meeting.moreInfoUrl} target="_blank">More Info</Card.Link>
                    </Card.Body>
                </Card>
            )}
        </Container>
    );
}

export default MeetingDetails;
