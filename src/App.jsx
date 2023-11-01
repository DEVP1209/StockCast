import React, { useState,useEffect } from "react";
import Chart from "./components/Chart";
import Search from "./components/Search";

function App() {
  const [choice, setChoice] = useState("");

  return (
    <div className="main-container">
      <Search setChoice={setChoice}/>
      <Chart choice={choice}/>
    </div>
  );
}

export default App;
