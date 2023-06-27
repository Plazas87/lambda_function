import os
from pymongo import MongoClient

def main():
    """Initilize mongo database."""
    client = MongoClient(
        host="localhost",
        port=27017,
        username=os.environ.get("MONGO_USER", "user"),
        password=os.environ.get("MONGO_PASSWORD", "password")
    )

    db = client.galeo
    temperature_collection = db["temperature"]
    temperature_collection.insert_one(
        {"temperature": "0"}
    )

if __name__ == "__main__":
    main()
