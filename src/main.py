import typer

from src.cli.commands import add_passage_query_app, start_discussion_app, add_twitter_users_app
from src.infrastructure.containers import Container

app = typer.Typer()
container = Container()
container.wire(packages=['src.application'])

app.add_typer(add_passage_query_app)
app.add_typer(start_discussion_app)
app.add_typer(add_twitter_users_app)


@app.callback()
def main():
    """
    Think better in the awesome CLI app.
    """


if __name__ == '__main__':
    app()
