import requests

import os

API_KEY = os.environ.get("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not set")


url = f"https://newsapi.org/v2/everything?q=technology&language=en&apiKey={API_KEY}"

response = requests.get(url)
data = response.json()

articles = data["articles"]

for i, article in enumerate(articles[:5]):
    print(f"{i+1}. {article['title']}")
