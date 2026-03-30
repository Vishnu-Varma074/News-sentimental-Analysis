from textblob import TextBlob
import requests

import os

API_KEY = os.environ.get("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not set")

url = f"https://newsapi.org/v2/everything?q=technology&language=en&apiKey={API_KEY}"
data = requests.get(url).json()

articles = data["articles"]

for article in articles[:10]:
    title = article["title"]
    sentiment = TextBlob(title).sentiment.polarity

    if sentiment > 0:
        mood = "Positive 😊"
    elif sentiment < 0:
        mood = "Negative 😡"
    else:
        mood = "Neutral 😐"

    print(f"{title} --> {mood}")
