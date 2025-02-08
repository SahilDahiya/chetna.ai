import typer

from .cli.commands import add_get_passage_app

app = typer.Typer()

app.add_typer(add_get_passage_app)


if __name__ == "__main__":
    app()