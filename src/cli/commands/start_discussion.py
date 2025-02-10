from uuid import UUID

import typer
from rich.console import Console

from src.application.modules.discussions.commands import DiscussCommand

console = Console(soft_wrap=True)

app = typer.Typer()


@app.command()
def start_discussion():
    discuss = DiscussCommand()
    discuss.create_discussion(user_id=UUID('123e4567-e89b-12d3-a456-426614174000'))
    print(discuss.passage.text_english)
    print('Ask me anything!')

    while True:
        query = typer.prompt('Your resposnse')

        if query.lower() == 'exit':
            console.print('[bold red]Goodbye![/bold red]')
            break

        with console.status('[bold yellow]Thinking[/bold yellow]', spinner='balloon'):
            content = discuss.ask(query)
        print(content)
