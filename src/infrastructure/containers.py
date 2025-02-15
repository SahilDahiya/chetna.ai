from dependency_injector import containers, providers

from src.domain.models.configuration import Configuration

from .data import (
    DiscussionRepository,
    PassageRepository,
    add_mongodb_client,
    add_anthropic_client,
    add_openai_client,
    LlmRepository,
)
from .llm import LlmCompletionService
from .recommendation import PassageRecommendationService


class Container(containers.DeclarativeContainer):
    config = providers.Singleton(Configuration, _env_file='.env', _env_file_encoding='utf-8')

    db_client = providers.Singleton(add_mongodb_client, configuration=config)

    openai_client = providers.Singleton(add_openai_client, configuration=config)
    anthropic_client = providers.Singleton(add_anthropic_client, configuration=config)

    passage_repository = providers.Singleton(PassageRepository, mongodb_client=db_client, configuration=config)
    discussion_repository = providers.Singleton(DiscussionRepository, mongodb_client=db_client, configuration=config)
    llm_repository = providers.Singleton(LlmRepository, openai_client=openai_client, anthropic_client=anthropic_client)

    llm_compeletion_service = providers.Singleton(
        LlmCompletionService, llm_repository=llm_repository, configuration=config
    )

    passage_recommendation_service = providers.Singleton(PassageRecommendationService, passage_repository)
