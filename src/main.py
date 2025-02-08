import typer

from src.cli.commands import add_get_passage_app
from src.infrastructure.container import Container

app = typer.Typer()
container = Container()
container.wire(packages=["src.application"])

app.add_typer(add_get_passage_app)

@app.callback()
def main(verbose: bool = False):
    """
    Think better in the awesome CLI app.
    """


if __name__ == "__main__":
    app()