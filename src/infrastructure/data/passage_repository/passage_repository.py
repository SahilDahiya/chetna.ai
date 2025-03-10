from uuid import UUID

from pymongo import MongoClient

from src.domain.interfaces import AbstractPassageRepository
from src.domain.models.configuration import Configuration
from src.domain.models.passages import Passage

from .daos.passage_dao import PassageDAO, passage_dao_to_passage


class PassageRepository(AbstractPassageRepository):
    def __init__(self, mongodb_client: MongoClient, configuration: Configuration):
        database = mongodb_client[configuration.database_name]
        self.__collection = database[configuration.passage_collection_name]

    def get_passage(self, book_name: str, chapter_name: str, passage_no: str) -> Passage:
        passage: PassageDAO = self.__collection.find_one(
            {'book_name': book_name, 'chapter_name': chapter_name, 'passage_no': passage_no}
        )

        return passage_dao_to_passage(passage)

    def get_book_chapter_passages(self, book_name: str, chapter_name: str) -> list[Passage]:
        passages: list[PassageDAO] = list(
            self.__collection.find({'book_name': book_name, 'chapter_name': chapter_name})
        )

        return [passage_dao_to_passage(passage) for passage in passages]

    def get_passage_by_id(self, passage_id: UUID) -> Passage:
        passage: PassageDAO = self.__collection.find_one({'uuid': passage_id})
        return passage_dao_to_passage(passage)
