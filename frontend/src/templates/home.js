import React from 'react';
import { Link } from 'react-router-dom';
import heroImage from '../static/images/banner.webp';

const Home = () => {
  return (
    <div>
      {/* Hero section */}
      <section className="hero">
        <img src={heroImage} alt="Hero" className="hero-image" />

        {/* Centered button */}
        <div className="hero-button">
          <Link to="/meetinglist" className="btn btn-primary btn-lg">Find Meeting</Link>
        </div>
      </section>
    </div>
  );
};

export default Home;
