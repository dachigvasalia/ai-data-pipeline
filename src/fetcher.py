import requests

class NewsFetcher:

    '''connects to NewsAPI over the internet and returns real news articles'''

    def __init__(self,api_key,volume=10):

        '''Initializes NewsFetcher's object,takes api_key and volume as arguments,volume is 10 by default'''

        self.api_key = api_key
        self.volume = volume

    def fetch(self):

        '''sends get request to NewsAPI to get apikey,category,language and pageSize parameters from it.
        then it converts json response into python dictionary and checks if it was succesful,
        in cae of success it retrieves the data from resonse and returns it'''
        
        parameters = {
            'apiKey': self.api_key,
            'category': 'technology',
            'language': 'en',
            'pageSize': self.volume
        }
        
        #send GET request to server
        response = requests.get('https://newsapi.org/v2/top-headlines',params=parameters)
        
        #after server's response,converts json response into python dictionary
        data = response.json()

        #checks status code before trusting the response
        if response.status_code == 200:
            return data['articles']
        else:
            print(f'Error: {response.status_code}')
            return []
