from src.data_record import DataRecord
from src.pipeline import DataPipeline

def main():
    pipeline = DataPipeline(name='news-pipeline-v1')

    raw_data = [
         ("BBC News", "  Georgian Economy Grows 6% in Q1  "),
        ("Reuters", "  TBILISI: New Tech Hub Opens Downtown  "),
        ("CNN", "  AI Adoption Accelerates Across Europe  "),
    ]

    for source,text in raw_data:
        record = DataRecord(source=source,raw_text=text)
        pipeline.add_record(record)
    
    pipeline.run()
    pipeline.summary()
    for record in pipeline.get_clean_records():
        print(record.to_dict())

if __name__ == '__main__':
    main()