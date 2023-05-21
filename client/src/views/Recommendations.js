import React, { useState } from 'react';
import api from '../utils/apiUtils';

const Recommendations = () => {
    const [input, setInput] = useState('');
    const [recommendations, setRecommendations] = useState([]);
    const [isLoading, setIsLoading] = useState(true);

    const handleChange = (e) => {
        setInput(e.target.value);
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await api.getAxios().post(api.getUrl() + "/recommend", { input: input });
        if (response.data) {
            setRecommendations(response.data.recommendations);
            setIsLoading(false)

        } else {
            console.error("Recommendations not found in response data:", response.data);
        }
    };


    return (
        <div className="center">
            <h1>Recommendations</h1>
            <div className="text-area-div">
                <form className="form-group text-area" onSubmit={handleSubmit}>
                    <textarea className="form-control text-area" id="summary"
                        value={input}
                        onChange={handleChange}
                        placeholder="Enter movie summary or keywords"
                    />
                    <button className="btn btn-secondary generate-btn" type="submit">Get Recommendations</button>
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
        </div>
    )
}

export default Recommendations;
