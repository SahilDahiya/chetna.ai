from ....domain.interfaces import AbstractServiceProvider

from .passage_repository import PassageRepository


def add_passage_repository(service_provider: AbstractServiceProvider) -> None:
    service_provider.add_singleton_service('passage_repository', PassageRepository)