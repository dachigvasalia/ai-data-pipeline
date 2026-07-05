from src.logger import Logger
import sqlite3
import os

class DataBaseManager:
    '''saves cleaned_articles to SQLite and retrieves them'''

    def __init__(self,db_path='data/news.db'):
        
        '''initializes DataBaseManager object with with database path that is already set.
        makes an instance of Logger class,then creates database folder with name data if it doesn't exists.
        opens connection to the sql database file and makes a log'''

        self.db_path = db_path
        self.logger = Logger()
        os.makedirs('data',exist_ok=True)
        self.connection = sqlite3.connect(db_path)
        self.logger.log(f'database is created : {self.db_path}')
        
    def create_table(self):

        '''Creates the articles table in SQLite if it doesn't already exist.
        Defines columns for id, source, text, timestamp, is_clean, sentiment and topic'''
        
        self.connection.execute('''
        CREATE TABLE IF NOT EXISTS articles(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            raw_text TEXT,
            cleaned_text TEXT,
            timestamp TEXT,
            is_clean INTEGER,
            sentiment TEXT,
            topic TEXT                       
        )
                                
        ''')
        self.connection.commit()
    
    def clear_table(self):

        '''clears table and adds a log'''

        self.connection.execute('DELETE FROM articles')
        self.connection.commit()
        self.logger.log('table cleared')
        
    def save_record(self,record):

        '''saves the records,adds an appropriate log andd returns the record'''

        cursor = self.connection.execute('''
        INSERT INTO articles(source,raw_text,cleaned_text,timestamp,is_clean,sentiment,topic)
        VALUES(?,?,?,?,?,?,?)
        ''', (record.source,record.raw_text,record.cleaned_text,record.timestamp,record.is_clean,None,None))
        self.connection.commit()
        record.id = cursor.lastrowid
        self.logger.log(f'{record}')
        return record
    
    def get_records(self):

        '''retrieves records,adds an appropriate log and return the rows of SQL tabl'''
        
        cursor = self.connection.execute('SELECT * FROM articles')
        rows = cursor.fetchall()
        self.logger.log(f'retrieved {len(rows)} records from database')
        return rows
    

        