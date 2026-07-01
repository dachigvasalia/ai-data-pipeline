from src.fetcher import NewsFetcher
from src.data_record import DataRecord
from src.pipeline import DataPipeline

def main():

    fetcher = NewsFetcher('f2ec8d54b236425ea923857bca58f582',volume=10)
    articles = fetcher.fetch()

    pipeline = DataPipeline(name='news-pipeline-v1')

    for article in articles:
        source = article['source']['name']
        text = article['title'] or ""
        record = DataRecord(source=source,raw_text=text)
        pipeline.add_record(record)

    
    pipeline.run()
    pipeline.summary()
    
    for record in pipeline.get_clean_records():
        print(record.to_dict())

if __name__ == '__main__':
    main()