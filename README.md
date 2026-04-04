# 📰 News Sentiment Analysis Dashboard

> **Search any topic → Fetch live news → Analyze sentiment instantly**  
> Powered by NewsAPI + VADER + Streamlit + FastAPI

---

## 📌 What is this?

**News Sentiment Analysis Dashboard** is an NLP-powered tool that fetches real-time news articles on any topic and analyzes the sentiment of each headline as Positive, Negative, or Neutral. It visualizes the results through charts and word clouds, giving you a quick pulse of how the media is covering any topic.

Built with **Streamlit (frontend) + FastAPI (backend) + VADER Sentiment (NLP) + NewsAPI**.

---

## ✨ Features

- 🔍 **Live News Fetching** — Fetches real-time articles using NewsAPI for any topic
- 🧠 **VADER Sentiment Analysis** — Analyzes each headline using VADER, optimized for news and social text
- 📊 **Sentiment Distribution** — Displays percentage breakdown of Positive, Negative, and Neutral sentiments
- 📈 **Bar Chart** — Visual count of sentiments across articles
- ☁️ **Word Cloud** — Generates a word cloud from all article titles
- 📰 **Top News List** — Shows top 10 headlines with sentiment labels and links
- 🚀 **REST API** — FastAPI backend exposes a `/analyze` endpoint for developers

---

## 🗂️ Project Structure

```
news-sentiment-analysis/
│
├── app.py              # Streamlit frontend — UI, charts, word cloud
├── main.py             # FastAPI backend — REST API for sentiment analysis
├── fetch_news.py       # Utility script — used to test NewsAPI during development
├── sentiment.py        # Utility script — used to test sentiment analysis during development
├── requirements.txt    # Project dependencies
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | FastAPI + Uvicorn |
| Sentiment Analysis | VADER (vaderSentiment) |
| News Source | NewsAPI |
| Visualization | Matplotlib + WordCloud |
| Language | Python 3.10+ |

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.10 or higher
- A free [NewsAPI Key](https://newsapi.org/) — sign up and get your key instantly

---

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/news-sentiment-analysis.git
cd news-sentiment-analysis
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Set up your `.env` file

Create a `.env` file in the project root:

```
NEWS_API_KEY=your_newsapi_key_here
```

> ⚠️ **Never share or commit this file.** It is already covered by `.gitignore`.

---

## 🚀 Running the App

### Option A — Streamlit UI (Recommended)

```bash
streamlit run app.py
```

Opens at: [http://localhost:8501](http://localhost:8501)

---

### Option B — FastAPI Backend

```bash
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

API docs available at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🖥️ How to Use (Streamlit)

1. Open the app in your browser
2. Enter any topic in the search box (e.g. `AI`, `India`, `Tesla`, `Cricket`)
3. Click **Analyze**
4. View sentiment metrics, bar chart, word cloud, and top headlines with sentiment labels

---

## 🌐 API Endpoints (FastAPI)

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check |
| `GET` | `/analyze?topic=AI` | Fetch and analyze news for a topic |

### Example API Usage

```bash
curl "http://127.0.0.1:8000/analyze?topic=Tesla"
```

### Example Response

```json
{
  "summary": {
    "positive": 8,
    "negative": 5,
    "neutral": 7,
    "positive_pct": 40.0,
    "negative_pct": 25.0,
    "neutral_pct": 35.0
  },
  "articles": [
    {
      "title": "Tesla hits record sales in Q1",
      "url": "https://example.com/article",
      "sentiment": "Positive"
    }
  ]
}
```

---

## 💬 Example Topics to Try

| Topic | What you'll see |
|---|---|
| `AI` | Sentiment around artificial intelligence news |
| `India` | Sentiment around India-related headlines |
| `Tesla` | Positive/negative coverage of Tesla |
| `Cricket` | Mood of cricket news |
| `Climate` | Sentiment around climate change articles |

---

## 📦 Dependencies (`requirements.txt`)

```
streamlit
fastapi
uvicorn
requests
vaderSentiment==3.3.2
matplotlib
wordcloud
python-dotenv
```

---

## ⚠️ Known Limitations

- NewsAPI free tier allows **100 requests per day**
- Free tier only returns articles from the **last 30 days**
- Sentiment analysis is based on **headline only** — not the full article content

---

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `NEWS_API_KEY` | Your NewsAPI key from [newsapi.org](https://newsapi.org/) |

---

## 🧠 Why VADER over TextBlob?

VADER (Valence Aware Dictionary and sEntiment Reasoner) is specifically designed for short social media and news text. Unlike TextBlob which is a general purpose NLP library, VADER accurately handles capitalization, punctuation emphasis, and news-style language — making it a better fit for analyzing news headlines.

---

*Built with ❤️ using NewsAPI + VADER + Streamlit — Know the mood of the news instantly.*
