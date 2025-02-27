from anthropic import Client as AnthropicClient

from src.domain.interfaces import AbstractPassageToSvgService
from src.domain.models.passages import Passage
from src.domain.prompts import PASSAGE_TO_SVG_PROMPT


class PassageToSvgService(AbstractPassageToSvgService):
    def __init__(self, anthropic_client: AnthropicClient):
        self.__anthropic_client = anthropic_client

    def convert(self, passage: Passage) -> str:
        """Convert a passage to SVG with semantic highlighting.

        Args:
            passage: The passage object containing text and metadata

        Returns:
            str: The finalized SVG code
        """
        # Create initial SVG
        svg_code = self.__generate_initial_svg(passage)

        # Check if SVG needs adjustment and adjust if necessary
        if not self.__should_adjust_size_of_svg(svg_code, passage.text):
            return self.__adjust_size_of_svg(svg_code, passage.text)
        return svg_code

    def __generate_initial_svg(self, passage: Passage) -> str:
        """Generate the initial SVG from the passage text."""
        messages = [
            {
                'role': 'user',
                'content': PASSAGE_TO_SVG_PROMPT.format(
                    passage=passage.text,
                    chapter_name=passage.chapter_name or '',  # Handle None values
                    passage_no=passage.passage_no or '',
                    book_name=passage.book_name or '',
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

        try:
            response = self.__anthropic_client.messages.create(
                model='claude-3-5-sonnet-20241022',
                system='You are a tool that converts text passages into SVG code with semantic highlighting. You only output valid SVG code.',  # noqa: E501
                messages=messages,
                tools=tools,
                max_tokens=4096,
                tool_choice={'type': 'tool', 'name': 'generate_svg'},
            )
            return response.content[0].input['svg_code']
        except Exception as e:
            # Log the error and raise or handle appropriately
            raise Exception(f'Error generating SVG: {str(e)}')

    def __should_adjust_size_of_svg(self, svg_content: str, passage_text: str) -> bool:
        """Determine if the SVG needs size adjustment."""
        # More efficient content structure - we don't need to send the full passage text twice
        svg_sample = svg_content[:1000] if len(svg_content) > 1000 else svg_content
        messages = [
            {'role': 'user', 'content': f'Passage length: {len(passage_text)} chars. SVG preview: {svg_sample}'}
        ]

        tools = [
            {
                'name': 'svg_validation',
                'description': 'Determine if SVG code needs refactoring to correctly display text.',
                'input_schema': {
                    'type': 'object',
                    'properties': {
                        'is_svg_correct': {
                            'type': 'boolean',
                            'description': 'Whether the SVG shows the passage correctly (true) or needs adjustment (false)',  # noqa: E501
                        }
                    },
                    'required': ['is_svg_correct'],
                },
            },
        ]

        try:
            response = self.__anthropic_client.messages.create(
                model='claude-3-5-sonnet-20241022',
                system='You are a tool that determines if SVG code needs adjustment to display passages with appropriate dimensions. Respond with true if correct, false if needs adjustment.',  # noqa: E501
                messages=messages,
                tools=tools,
                max_tokens=64,
                tool_choice={'type': 'tool', 'name': 'svg_validation'},
            )
            return response.content[0].input['is_svg_correct']
        except Exception:
            # If validation fails, assume adjustment is needed
            return False

    def __adjust_size_of_svg(self, svg_content: str, passage_text: str) -> str:
        """Adjust the SVG size to better fit the passage."""
        messages = [
            {
                'role': 'user',
                'content': [
                    {
                        'type': 'text',
                        'text': passage_text,
                    },
                    {'type': 'image', 'source': {'type': 'svg', 'data': svg_content}},
                ],
            }
        ]

        tools = [
            {
                'name': 'adjust_size_of_svg_image',
                'description': 'Refactor SVG to adjust height removing excess blank space while ensuring the passage is displayed comfortably.',  # noqa: E501
                'input_schema': {
                    'type': 'object',
                    'properties': {
                        'refactor_svg_code': {
                            'type': 'string',
                            'description': 'The refactored SVG code with adjusted height.',
                        }
                    },
                    'required': ['refactor_svg_code'],
                },
            },
        ]

        try:
            response = self.__anthropic_client.messages.create(
                model='claude-3-5-sonnet-20241022',
                system='You are a tool that refactors SVG code to display passages with appropriate height. Maintain all semantic highlighting and styling. Only output valid SVG code.',  # noqa: E501
                messages=messages,
                tools=tools,
                max_tokens=4096,
                tool_choice={'type': 'tool', 'name': 'adjust_size_of_svg_image'},
            )
            return response.content[0].input['refactor_svg_code']
        except Exception:
            # If adjustment fails, return the original SVG
            return svg_content
