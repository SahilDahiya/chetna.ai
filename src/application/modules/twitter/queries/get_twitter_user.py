from uuid import uuid4

from dependency_injector.wiring import Provide, inject

from src.domain.interfaces import AbstractTweetSearchService, AbstractTwitterRepository
from src.domain.models.twitter import Tweet, User
from src.domain.models.twitter.tweet import PublicMetrics
from src.infrastructure.containers import Container


@inject
def get_twitter_user(
    user_id: str,
    twitter_repository: AbstractTwitterRepository = Provide[Container.twitter_repository],
    tweet_search_service: AbstractTweetSearchService = Provide[Container.tweet_search_service],
):
    response = tweet_search_service.user_tweets(user_id)
    user = User(
            id=uuid4(),
            user_id=response['data'][0]['author_id'],
            user_name=user_id,
        )
    twitter_repository.add_user(user)
    for tweet_data in response['data']:
        public_metrics = tweet_data['public_metrics']
        tweet = Tweet(
            id=uuid4(),
            tweet_id=tweet_data['id'],
            user_id=user_id,
            text=tweet_data['text'],
            created_at=tweet_data['created_at'],
            public_metrics=PublicMetrics(
                retweet_count=public_metrics['retweet_count'],
                reply_count=public_metrics['reply_count'],
                like_count=public_metrics['like_count'],
                quote_count=public_metrics['quote_count'],
                impression_count=public_metrics['impression_count'],
                bookmark_count=public_metrics['bookmark_count'],
            )
        )
        twitter_repository.save_tweet(tweet)
