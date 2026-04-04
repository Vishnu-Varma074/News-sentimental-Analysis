import streamlit as st
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os
from dotenv import load_dotenv

load_dotenv()

# 🔑 API Key
API_KEY = os.getenv("NEWS_API_KEY")

# Initialize VADER
analyzer = SentimentIntensityAnalyzer()


# 🚀 Fetch News
def get_news(topic):
    url = f"https://newsapi.org/v2/everything?q={topic}&language=en&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data.get("status") != "ok":
        st.error(f"API Error: {data.get('message', 'Unknown error')}")
        return []

    return data.get("articles", [])


# 🧠 Sentiment Analysis using VADER
def analyze_sentiment(articles):
    sentiments = []
    texts = []
    sentiment_labels = []

    for article in articles:
        title = article.get("title", "")
        texts.append(title)

        score = analyzer.polarity_scores(title)["compound"]

        if score > 0.05:
            sentiments.append("Positive")
            sentiment_labels.append("Positive 😊")
        elif score < -0.05:
            sentiments.append("Negative")
            sentiment_labels.append("Negative 😡")
        else:
            sentiments.append("Neutral")
            sentiment_labels.append("Neutral 😐")

    return sentiments, texts, sentiment_labels


# 🎨 Streamlit UI
st.set_page_config(page_title="News Sentiment Dashboard", layout="wide")

st.title("📰 News Sentiment Analysis Dashboard")

topic = st.text_input("Enter Topic (e.g., AI, India, Tesla):")

if st.button("Analyze"):

    if not topic:
        st.warning("Please enter a topic")
        st.stop()

    articles = get_news(topic)

    if not articles:
        st.warning("No articles found or API error occurred.")
        st.stop()

    sentiments, texts, sentiment_labels = analyze_sentiment(articles[:20])

    # 📊 Count sentiments
    pos = sentiments.count("Positive")
    neg = sentiments.count("Negative")
    neu = sentiments.count("Neutral")
    total = len(sentiments)

    # 📈 Percentages
    pos_p = (pos / total) * 100
    neg_p = (neg / total) * 100
    neu_p = (neu / total) * 100

    # 📊 Show metrics
    st.subheader("📊 Sentiment Distribution")
    col1, col2, col3 = st.columns(3)
    col1.metric("Positive 😊", f"{pos_p:.2f}%")
    col2.metric("Negative 😡", f"{neg_p:.2f}%")
    col3.metric("Neutral 😐", f"{neu_p:.2f}%")

    # 📊 Bar Chart 
    labels = ["Positive", "Negative", "Neutral"]
    values = [pos, neg, neu]
    colors = ["#4CAF50", "#F44336", "#2196F3"]

    st.subheader("📊 Sentiment Count")
    fig, ax = plt.subplots()
    ax.bar(labels, values, color=colors)
    ax.set_title("Sentiment Count")
    ax.set_ylabel("Number of Articles")
    st.pyplot(fig)


    # ☁️ Word Cloud
    st.subheader("☁️ Word Cloud")
    text_combined = " ".join(texts)

    if text_combined.strip():
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text_combined)
        fig_wc, ax_wc = plt.subplots()
        ax_wc.imshow(wordcloud)
        ax_wc.axis("off")
        st.pyplot(fig_wc)
    else:
        st.write("No text available for word cloud.")

    # 📰 Top News with Sentiment Labels
    st.subheader("📰 Top News")

    for i, article in enumerate(articles[:10]):
        title = article.get("title", "No Title")
        url = article.get("url", "")
        label = sentiment_labels[i] if i < len(sentiment_labels) else ""
        st.write(f"**{title}** — {label}")
        st.write(url)
        st.write("---")
