from pymongo import MongoClient

from ....domain.models.configuration import Configuration


def mongodb_client(configuration: Configuration) -> None:
    return MongoClient(
        configuration.mongodb_connection_string,
        uuidRepresentation='standard',
        tz_aware=True,
    )
