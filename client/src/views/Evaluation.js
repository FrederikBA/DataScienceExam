import React from 'react';

const Evaluation = () => {
    const movieExamples = [
        {
            title: 'Movie 1',
            similarMovies: ['Similar Movie 1', 'Similar Movie 2', 'Similar Movie 3'],
        },
        {
            title: 'Movie 2',
            similarMovies: ['Similar Movie 4', 'Similar Movie 5', 'Similar Movie 6'],
        },
        // Add more examples as needed
    ];

    return (
        <div className="center">
            <h1>Evaluation</h1>
            {movieExamples.map((movie, index) => (
                <div key={index}>
                    <h3>{movie.title}</h3>
                    <ul>
                        {movie.similarMovies.map((similarMovie, idx) => (
                            <li key={idx}>{similarMovie}</li>
                        ))}
                    </ul>
                </div>
            ))}
        </div>
    )
}

export default Evaluation;
