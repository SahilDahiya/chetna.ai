from abc import ABC, abstractmethod
from typing import TypeVar

TService = TypeVar('TService')


class AbstractServiceProvider(ABC):
    @abstractmethod
    def get_service(self, service_name: str) -> TService:
        pass

    @abstractmethod
    def add_singleton_service(self, service_name: str, service: TService) -> None:
        pass

    @abstractmethod
    def add_transient_service(self, service_name: str, service: TService) -> None:
        pass