from src.logger import Logger
import sqlite3

class Analyzer:

    '''extracts business insights from database with SQL queries'''

    def __init__(self,db_path='data/news.db'):

        '''initializes Analyzer's object with db_path parameter that is already set.
        creates object of Logger's class and connection to database file.makes a log'''

        self.db_path = db_path
        self.logger = Logger()
        self.connection = sqlite3.connect(db_path)
        self.logger.log(f'analytics connected to {self.db_path} database')  
    
    def articles_per_source(self):

        '''count the articles of each source,adds an appropirate log and returns rows of SQL table'''

        cursor = self.connection.execute('''
        SELECT source,COUNT(*) as article_count
        From articles
        GROUP BY source
        ORDER BY article_count DESC                       
        ''')
        rows = cursor.fetchall()
        self.logger.log(f'found {len(rows)} sources')
        return rows
    
    def most_recent_articles(self):

        '''returns 5 most recent articles(returns 5 tuples)'''

        cursor = self.connection.execute('''
        SELECT source,raw_text,timestamp
        FROM articles
        ORDER BY timestamp DESC
        LIMIT 5
                                        ''')
        rows = cursor.fetchall()
        self.logger.log(f'retrieved 5 most recent articles')
        return rows
    
    def total_articles(self):

        '''returns total number of articles and adds log'''

        cursor = self.connection.execute('SELECT COUNT(*) FROM articles')
        row = cursor.fetchone()
        count = row[0]
        self.logger.log(f'total number of articles: {count}')
        return count