import typer
from rich import print

from src.application.modules.passages.queries import passage_query

app = typer.Typer()


@app.command()
def get_passage(
    book_name: str,
    chapter: str = typer.Argument('chapter_1'),
    verse: str = typer.Argument('19'),
):
    print(passage_query(book_name, chapter, verse))
