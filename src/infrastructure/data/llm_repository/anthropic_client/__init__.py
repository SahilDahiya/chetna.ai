from anthropic import Anthropic

from src.domain.models.configuration import Configuration


def add_anthropic_client(configuration: Configuration) -> Anthropic:
    return Anthropic(
        api_key=configuration.anthropic_api_key,
    )
