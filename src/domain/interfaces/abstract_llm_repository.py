from abc import abstractmethod, ABC


class AbstractLlmRepository(ABC):
    @abstractmethod
    def get_llm_client(self, llm_id: str) -> Llm:
        pass
