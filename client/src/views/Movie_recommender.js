// client/src/views/Movie_recommender.js

import React, { useState, useEffect } from "react";
import Plot from "react-plotly.js";
import api from "../utils/apiUtils";

const Movie_recommender = () => {
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(true);
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
      setIsLoading(false)
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
      <div className="text-area-div">
        <form className="form-group text-area" onSubmit={handleSubmit}>
          <label htmlFor="summary">Enter a movie summary:</label>
          <textarea className="form-control text-area" id="summary" value={input} onChange={(e) => setInput(e.target.value)} />
          <button className="btn btn-secondary generate-btn" type="submit">Generate Recommendations</button>
        </form>
      </div>
      <div>
        {!isLoading ?
          <div>
            <ul>
              {recommendations.map((movie, index) => (
                <li className="recommended-movies" key={index}>{movie.title}</li>
              ))}
            </ul></div>
          : <br></br>}
      </div>
      {!isLoading ?
        <div>
          <Plot
            data={plotData}
            layout={{ width: 800, height: 600, title: "Movie Embeddings" }}
          />
        </div>
        : <br></br>}
    </div>
  );
};

export default Movie_recommender;


