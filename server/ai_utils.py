# server/ai_utils.py

import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors
from sklearn.decomposition import PCA

model_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
model = hub.load(model_url)

def embed(texts):
    return model(texts)

import os

csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "services", "movies_cleaned.csv")
df = pd.read_csv(csv_file_path)
df = df[["title", "genre", "summary", "directors", "actors"]]

summaries = list(df['summary'])
embeddings = embed(summaries)

nn = NearestNeighbors(n_neighbors=10)
nn.fit(embeddings)

def recommend(text):
    emb = embed([text])
    neighbors = nn.kneighbors(emb, return_distance=False)[0]
    return df['title'].iloc[neighbors].tolist()

def generate_recommendations(input_text):
    return recommend(input_text)
