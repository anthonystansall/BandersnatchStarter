"""Module to create and load prediction models."""
from datetime import datetime

import joblib
from pandas import DataFrame
from sklearn.linear_model import LogisticRegression


class Machine:
    """Class containing prediction model and related info."""

    def __init__(self, df: DataFrame):
        """Initializes LR model with training data."""
        self.name = "Logistic Regression Model"
        target = df["Rarity"]
        features = df.drop(columns=['Rarity'])
        self.model = LogisticRegression()
        self.model.fit(features, target)
        self.init_time = datetime.now()

    def __call__(self, pred_basis: DataFrame):
        """Makes a prediction based on input features."""
        prediction = self.model.predict(pred_basis)[0]
        confidence = self.model.predict_proba(pred_basis).max(axis=1)[0]
        return prediction, confidence

    def save(self, filepath):
        """Saves the current model."""
        joblib.dump(self, filepath)

    @staticmethod
    def open(filepath):
        """Loads a model from filepath."""
        machine = joblib.load(filepath)
        return machine

    def info(self):
        """Returns a string containing information about the model."""
        return (f"Base Model: {self.name}<br>Timestamp: "
                f"{self.init_time.strftime('%Y-%m-%d %I:%M:%S %p')}")
