"""Container aplication module."""

import os
from galeo_lambda.factories import data_loader_selector
from galeo_lambda.data_processors import JsonDataProcessor

class Container:
    """Assamble all neccesary instances."""


    data_loader_cls = data_loader_selector(
        storage_name=os.environ.get("STORAGE_NAME", "DOCUMENT_DB")
    )  # chose data loadaer using an env variable.

    # build the data loader using virtual env
    data_loader = data_loader_cls(
        host=os.environ.get("MONGO_HOST", "mongodb"),
        port=os.environ.get("MONGO_PORT", "27017"),
        username=os.environ.get("MONGO_USER", "user"),
        password=os.environ.get("MONGO_PASSWORD", "password"),
        database_name=os.environ.get("MONGO_DATABASE_NAME", "galeo"),
        collection_name=os.environ.get("MONGO_COLLECTION_NAME", "temperature")
    )  # type: ignore
    data_processor = JsonDataProcessor()  # Default data_processor

container = Container()
