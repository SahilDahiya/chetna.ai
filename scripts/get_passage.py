import os

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
console_bot = Console(style="bold cyan")
console_user = Console(style="bold green")

# Custom styles
passage_style = Style(color="magenta")
question_style = Style(color="green", italic=True)
bot_style = Style(color="cyan")

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
        model='gpt-4o',
        max_tokens=256
    )
    

click.command()
def chat() -> None:
    passage = passages.find_one({'book_name': 'joyous_wisdom'})['text_english']
    console.print(Panel(passage, title="Passage", style=passage_style))
    
    console_bot.print("[bold yellow]Ask me anything about passage![/bold yellow]")
    question = console_user.input("[bold green]Question: [/bold green]")
    messages=[
            {
                'role': 'developer',
                'content': SYSTEM_PROMPT.format(passage=passage),
            },
            {
                'role': 'assistant',
                'content': "Use only the information provided in the passage.\n{passage}",
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
        console_bot.print(Panel(ai, style=bot_style))
        question = console_user.input("[bold green]Question: [/bold green]")
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

