import streamlit as st
import requests
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 🔑 Replace with your NewsAPI key
API_KEY = your_actual_key

# 🚀 Fetch News
def get_news(topic):
    url = f"https://newsapi.org/v2/everything?q={topic}&language=en&apiKey={API_KEY}"
    
    response = requests.get(url)
    data = response.json()

    # 🔍 Debug (optional)
    # st.write(data)

    # ✅ Handle API errors safely
    if data.get("status") != "ok":
        st.error(f"API Error: {data.get('message', 'Unknown error')}")
        return []

    return data.get("articles", [])


# 🧠 Sentiment Analysis
def analyze_sentiment(articles):
    sentiments = []
    texts = []

    for article in articles:
        title = article.get("title", "")
        texts.append(title)

        polarity = TextBlob(title).sentiment.polarity

        if polarity > 0:
            sentiments.append("Positive")
        elif polarity < 0:
            sentiments.append("Negative")
        else:
            sentiments.append("Neutral")

    return sentiments, texts


# 🎨 Streamlit UI
st.set_page_config(page_title="News Sentiment Dashboard", layout="wide")

st.title("📰 News Sentiment Analysis Dashboard")

topic = st.text_input("Enter Topic (e.g., AI, India, Tesla):")

if st.button("Analyze"):

    if not topic:
        st.warning("Please enter a topic")
        st.stop()

    articles = get_news(topic)

    # ❌ No data case
    if not articles:
        st.warning("No articles found or API error occurred.")
        st.stop()

    sentiments, texts = analyze_sentiment(articles[:20])

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
    col1.metric("Positive", f"{pos_p:.2f}%")
    col2.metric("Negative", f"{neg_p:.2f}%")
    col3.metric("Neutral", f"{neu_p:.2f}%")

    # 📊 Bar Chart
    labels = ["Positive", "Negative", "Neutral"]
    values = [pos, neg, neu]

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_title("Sentiment Count")
    st.pyplot(fig)

    # ☁️ Word Cloud
    st.subheader("☁️ Word Cloud")

    text_combined = " ".join(texts)

    if text_combined.strip():
        wordcloud = WordCloud(width=800, height=400).generate(text_combined)

        fig_wc, ax_wc = plt.subplots()
        ax_wc.imshow(wordcloud)
        ax_wc.axis("off")
        st.pyplot(fig_wc)
    else:
        st.write("No text available for word cloud.")

    # 📰 News List
    st.subheader("📰 Top News")

    for article in articles[:10]:
        st.write(f"**{article.get('title', 'No Title')}**")
        st.write(article.get("url", ""))
        st.write("---")
