from enum import Enum

from domain.interfaces import AbstractLlmRepository
from domain.models.configuration import Configuration

from openai import Client as OpenAiClient
from anthropic import Client as AnthropiClient


class LlmType(Enum):
    OPENAI = 'openai'
    ANTHROPIC = 'anthropic'


class LlmRepository(AbstractLlmRepository):
    def __init__(self, openai_client: OpenAiClient, anthropic_client: AnthropiClient, configuration: Configuration):
        self.__openai_client = openai_client
        self.__anthropic_client = anthropic_client
        self.__configuration = configuration

    def get_llm_client(self, llm_type: LlmType) -> OpenAiClient | AnthropiClient:
        if llm_type == LlmType.OPENAI:
            return self.__openai_client
        if llm_type == LlmType.ANTHROPIC:
            return self.__anthropic_client
        raise ValueError(f'Unknown LLM type: {llm_type}')
