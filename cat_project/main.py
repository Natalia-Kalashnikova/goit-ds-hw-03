"""This module provides CRUD operations for managing cat documents in MongoDB."""

import os
from typing import List, Optional

from pymongo import MongoClient
from pymongo.errors import PyMongoError
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME", "cat_db")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "cats")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]


def create_cat(name: str, age: int, features: List[str]) -> str:
    """Insert a new cat document into the collection."""
    try:
        result = collection.insert_one({"name": name, "age": age, "features": features})
        return str(result.inserted_id)
    except PyMongoError as e:
        print(f"Error inserting cat: {e}")
        return ""


def get_all_cats() -> List[dict]:
    """Return all cat documents from the collection."""
    try:
        return list(collection.find())
    except PyMongoError as e:
        print(f"Error fetching cats: {e}")
        return []


def get_cat_by_name(name: str) -> Optional[dict]:
    """Return a cat document by name."""
    try:
        return collection.find_one({"name": name})
    except PyMongoError as e:
        print(f"Error fetching cat: {e}")
        return None


def update_cat_age(name: str, new_age: int) -> bool:
    """Update the age of a cat by name."""
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        return result.modified_count > 0
    except PyMongoError as e:
        print(f"Error updating age: {e}")
        return False


def add_feature_to_cat(name: str, feature: str) -> bool:
    """Add a new feature to a cat's features list by name."""
    try:
        result = collection.update_one(
            {"name": name}, {"$addToSet": {"features": feature}}
        )
        return result.modified_count > 0
    except PyMongoError as e:
        print(f"Error adding feature: {e}")
        return False


def delete_cat_by_name(name: str) -> bool:
    """Delete a cat document by name."""
    try:
        result = collection.delete_one({"name": name})
        return result.deleted_count > 0
    except PyMongoError as e:
        print(f"Error deleting cat: {e}")
        return False


def delete_all_cats() -> int:
    """Delete all cat documents from the collection."""
    try:
        result = collection.delete_many({})
        return result.deleted_count
    except PyMongoError as e:
        print(f"Error deleting all cats: {e}")
        return 0


if __name__ == "__main__":
    # Example of the function in operation
    # if not get_all_cats():
    #     print("Collection is empty. Adding a cat...")
    #     create_cat("barsik", 3, ["ходит в капці", "дає себе гладити", "рудий"])
    print("All cats:", get_all_cats())
    # print("Cat by name:", get_cat_by_name("barsik"))
    # print("Update age:", update_cat_age("barsik", 5))
    # print("Add feature:", add_feature_to_cat("barsik", "любить спати на сонці"))
    # print("Delete cat:", delete_cat_by_name("barsik"))
    # print("Delete all cats:", delete_all_cats())
