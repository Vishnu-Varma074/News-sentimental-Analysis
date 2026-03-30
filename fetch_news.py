import requests

API_KEY = your_actual_key


url = f"https://newsapi.org/v2/everything?q=technology&language=en&apiKey={API_KEY}"

response = requests.get(url)
data = response.json()

articles = data["articles"]

for i, article in enumerate(articles[:5]):
    print(f"{i+1}. {article['title']}")
