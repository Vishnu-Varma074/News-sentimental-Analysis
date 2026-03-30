from fastapi import FastAPI, Query
import requests
from textblob import TextBlob

app = FastAPI()

# 🔑 Add your API key
API_KEY = "69d064f0759944d3a45538a68611fc06"

# 📰 Fetch News
def get_news(topic):
    url = f"https://newsapi.org/v2/everything?q={topic}&language=en&apiKey={API_KEY}"
    
    response = requests.get(url)
    data = response.json()

    print("DEBUG RESPONSE:", data)  # 👈 ADD THIS

    if data.get("status") != "ok":
        return []

    return data.get("articles", [])


# 🧠 Sentiment Analysis
def analyze_sentiment(articles):
    results = []

    pos = neg = neu = 0

    for article in articles:
        title = article.get("title", "")

        polarity = TextBlob(title).sentiment.polarity

        if polarity > 0:
            sentiment = "Positive"
            pos += 1
        elif polarity < 0:
            sentiment = "Negative"
            neg += 1
        else:
            sentiment = "Neutral"
            neu += 1

        results.append({
            "title": title,
            "url": article.get("url"),
            "sentiment": sentiment
        })

    total = len(results) if results else 1

    return {
        "summary": {
            "positive": pos,
            "negative": neg,
            "neutral": neu,
            "positive_pct": round((pos/total)*100, 2),
            "negative_pct": round((neg/total)*100, 2),
            "neutral_pct": round((neu/total)*100, 2),
        },
        "articles": results
    }


# 🚀 API Endpoint
@app.get("/")
def home():
    return {"message": "News Sentiment API is running 🚀"}


@app.get("/analyze")
def analyze(topic: str = Query(..., description="Topic to search news for")):
    articles = get_news(topic)

    if not articles:
        return {"error": "No articles found or API issue"}

    return analyze_sentiment(articles[:20])