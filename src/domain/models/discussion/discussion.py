import datetime
from uuid import UUID

from openai import BaseModel

from .discussion_message import DiscussionMessage


class Discussion(BaseModel):
    user_id: UUID
    passage_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    messages: list[DiscussionMessage]
