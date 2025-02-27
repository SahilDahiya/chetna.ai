from dependency_injector.wiring import Provide, inject

from src.domain.interfaces import AbstractPassageRepository, AbstractPassageToSvgService
from src.infrastructure.containers import Container


@inject
def passage_to_svg_query(
    book_name: str,
    passage_no: str,
    passage_repository: AbstractPassageRepository = Provide[Container.passage_repository],
    passage_to_svg_service: AbstractPassageToSvgService = Provide[Container.passage_to_svg_service],
):
    passage = passage_repository.get_passage(book_name, chapter_name='BOOK FIRST', passage_no=passage_no)
    svg_content = passage_to_svg_service.convert(passage)

    with open(f'{passage.passage_id}.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
