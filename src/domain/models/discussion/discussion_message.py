from typing import Literal

from pydantic import BaseModel


class DiscussionMessage(BaseModel):
    role: Literal['developer', 'user', 'assistant']
    content: str
