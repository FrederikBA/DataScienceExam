import React, { useState, useEffect } from "react";
import Plot from "react-plotly.js";
import api from "../utils/apiUtils";
import Posters from '../components/Posters';

const MovieRecommender = () => {
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(true);
  const [recommendations, setRecommendations] = useState([]);
  const [embeddings, setEmbeddings] = useState([]);

  // useEffect(() => {
  //   fetchEmbeddings();
  // }, []);

  // const fetchEmbeddings = async () => {
  //   try {
  //     const response = await api.getAxios().get(api.getUrl() + "/embeddings");
  //     setEmbeddings(response.data);
  //   } catch (error) {
  //     console.error("Error fetching embeddings:", error);
  //   }
  // };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await api.getAxios().post(api.getUrl() + "/recommend", { summary: input });

    if (response.data) {
      setRecommendations(response.data.recommendations);
      console.log(recommendations)
      setEmbeddings(response.data.embeddings)
      setIsLoading(false)
    } else {
      console.error("Recommendations not found in response data:", response.data);
    }
  };



  const colorRecommendedMovies = () => {
    // Get titles of recommended movies
    const recommendedTitles = recommendations.map((r) => r.title);

    // Update colors of embeddings
    const updatedEmbeddings = embeddings.map((e) => ({
      ...e,
      color: recommendedTitles.includes(e.title) ? 'red' : 'blue',
    }));

    setEmbeddings(updatedEmbeddings);
  };

  useEffect(() => {
    colorRecommendedMovies();
  }, [recommendations]);

  const plotData = [
    {
      x: embeddings.map((e) => e.x),
      y: embeddings.map((e) => e.y),
      z: embeddings.map((e) => e.z),  // New field for the z-coordinate
      text: embeddings.map((e) => e.title),
      mode: "markers",
      type: "scatter3d",
      marker: {
        size: 2,
        color: embeddings.map((e) => e.color),
      },
    },
  ];

  return (
    <div className="center">
      <h1>Movie Recommender</h1>
      <div className="text-area-div">
        <form className="form-group text-area" onSubmit={handleSubmit}>
          <label htmlFor="summary">Descripe what kind of movie you want to see, you can include actor names and genres if you wish:</label>
          <textarea className="form-control text-area" id="summary" value={input} onChange={(e) => setInput(e.target.value)} />
          <button className="btn btn-secondary generate-btn" type="submit">Generate Recommendations</button>
        </form>
      </div>
      {!isLoading ? (
        <div className='container mt-5'>
          <Posters movies={recommendations} isLoading={isLoading} />
        </div>
      ) : (<br />)}
      {!isLoading ? (
        <div>
          <Plot
            data={plotData}
            layout={{ width: 800, height: 600, title: "Movie Embeddings" }}
          />
        </div>
      ) : (
        <br />
      )}
    </div>
  );
};

export default MovieRecommender;


