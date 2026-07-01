from src.data_record import DataRecord
from src.logger import Logger

class DataPipeline:
    def __init__(self,name):
        self.name = name
        self.records = []
        self.logger = Logger()
        self.logger.log(f'{self.name} was initialized!')

    def add_record(self,record):
        self.records.append(record)
        self.logger.log(f'record added from {record.source}')

    def run(self):
        self.logger.log(f'{self.name} pipeline is starting')
        for record in self.records:
            record.clean()
            self.logger.log(f'{record}')
    
    def get_clean_records(self):
        return [record for record in self.records if record.is_clean is True]
    
    def summary(self):
        total = len(self.records)
        clean = len(self.get_clean_records())
        print(f'--- Pipeline Summary: {self.name} ---')
        print(f'Total records : {total}')
        print(f'Clean records : {clean}')
        print(f'Pending       : {total - clean}')
        