from src.classifier import Classifier
from src.analytics import Analyzer
from src.database import DataBaseManager
from src.fetcher import NewsFetcher
from src.data_record import DataRecord
from src.pipeline import DataPipeline
from dotenv import load_dotenv
import os

load_dotenv()

def main():

    openrouter_api_key= os.getenv('OPENROUTER_API_KEY')
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
    
    classifier = Classifier(api_key=openrouter_api_key)
    for record in pipeline.get_clean_records():
        classifier.classify(record)
    
    rows = db.get_records()
    print(f'database contains {len(rows)} articles')
    for row in rows:
        print(row)
    
    analyzer = Analyzer()
    print('\n---Articles per source')
    for row in analyzer.articles_per_source():
        print(f'{row[0]}: {row[1]} articles')
    
    print('\n most recent articles')
    for row in analyzer.most_recent_articles():
        print(f'{row[2]} | {row[0]} | {row[1]}')
    
    print(f'\n ---toatl articels in database : {analyzer.total_articles()}---')


if __name__ == '__main__':
    main()