from pydantic import BaseModel
from typing import List, Dict

class testDTO(BaseModel):
    name: str

class GraphDTO(BaseModel):
    nodes: List[Dict[str, str]]
    links: List[Dict[str, str]]

class NeighborInput(BaseModel):
    input: str

class sentimentDTO(BaseModel):
    text: str