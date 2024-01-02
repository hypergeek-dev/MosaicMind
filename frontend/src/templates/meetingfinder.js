import React from 'react';
import heroImage from '../static/images/banner.webp';
import '../Global.css';

const Home = () => {
  return (
    <div>
      <section className="hero">
        <img src={heroImage} alt="Hero" className="hero-image" />
        <div className="col text-center hero_overlay_text text-box">
          <p>"Diversity: the art of thinking independently together." <br></br> - Malcolm Forbes</p>
        </div>
        <div className="container mt-4">
          <div className="row">
            <div className="col text-center text-box">
              <h2 className="header">What We Are</h2>
              <p className="content home_text_box">
                <strong>Mosaic Minds</strong> is a UK-wide network celebrating neurodiversity, connecting unique minds in a supportive online community. We offer a spectrum of events, from educational workshops to creative meet-ups, fostering a space where every neurodiverse individual can thrive. Our platform is a sanctuary for connection, learning, and growth, where each voice is heard and every story is valued. Together, we are redefining neurodiversity, championing understanding, acceptance, and empowerment.
              </p>
            </div>
            <div className="col text-center button-box">
              <a href="/meetingfinder/" className="btn btn-primary btn-lg">Search Meetings</a>
            </div>
            <div className="col text-center">
              <h2 className="header">Why We Do It</h2>
              <p className="content home_text_box">
                At Mosaic Minds, we're driven by the untapped potential within the neurodiverse community. Our mission is to illuminate and celebrate neurodiversity, creating an environment where every individual flourishes. Through shared experiences and mutual support, we're building a future where neurodiversity is recognized as a unique advantage. We're not just envisioning a more inclusive world; we're actively crafting it, one event and one connection at a time.
              </p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;
