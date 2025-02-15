from uuid import UUID

import typer
from rich.console import Console
from rich.panel import Panel
from rich.theme import Theme

from src.application.modules.discussions.commands import DiscussCommand

custom_theme = Theme(
    {
        'info': 'yellow on blue',
        'prompt': 'green italic',
        'thinking': 'yellow',
        'goodbye': 'red bold',
    }
)

console = Console(theme=custom_theme)

app = typer.Typer()


@app.command()
def start_discussion():
    discuss = DiscussCommand()
    discuss.create_discussion(user_id=UUID('123e4567-e89b-12d3-a456-426614174000'))
    console.print(
        Panel(
            discuss.passage.text,
            title=discuss.passage.book_name,
            subtitle=f'{discuss.passage.chapter_name}#{discuss.passage.passage_no}',
            style='info',
            highlight=True,
        )
    )

    console.print(Panel('Ask me anything!', title='🤖', style='prompt'))

    while True:
        console.print('─' * console.width, style='dim')
        console.print('[green]You:[/green]')
        query = input(' > ').strip()

        if query.lower() == 'exit':
            console.print('[bold red]Goodbye![/bold red]')
            break

        with console.status('[bold yellow]Thinking[/bold yellow]', spinner='balloon'):
            content = discuss.ask(query)
        console.print(Panel(content, title='🤖', style='prompt'))
