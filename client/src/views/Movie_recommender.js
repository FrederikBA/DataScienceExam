// client/src/views/Movie_recommender.js

import React, { useState, useEffect } from "react";
import Plot from "react-plotly.js";
import api from "../utils/apiUtils";

const Movie_recommender = () => {
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
    const response = await api.getAxios().post(api.getUrl() + "/recommend", { input: input });
    if (response.data) {
      setRecommendations(response.data.recommendations);
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

  const Card = ({ src, title, duration }) => {
    return (
      <div className="card">
        <img src={src} alt="course image" />
        <footer>
          <h2>{title}</h2>
        </footer>
      </div>
    );
  };
  
  const Flexbox = (props) => {
    return <div className="flex">{props.children}</div>;
  };


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
            <ul id="customrow">
              {recommendations.map((movie, index) => (
                      <Flexbox>
                      <Card
                        key={index}
                        src="https://images.ctfassets.net/qz1k4i0kbshi/4JpOhXeZy37AWiqcn2dswS/c6e3aecdf50049a0ba6cfa01bfcdc669/html-css-logo.png?w=600&h=338&q=50"
                        title={movie.title}
                      />
                      </Flexbox>
              ))}
            </ul></div>
          : <br></br>}
      </div>
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

export default Movie_recommender;


