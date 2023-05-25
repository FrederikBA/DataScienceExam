from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List


from services import  graph_service, recommender_service, sentiment_service, estimated_earnings_service
from models import dtos
from models.dtos import NeighborInput

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Read Root.
@app.get("/")
def read_root():
    return "Welcome to the Data Science course exam API!"

@app.post("/recommend")
def get_recommendations(input_data: dtos.RecommendationDto):
    return recommender_service.get_recommendations(input_data.summary)

@app.get("/embeddings")
def get_embeddings() -> List[dict]:
    return recommender_service.get_embeddings()

@app.get("/graph")
def get_graph():
    return graph_service.get_movie_graph()

@app.post("/earnings")
def predict_movie_earnings(movieFeaturesDTO: dtos.MovieFeaturesDto):
    return estimated_earnings_service.predict_movie_earnings(movieFeaturesDTO)

@app.post("/sentiment")
def get_sentiment(sentimentDTO: dtos.SentimentDTO):
    return sentiment_service.predict_sentiment(sentimentDTO.text)
    