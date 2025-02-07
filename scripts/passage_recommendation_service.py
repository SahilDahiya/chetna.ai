import random


class PassageRecommendationService:
    def __init__(self, passage_repository):
        self.passage_repository = passage_repository

    def recommend(self, book_name: str):
        chapter_no = '1'
        passages = self.passage_repository.get_book_passages(book_name, chapter_no)
        passage = random.choices(passages, k=1)
        
        while len(passage["text_english"]) < 256:
            passage = random.choices(passages, k=1)
        return passage
