from ...domain.interfaces import AbstractServiceProvider
from ...domain.models.configuration import Configuration
from .mongodb_client import add_mongodb_client, cleanup_mongodb_client
from .passage_repository import add_passage_repository


def add_data_services(service_provider: AbstractServiceProvider, configuration: Configuration) -> None:
    add_mongodb_client(service_provider, configuration)
    add_passage_repository(service_provider)

def cleanup_data_services(service_provider: AbstractServiceProvider) -> None:
    cleanup_mongodb_client(service_provider)