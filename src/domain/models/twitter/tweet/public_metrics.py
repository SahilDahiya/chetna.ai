from pydantic import BaseModel


class PublicMetrics(BaseModel):
    retweet_count: int
    reply_count: int
    like_count: int
    quote_count: int
    impression_count: int
    bookmark_count: int
