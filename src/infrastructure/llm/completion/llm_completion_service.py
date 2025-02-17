from openai import Client

from src.domain.interfaces import AbstractLlmCompletionService


class LlmCompletionService(AbstractLlmCompletionService):
    def __init__(self, openai_client: Client, configuration):
        self.__openai_client = openai_client
        self.__configuration = configuration

    def complete(self, messages):
        response = self.__openai_client.chat.completions.create(
            messages=messages,
            model=self.__configuration.openai_model_name,
            max_tokens=self.__configuration.openai_max_tokens,
        )
        return response.choices[0].message.content
