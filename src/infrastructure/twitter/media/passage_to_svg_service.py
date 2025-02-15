from anthropic import Client as AnthropicClient

from src.domain.interfaces import AbstractPassageToSvgService
from src.domain.models.passages import Passage
from src.domain.prompts import PASSAGE_TO_SVG_PROMPT


class PassageToSvgService(AbstractPassageToSvgService):
    def __init__(self, anthropic_client: AnthropicClient):
        self.__anthropic_client = anthropic_client

    def convert(self, passage: Passage):
        messages = [
            {
                'role': 'user',
                'content': PASSAGE_TO_SVG_PROMPT.format(
                    passage=passage.text,
                    chapter_name=passage.chapter_name,
                    passage_no=passage.passage_no,
                    book_name=passage.book_name,
                ),
            }
        ]

        tools = [
            {
                'name': 'generate_svg',
                'description': 'Converts a text passage into an SVG with semantic highlighting for philosophical concepts, arguments, metaphors, paradoxes, lists, conclusions, and philosophical statements',  # noqa: E501
                'input_schema': {
                    'type': 'object',
                    'properties': {'svg_code': {'type': 'string', 'description': 'The generated SVG code'}},
                    'required': ['svg_code'],
                },
            },
        ]

        response = self.__anthropic_client.messages.create(
            model='claude-3-5-sonnet-20241022',
            system='You are a tool that converts text passages into SVG code with semantic highlighting. You only output valid SVG code.',  # noqa: E501
            messages=messages,
            tools=tools,
            max_tokens=4096,
        )

        # Extract SVG code from the response
        return response.content[1].input['svg_code']
    
    
