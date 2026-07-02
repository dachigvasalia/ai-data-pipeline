import requests

class NewsFetcher:
    def __init__(self,api_key,volume=10):
        self.api_key = api_key
        self.volume = volume

    def fetch(self):
        parameters = {
            'apiKey': self.api_key,
            'category': 'technology',
            'language': 'en',
            'pageSize': self.volume
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
