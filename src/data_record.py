from datetime import datetime
class DataRecord:
    def __init__(self,source,raw_text):
        self.source = source
        self.raw_text = raw_text
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        self.is_clean = False
        self.cleaned_text = None

    def clean(self):
        self.cleaned_text = self.raw_text.strip().lower()
        self.is_clean = True

    def to_dict(self):
        organized = {'source': self.source,'raw_text':self.raw_text,'time':self.timestamp,'cleaned_status':self.is_clean,'cleaned_text':self.cleaned_text}
        return organized
    
    def __repr__(self):
        status = 'clean' if self.is_clean is True else 'raw'
        return f'status: {status}, source: {self.source}'