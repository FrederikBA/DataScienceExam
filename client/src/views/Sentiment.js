import { useState } from "react"
import apiUtils from "../utils/apiUtils"

const Sentiment = () => {
  const [text, setText] = useState('');
  const [result, setResult] = useState('');
  const [error, setError] = useState('');
  const URL = apiUtils.getUrl()

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (text.trim() === '') {
      setError('Type some text into the text area before clicking the button');
      setResult('');
      return;
    }

    try {
      const response = await apiUtils.getAxios().post(URL + '/sentiment', { text }, {
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (response.status === 200) {
        const data = response.data;
        setResult(data.sentiment);
        setError('');
      } else {
        console.error('Request failed with status:', response.status);
        setError('An error occurred. Please try again later.');
        setResult('');
      }
    } catch (error) {
      console.error('An error occurred:', error);
      setError('An error occurred. Please try again later.');
      setResult('');
    }
  };


  return (
    <div className='center'>
      <h1>Sentiment Prediction</h1>
      <div className="text-area-div">
        <form className="form-group text-area" onSubmit={handleSubmit}>
          <label htmlFor="summary">Enter a movie review:</label>
          <textarea className="form-control text-area" id="summary" value={text} onChange={(e) => setText(e.target.value)} />
          <button className="btn btn-secondary generate-btn" type="submit">Get Sentiment Prediction</button>
          {error && <p className="error">{error}</p>}
          {result && <p>Predicted sentiment: {result}</p>}
        </form>
      </div>
    </div>
  );
}

export default Sentiment;
