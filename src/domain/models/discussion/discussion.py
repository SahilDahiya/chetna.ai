from uuid import UUID

from openai import BaseModel


class Discussion(BaseModel):
    user_id: UUID
    passage_id: UUID
    messages: list[dict[str, str]]
