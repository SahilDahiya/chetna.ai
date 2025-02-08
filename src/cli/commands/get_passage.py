import typer
from rich import print

from src.application.modules.queries import get_passage

app = typer.Typer()
    
@app.command()
def passage(
    book_name: str,
    chapter: str = typer.Argument("chapter_1"),
    verse: str = typer.Argument("19"),
):
    print(get_passage(book_name, chapter, verse))