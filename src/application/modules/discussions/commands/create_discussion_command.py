from dependency_injector.wiring import Provide, inject

from src.domain.interfaces import AbstractLlmCompletionService
from src.domain.models.passages import Passage
from src.domain.prompts import SYSTEM_PROMPT
from src.infrastructure.containers import Container
from src.infrastructure.recommendation import PassageRecommendationService


@inject
class DiscussCommand:
    def __init__(
        self, 
        llm_completion_service: AbstractLlmCompletionService = Provide[Container.llm_compeletion_service],
        passage_recommendation_service: PassageRecommendationService = Provide[Container.passage_recommendation_service]
    ):
        self.passage = None
        self.messages = None
        self.llm_completion_service = llm_completion_service
        self.passage_recommendation_service = passage_recommendation_service

    def create_discussion(self):
        self.passage = self.get_next_passage()
        self.messages = [
            {
                'role': 'developer',
                'content': SYSTEM_PROMPT,
            },
            {
                'role': 'assistant',
                'content': f'Only answer from this passage: {self.passage.text_english}',
            },
        ]
        

    def get_next_passage(self, book_name: str | None = 'joyous_wisdom') -> Passage:
        return self.passage_recommendation_service.recommend(book_name=book_name)

    def ask(self, query) -> str:
        self.messages.append({
            'role': 'user',
            'content': query
        })
        response = self.llm_completion_service.complete(messages=self.messages)
        self.messages.append({
            'role': 'assistant',
            'content': response
        })

        return response


