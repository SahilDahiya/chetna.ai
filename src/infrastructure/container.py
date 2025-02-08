from dependency_injector import containers, providers

from src.domain.models.configuration import Configuration

from .data import mongodb_client
from .data.passage_repository import PassageRepository


class Container(containers.DeclarativeContainer):
    config = providers.Singleton(
        Configuration,
        _env_file=".env",
        _env_file_encoding="utf-8"
    )

    db_client = providers.Singleton(
        mongodb_client,
        configuration=config
    )

    passage_repository = providers.Singleton(
        PassageRepository,
        mongodb_client=db_client,
        configuration=config
    )