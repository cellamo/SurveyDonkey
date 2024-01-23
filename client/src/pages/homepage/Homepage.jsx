import React from "react";
import "./Homepage.css";
import welcomeImage from "../../assets/welcome-image.png";

const Homepage = () => {
  return (
    <div id="homepage-content">
      <div id="welcome">
        <div id="welcome-left-side">
          <h1>WELCOME TO SURVEY DONKEY!</h1>
          <p>
            Creating surveys has never been easier. With our user-friendly drag
            and drop interface, you can design, customize and share surveys
            effortlessly. Enage with your audience, gather valuable insights and
            make data-driven decisions. Get started today and discover the power
            of easy, effective surveys!
          </p>
          <div id="welcome-left-buttons">
            <button id="call-to-action">CALL TO ACTION</button>
            <button id="learn-more">LEARN MORE</button>
          </div>
        </div>
        <div id="welcome-right-side">
          <img id="welcome-image" src={welcomeImage} alt="welcome image" />
        </div>
      </div>
      <div className="homepage-section-splitter">
        <hr className="line" />
      </div>
      <div id="homepage-explanation">
        <p id="homepage-explanation-text">
          Lorem, ipsum dolor sit amet consectetur adipisicing elit. Magnam
          expedita ducimus reprehenderit assumenda quos, optio commodi impedit
          quod deleniti accusamus blanditiis porro itaque cupiditate delectus
          quo in, quia maiores suscipit laboriosam doloribus cum! Assumenda
          voluptatem cum et exercitationem aliquid quis?
        </p>
      </div>
      <div className="homepage-section-splitter">
        <hr className="line" />
      </div>
      <div id="how-this-works">
        <h1>How This Works?</h1>
        <p>
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Enim,
          corporis?
        </p>
        <div id="how-this-works-steps">
          <div className="how-this-works-step-div">
            <div className="step-circle">01</div>
            <h5 className="step-header">Create</h5>
            <p className="step-explanation">
              Create surveys by using your email
            </p>
          </div>
          <div className="how-this-works-step-div">
            <div className="step-circle">02</div>
            <h5 className="step-header">Share</h5>
            <p className="step-explanation">
              Share your surveys with a 24 hours link
            </p>
          </div>
          <div className="how-this-works-step-div">
            <div className="step-circle">03</div>
            <h5 className="step-header">Survey</h5>
            <p className="step-explanation">
              Make your customers fill the surveys you created
            </p>
          </div>
          <div className="how-this-works-step-div">
            <div className="step-circle">04</div>
            <h5 className="step-header">Analyze</h5>
            <p className="step-explanation">
              Examine your survey results with easy to understand graphs and
              charts
            </p>
          </div>
        </div>
      </div>
      <div className="homepage-section-splitter">
        <hr className="line" />
      </div>
      <div id="advantages">
        <h1 id="advantages-header">Our Advantages</h1>
        <p id="advantages-explanation">
          Lorem ipsum dolor sit, amet consectetur adipisicing elit. Non, nihil.
        </p>
        <div id="benefits-div">
          <div className="benefit-div">
            <i className="benefit-icon pi pi-heart"></i>
            <h2 className="benefit-header">Benefit 1</h2>
            <p className="benefit-explanation">
              Lorem ipsum dolor sit amet consectetur adipisicing elit.
            </p>
          </div>
          <div className="benefit-div">
            <i className="benefit-icon pi pi-heart-fill"></i>
            <h2 className="benefit-header">Benefit 2</h2>
            <p className="benefit-explanation">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Harum
              deleniti non eius?{" "}
            </p>
          </div>
          <div className="benefit-div">
            <i className="benefit-icon pi pi-heart"></i>
            <h2 className="benefit-header">Benefit 3</h2>
            <p className="benefit-explanation">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet
              ea debitis magni dolorum praesentium illo voluptates.{" "}
            </p>
          </div>
        </div>
      </div>
      <div className="homepage-section-splitter">
        <hr className="line" />
      </div>
      <div id="contact-us">
        <div id="contact-div">
          <h2 id="contact-us-header">Contact Us</h2>
          <div id="contact-us-addresses">
            <div className="contact-address">
              <h5 className="contact-address-header">Ankara, Türkiye</h5>
              <div className="contact-content">
                <i className="contact-content-icon pi pi-map-marker"></i>
                <p className="contact-content-info">
                  Potsdamer Platz 16B, 10785
                </p>
              </div>
              <div className="contact-content">
                <i className="contact-content-icon pi pi-envelope"></i>
                <p className="contact-content-info">contact-tr@company.tr</p>
              </div>
              <div className="contact-content">
                <i className="contact-content-icon pi pi-phone"></i>
                <p className="contact-content-info">01234 56789</p>
              </div>
            </div>
            <div className="contact-address">
              <h5 className="contact-address-header">Istanbul, Türkiye</h5>
              <div className="contact-content">
                <i className="contact-content-icon pi pi-map-marker"></i>
                <p className="contact-content-info">
                  177 Huntington Ave Ste 1703
                </p>
              </div>
              <div className="contact-content">
                <i className="contact-content-icon pi pi-envelope"></i>
                <p className="contact-content-info">contact-us@company.tr</p>
              </div>
              <div className="contact-content">
                <i className="contact-content-icon pi pi-phone"></i>
                <p className="contact-content-info">+90 987 654 32 10</p>
              </div>
            </div>
          </div>
        </div>
        <div id="contact-us-location-div">
          <iframe
            className="location-google-maps-iframe"
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1975.8514028062395!2d32.73539960554325!3d39.870643703941695!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14d3476c7df6a739%3A0xd3ae6a4e60ccb982!2sHacettepe%20%C3%9Cniversitesi%20Bilgisayar%20M%C3%BChendisli%C4%9Fi!5e0!3m2!1sen!2str!4v1705908284831!5m2!1sen!2str"
            width="100%"
            height="100%"
            allowFullScreen=""
            loading="lazy"
            referrerPolicy="no-referrer-when-downgrade"
          ></iframe>
        </div>
      </div>
    </div>
  );
};

export default Homepage;
