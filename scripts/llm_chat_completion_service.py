from openai import Client


class LlmChatCompletionService:
    def __init__(self, openai_client: Client, passage_repository, configuration):
        self.__openai_client = openai_client
        self.__passage_repository = passage_repository
        self.__configuration = configuration

    def complete(self, messages, max_tokens: int):
        response = self.__openai_client.chat.completions.create(messages=messages, model=self.__configuration.model_name, max_tokens=max_tokens)
        return response.choices[0].message.content