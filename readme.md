# AI Powered News Data Pipeline
A Python data pipeline that automatically fetches real news articles from NewsAPI,
cleans and normalizes the data, stores it in a SQLite database, and uses an LLM 
(via OpenRouter) to classify each article by sentiment (positive/negative/neutral) 
and topic (tech/gaming/business/science).

## Technologies Used
- Python
- SQLite
- NewsAPI
- OpenRouter(LLM)
- libraries(requests,dotenv,openai)

## Project Structure

```
ai-data-pipeline/
├── src/
│   ├── fetcher.py       #sends GET request to NewsAPI and converts json response into python dictionary
│   ├── data_record.py   #representation of single news article
│   ├── pipeline.py      #managing DataRecord objects and cleaning process
│   ├── database.py      #saves cleaned_articles to SQLite and retrieves them
│   ├── classifier.py    #sends cleaned text to LLM API'S,stores response in SQLite database
│   ├── analytics.py     #extracts business insights from database with SQL queries
│   └── logger.py        #records every event of pipeline with timestamp
├── main.py              #Orchestrates fetching,cleaning,storing,classifying and analyzing news articles
├── requirements.txt     #Python dependencies
└── .env                 #stores api keys
```
## How To Run
1.**Clone the repository**

```bash
git clone https://github.com/dachigvasalia/ai-data-pipeline.git
cd ai-data-pipeline
```

2.**Install dependencies***

```bash
pip install -r requirements.txt
```
3.**Set up enviroment variables**

Create `.env` variable in file of root folder with following:
NEWS_API_KEY=your_api_key_here
OPENROUTER_API_KEY=your_api_key_here

- Get your free NewsAPI key at: https://newsapi.org
- Get your free OpenRouter key at: https://openrouter.ai

4.**Run the pipeline**
```bash
python -m main
```

## Pipeline Stages
1. **Fetch** — retrieves news articles from NewsAPI
2. **Clean** — normalizes text by stripping whitespace and lowercasing
3. **Store** — saves articles to SQLite database
4. **Classify** — uses LLM to label sentiment and topic
5. **Analyze** — runs SQL queries to extract insights