from pydantic_settings import BaseSettings


class Configuration(BaseSettings):
    anthropic_api_key: str
    anthropic_model_name: str

    openai_api_key: str
    openai_model_name: str
    openai_max_tokens: int

    mongodb_connection_string: str
    database_name: str
    passage_collection_name: str
    discussion_collection_name: str

    twitter_bearer_token: str
