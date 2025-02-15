from abc import ABC, abstractmethod

from src.domain.models.passages import Passage


class AbstractTweetPostService(ABC):
    @abstractmethod
    def post(self, text: str, reply_tweet_id: str, passage: Passage) -> dict:
        pass
