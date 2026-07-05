from src.data_record import DataRecord
from src.logger import Logger

class DataPipeline:

    '''manages a collection of Datarecord objects and coordinates cleaning the process'''

    def __init__(self,name):

        '''initializes DataPipeline object,name as an input,creates list where it stores record and adds a log'''
        
        self.name = name
        self.records = []
        self.logger = Logger()
        self.logger.log(f'{self.name} was initialized!')
    
    def add_record(self,record):

        ''' adds record instance to self.records and log'''
        
        self.records.append(record)
        self.logger.log(f'record added from {record.source}')

    def run(self):

        '''adds log and runs the loop for self.records where each record is cleaned and logged'''

        self.logger.log(f'{self.name} pipeline is starting')
        for record in self.records:
            record.clean()
            self.logger.log(f'{record}')
    
    def get_clean_records(self):

        '''returns record if the record.is_clean variable is True(if the record is cleaned)'''

        return [record for record in self.records if record.is_clean is True]
    
    def summary(self):

        '''prints total number of records,clean records and records that are pending'''
        
        total = len(self.records)
        clean = len(self.get_clean_records())
        print(f'--- Pipeline Summary: {self.name} ---')
        print(f'Total records : {total}')
        print(f'Clean records : {clean}')
        print(f'Pending       : {total - clean}')
        