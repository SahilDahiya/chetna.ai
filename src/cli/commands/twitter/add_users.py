import typer
from rich import print

from src.application.modules.twitter.queries import get_twitter_user

app = typer.Typer()


@app.command()
def add_user(user_id: str):
    print(get_twitter_user(user_id))
    print(f'{user_id} added to the database')
