from pydantic import BaseModel


class Passage(BaseModel):
    passage_id: str
    book_name: str
    author: str
    chapter_name: str
    passage_no: str
    text: str
