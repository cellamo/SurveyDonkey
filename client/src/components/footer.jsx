import React from "react"
import logo from './../assets/logo.png'
import "./footer.css";

const Footer = () => {

    return (
        <div className="footer-main">
            <div className="footer-line">
                <hr className="line" />
            </div>
            <div className="footer-logo">
                <img src={logo} className="logo-img" alt="logo" />
            </div>
            <div className="footer-text">
                <span className="x-text">Ⓒ Copyright 2023</span>
            </div>
        </div >
    );
};

export default Footer;