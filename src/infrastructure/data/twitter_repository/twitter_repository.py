from pymongo import MongoClient

from src.domain.interfaces import AbstractTwitterRepository
from src.domain.models.configuration import Configuration
from src.domain.models.twitter import Tweet, User


class TwitterRepository(AbstractTwitterRepository):
    def __init__(self, mongodb_client: MongoClient, configuration: Configuration):
        self.__mongodb_client = mongodb_client
        self.__configuration = configuration

    def get_user_tweets(self, user_id: str) -> list[Tweet]:
        pass

    def add_tweets(self, tweets: list[Tweet]):
        pass

    def add_user(self, user: User):
        pass
