import pickle
from sklearn.feature_extraction.text import CountVectorizer

# load the saved model
with open("../../notebooks/naive_bayes_model.pkl", "rb") as f:
    MNB = pickle.load(f)

def predict_sentiment(text, cv, model):
    # Transform the text into a bag-of-words representation
    text_counts = cv.transform([text])

    # Use the trained model to predict the sentiment of the text
    predicted_sentiment = model.predict(text_counts)

    # Convert the predicted sentiment to a string ("Positive" or "Negative")
    if predicted_sentiment == 1:
        return "Positive"
    else:
        return "Negative"
    

# Load the saved model and the count vectorizer
with open("naive_bayes_model.pkl", "rb") as f:
    MNB = pickle.load(f)
with open("count_vectorizer.pkl", "rb") as f:
    cv = pickle.load(f)

# Call the predict_sentiment function with a text input
review_text = "The plot is stolen from many different movies, there was only 3 good actors, the characters are either bland or stereotypical, and yet it made almost 3 billion. When I think a film is overrated I usually like it. I don't think of it as Oscar worthy, but I like it."
predicted_sentiment = predict_sentiment(review_text, cv, MNB)
print("Predicted sentiment for text: ", predicted_sentiment)
