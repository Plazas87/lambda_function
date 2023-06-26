"""Factories module."""



from typing import Any, Dict, Type
from galeo_lambda.data_loaders import DataLoader, DocumentDBDataLoader, DynamoDBDataLoader, StorageType

data_loaders_class_map: Dict[StorageType, Type[DataLoader[str, Any]]] = {
    StorageType.DYNAMO_DB: DynamoDBDataLoader,
    StorageType.DOCUMENT_DB: DocumentDBDataLoader
}

def data_loader_factory(storage_name: str) -> DataLoader:
    """Build and return a dataloader instance."""

    try:
        data_loader_cls = data_loaders_class_map[StorageType[storage_name]]

    except KeyError as err:
        raise Exception(f"Data loader '{storage_name}' not supported: '{str(err)}'")

    return data_loader_cls()
