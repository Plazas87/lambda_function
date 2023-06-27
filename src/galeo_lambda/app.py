# pylint: disable=all
import json
import logging
from typing import Any, Dict
from http import HTTPStatus

from galeo_lambda.container import container

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event: Dict[str, Any], context: Any):
    """Lambda function that process incoming data."""
    logger.info("Request to process data started.")
    logger.info("Event: %s", event)
    logger.info("Event type: %s", type(event))

    data_processor = container.data_processor
    data_loader = container.data_loader

    response = {
        "isBase64Encoded": False,
        "statusCode": HTTPStatus.OK.value,
        "body": "",
        "headers": {"content-type": "application/json"},
    }

    logger.info("Request validation started.")
    
    try:
        body = event["body"]
        logger.info("Body: %s", type(body))
        data = body.get("data")
    
    except Exception:
        response.update(
            {
                "statusCode": HTTPStatus.BAD_REQUEST.value,
                "body": json.dumps(
                    {
                        "error": "Bad request syntax or unsupported method",
                    }
                ),
            }
        )
        return response

    logger.info("Request validation completed.")
    print(data)
    
    # process the data
    logger.info("Start processing the data...")
    try:
        print(data)
        processed_data = data_processor.process(data=data)

    except Exception as err:
        response.update(
            {
                "statusCode": HTTPStatus.INTERNAL_SERVER_ERROR.value,
                "body": json.dumps({"error": str(err)})
            }
        )
        return response

    logger.info("Data processing completed!")
    
    # load the data
    logger.info("Start processing saving the data...")
    try:
        with data_loader:
            for obj in processed_data:
                data_loader.load(obj=obj)

    except Exception as err:
        response.update(
            {
                "statusCode": HTTPStatus.INTERNAL_SERVER_ERROR.value, 
                "body": json.dumps({"error": str(err)})
            }
        )
        return response

    logger.info("Data has been successfully processed and saved!")

    response.update(
        {
            "body": "Data has been successfully processed and saved."
        }
    )
    return response
