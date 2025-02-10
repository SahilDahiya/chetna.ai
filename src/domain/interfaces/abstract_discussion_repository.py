from abc import ABC, abstractmethod
from uuid import UUID

from src.domain.models.discussion import Discussion


class AbstractDiscussionRepository(ABC):
    @abstractmethod
    def get(self, passage_id: UUID, user_id: UUID) -> Discussion | None:
        pass

    @abstractmethod
    def save(self, discussion: Discussion) -> None:
        pass
