from abc import ABC, abstractmethod

from src.domain.models.passages import Passage


class AbstractPassageToSvgService(ABC):
    @abstractmethod
    def convert(self, passage: Passage) -> str:
        pass
