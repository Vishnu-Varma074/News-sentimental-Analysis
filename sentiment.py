from textblob import TextBlob
import requests

API_KEY = "69d064f0759944d3a45538a68611fc06"

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