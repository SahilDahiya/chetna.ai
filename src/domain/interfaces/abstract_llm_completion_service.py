from abc import ABC, abstractmethod


class AbstractLlmCompletionService(ABC):
    @abstractmethod
    def complete(self, messages: list[dict[str, str]]) -> list[str]:
        pass