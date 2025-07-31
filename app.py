
import streamlit as st
import pickle

# Load model and vectorizer
with open("sentiment_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

st.title("Sentiment Analysis App")
user_input = st.text_area("Enter a review:")
if st.button("Analyze"):
    transformed = vectorizer.transform([user_input])
    prediction = model.predict(transformed)[0]
    st.write("Prediction:", "Positive" if prediction == 1 else "Negative")
