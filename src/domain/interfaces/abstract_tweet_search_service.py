from abc import ABC, abstractmethod

from src.domain.models.twitter import Tweet


class AbstractTweetSearchService(ABC):
    @abstractmethod
    def user_tweets(self, user_id: str) -> list[Tweet]:
        pass

    @abstractmethod
    def search_by_tweet_id(self, tweet_id: str) -> Tweet:
        pass
