from typing import Literal, TypedDict

from src.domain.models.discussion import DiscussionMessage


class DiscussionMessageDAO(TypedDict):
    role: Literal['developer', 'user', 'assistant']
    content: str


def discussion_message_dao_to_discussion_message(discussion_message_dao: DiscussionMessageDAO) -> DiscussionMessage:
    return DiscussionMessage(role=discussion_message_dao['role'], content=discussion_message_dao['content'])


def discussion_message_to_discussion_message_dao(discussion_message: DiscussionMessage) -> DiscussionMessageDAO:
    if not isinstance(discussion_message, DiscussionMessage):
        raise TypeError(f'Expected DiscussionMessage, got {type(discussion_message)}')
    return DiscussionMessageDAO(role=discussion_message.role, content=discussion_message.content)
