import React from "react";
import { useState } from "react";
import { InputText } from "primereact/inputtext";
import { Button } from "primereact/button";
import { Message } from "primereact/message";
import "./Login.css";
import logo from "./../../assets/logo.png";
import "primereact/resources/themes/lara-light-indigo/theme.css"; //theme
import "primereact/resources/primereact.min.css"; //core css
import "primeicons/primeicons.css";
import "primeicons/primeicons.css";
import Footer from "../../components/footer/Footer";
import { useNavigate } from "react-router-dom";

export const Login = () => {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [isValid, setIsValid] = useState(true);

  const validateEmail = (input) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(input);
  };

  const handleInputChange = (e) => {
    const inputValue = e.target.value;
    setEmail(inputValue);
    // setIsValid(validateEmail(inputValue));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!validateEmail(email)) {
      setIsValid(false);
      return;
    } else {
      setIsValid(true);
      //TODOOO
      console.log("Oldu");
    }
  };

  return (
    <div className="main-div">
      <div className="login-div">
        <div className="login-sec-div">
          <div className="logo-div">
            <img className="logo-img" src={logo} alt="logo" />
          </div>
          <div className="mail-field">
            <InputText
              id="email"
              placeholder="Enter your email to start!"
              type="text"
              value={email}
              onChange={handleInputChange}
            />
            <div className="p-error">
              {!isValid && <small>Please enter a valid email address</small>}
            </div>
          </div>
          <div className="buttons-div">
            <button onClick={() => navigate("/")} className="back-button">
              Go Back
            </button>
            <button onClick={handleSubmit} className="sign-in-button">
              Login
            </button>
          </div>

          <div className="socials">
            <div id="social">
              <a id="a" href="https://www.instagram.com/">
                <i
                  className="pi pi-instagram"
                  style={{ color: "black", fontSize: "100%" }}
                  alt="Instagram"
                />
                <span id="s">Follow us on Instagram!</span>
              </a>
            </div>
            <div id="social">
              <a id="a" href="https://www.facebook.com/">
                <i
                  className="pi pi-facebook"
                  style={{ color: "black", fontSize: "100%" }}
                  alt="Facebook"
                />
                <span id="s">Follow us on Facebook!</span>
              </a>
            </div>
            <div id="social">
              <a id="a" href="https://twitter.com/">
                <i
                  className="pi pi-twitter"
                  style={{ color: "black", fontSize: "100%" }}
                  alt="Twitter"
                />
                <span id="s">Follow us on Twitter!</span>
              </a>
            </div>
          </div>
        </div>
      </div>
      <div className="footer-div">
        <Footer />
      </div>
    </div>
  );
};
