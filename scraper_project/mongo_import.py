"""
This module loads quotes and author data from JSON files and imports them into
a MongoDB database.
"""

import json
import os
from typing import List, Dict

from pymongo import MongoClient
from dotenv import load_dotenv


def load_json(filename: str) -> List[Dict]:
    """Load data from a JSON file."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)


def get_mongo_client() -> MongoClient:
    """Create and return a MongoDB client using URI from .env."""
    load_dotenv()
    uri = os.getenv("MONGODB_URI")
    if not uri:
        raise ValueError("MONGODB_URI not set in .env")
    return MongoClient(uri)


def import_collection(
    client: MongoClient, db_name: str, collection_name: str, data: List[Dict]
) -> None:
    """Import data into the specified MongoDB collection."""
    db = client[db_name]
    collection = db[collection_name]
    collection.delete_many({})
    if data:
        collection.insert_many(data)


def main():
    """Main entry point for importing data into MongoDB."""
    client = get_mongo_client()
    quotes = load_json("quotes.json")
    authors = load_json("authors.json")
    import_collection(client, "quotes_db", "quotes", quotes)
    import_collection(client, "quotes_db", "authors", authors)
    print("Data imported successfully.")


if __name__ == "__main__":
    main()
