from datetime import datetime

class Logger:
    shared_logs = []

    def log(self,message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        x = f'{timestamp} {message}'
        self.shared_logs.append(x)
        print(x)

