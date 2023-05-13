import React, { useState } from 'react';
import axios from 'axios';
import api from '../utils/apiUtils';

const Recommendations = () => {
    const [input, setInput] = useState('');
    const [recommendations, setRecommendations] = useState([]);

    const handleChange = (e) => {
        setInput(e.target.value);
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await api.getAxios().post(api.getUrl() + "/recommend", { input: input });
        if (response.data) {
          setRecommendations(response.data);
        } else {
          console.error("Recommendations not found in response data:", response.data);
        }
      };
      

    return (
        <div className="center">
            <h1>Recommendations</h1>
            <form onSubmit={handleSubmit}>
                <textarea
                    value={input}
                    onChange={handleChange}
                    placeholder="Enter movie summary or keywords"
                />
                <button type="submit">Get Recommendations</button>
            </form>
            {recommendations.map((movie, index) => (
                <div key={index}>

                    <h2>{movie.title}</h2>
                    <p>{movie.summary}</p>
                </div>
            ))}
        </div>
    )
}

export default Recommendations;
