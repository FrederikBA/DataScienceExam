import pickle
import numpy as np
import pandas as pd

def load_model():
    with open("pre_trained_models/decision_tree_earnings.pkl", "rb") as f:
        model = pickle.load(f)
    return model

def predict_movie_earnings(movie):
    # Load model
    classifier = load_model()

    # New movie features
    new_movie_X = np.array([[movie.year, movie.runtime, movie.rating, movie.certificate]])
    predicted_page = int(classifier.predict(new_movie_X))

    # Get estimated earnings
    df = pd.read_csv('../data/movies.csv')
    df = df[['title', 'page', 'lifetime gross in $']]
    df = df[df['page'] == predicted_page]

    # max, min, avg
    max_gross = format(max(df['lifetime gross in $']), ',').replace(",", ".")
    min_gross = format(min(df['lifetime gross in $']), ',').replace(",", ".")
    avg_gross = format(int(sum(df['lifetime gross in $'] / len(df['lifetime gross in $']))), ',').replace(",", ".")

    # Position: example: "Top 100", "Top 200" etc...
    top = f"Top {predicted_page*100}"

    viewModel = {"min": min_gross, "max": max_gross, "avg": avg_gross, "top": top}

    return viewModel
