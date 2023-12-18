// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import BaseLayout from './BaseLayout';
import Index from './templates/index';
import AboutUs from './templates/aboutus'; // Assuming this is the correct path
import AddEditMeeting from './templates/add_edit_meeting';
import MeetingFinder from './templates/meetingfinder';
import MeetingList from './templates/meetinglist';
import Volunteer from './templates/volunteer';

function App() {
  return (
      <Router>
          <BaseLayout>
              <Switch>
                  <Route exact path="/" component={Index} />
                  <Route path="/about-us" component={AboutUs} />
                  <Route path="/add-edit-meeting" component={AddEditMeeting} />
                  <Route path="/meeting-finder" component={MeetingFinder} />
                  <Route path="/meeting-list" component={MeetingList} />
                  <Route path="/volunteer" component={Volunteer} />
              </Switch>
          </BaseLayout>
      </Router>
  );
}

export default App;

