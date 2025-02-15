from anthropic import Client as AnthropiClient
from openai import Client as OpenAiClient

from src.domain.interfaces import AbstractLlmRepository
from src.domain.models.configuration import Configuration
from src.domain.models.llm import LlmType


class LlmRepository(AbstractLlmRepository):
    def __init__(self, openai_client: OpenAiClient, anthropic_client: AnthropiClient, configuration: Configuration):
        self.__openai_client = openai_client
        self.__anthropic_client = anthropic_client
        self.__configuration = configuration

    def llm(self, llm_type: LlmType):
        if llm_type == LlmType.OPENAI:
            return self.__openai_client
        if llm_type == LlmType.ANTHROPIC:
            return self.__anthropic_client
        raise ValueError(f'Unknown LLM type: {llm_type}')
