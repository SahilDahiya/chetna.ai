from abc import abstractmethod

from src.domain.models.passages import Passage


class AbstractPassageRecommendationService:
    @abstractmethod
    def recommend(self, query: str) -> Passage:
        pass
