"""Data loaders module.

This module gather all the implementations for posible 
stogares. 

This time there will be only two posible implementations: 
    - DynamoDB
    - DocumentDB

"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Dict, Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class StorageType(Enum):
    """Storage types"""
    DYNAMO_DB = 0
    DOCUMENT_DB = 1


class DataLoader(ABC, Generic[K, V]):
    """DataLoader Interface."""

    @abstractmethod
    def load(self, data: Dict[K, V]) -> None:
        """Save the data into the storage.""" 


class DynamoDBDataLoader(DataLoader[str, Any]):
    """DynamoDB data loader."""
    
    def load(self, data: Dict[str, Any]) -> None:
        """Save the data into the storage."""
        ...

    
class DocumentDBDataLoader(DataLoader[str, Any]):
    """DocumentDB data loader."""
    
    def load(self, data: Dict[str, Any]) -> None:
        """Save the data into the storage."""
        ...