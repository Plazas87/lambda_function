"""Data Processors module."""


from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class DataProcessor(ABC, Generic[K, V]):
    """DataProcessor Interface."""

    @abstractmethod
    def process(self, data: Dict[K, V]) -> Dict[K, V]:
        """Process the data.""" 


class JsonDataProcessor(DataProcessor[str, Any]):
    """Json format data processor."""

    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Process the data."""
        return {} 