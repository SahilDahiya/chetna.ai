from typing import TypedDict
from uuid import UUID

from src.domain.models.discussion import Discussion


class DiscussionDAO(TypedDict):
    user_id: UUID
    passage_id: UUID
    messages: list[dict[str, str]]


def discussion_dao_to_discussion(discussion_dao: DiscussionDAO) -> Discussion:
    return Discussion(
        user_id=discussion_dao['user_id'], passage_id=discussion_dao['passage_id'], messages=discussion_dao['messages']
    )


def discussion_to_discussion_dao(discussion: Discussion) -> DiscussionDAO:
    return DiscussionDAO(user_id=discussion.user_id, passage_id=discussion.passage_id, messages=discussion.messages)
