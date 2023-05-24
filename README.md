<h1 align="center">Client/Server with FastAPI and React</h1>
<p>
</p>

## Dependencies
For Windows:
```python
conda create -n datascience_movie_exam python=3.10.11 -y
conda activate datascience_movie_exam
pip install -r requirements.txt
```

For Mac with M1-Chipset
```python
conda create -n datascience_movie_exam python=3.10.11 -y
conda activate datascience_movie_exam
pip install -r requirementsmac.txt
```

Then run the following python script to download Google Sentence Encoder:
(Make sure you're standing in the root of the project in your terminal)

```python
python .\download_Google_Sentence_Encoder.py
```

## Usage

### Notebooks:
1. Navigate to the notebooks folder
2. Run the following notebooks to save the models to the correct folder (these are ignored on git). This step is required to run the server.
   * Movie Earnings Classifier.ipynb
   * Naive_bayes_sentiment_analysis.ipynb

### Server:
1. Navigate to /server
2. Run the server: `uvicorn main:app --reload`
3. Server URL: `http://127.0.0.1:8000`
4. Swagger API Documentation: `http://127.0.0.1:8000/docs`

### Client:
1. Navigate to /client
2. Install dependencies: `npm install`
3. Run the client: `npm start`
