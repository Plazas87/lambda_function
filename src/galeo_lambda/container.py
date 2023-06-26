"""Container aplication module."""

import os
from galeo_lambda.factories import data_loader_factory
from galeo_lambda.data_processors import JsonDataProcessor


class Container:
    """Assamble all neccesary instances."""

    data_loader = data_loader_factory(
        storage_name=os.environ.get("STORAGE_NAME", "DYNAMO_DB")
    )  # chose data loadaer using an env variable.
    data_processor = JsonDataProcessor()  # Default data_processor


container = Container()
