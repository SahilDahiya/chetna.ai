from pydantic_settings import BaseSettings


class Configuration(BaseSettings):

    openai_api_key: str
    model_name: str
    max_tokens: int

    mongodb_connection_string: str
    database_name: str
    passage_collection_name: str