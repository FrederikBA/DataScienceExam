from typing import List
from typing import Dict
from models.dtos import GraphDTO
import pandas as pd
import tensorflow as tf
from sklearn.neighbors import NearestNeighbors
from sklearn.manifold import TSNE
import os
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
import spacy

#nlp = spacy.load("en_core_web_sm")
# mlb = MultiLabelBinarizer()

# Load Universal Sentence Encoder from local directory
model_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "pre_trained_models")
model = tf.saved_model.load(model_dir)

def embed(texts):
    # Function to generate embeddings for a list of texts
    return model.signatures['serving_default'](tf.constant(texts))['outputs'].numpy()

df = pd.read_csv('../data/movies.csv')
df = df[["title", "genre", "summary", "directors", "actors", "Poster"]]
# df['genre'] = df['genre'].str.split(', ')

# Find all unique genres
# all_genres = set(genre for genres in df['genre'] for genre in genres)

# Fit MultiLabelBinarizer to all genres
# mlb.fit([list(all_genres)])

#Transform genre strings to binary encoding and add to DataFrame
# genre_transformed = mlb.transform(df['genre'].tolist())
# df_genres = pd.DataFrame(genre_transformed, columns=mlb.classes_)
# df = pd.concat([df, df_genres], axis=1)
# del df['genre']  # delete the old genre column

# print(df_genres.shape)

# Generate embeddings for summaries, actors, directors
summaries = list(df['summary'])
embeddings = embed(summaries)

actors = list(df['actors'])
actors_embeddings = embed(actors)

# directors = list(df['directors'])
# directors_embeddings = embed(directors)

# Get genre binary encodings as numpy array
# genres = df[mlb.classes_].to_numpy()

# Concatenate all features
# all_features = np.concatenate((embeddings, actors_embeddings, directors_embeddings, genres), axis=1)
all_features = np.concatenate((embeddings, actors_embeddings), axis=1)
# print('all_features shape:', all_features.shape)

#Fit Nearest Neighbors to all features
nn = NearestNeighbors(n_neighbors=10)
nn.fit(all_features)

#def preprocess_text(text):
    
    # Tokenize the text and remove stop words and punctuation
    #doc = nlp(text)
    #tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct and not token.is_digit]

    #return tokens


def get_recommendations(summary: str) -> List[dict]:
    # , actors: str, directors: str, genres: List[str]
    # unction to get recommendations for a movie with given summary, actors, directors, genres

    
    
    #Generate embeddings for summary, actors, directors
    summary_emb = embed([summary])

    # Actors
    actor_entities = []
    # sample_processed = (" ").join(preprocess_text(summary))
    # doc = nlp(sample_processed)
    # for entity in doc.ents:
    #     print(entity.text)
    #     if(entity.label_ == "PERSON"): 
    #         actor_entities.append(entity.text)

    actors_emb = embed([actors])
    # directors_emb = embed([directors])
    
    # Convert input genres to binary encoding
    # input_genres_encoded = mlb.transform([genres])

    emb = np.concatenate((summary_emb, actors_emb), axis=1)
    # , directors_emb, input_genres_encoded
    
    neighbors = nn.kneighbors(emb, return_distance=False)[0]
    recommended_movies = df.iloc[neighbors]
    
    recommendations = []
    for _, row in recommended_movies.iterrows():
        recommendations.append({"title": row["title"], "description": row["summary"], "poster": row["Poster"]})

    # Perform t-SNE dimensionality reduction for visualization
    tsne = TSNE(n_components=3)
    embeddings_2d = tsne.fit_transform(all_features)
    
    embeddings_data = []

    for idx, row in df.iterrows():
        embeddings_data.append({"x": float(embeddings_2d[idx][0]), "y": float(embeddings_2d[idx][1]), "z": float(embeddings_2d[idx][2]), "title": row["title"], "description": row["summary"]})

    viewModel = {"recommendations": recommendations, "embeddings": embeddings_data, "persons": actor_entities}

    return viewModel

def get_embeddings() -> List[dict]:
    # Function to get 2D embeddings for visualization

    tsne = TSNE(n_components=2)
    embeddings_2d = tsne.fit_transform(embeddings)

    embeddings_data = []
    for idx, row in df.iterrows():
        embeddings_data.append({"x": float(embeddings_2d[idx][0]), "y": float(embeddings_2d[idx][1]), "title": row["title"], "description": row["summary"], "marker": {"color": 'red'}})
    

    return embeddings_data

def get_neighbors(input_data: str) -> GraphDTO:
    # Function to get nearest neighbors to a given input

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
