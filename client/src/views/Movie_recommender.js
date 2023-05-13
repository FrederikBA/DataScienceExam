// client/src/views/Movie_recommender.js

import React, { useState, useEffect } from "react";
import Plot from "react-plotly.js";
import api from "../utils/apiUtils";

const Movie_recommender = () => {
  const [input, setInput] = useState("");
  const [recommendations, setRecommendations] = useState([]);
  const [embeddings, setEmbeddings] = useState([]);

  useEffect(() => {
    fetchEmbeddings();
  }, []);

  const fetchEmbeddings = async () => {
    try {
      const response = await api.getAxios().get(api.getUrl() + "/embeddings");
      setEmbeddings(response.data);
    } catch (error) {
      console.error("Error fetching embeddings:", error);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await api.getAxios().post(api.getUrl() + "/recommend", { input: input });
    if (response.data) {
      setRecommendations(response.data);
    } else {
      console.error("Recommendations not found in response data:", response.data);
    }
  };
  
  

  const plotData = [
    {
      x: embeddings.map((e) => e.x),
      y: embeddings.map((e) => e.y),
      text: embeddings.map((e) => e.title),
      mode: "markers",
      type: "scatter",
      marker: { size: 12 },
    },
  ];

  return (
    <div className="center">
      <h1>Movie Recommender</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="summary">Enter a movie summary:</label>
        <textarea id="summary" value={input} onChange={(e) => setInput(e.target.value)} />
        <button type="submit">Get Recommendations</button>
      </form>
      <div>
        <h2>Recommended Movies:</h2>
        <ul>
            {recommendations.map((movie, index) => (
                <li key={index}>{movie.title}</li>
            ))}
        </ul>
      </div>
      <Plot
        data={plotData}
        layout={{ width: 800, height: 600, title: "Movie Embeddings" }}
      />
    </div>
  );
};

export default Movie_recommender;


