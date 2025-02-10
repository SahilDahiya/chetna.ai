from uuid import UUID

from pymongo import MongoClient

from src.domain.interfaces import AbstractDiscussionRepository
from src.domain.models.configuration import Configuration
from src.domain.models.discussion import Discussion

from .daos import DiscussionDAO, discussion_dao_to_discussion, discussion_to_discussion_dao


class DiscussionRepository(AbstractDiscussionRepository):
    def __init__(self, mongodb_client: MongoClient, configuration: Configuration):
        database = mongodb_client[configuration.database_name]
        self.__collection = database[configuration.discussion_collection_name]

    def get(self, passage_id: UUID, user_id: UUID) -> Discussion | None:
        discussion: DiscussionDAO = self.__collection.find_one({'user_id': user_id, 'passage_id': passage_id})
        if not discussion:
            return None
        return discussion_dao_to_discussion(discussion)

    def save(self, discussion: Discussion) -> None:
        discussion_dao = discussion_to_discussion_dao(discussion)
        self.__collection.update_one(
            {'user_id': discussion.user_id, 'passage_id': discussion.passage_id}, {'$set': discussion_dao}, upsert=True
        )
