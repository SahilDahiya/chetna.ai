import typer
from rich import print

from src.application.modules.passages.queries import passage_query, passage_to_svg_query

app = typer.Typer()


@app.command()
def get_passage(book_name: str):
    print(passage_query(book_name))

@app.command()
def convert_to_svg(book_name: str):
    passage = passage_to_svg_query(book_name)
    passage
