from abc import ABC, abstractmethod

from src.domain.models.twitter import Tweet, User


class AbstractTwitterRepository(ABC):
    @abstractmethod
    def get_user_tweets(self, user_id: str) -> list[Tweet]:
        pass

    @abstractmethod
    def save_tweet(self, tweets: list[Tweet]):
        pass

    @abstractmethod
    def add_user(self, user: User):
        pass
