import requests

class NewsFetcher:
    def __init__(self,apiKey,volume=10):
        self.apiKey = apiKey
        self.volume = volume

    def fetch(self):
        parameters = {
            'apiKey': self.apiKey,
            'category': 'technology',
            'language': 'en',
            'pagesSize': self.volume
        }
        
        #creating hhtp request for newsapi
        response = requests.get('https://newsapi.org/v2/top-headlines',params=parameters)
        
        #converting nwesapi json response to python dictionary
        data = response.json()

        #checking if request succeeded(200 means success in http)
        if response.status_code == 200:
            return data['articles']
        else:
            print(f'Error: {response.status_code}')
            return []

