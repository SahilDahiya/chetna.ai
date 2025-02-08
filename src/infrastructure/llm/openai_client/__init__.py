from openai import OpenAI

from src.domain.models.configuration import Configuration


def add_openai_client(configuration: Configuration) -> OpenAI:
    return OpenAI(
        api_key=configuration.openai_api_key,
    )