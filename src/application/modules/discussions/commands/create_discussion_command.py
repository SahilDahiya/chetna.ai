from dependency_injector.wiring import Provide, inject

from src.domain.interfaces import AbstractLlmCompletionService
from src.infrastructure.containers import Container


@inject
class CreateDiscussionCommand:
    def __init__(
        self, llm_completion_service: AbstractLlmCompletionService = Provide[Container.llm_compeletion_service]
    ):
        self.llm_completion_service = llm_completion_service

    def create_discussion(self, query: str):
        messages = [
            {
                'role': 'developer',
                'content': 'You are a nice assitant!',
            },
            {
                'role': 'user',
                'content': query,
            },
        ]
        return self.llm_completion_service.complete(messages=messages)
