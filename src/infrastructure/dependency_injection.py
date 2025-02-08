from domain.interfaces import AbstractServiceProvider
from .configuration import add_configuration
from .data import add_data_services, cleanup_data_services


def add_infrastructure(service_provider: AbstractServiceProvider) -> None:
    config = add_configuration(service_provider)
    add_data_services(service_provider, config)


def cleanup_infrastucture(service_provider: AbstractServiceProvider) -> None:
    cleanup_data_services(service_provider)