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
from sklearn.preprocessing import StandardScaler
import spacy

nlp = spacy.load("en_core_web_md")
mlb = MultiLabelBinarizer()

# Load Universal Sentence Encoder from local directory
model_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "pre_trained_models")
model = tf.saved_model.load(model_dir)

def embed(texts):
    # Function to generate embeddings for a list of texts
    return model.signatures['serving_default'](tf.constant(texts))['outputs'].numpy()

df = pd.read_csv('../data/movies.csv')
df = df[["title", "genre", "summary", "directors", "actors", "Poster"]]

# Get genre information from DataFrame and split each string into a list of genres
df['genre'] = df['genre'].str.split(', ')

# Convert all genres to lowercase
df['genre'] = df['genre'].apply(lambda x: [genre.lower() for genre in x])

all_genres = set(genre for genres in df['genre'] for genre in genres)

# Fit MultiLabelBinarizer to all genres
mlb.fit([list(all_genres)])

#Transform genre strings to binary encoding and add to DataFrame
genre_transformed = mlb.transform(df['genre'].tolist())
df_genres = pd.DataFrame(genre_transformed, columns=mlb.classes_)
df = pd.concat([df, df_genres], axis=1)
del df['genre']  # delete the old genre column

# Get genre binary encodings as numpy array
genres = df[mlb.classes_].to_numpy()

# Generate embeddings for summaries, actors
summaries = list(df['summary'])
embeddings = embed(summaries)

actors = list(df['actors'])
actors_embeddings = embed(actors)

# Concatenate all features
all_features = np.concatenate((embeddings, actors_embeddings, genres), axis=1)

#Fit Nearest Neighbors to all features and using the scalar to ensure everything is weighted correctly.
scaler = StandardScaler()
all_features_normalized = scaler.fit_transform(all_features)

nn = NearestNeighbors(n_neighbors=10)
nn.fit(all_features_normalized)


def extract_input_genres(text):
    """ Extracting genres from the input string """
    doc = nlp(text)
    genres_in_text = [token.lemma_.lower() for token in doc if token.lemma_.lower() in mlb.classes_]
    input_genres_encoded = mlb.transform([genres_in_text])
    return input_genres_encoded

def preprocess_text(text):
    """ Tokenizing the text """
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if not token.is_digit]
    return tokens

def get_recommendations(input_text: str):
    """ Very scuffed docstring """
    genre = extract_input_genres(input_text)
    input_text_emb = embed([input_text])

    # Actors
    actor_entities = []
    sample_processed = (" ").join(preprocess_text(input_text))
    doc = nlp(sample_processed)
    for entity in doc.ents:
        print(f'Actor output from entity.text: {entity.text}')
        if(entity.label_ == "PERSON"): 
            actor_entities.append(entity.text)

    # Here we checks if the list is not empty
    if actor_entities:  # this checks if the list is not empty
        actor_entities = ', '.join(actor_entities)
        print(actor_entities)
        actors_emb = embed([actor_entities])
    else:
        actors_emb = np.zeros_like(input_text_emb)  # replace with a zero array of the same shape

    # Now concatenate including genre
    emb = np.concatenate((input_text_emb, actors_emb, genre), axis=1)

    # Apply the same normalization
    emb = scaler.transform(emb)
    
    #Prediction
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
    """ Function to get 2D embeddings for visualization """

    tsne = TSNE(n_components=2)
    embeddings_2d = tsne.fit_transform(embeddings)

    embeddings_data = []

    for idx, row in df.iterrows():
        embeddings_data.append({"x": float(embeddings_2d[idx][0]), "y": float(embeddings_2d[idx][1]), "title": row["title"], "description": row["summary"], "marker": {"color": 'red'}})
    
    return embeddings_data
