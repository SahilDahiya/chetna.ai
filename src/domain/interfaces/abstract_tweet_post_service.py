from abc import ABC, abstractmethod

from domain.models.passages import Passage


class AbstractTweetPostService(ABC):
    @abstractmethod
    def post(self, text: str, reply_tweet_id: str, passage: Passage) -> dict:
        pass
