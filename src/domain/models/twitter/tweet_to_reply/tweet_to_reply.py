from pydantic import BaseModel


class TweetToReply(BaseModel):
    user_id: str
    conversation_id: str
    last_tweet_id: str
