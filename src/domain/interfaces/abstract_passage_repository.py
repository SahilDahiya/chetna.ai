from abc import ABC, abstractmethod

from ...domain.models.passages import Passage


class AbstractPassageRepository(ABC):
    @abstractmethod
    def get_passage(self, book_name: str, chapter_no: str, passage_no: str) -> Passage:
        pass

    @abstractmethod
    def get_book_chapter_passages(self, book_name: str, chapter_no: str) -> list[Passage]:
        pass
