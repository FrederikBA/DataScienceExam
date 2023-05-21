import pickle
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import  RegexpTokenizer

def load_model_and_vectorizer():
    # Load the saved model and the count vectorizer
    with open("pre_trained_models/naive_bayes_model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("pre_trained_models/count_vec.pkl", "rb") as f:
        cv = pickle.load(f)
    return model, cv

def predict_sentiment(text):
    model, cv = load_model_and_vectorizer()

    # Transform the text into a bag-of-words representation
    text_counts = cv.transform([text])

    # Use the trained model to predict the sentiment of the text
    predicted_sentiment = model.predict(text_counts)

    # Convert the predicted sentiment to a string ("Positive" or "Negative")
    if predicted_sentiment == 1:
        return {"sentiment": "Positive"}
    else:
        return {"sentiment": "Negative"}

# Call the predict_sentiment function with a text input
#review_text = "The plot is stolen from many different movies, there was only 3 good actors, the characters are either bland or stereotypical, and yet it made almost 3 billion. When I think a film is overrated I usually like it. I don't think of it as Oscar worthy, but I like it."
#predicted_sentiment = predict_sentiment(text)
