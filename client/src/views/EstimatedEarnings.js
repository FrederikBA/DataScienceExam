import { useState } from "react"
import apiUtils from "../utils/apiUtils";

const EstimatedEarnings = () => {
    const [viewModel, setViewModel] = useState({});
    const [isLoading, setIsLoading] = useState(true);
    const [movieDto, setMovieDto] = useState({
        "year": 2023,
        "runtime": 60,
        "rating": 1,
        "certificate": 1
    });

    const URL = apiUtils.getUrl()

    const predictEarnings = async () => {
        const response = await apiUtils.getAxios().post(URL + '/earnings', movieDto)
        setViewModel(response.data)
        setIsLoading(false)
    }

    const updateMovieDto = (event) => {
        setMovieDto({ ...movieDto, [event.target.id]: Number(event.target.value) })
        console.log(movieDto);
    }

    let minutes = [];
    for (let i = 60; i <= 300; i += 10) {
        minutes.push(i);
    }

    let years = [];
    for (let i = 2023; i >= 1920; i--) {
        years.push(i);
    }

    let certificates = {
        'PG-13': 1,
        'PG': 2,
        'R': 3,
        'G': 4,
        'Not Rated': 5,
        'TV-MA': 6,
        'Passed': 7,
        'TV-Y7': 8,
        'TV-PG': 9,
        'Approved': 10
    };

    let ratings = [];
    for (let i = 1; i <= 9; i++) {
        for (let j = 0; j < 10; j++) {
            let rating = parseFloat(i + '.' + j);
            ratings.push(rating);
        }
    }


    return (
        <div className="center">
            <h1>Predict Movie Earnings</h1>
            <div className="text-area-div">
                <div className="text-area">
                    <form onChange={updateMovieDto} className="form-group">
                        <div className="grid-container">
                            {/* Release year */}
                            <div>
                                <label htmlFor="year">Release Year:</label>
                                <select id="year" className="form-select form-select-sm earnings-select" aria-label=".form-select-sm example">
                                    {years.map((year) => (
                                        <option key={year} value={year} id="year">
                                            {year}
                                        </option>
                                    ))}
                                </select>
                            </div>

                            {/* Runtime */}
                            <div>
                                <label htmlFor="runtime">Runtime:</label>
                                <select id="runtime" className="form-select form-select-sm earnings-select" aria-label=".form-select-sm example">
                                    {minutes.map((minute) => (
                                        <option key={minute} value={minute} id="runtime">
                                            {minute} minutes
                                        </option>
                                    ))}
                                </select>
                            </div>

                            {/* Rating */}
                            <div>
                                <label htmlFor="rating">Rating:</label>
                                <select id="rating" className="form-select form-select-sm earnings-select" aria-label=".form-select-sm example">
                                    {ratings.map((rating) => (
                                        <option key={rating} value={rating} id="rating">
                                            {rating}
                                        </option>
                                    ))}
                                </select>
                            </div>

                            {/* Certificate */}
                            <div>
                                <label htmlFor="certificate">Certificate:</label>
                                <select id="certificate" className="form-select form-select-sm earnings-select" aria-label=".form-select-sm example">
                                    {Object.entries(certificates).map(([c, value]) => (
                                        <option key={c} value={value} id="certificate">
                                            {c}
                                        </option>
                                    ))}
                                </select>
                            </div>
                        </div>
                    </form>
                    <button onClick={predictEarnings} type="submit" className="btn btn-secondary earnings-btn">Predict</button>
                    <div>
                        {!isLoading ? (
                            <div className="mt-5">
                                <p>Your movie is predicted to be a <strong>{viewModel.top}</strong> movie!</p>
                                <p>Movies in this category have earned between <strong>{viewModel.min}$</strong> and <strong>{viewModel.max}$</strong></p>
                                <p>The average movie in {viewModel.top} has earned <strong>{viewModel.avg}$</strong></p>
                            </div>
                        ) : (
                            <br />
                        )}
                    </div>
                </div>
            </div>
        </div>)
}

export default EstimatedEarnings