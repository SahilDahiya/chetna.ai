import typer
from dependency_injector.wiring import Provide, inject
from rich import print

from src.domain.interfaces import AbstractPassageRepository
from src.infrastructure.container import Container

app = typer.Typer()



@inject
def get_passage(
    book_name: str,
    chapter: str = typer.Argument("chapter_1"),
    verse: str = typer.Argument("19"),
    passage_repository: AbstractPassageRepository = Provide[Container.passage_repository]
):
    return passage_repository.get_passage(book_name, 'chapter_1', '19')
    
    
@app.command()
def passage(
    book_name: str,
    chapter: str = typer.Argument("chapter_1"),
    verse: str = typer.Argument("19"),
):
    print(get_passage(book_name, chapter, verse))