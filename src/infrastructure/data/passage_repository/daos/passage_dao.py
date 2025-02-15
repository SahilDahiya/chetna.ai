from uuid import UUID

from typing_extensions import TypedDict

from src.domain.models.passages import Passage


class PassageDAO(TypedDict):
    _id: UUID
    passage_id: str
    book_name: str
    author: str
    chapter_name: str
    passage_no: str
    text: str


def passage_dao_to_passage(passage_dao: PassageDAO) -> Passage:
    return Passage(
        passage_id=passage_dao['passage_id'],
        book_name=passage_dao['book_name'],
        author=passage_dao['author'],
        chapter_name=passage_dao['chapter_name'],
        passage_no=passage_dao['passage_no'],
        text=passage_dao['text'],
    )
