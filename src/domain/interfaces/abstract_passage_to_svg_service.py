from abc import ABC, abstractmethod

from src.domain.models.passages import Passage


class AbstractPassageToSvgService(ABC):
    @abstractmethod
    def get_svg(self, passage: Passage) -> str:
        pass
