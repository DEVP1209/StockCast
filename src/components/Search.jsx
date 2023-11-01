import React, { useState, useEffect } from "react";
import axios from "axios";
import ReactSearchBox from "react-search-box";

function Search({setChoice}) {
  const [formData, setFormData] = useState({
    inputField: "",
  });
  const [symbol, setSymbol] = useState([]);

  const fetchData = () => {
    fetch("symbols.json")
      .then((response) => response.json())
      .then((jsonData) => {
        setSymbol(jsonData);
      })
      .catch((error) => {
        console.error("Error loading data:", error);
      });
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/api/processFormData",
        formData
      );
      console.log(response.data);
      setChoice(formData.inputField)
    } catch (error) {
      console.error("Error sending data:", error);
    }
  };

  return (
    <div className="search-container">
      <form onSubmit={handleSubmit}>
        {/* <input
        type="text"
        name="inputField"
        value={formData.inputField}
        onChange={(e) => setFormData({ inputField: e.target.value })}
      /> */}
        {symbol && (
          <ReactSearchBox
            placeholder="Search..."
            name="inputField"
            data={symbol}
            value={formData.inputField}
            onChange={(e) => setFormData({ inputField: e })}
          />
        )}
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default Search;
