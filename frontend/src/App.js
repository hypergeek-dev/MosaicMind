import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import BaseLayout from './BaseLayout';
import Home from './templates/home';
import AboutUs from './templates/aboutus';
import AddMeeting from './templates/add_meeting';
import EditMeeting from './templates/edit_meeting';
import MeetingFinder from './templates/meetingfinder';
import MeetingListQuery from './templates/meeting_list_query';
import MeetingListAll from './templates/meeting_list_all';
import Volunteer from './templates/volunteer';
import './Global.css';

function App() {
    return (
        <Router>
            <BaseLayout>
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/aboutus" element={<AboutUs />} />
                    <Route path="/add-meeting" element={<AddMeeting />} />
                    <Route path="/edit-meeting" element={<EditMeeting />} />
                    <Route path="/meetingfinder" element={<MeetingFinder />} />
                    <Route path="/meeting_list_query" element={<MeetingListQuery />} />
                    <Route path="/meeting_list_all" element={<MeetingListAll />} />
                    <Route path="/volunteer" element={<Volunteer />} />
                </Routes>
            </BaseLayout>
        </Router>
    );
}

export default App;
