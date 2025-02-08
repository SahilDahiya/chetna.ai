from uuid import UUID

from pydantic import BaseModel


class Passage(BaseModel):
    id: UUID
    book_name: str
    author: str
    chapter_no: str
    passage_no: str
    text_english: str
    text_german: str