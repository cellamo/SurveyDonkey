import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import App from "./App.jsx";
import { WrongUrl } from "./pages/wrongUrl/WrongUrl.jsx";
import { SurveyCreate } from "./pages/surveyCreate/SurveyCreate.jsx";
import { Login } from "./pages/login/Login.jsx";
import { Deneme } from "./pages/deneme/Deneme.jsx";
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/login" element={<Login />} />
        <Route path="/createSurvey" element={<SurveyCreate />} />

        <Route path="*" element={<WrongUrl />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
