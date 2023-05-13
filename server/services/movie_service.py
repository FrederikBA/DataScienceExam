import pandas as pd
import json
from ast import literal_eval


def get_data():
    return {"Data": "This is data"}


def get_movie_graph():
    df = pd.read_csv('../data/movies_new.csv')
    df['reviews'] = df['reviews'].apply(literal_eval)
    df['review_score'] = df['review_score'].apply(literal_eval)

    df = df.head(100)

    movies = []

    for index, row in df.iterrows():
        movie = {"id": row['id'], "name": row['title']}

        movies.append(movie)

    nodes = []
    links = []

    for i in range(len(movies)):
        movie = movies[i]
        reviews = []
        for r in df['reviews'][i]:
            reviews.append(r)
        count = 0
        movie_reviews = []
        movie_id = movie["id"]
        movie_name = movie["name"]
        review_count = len(reviews)
        nodes.append({
            "id": movie_id,
            "name": movie_name,
            "val": review_count,
            "color": "red"
        })

        for i, review in enumerate(reviews):
            count += 1
            review_id = f"{movie_id}-review-{count}"
            nodes.append({
                "id": review_id,
                "name": review,
                "val": count + 1,
                "color": "white"
            })
            links.append({
                "source": movie_id,
                "target": review_id
            })

    graph = {
        "nodes": nodes,
        "links": links
    }

    return graph
