from pydantic import BaseModel
from typing import List, Dict

class GraphDTO(BaseModel):
    nodes: List[Dict[str, str]]
    links: List[Dict[str, str]]

class NeighborInput(BaseModel):
    input: str

class SentimentDTO(BaseModel):
    text: str

class MovieFeaturesDto(BaseModel):
    year: int
    runtime: int
    rating: float
    certificate: int

class RecommendationDto(BaseModel):
    summary: str

