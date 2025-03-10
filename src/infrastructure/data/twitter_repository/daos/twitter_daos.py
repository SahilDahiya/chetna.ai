import datetime
from uuid import UUID

from typing_extensions import TypedDict

from src.domain.models.twitter import Tweet, User
from src.infrastructure.data.twitter_repository.daos import (
    PublicMetricsDAO,
    public_metrics_dao_to_public_metrics,
    public_metrics_to_public_metrics_dao,
)


class UserDAO(TypedDict):
    _id: UUID
    user_id: str
    user_name: str


class TweetDAO(TypedDict):
    _id: UUID
    user_id: str
    tweet_id: str
    text: str
    created_at: datetime.datetime
    public_metrics: PublicMetricsDAO
    edit_history_tweet_ids: list[str]


def tweet_dao_to_tweet(tweet_dao: TweetDAO) -> Tweet:
    return Tweet(
        id=tweet_dao['_id'],
        user_id=tweet_dao['user_id'],
        tweet_id=tweet_dao['tweet_id'],
        text=tweet_dao['text'],
        created_at=tweet_dao['created_at'],
        public_metrics=public_metrics_dao_to_public_metrics(tweet_dao['public_metrics']),
        edit_history_tweet_ids=tweet_dao['edit_history_tweet_ids'],
    )


def tweet_to_tweet_dao(tweet: Tweet) -> TweetDAO:
    return TweetDAO(
        _id=tweet.id,
        user_id=tweet.user_id,
        tweet_id=tweet.tweet_id,
        text=tweet.text,
        created_at=tweet.created_at,
        public_metrics=public_metrics_to_public_metrics_dao(tweet.public_metrics),
        edit_history_tweet_ids=tweet.edit_history_tweet_ids,
    )


def user_dao_to_user(user_dao: UserDAO) -> User:
    return User(user_id=user_dao['user_id'], user_name=user_dao['user_name'])


def user_to_user_dao(user: User) -> UserDAO:
    return UserDAO(user_id=user.user_id, user_name=user.user_name)
