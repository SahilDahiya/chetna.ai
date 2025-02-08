from pymongo import MongoClient

from src.domain.models.configuration import Configuration


def mongodb_client(configuration: Configuration) -> MongoClient:
    return MongoClient(
        configuration.mongodb_connection_string,
        uuidRepresentation='standard',
        tz_aware=True,
    )
