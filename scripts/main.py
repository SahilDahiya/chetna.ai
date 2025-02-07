import datetime
import os
import uuid

import click
from dotenv import load_dotenv
from openai import OpenAI
from pymongo import MongoClient
from rich.console import Console
from rich.panel import Panel
from rich.style import Style
from system_prompt import SYSTEM_PROMPT

load_dotenv()


# Create styled consoles
console = Console()
console_bot = Console(style='bold cyan')
console_user = Console(style='bold green')

# Custom styles
passage_style = Style(color='magenta')
question_style = Style(color='green', italic=True)
bot_style = Style(color='cyan')

client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
)

db_uri = r'mongodb://localhost:27017/'
database_name = 'nietzsche'
passage_collection_name = 'Passages'
discussion_collection_name = 'Discussions'


db = MongoClient(
    db_uri,
    uuidRepresentation='standard',
    tz_aware=True,
)
passages = db[database_name][passage_collection_name]
discussions = db[database_name][discussion_collection_name]


def get_response(messages):
    return client.chat.completions.create(messages=messages, model='gpt-4o', max_tokens=256)


def save_discussion(discussion):
    discussions.insert_one(discussion)


click.command()


def chat() -> None:
    passage_data = passages.find_one({'book_name': 'joyous_wisdom'})
    passage = passage_data['text_english']
    console.print(Panel(passage, title='Passage', style=passage_style))
    discussion = {
        'discussion_id': uuid.uuid4(),
        'book_name': passage_data['book_name'],
        'chapter_no': passage_data['chapter_no'],
        'passage_no': passage_data['passage_no'],
        'user_id': 'Test1',
        'created_at': datetime.datetime.now(),
        'messages': [],
    }

    console_bot.print('[bold yellow]Ask me anything about passage![/bold yellow]')
    question = console_user.input('[bold green]Question: [/bold green]')
    messages = [
        {
            'role': 'developer',
            'content': SYSTEM_PROMPT,
        },
        {
            'role': 'assistant',
            'content': 'Use only the information provided in the passage.\n{passage}',
        },
        {
            'role': 'user',
            'content': f'{question}',
        },
    ]
    discussion['messages'].extend(messages)
    response = get_response(messages)

    while question != 'save':
        response = get_response(messages)
        ai = response.choices[0].message.content
        console_bot.print(Panel(ai, style=bot_style))
        question = console_user.input('[bold green]Question: [/bold green]')
        messages.extend(
            [
                {
                    'role': 'assistant',
                    'content': ai,
                },
                {
                    'role': 'user',
                    'content': f'{question}',
                },
            ]
        )
        discussion['messages'].extend(messages)

    if len(discussion['messages']) > 2:
        save_discussion(discussion)
        print('saved!')


if __name__ == '__main__':
    chat()
