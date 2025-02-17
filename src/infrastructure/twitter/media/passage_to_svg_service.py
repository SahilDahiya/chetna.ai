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
            tool_choice={'type': 'tool', 'name': 'generate_svg'},
        )

        svg_code = response.content[0].input['svg_code']

        # Extract SVG code from the response
        svg_refactor = self.should_adjust_size_of_svg(svg_code, passage.text)

        if not svg_refactor:
            return self.adjust_size_of_svg(svg_code, passage.text)
        else:
            return svg_code

    def should_adjust_size_of_svg(self, svg_content: str, passage_text: str):
        messages = [{'role': 'user', 'content': f'Passage: {passage_text}, SVG code: {svg_content}'}]

        tools = [
            {
                'name': 'svg_validation',
                'description': 'Is SVG code need refactor or not to correctly display of text in svg image.',  # noqa: E501
                'input_schema': {
                    'type': 'object',
                    'properties': {
                        'is_svg_correct': {
                            'type': 'boolean',
                            'description': 'true or false, whether the SVG shows the passage correctly ot not!',
                        }
                    },  # noqa: E501
                    'required': ['is_svg_correct'],
                },
            },
        ]

        response = self.__anthropic_client.messages.create(
            model='claude-3-5-sonnet-20241022',
            system='You are a tool that decides whether to refactors SVG code to have passage displayed in reasonalble width and height. You only output True or False.',  # noqa: E501
            messages=messages,
            tools=tools,
            max_tokens=64,
            tool_choice={'type': 'tool', 'name': 'svg_validation'},
        )

        return response.content[0].input['is_svg_correct']

    def adjust_size_of_svg(self, svg_content: str, passage_text):
        messages = [{'role': 'user', 'content': f'Passage: {passage_text}, SVG code: {svg_content}'}]

        tools = [
            {
                'name': 'adjust_size_of_svg_image',
                'description': 'Refactor a given svg image of a passage, only adjust height of the image so that there is not too much blank space. Make sure the whole passage is displayed comfortably.',  # noqa: E501
                'input_schema': {
                    'type': 'object',
                    'properties': {
                        'refactor_svg_code': {
                            'type': 'string',
                            'description': 'The generated refactored SVG code with adjusted height.',
                        }
                    },  # noqa: E501
                    'required': ['refactor_svg_code'],
                },
            },
        ]

        response = self.__anthropic_client.messages.create(
            model='claude-3-5-sonnet-20241022',
            system='You are a tool that refactors SVG code to have passage displayed in reasonalble height. You only output valid SVG code.',  # noqa: E501
            messages=messages,
            tools=tools,
            max_tokens=4096,
            tool_choice={'type': 'tool', 'name': 'adjust_size_of_svg_image'},
        )

        return response.content[0].input['refactor_svg_code']
