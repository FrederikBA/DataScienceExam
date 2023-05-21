import pandas as pd
from ast import literal_eval

def get_movie_graph():
    df = pd.read_csv('../data/movies_new.csv')
    df['reviews'] = df['reviews'].apply(literal_eval)
    df['review_score'] = df['review_score'].apply(literal_eval)
    df['review_user'] = df['review_user'].apply(literal_eval)

    df = df.head(50)

    movies = []
    
    for index, row in df.iterrows():
        movie = {"id": row['id'], "name": row['title']}
        movies.append(movie)

    nodes = []
    links = []

    user_review_map = {}

    for i in range(len(movies)):
        movie = movies[i]
        reviews = df['reviews'][i]
        users = df['review_user'][i]
        review_count = len(reviews)
        
        movie_id = movie["id"]
        movie_name = movie["name"]
        
        nodes.append({
            "id": movie_id,
            "name": movie_name,
            "val": review_count,
            "color": "red"
        })
        
        for j, review in enumerate(reviews):
            review_id = f"{movie_id}-review-{j+1}"
            user = users[j] if j < len(users) else "Unknown User"

            if user not in user_review_map:
                # Create a new user node
                user_id = f"{movie_id}-user-{j+1}"
                nodes.append({
                    "id": user_id,
                    "name": user,
                    "val": 1,
                    "color": "yellow"
                })
                user_review_map[user] = user_id
            else:
                # Use existing user node ID
                user_id = user_review_map[user]
            
            nodes.append({
                "id": review_id,
                "name": review,
                "val": j + 2,
                "color": "white"
            })
            
            links.append({
                "source": movie_id,
                "target": review_id
            })
            links.append({
                "source": review_id,
                "target": user_id
            })
            
    graph = {
        "nodes": nodes,
        "links": links
    }

    return graph
