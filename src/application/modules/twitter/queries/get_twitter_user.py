from dependency_injector.wiring import Provide, inject

from src.domain.interfaces import AbstractTweetSearchService, AbstractTwitterRepository
from src.infrastructure.containers import Container


@inject
def get_twitter_user(
    user_id: str,
    twitter_repository: AbstractTwitterRepository = Provide[Container.passage_repository],
    tweet_search_service: AbstractTweetSearchService = Provide[Container.tweet_search_service],
):
    return tweet_search_service.user_tweets(user_id)