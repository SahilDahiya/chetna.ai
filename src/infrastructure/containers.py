from dependency_injector import containers, providers

from src.domain.models.configuration import Configuration

from .data import add_mongodb_client, PassageRepository
from .llm import LlmCompletionService, add_openai_client


class Container(containers.DeclarativeContainer):
    config = providers.Singleton(
        Configuration,
        _env_file=".env",
        _env_file_encoding="utf-8"
    )

    db_client = providers.Singleton(
        add_mongodb_client,
        configuration=config
    )

    openai_client = providers.Singleton(add_openai_client, configuration=config)

    passage_repository = providers.Singleton(
        PassageRepository,
        mongodb_client=db_client,
        configuration=config
    )

    llm_compeletion_service = providers.Singleton(
        LlmCompletionService,
        openai_client= openai_client,
        configuration=config
    )