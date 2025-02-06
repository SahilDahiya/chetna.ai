from pydantic import BaseModel


class Configuration(BaseModel):
    max_tokens: int = 256
    model_name: str = 'gpt-4o'
