import typer
from rich import print

from src.application.modules.discussions.commands import CreateDiscussionCommand

app = typer.Typer()
    
@app.command()
def discuss(
    query:str
):
    create_discussion_command = CreateDiscussionCommand()
    print(create_discussion_command.create_discussion(query))