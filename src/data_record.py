from datetime import datetime

class DataRecord:
    '''represents a single news article moving through the pipeline.
    stores raw text,cleaned text,timestamp and AI-genereated labels.'''

    def __init__(self,source,raw_text):

        '''Initializes DtaRecord with source and raw text.
        sets is_clean to False and cleaned_text to None by default'''

        self.source = source
        self.raw_text = raw_text
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        self.is_clean = False
        self.cleaned_text = None
        self.sentiment = None
        self.topic = None
        self.id = None

    def clean(self):
        '''removes leading and trailing whitespace and converts to lowercase'''

        self.cleaned_text = self.raw_text.strip().lower()
        self.is_clean = True

    def to_dict(self):
        ''''Returns all record fields as a dictionary.
        used when saving to database or sending to external API's'''

        organized = {'source': self.source,'raw_text':self.raw_text,'time':self.timestamp,'cleaned_status':self.is_clean,'cleaned_text':self.cleaned_text}
        return organized
    
    def __repr__(self):
        '''Returns an unambiguous string representation of the object for debugging'''

        status = 'clean' if self.is_clean is True else 'raw'
        return f'status: {status}, source: {self.source}'