import React, { useState } from 'react';

function Sentiment() {
  const [text, setText] = useState('');
  const [result, setResult] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('http://127.0.0.1:8000/sentiment', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      });

      if (response.ok) {
        const data = await response.json();
        setResult(data.sentiment); // Extract the "sentiment" property
      } else {
        console.error('Request failed with status:', response.status);
      }
    } catch (error) {
      console.error('An error occurred:', error);
    }
  };

  return (
    <div className='center'>
    <form onSubmit={handleSubmit}>
      <textarea
        style={{ height: '200px', width: '400px' }} // Increase the size of the text area
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <br />
      <button type="submit">Get Sentiment</button>
    </form>
    {result && <p>Predicted sentiment: {result}</p>}
  </div>
  );
}

export default Sentiment;
