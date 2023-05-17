from typing import List
from typing import Dict
from models.dtos import GraphDTO
import pandas as pd
import tensorflow as tf
from sklearn.neighbors import NearestNeighbors
from sklearn.manifold import TSNE
import os

# Load Universal Sentence Encoder from local directory
model_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "pre_trained_models")
model = tf.saved_model.load(model_dir)

def embed(texts):
    return model.signatures['serving_default'](tf.constant(texts))['outputs'].numpy()

# Load movie data
df = pd.read_csv('../data/movies_cleaned.csv')
df = df[["title", "genre", "summary", "directors", "actors"]]
summaries = list(df['summary'])

# Generate embeddings
embeddings = embed(summaries)

# Fit Nearest Neighbors
nn = NearestNeighbors(n_neighbors=10)
nn.fit(embeddings)

def get_recommendations(summary: str) -> List[dict]:
    emb = embed([summary])
    neighbors = nn.kneighbors(emb, return_distance=False)[0]
    recommended_movies = df.iloc[neighbors]

    
    recommendations = []
    for _, row in recommended_movies.iterrows():
        recommendations.append({"title": row["title"], "description": row["summary"]})

    tsne = TSNE(n_components=2)
    embeddings_2d = tsne.fit_transform(embeddings)
    
    embeddings_data = []
    for idx, row in df.iterrows():
        if():
            embeddings_data.append({"x": float(embeddings_2d[idx][0]), "y": float(embeddings_2d[idx][1]), "title": row["title"], "description": row["summary"]})
        else:
            embeddings_data.append({"x": float(embeddings_2d[idx][0]), "y": float(embeddings_2d[idx][1]), "title": row["title"], "description": row["summary"]})


    viewModel = {"recommendations": recommendations, "embeddings": embeddings_data}

    return recommendations

def get_embeddings() -> List[dict]:
    tsne = TSNE(n_components=2)
    embeddings_2d = tsne.fit_transform(embeddings)

    embeddings_data = []
    for idx, row in df.iterrows():
        embeddings_data.append({"x": float(embeddings_2d[idx][0]), "y": float(embeddings_2d[idx][1]), "title": row["title"], "description": row["summary"], "marker": {"color": 'red'}})
    

    return embeddings_data

def get_neighbors(input_data: str) -> GraphDTO:
    emb = embed([input_data])
    neighbors = nn.kneighbors(emb, return_distance=False)[0]
    recommended_movies = df.iloc[neighbors]

    nodes = []
    links = []
    for idx, row in recommended_movies.iterrows():
        nodes.append({"id": row["title"], "label": row["title"]})
        links.append({"source": input_data, "target": row["title"]})

    graph_data = GraphDTO(nodes=nodes, links=links)
    return graph_data
