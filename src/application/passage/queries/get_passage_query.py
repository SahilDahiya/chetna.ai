from domain.interfaces import AbstractPassageRepository
from domain.models.passages import Passage


class GetPassageQuery:
    def __init__(self, passage_repository: AbstractPassageRepository):
        self.__passage_repository = passage_repository

    def get_passage(self, book_name: str) -> Passage:
        return self.__passage_repository.get_passage(book_name, '1', '19')
