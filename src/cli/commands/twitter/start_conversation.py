import typer
from rich import print

from src.application.modules.twitter.commands import send_out_tweets

app = typer.Typer()


@app.command()
def start_twitter_conversation():
    print(send_out_tweets())