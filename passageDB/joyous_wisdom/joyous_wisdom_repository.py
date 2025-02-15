from typing import Literal

from pydantic import BaseModel, field_validator


class JoyousWisdomPassage(BaseModel):
    book_name: str = 'The Joyous Wisdom'
    author: str = 'Friedrich Nietzsche'
    chapter_name: Literal['BOOK FIRST', 'BOOK SECOND', 'BOOK THIRD', 'BOOK FIFTH']
    passage_no: str
    text: str
    passage_id: str | None = None

    def model_post_init(self, __context) -> None:
        self.passage_id = f'{self.book_name.lower().replace(" ", "_")}#{self.chapter_name.lower().replace(" ", "_")}#{self.passage_no}'  # noqa: E501

    @field_validator('passage_no')
    def validate_passages(cls, v, values):
        ranges = {'BOOK FIRST': (1, 58), 'BOOK SECOND': (58, 108), 'BOOK THIRD': (108, 276), 'BOOK FIFTH': (276, 384)}

        passage_num = int(v)
        chapter = values.get('chapter_name')

        if chapter not in ranges:
            raise ValueError(f'Invalid chapter name: {chapter}')

        start, end = ranges[chapter]
        if not (start <= passage_num < end):
            raise ValueError(
                f'Passage number {passage_num} is out of range for {chapter}. Valid range is [{start}, {end})'
            )

        return v


class JoyousWisdomRepository:
    def __init__(self, mongodb_client, db_name):
        self.db = mongodb_client[db_name]
        self.collection = self.db['Books']

    def save(self, jw_passage: JoyousWisdomPassage):
        self.collection.insert_one(jw_passage.model_dump())


if __name__ == '__main__':
    passage = JoyousWisdomPassage(chapter_name='BOOK FIRST', passage_no='1', text='The text of the passage')
