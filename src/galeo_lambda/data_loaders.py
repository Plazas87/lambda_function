"""Data loaders module.

This module gather all the implementations for posible 
stogares. 

This time there will be only two posible implementations: 
    - DynamoDB
    - DocumentDB

"""
import os
import logging
from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Dict, Generic, List, Optional, TypeVar
from pymongo import MongoClient

K = TypeVar("K")
V = TypeVar("V")

logger = logging.getLogger(__name__)


class StorageType(Enum):
    """Storage types"""
    DYNAMO_DB = 0
    DOCUMENT_DB = 1


class DataLoader(ABC, Generic[K, V]):
    """DataLoader Interface."""

    @abstractmethod
    def load(self, obj: Dict[K, V]) -> None:
        """Save the data into the storage.""" 


class DynamoDBDataLoader(DataLoader[str, Any]):
    """DynamoDB data loader."""
    
    def load(self, obj: Dict[str, Any]) -> None:
        """Save the data into the storage."""
        raise NotImplementedError

    
class DocumentDBDataLoader(DataLoader[str, Any]):
    """DocumentDB data loader.
    
    This class is meant to be used as a context manager to handle connection cicle.
    """
    _client: Optional[MongoClient]
    _host: str
    _port: str
    _username: str
    _password: str
    _database_name: str
    _collection_name: str
    _db: Any
    _collection: Any

    def __init__(
        self,
        host: str,
        port: str,
        username: str,
        password: str,
        database_name: str,
        collection_name: str
    ) -> None:
        self._client = None
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._database_name = database_name
        self._collection_name = collection_name
    
    def load(self, obj: Dict[str, Any]) -> None:
        """Save the object into the database."""
        self._collection.insert_one(obj)

    def bulk_load(self, objs: List[Dict[str, Any]]) -> None:
        """
        Insert many documents at once. If there are any fails during this process,
        only Documents with errors wont be inserted.
        """
        try:
            self._collection.insert_many(objs, ordered=False)

        except Exception as err:
            logger.error(
                "Error while inserting messages using a bulk operation: '%s'. ", str(err)
            )

    def __enter__(self) -> None:
        """Stablish a new connection with the database."""
        print(self._host)
        print(int(self._port))
        print(self._username)
        print(self._password)

        self._client = MongoClient(
            host=self._host,
            port=int(self._port),
            username=self._username,
            password=self._password
        )
        self._db = self._client[self._database_name]
        self._collection = self._db[self._collection_name]

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Close the connection.

        Returns:
            None
        """
        assert self._client
        self._client.close()
        self._db = None
        self._collection = None

    # def _build_connection_string(self) -> str:

    #     if self._as_local:
    #         host = os.environ.get("DDB_USER")
    #         port = os.environ.get("DDB_PORT")
    #         connection_string = f"mongodb://{host}:{port}/"

    #     else:
    #         user = os.environ.get("DDB_USER", self._connection_conf.get("user"))
    #         password = os.environ.get("DDB_PASSWORD", self._connection_conf.get("password"))
    #         host = os.environ.get("DDB_HOST", self._connection_conf.get("host"))

    #         connection_string = f"mongodb://{user}:{password}@{host}"

    #     return connection_string
