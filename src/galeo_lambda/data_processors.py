"""Data Processors module."""


from abc import ABC, abstractmethod
import time
from typing import Any, Dict, Generic, List, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class DataProcessor(ABC, Generic[K, V]):
    """DataProcessor Interface."""

    @abstractmethod
    def process(self, data: List[Dict[K, V]]) -> List[Dict[K, V]]:
        """Process the data.""" 


class JsonDataProcessor(DataProcessor[str, Any]):
    """Json format data processor."""

    def process(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Process the data."""
        # This time there won't be a data process at all just simulate it with a
        #  blocking time.sleep(1) call and return the data as received.
        time.sleep(1)

        return data