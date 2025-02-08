from ...domain.interfaces import AbstractServiceProvider
from ...domain.models.configuration import Configuration


def add_configuration(service_provider: AbstractServiceProvider) -> Configuration:
    # noinspection PyArgumentList
    configuration = Configuration(__env_file='.env', _env_file_encoding='utf-8')

    service_provider.add_singleton_service('configuration', configuration)

    return configuration