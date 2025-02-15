import random

from src.domain.interfaces import AbstractPassageRecommendationService, AbstractPassageRepository
from src.domain.models.passages import Passage


class PassageRecommendationService(AbstractPassageRecommendationService):
    def __init__(self, passage_repository: AbstractPassageRepository):
        self.__passage_repository = passage_repository

    def recommend(self, book_name: str) -> Passage:
        chapter_name = 'BOOK FIRST'
        passages = self.__passage_repository.get_book_chapter_passages(book_name, chapter_name)
        passage = random.choices(passages, k=1)[0]

        while len(passage.text) < 256:
            passage = random.choices(passages, k=1)
        return passage
