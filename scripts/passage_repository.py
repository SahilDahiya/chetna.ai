from pymongo import MongoClient


class PassageRepository():
    def __init__(self, mongodb_client: MongoClient, configuration: dict):
        self.__collection = mongodb_client[configuration['passage_collection_name']]

    def get_passage(self, book_name:str, chapter_no:str, passage_no: str):
        return self.__collection.find_one({"book_name": book_name, "chapter_no": chapter_no, "passage_no": passage_no})
    
    def get_book_passages(self, book_name:str, chapter_no:str):
        return self.__collection.find({"book_name": book_name, "chapter_no": chapter_no})