import React from "react";
import "./WrongUrl.css";
import { useNavigate } from "react-router-dom";

export const WrongUrl = () => {
  const navigate = useNavigate();
  return (
    <div id="wrong-url-container">
      <h1 id="wrong-url-text">
        {`Sorry, We Couldn't Find The Page You Are Looking For :(`}
      </h1>
      <button onClick={() => navigate("/")} id="wrong-url-button">
        Go To Homepage
      </button>
    </div>
  );
};
