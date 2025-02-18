from uuid import UUID

from pydantic import BaseModel


class User(BaseModel):
    id: UUID
    user_id: str
    user_name: str
