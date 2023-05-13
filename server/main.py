from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services import movie_service
from models import dtos

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


@app.get("/")
def read_root():
    return movie_service.get_data()


@app.get("/graph")
def get_graph():
    return movie_service.get_movie_graph()
