import React from "react";
import "./WrongUrl.css";
import { useNavigate } from "react-router-dom";
import Header from "../../components/header/Header";
import Footer from "../../components/footer/Footer";

export const WrongUrl = () => {
  const navigate = useNavigate();
  return (
    <div id="wrong-url-container">
      <Header />
      <div id="wrong-url-content">
        <h1 id="wrong-url-text">
          {`Sorry, We Couldn't Find The Page You Are Looking For :(`}
        </h1>
        <button onClick={() => navigate("/")} id="wrong-url-button">
          Go To Homepage
        </button>
      </div>
      <Footer />
    </div>
  );
};
