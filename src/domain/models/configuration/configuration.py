from pydantic_settings import BaseSettings


class Configuration(BaseSettings):

    openai_api_key: str

    mongodb_connection_string: str
    database_name: str
    passage_collection_name: str