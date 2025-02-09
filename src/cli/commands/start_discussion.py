import typer
from rich import print

from src.application.modules.discussions.commands import DiscussCommand

app = typer.Typer()


@app.command()
def start_discussion():
    discuss = DiscussCommand()
    discuss.create_discussion()
    print(discuss.passage.text_english)
    print('Ask me anything!')

    while True:
        query = typer.prompt('Your resposnse')

        if query.lower() == 'exit':
            print('[bold red]Goodbye![/bold red]')
            break

        content = discuss.ask(query)
        print(content)
