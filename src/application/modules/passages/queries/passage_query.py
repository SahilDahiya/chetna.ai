from dependency_injector.wiring import Provide, inject

from src.domain.interfaces import AbstractPassageRepository
from src.infrastructure.containers import Container


@inject
def passage_query(
    book_name: str,
    chapter_no: str,
    passage_no: str,
    passage_repository: AbstractPassageRepository = Provide[Container.passage_repository]
):
    return passage_repository.get_passage(book_name, 'chapter_1', '19')