from pandas import DataFrame
from sklearn.linear_model import LogisticRegression
from datetime import datetime
import joblib

class Machine:

    def __init__(self, df: DataFrame):
        self.name = "Logistic Regression Model"
        target = df["Rarity"]
        features = df.drop(columns=['Rarity'])
        self.model = LogisticRegression()
        self.model.fit(features, target)
        self.init_time = datetime.now()

    def __call__(self, pred_basis: DataFrame):
        prediction = self.model.predict(pred_basis)[0]
        confidence = self.model.predict_proba(pred_basis).max(axis=1)[0]
        return prediction, confidence

    def save(self, filepath):
        joblib.dump(self, filepath)

    @staticmethod
    def open(filepath):
        machine = joblib.load(filepath)
        return machine

    def info(self):
        return f"Base Model: {self.name}<br>TimeStamp: {self.init_time.strftime('%Y-%m-%d %I:%M:%S %p')}"
        
