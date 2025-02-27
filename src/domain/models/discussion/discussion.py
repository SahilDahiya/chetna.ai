import datetime

from openai import BaseModel

from .discussion_message import DiscussionMessage


class Discussion(BaseModel):
    user_id: str
    passage_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    messages: list[DiscussionMessage]
