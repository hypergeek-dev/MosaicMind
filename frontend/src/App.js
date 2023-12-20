import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import BaseLayout from './BaseLayout';
import Home from './templates/home';
import AboutUs from './templates/aboutus';
import AddMeeting from './templates/add_meeting';
import EditMeeting from './templates/edit_meeting';
import MeetingFinder from './templates/meetingfinder';
import MeetingList from './templates/meetinglist';
import Volunteer from './templates/volunteer';
import './Global.css';
function App() {
    return (
        <Router>
            <BaseLayout>
                <Routes>
                    <Route path="/templates/home" element={<Home />} />
                    <Route path="/templates/about-us" element={<AboutUs />} />
                    <Route path="/templates/add_meeting" element={<AddMeeting/>} />
                    <Route path="/templates/edit_meeting" element={<EditMeeting/>} />
                    <Route path="/templates/meetingfinder" element={<MeetingFinder/>} />
                    <Route path="/templates/meetinglist" element={<MeetingList />} />
                    <Route path="/templates/volunteer" element={<Volunteer />} />
                </Routes>
            </BaseLayout>
        </Router>
    );
}

export default App;
