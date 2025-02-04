import os

import click
from dotenv import load_dotenv
from openai import OpenAI
from pymongo import MongoClient
from system_prompt import SYSTEM_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
)

db_uri = r'mongodb://localhost:27017/'
database_name = 'nietzsche'
collection_name = 'Passages'

db = MongoClient(db_uri)
passages = db[database_name][collection_name]

def get_response(messages):
    return client.chat.completions.create(
        messages=messages,
        model='gpt-4o-mini',
    )
    

click.command()
def chat() -> None:
    passage = passages.find_one()['text_english']
    print("passage: ", passage)
    print("Ask me anything about passage!")
    question = input("Question: ")
    messages=[
            {
                'role': 'developer',
                'content': SYSTEM_PROMPT.format(passage=passage),
            },
            {
                'role': 'user',
                'content': f'{question}',
            }
        ]
    response = get_response(messages)
    
    while question != "stop!":
        response = get_response(messages)
        ai = response.choices[0].message.content
        print(ai)
        question = input("Question: ")
        messages.extend([
            {
                'role': 'assistant',
                'content': ai,
            },
            {
                'role': 'user',
                'content': f'{question}',
            }
        ])
        
        
if __name__ == '__main__':
    chat()

