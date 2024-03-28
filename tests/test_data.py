"""Module to test methods of the Database class in data.py.

This module utilizes pytest and mongomock to create a mock database environment
for testing the methods in the Database class. It uses a fixture to mock
the MongoDB client connections and tests the seed, reset, count, dataframe,
and html methods.
"""
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


def test_seed(mock_db):
    """Tests the seed method of the Database class."""
    mock_db.seed(5)
    assert mock_db.count() == 5


def test_reset(mock_db):
    """Tests the reset method of the Database class."""
    mock_db.seed(5)
    assert mock_db.count() == 5
    mock_db.reset()
    assert mock_db.count() == 0


def test_count(mock_db):
    """Tests the count method of the Database class."""
    mock_db.seed(3)
    assert mock_db.count() == 3


def test_dataframe(mock_db):
    """Tests the dataframe method of the Database class."""
    mock_db.seed(1)
    df = mock_db.dataframe()
    assert df is not None
    assert len(df) == 1


def test_html_table(mock_db):
    """Tests the html_table method of the Database class."""
    mock_db.seed(1)
    html_table = mock_db.html_table()
    assert html_table is not None
    assert "<table" in html_table
