import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import App from "./App.jsx";
import { WrongUrl } from "./pages/wrongUrl/WrongUrl.jsx";
import "./index.css";
import { Login } from "./pages/login/Login.jsx";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/login" element={<Login />} />
        <Route path="*" element={<WrongUrl />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
