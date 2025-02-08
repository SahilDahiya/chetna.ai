import typer
from pymongo import MongoClient
from rich import print

from ...infrastructure.configuration import Configuration
from ...infrastructure.data.passage_repository import PassageRepository

app = typer.Typer()


@app.command()
def get_passage(book_name: str):
    db_uri = r'mongodb://localhost:27017/'
    database_name = 'nietzsche'

    mgc = MongoClient(
        db_uri,
        uuidRepresentation='standard',
        tz_aware=True,
    )
    
    config = Configuration(
        openai_api_key= "nothing",
        mongodb_connection_string=db_uri,
        database_name = database_name,
        passage_collection_name="Passages"
        
    )
    passage_repository = PassageRepository(mgc, config)
    print(passage_repository.get_passage(book_name, 'chapter_1', '19'))