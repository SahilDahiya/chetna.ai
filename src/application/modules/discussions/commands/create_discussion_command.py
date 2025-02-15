import datetime
from uuid import UUID

from dependency_injector.wiring import Provide, inject

from src.domain.interfaces import AbstractDiscussionRepository, AbstractLlmCompletionService
from src.domain.models.discussion import Discussion, DiscussionMessage
from src.domain.models.passages import Passage
from src.domain.prompts import SYSTEM_PROMPT
from src.infrastructure.containers import Container
from src.infrastructure.recommendation import PassageRecommendationService


@inject
class DiscussCommand:
    def __init__(
        self,
        discussion_repository: AbstractDiscussionRepository = Provide[Container.discussion_repository],
        llm_completion_service: AbstractLlmCompletionService = Provide[Container.llm_compeletion_service],
        passage_recommendation_service: PassageRecommendationService = Provide[
            Container.passage_recommendation_service
        ],
    ):
        self.passage = None
        self.discussion = None
        self.__discussion_repository = discussion_repository
        self.__llm_completion_service = llm_completion_service
        self.__passage_recommendation_service = passage_recommendation_service

    def create_discussion(self, user_id: UUID) -> None:
        self.passage = self.get_next_passage()
        self.discussion = self.__discussion_repository.get(user_id, self.passage.passage_id)
        # TODO: summarize already existing discussion
        if not self.discussion:
            messages = [
                DiscussionMessage(
                    role='developer',
                    content=SYSTEM_PROMPT,
                ),
                DiscussionMessage(
                    role='assistant',
                    content=f'Only answer from this passage: {self.passage.text}',
                ),
            ]
            self.discussion = Discussion(
                user_id=user_id,
                created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now(),
                passage_id=self.passage.passage_id,
                messages=messages,
            )

    def get_next_passage(self, book_name: str | None = 'The Joyous Wisdom') -> Passage:
        return self.__passage_recommendation_service.recommend(book_name=book_name)

    def ask(self, query) -> str:
        self.discussion.messages.append(
            DiscussionMessage(
                role='user',
                content=query,
            )
        )
        response = self.__llm_completion_service.complete(messages=self.discussion.messages)
        self.discussion.messages.append(
            DiscussionMessage(
                role='assistant',
                content=response,
            )
        )
        self.__discussion_repository.save(self.discussion)
        return response
