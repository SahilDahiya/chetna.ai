import datetime
from uuid import UUID

from pydantic import BaseModel


class Discussion(BaseModel):
    discussion_id: UUID
    book_name: str
    chapter_no: str
    passage_no: str
    user_id: str
    created_at: datetime.datetime
    messages: list[dict[str, str]]
