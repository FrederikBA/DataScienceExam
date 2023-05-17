import pickle
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import  RegexpTokenizer

def load_model():
    # Load the saved model and the count vectorizer
    with open("pre_trained_models/naive_bayes_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

def predict_sentiment():
    token = RegexpTokenizer(r'[a-zA-Z0-9]+')
    cv = CountVectorizer(stop_words='english',ngram_range = (1,1),tokenizer = token.tokenize)
    model = load_model()

    # Transform the text into a bag-of-words representation
    text = "this is a positive text"
    
    text_counts = cv.transform([text])

    # Use the trained model to predict the sentiment of the text
    predicted_sentiment = model.predict(text_counts)

    # Convert the predicted sentiment to a string ("Positive" or "Negative")
    if predicted_sentiment == 1:
        return "Positive"
    else:
        return "Negative"

# Call the predict_sentiment function with a text input
#review_text = "The plot is stolen from many different movies, there was only 3 good actors, the characters are either bland or stereotypical, and yet it made almost 3 billion. When I think a film is overrated I usually like it. I don't think of it as Oscar worthy, but I like it."
#predicted_sentiment = predict_sentiment(textstring)
#print("Predicted sentiment for text:", predicted_sentiment)
