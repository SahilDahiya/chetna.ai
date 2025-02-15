from abc import ABC, abstractmethod

from src.domain.models.llm import LlmType


class AbstractLlmRepository(ABC):
    @abstractmethod
    def llm(self, llm_type: LlmType):
        pass
