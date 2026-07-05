from datetime import datetime

class Logger:
    '''records every event of pipeline with timetsamp'''
    shared_logs = [] #every logger's instance's logs are stored here


    def log(self,message):
        '''adds logs with timestamp to the shared_logs list and prints them'''
        timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        entry = f'{timestamp} {message}'
        self.shared_logs.append(entry)
        print(entry)

