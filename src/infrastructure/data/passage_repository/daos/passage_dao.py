from uuid import UUID

from typing_extensions import TypedDict

from .....domain.models.passages import Passage


class PassageDAO(TypedDict):
    _id: UUID
    uuid: UUID
    book_name: str
    author: str
    chapter_title: str
    chapter_no: str
    passage_no: str
    text_english: str
    text_german: str


def passage_dao_to_passage(passage_dao: PassageDAO) -> Passage:
    return Passage(
        id=passage_dao['uuid'],
        book_name=passage_dao['book_name'],
        author=passage_dao['author'],
        chapter_no=passage_dao['chapter_no'],
        passage_no=passage_dao['passage_no'],
        text_english=passage_dao['text_english'],
        text_german=passage_dao['text_german']
    )