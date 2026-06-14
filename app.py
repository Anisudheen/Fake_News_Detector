import streamlit as st

import joblib

import re
import string


# ==========================================
# LOAD MODEL
# ==========================================

model = joblib.load("fake_news_model.pkl")

vectorizer = joblib.load("vectorizer.pkl")


# ==========================================
# CLEAN TEXT FUNCTION
# ==========================================

def clean_text(text):

    text = text.lower()

    text = re.sub(r'http\\S+', '', text)

    text = re.sub(r'\\d+', '', text)

    text = text.translate(
        str.maketrans('', '', string.punctuation)
    )

    text = text.strip()

    return text


# ==========================================
# PAGE TITLE
# ==========================================

st.title("📰 Fake News Detector")


st.write(
    "Enter a news article below to check whether it is Fake or Real."
)


# ==========================================
# USER INPUT
# ==========================================

news = st.text_area("Enter News Article")


# ==========================================
# PREDICTION BUTTON
# ==========================================

if st.button("Predict"):

    if news.strip() == "":

        st.warning("Please enter news text.")

    else:

        cleaned_news = clean_text(news)

        vectorized_news = vectorizer.transform(
            [cleaned_news]
        )

        prediction = model.predict(
            vectorized_news
        )[0]


        if prediction == 1:

            st.success("✅ REAL NEWS")

        else:

            st.error("❌ FAKE NEWS")