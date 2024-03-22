"""Module for interacting with the MongoDB database.

This module contains the Database class that includes operations such as
creating a set amount of monsters to add to the database, counting the number
of documents in the database, and converting the documents to a Pandas
DataFrame or HTML table.
"""
from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    """Class to interact with the MongoDB database.

    This class provides methods to fill the database with random monster data,
    delete all documents in the collection, count the documents, and convert
    the documents to a Pandas DataFrame or HTML table.
    """

    load_dotenv()
    database = MongoClient(getenv("DB_URL"),
                           tls=True,
                           tlsCAFile=where())["Bandersnatch_DB"]

    def __init__(self, collection):
        self.collection = self.database[collection]

    def seed(self, amount):
        """Fills the database with random monster data.

        Parameters:
            amount: The number of random monsters to insert.
        """
        monsters = [Monster().to_dict() for _ in range(amount)]
        self.collection.insert_many(monsters)

    def reset(self):
        """Deletes all the documents in the colletion."""
        self.collection.delete_many({})

    def count(self) -> int:
        """Counts the number of documents in the collection.

        Returns:
            The number of documents in the collection.
        """
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        """Converts all documents in the collection to a Pandas DataFrame.

        Returns:
            A Pandas DataFrame containing the documents or None if the
            collection is empty.
        """
        if self.count() == 0:
            return None
        documents = list(self.collection.find({}))
        df = DataFrame(documents)
        df.drop('_id', axis=1, inplace=True)
        return df

    def html_table(self) -> str:
        """Converts all documents in the collection to an HTML table.

        Returns:
            A string containing an HTML table of the documents or None if the
            collection is empty."""
        df = self.dataframe()
        if df is None:
            return None
        html_table = df.to_html()
        return html_table


if __name__ == "__main__":
    db = Database("monsters")
    db.seed(1000)
    # df = db.dataframe()
    # print(df.head())
    # html_df = db.html_table()
    # print(type(html_df))
    # print(html_df)
    # db.reset()
