import React from "react";
import "./App.css";
import Header from "./components/header/Header";
import Homepage from "./pages/homepage/Homepage";
import Footer from "./components/footer/Footer";

function App() {
  return (
    <div id="app-container">
      <Header />
      <Homepage />
      <Footer />
    </div>
  );
}

export default App;
