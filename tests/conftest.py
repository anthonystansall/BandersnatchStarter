"""Module to create mock database fixture for unit tests."""

import pytest
from mongomock import MongoClient

from app import data


@pytest.fixture
def mock_db(monkeypatch):
    """Fixture to mock the MongoDB database."""
    mock_client = MongoClient()

    def mock_mongo_client(*args, **kwargs):
        return mock_client

    monkeypatch.setattr("pymongo.MongoClient", mock_mongo_client)

    db_instance = data.Database("test_collection")
    db_instance.collection.delete_many({})
    yield db_instance

    mock_client.drop_database("Bandersnatch_DB")
