import datetime
from typing import TypedDict
from uuid import UUID

from src.domain.models.discussion import Discussion

from .discussion_message_dao import (
    DiscussionMessageDAO,
    discussion_message_dao_to_discussion_message,
    discussion_message_to_discussion_message_dao,
)


class DiscussionDAO(TypedDict):
    user_id: UUID
    passage_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    messages: list[DiscussionMessageDAO]


def discussion_dao_to_discussion(discussion_dao: DiscussionDAO) -> Discussion:
    return Discussion(
        user_id=discussion_dao['user_id'],
        passage_id=discussion_dao['passage_id'],
        created_at=discussion_dao['created_at'],
        updated_at=discussion_dao['updated_at'],
        messages=[discussion_message_dao_to_discussion_message(msg_dao) for msg_dao in discussion_dao['messages']],
    )


def discussion_to_discussion_dao(discussion: Discussion) -> DiscussionDAO:
    return DiscussionDAO(
        user_id=discussion.user_id,
        passage_id=discussion.passage_id,
        created_at=discussion.created_at,
        updated_at=discussion.updated_at,
        messages=[discussion_message_to_discussion_message_dao(msg) for msg in discussion.messages],
    )
