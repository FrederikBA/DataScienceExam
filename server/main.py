from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List


from services import test_service, recommender_service
from ai_utils import generate_recommendations
from services import movie_service
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


class RecommendationInput(BaseModel):
    input: str

# Read Root.
@app.get("/")
def read_root():
    return test_service.get_data()

@app.post("/neighbors")
def get_neighbors(input_data: NeighborInput):
    return recommender_service.get_neighbors(input_data.input)

@app.post("/recommend")
def get_recommendations(input_data: RecommendationInput):
    return recommender_service.get_recommendations(input_data.input)

# Visualizing our embeddings.
@app.get("/embeddings")
def get_embeddings() -> List[dict]:
    return recommender_service.get_embeddings()

@app.get("/graph")
def get_graph():
    return movie_service.get_movie_graph()

