from enum import Enum


class LlmType(Enum):
    OPENAI = 'openai'
    ANTHROPIC = 'anthropic'