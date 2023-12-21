import React from "react";
import "./Header.css";
import logo from "./../../assets/logo.png";
import { useNavigate } from "react-router-dom";

const Header = () => {
  const navigate = useNavigate();
  return (
    <div id="header-container">
      <div id="header-left" onClick={() => navigate("/")}>
        <img src={logo} id="header-logo" alt="logo" />
        <span id="header-title">SurveyDonkey</span>
      </div>
      <div id="header-right">
        <button className="header-button" onClick={() => navigate("/login")}>
          Sign In
        </button>
        <button className="header-button" onClick={() => navigate("/BBM479")}>
          Wrong URL
        </button>
        <button className="header-button">Option Three</button>
      </div>
    </div>
  );
};

export default Header;
