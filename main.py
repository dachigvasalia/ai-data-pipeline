from src.database import DataBaseManager
from src.fetcher import NewsFetcher
from src.data_record import DataRecord
from src.pipeline import DataPipeline
from dotenv import load_dotenv
import os

load_dotenv()

def main():

    fetcher = NewsFetcher(api_key=os.getenv('NEWS_API_KEY'),volume=10)
    articles = fetcher.fetch()

    pipeline = DataPipeline(name='news-pipeline-v1')
    for article in articles:
        source = article['source']['name']
        text = article['title'] or ""
        record = DataRecord(source=source,raw_text=text)
        pipeline.add_record(record)

    
    pipeline.run()
    pipeline.summary()

    db = DataBaseManager()
    db.create_table()
    db.clear_table()
    
    for record in pipeline.get_clean_records():
        db.save_record(record)
    
    rows = db.get_records()
    print(f'database contains {len(rows)} articles')
    for row in rows:
        print(row)

if __name__ == '__main__':
    main()

