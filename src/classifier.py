from openai import OpenAI
from src.logger import Logger
import sqlite3
import json
import re
import time

class Classifier:
    def __init__(self,api_key,db_path='data/news.db'):
        self.api_key = api_key
        self.db_path = db_path
        self.logger = Logger()
        self.connection = sqlite3.connect(db_path)
        self.logger.log('Classifier is ready')
    
    def classify(self,record):
        time.sleep(5)
        client = OpenAI(
        api_key=self.api_key,
        base_url="https://openrouter.ai/api/v1"
        )

        response = client.chat.completions.create(
        model="openrouter/auto",
        messages=[
        {
            'role': 'user',
            'content': f'Respond with ONLY a valid JSON object, no explanation, no text before or after, just the JSON. Format: {{"sentiment": "positive", "negative", or "neutral", "topic": "tech", "business", "gaming", "science", or "other"}}\n\nHeadline: {record.cleaned_text}'
        }
        ],
        max_tokens=150
        )
        
        if not response.choices:
            return ''
        else:
            result = response.choices[0].message.content

        print(f"AI response: {result}")
        
        try:
            match = re.search(r'\{[^{}]*"sentiment"[^{}]*"topic"[^{}]*\}', result, re.DOTALL)
            if not match:
             match = re.search(r'\{[^{}]*"topic"[^{}]*"sentiment"[^{}]*\}', result, re.DOTALL)
            if match:
                data = json.loads(match.group())
            else:
                data = {"sentiment": "unknown", "topic": "other"}
        except (json.JSONDecodeError, KeyError):
            data = {"sentiment": "unknown", "topic": "other"}
        except Exception as e:
            self.logger.log(f'classification failed: {e}')
            data = {"sentiment": "unknown", "topic": "other"}


        record.sentiment = data['sentiment']
        record.topic = data['topic']

        self.connection.execute('''
        UPDATE articles
        SET sentiment=?, topic=?
        WHERE id=?
        ''', (record.sentiment,record.topic,record.id))
        self.connection.commit()

        self.logger.log(f'classified: sentiment={record.sentiment}, topic={record.topic}')
        return record
