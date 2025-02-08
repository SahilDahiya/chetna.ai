from pymongo import MongoClient

from ....domain.interfaces.abstract_service_provider import AbstractServiceProvider
from ....domain.models.configuration import Configuration


def add_mongodb_client(service_provider: AbstractServiceProvider, configuration: Configuration) -> None:
    mongodb_client = MongoClient(
        configuration.mongodb_connection_string,
        uuidRepresentation='standard',
        tz_aware=True,
    )

    service_provider.add_singleton_service('mongodb_client', mongodb_client)


def cleanup_mongodb_client(service_provider: AbstractServiceProvider) -> None:
    mongodb_client: MongoClient = service_provider.get_service('mongodb_client')
    mongodb_client.close()
