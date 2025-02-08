import typer
from rich import print

from ...domain.models.configuration import Configuration
from ...infrastructure.data import mongodb_client
from ...infrastructure.data.passage_repository import PassageRepository

app = typer.Typer()


@app.command()
def get_passage(book_name: str):

    
    config = Configuration(_env_file=".env", _env_file_encoding="utf-8")
    
    db_client = mongodb_client(configuration=config)
    

    passage_repository = PassageRepository(db_client, config)
    print(passage_repository.get_passage(book_name, 'chapter_1', '19'))