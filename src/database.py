from src.logger import Logger
import sqlite3
import os

class DataBaseManager:
    def __init__(self,db_path='data/news.db'):
        self.db_path = db_path
        self.logger = Logger()
        os.makedirs('data',exist_ok=True)
        self.connection = sqlite3.connect(db_path)
        self.logger.log(f'database is created : {self.db_path}')
        
    def create_table(self):
        self.connection.execute('''
        CREATE TABLE IF NOT EXISTS articles(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            raw_text TEXT,
            cleaned_text TEXT,
            timestamp TEXT,
            is_clean INTEGER                        
        )
                                
        ''')
        self.connection.commit()

    def clear_table(self):
        self.connection.execute('DELETE FROM articles')
        self.connection.commit()
        self.logger.log('table cleared')
        
    def save_record(self,record):
        self.connection.execute('''
        INSERT INTO articles(source,raw_text,cleaned_text,timestamp,is_clean)
        VALUES(?,?,?,?,?)
        ''', (record.source,record.raw_text,record.cleaned_text,record.timestamp,record.is_clean))
        self.connection.commit()
        self.logger.log(f'{record}')
    
    def get_records(self):
        cursor = self.connection.execute('SELECT * FROM articles')
        rows = cursor.fetchall()
        self.logger.log(f'retrieved {len(rows)} records from database')
        return rows
    

        