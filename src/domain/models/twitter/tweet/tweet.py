import datetime

from pydantic import BaseModel

from .public_metrics import PublicMetrics


class Tweet(BaseModel):
    user_id: str
    tweet_id: str
    text: str
    created_at: datetime.datetime
    public_metrics: PublicMetrics
