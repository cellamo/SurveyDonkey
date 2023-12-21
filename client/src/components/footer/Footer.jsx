import React from "react";
import logo from "./../../assets/logo.png";
import "./Footer.css";

const Footer = () => {
  return (
    <div id="footer-container">
      <div id="footer-line">
        <hr className="line" />
      </div>
      <div id="footer-logo">
        <img src={logo} id="footer-logo-img" alt="logo" />
      </div>
      <div id="footer-text">
        <span id="x-text">Ⓒ Copyright 2023</span>
      </div>
    </div>
  );
};

export default Footer;
