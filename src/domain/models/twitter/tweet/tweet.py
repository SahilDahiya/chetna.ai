import datetime
from uuid import UUID

from pydantic import BaseModel

from .public_metrics import PublicMetrics


class Tweet(BaseModel):
    id: UUID
    user_id: str
    tweet_id: str
    text: str
    created_at: datetime.datetime
    public_metrics: PublicMetrics
    edit_history_tweet_ids: list[str]
