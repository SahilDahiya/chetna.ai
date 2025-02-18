from pymongo import MongoClient

from src.domain.interfaces import AbstractTwitterRepository
from src.domain.models.configuration import Configuration
from src.domain.models.twitter import Tweet, User


class TwitterRepository(AbstractTwitterRepository):
    def __init__(self, mongodb_client: MongoClient, configuration: Configuration):
        database = mongodb_client[configuration.database_name]
        self.__user_collection = database[configuration.user_collection_name]
        self.__tweet_collection = database[configuration.tweet_collection_name]

    def get_user_tweets(self, user_id: str) -> list[Tweet]:
        tweets_cursor = self.__tweet_collection.find({"user_id": user_id})
        return [Tweet(**tweet) for tweet in tweets_cursor]

    def save_tweet(self, tweet: Tweet):
        self.__tweet_collection.insert_one(tweet.dict())

    def add_user(self, user: User):
        self.__user_collection.update_one(
            {"user_id": user.user_id},
            {"$set": user.dict()},
            upsert=True
        )
