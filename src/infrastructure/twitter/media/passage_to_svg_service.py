from domain.interfaces import AbstractPassageRepository, AbstractLlmCompletionService


class PassageToSvgService:
    def __init__(
        self, passage_repository: AbstractPassageRepository, llm_completion_service: AbstractLlmCompletionService
    ):
        self.__passage_repository = passage_repository

    def convert(self, passage_id: str) -> str:
        passage = self.__passage_repository.get_passage_by_id(passage_id)
