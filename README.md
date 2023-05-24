# Client/Server with FastAPI and React

This project provides a movie recommendation system developed using FastAPI and React. The movie recommendation model makes use of a pre-trained Google Sentence Encoder. This readme provides instructions on how to set up the project.

## Setup

### Prerequisites

Make sure you have Anaconda or Miniconda installed to manage environments and dependencies. Also, you will need npm for client-side dependency management.

### Environment and Dependency Setup

#### Windows:

```bash
conda create -n datascience_movie_exam python=3.10.11 -y
conda activate datascience_movie_exam
pip install -r requirements.txt
```

#### Mac with M1-Chipset:

```bash
conda create -n datascience_movie_exam python=3.10.11 -y
conda activate datascience_movie_exam
pip install -r requirementsmac.txt
```

After setting up the environment and installing the dependencies, run the following Python script to download the Google Sentence Encoder. Make sure you're at the root of the project in your terminal:

```bash
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
