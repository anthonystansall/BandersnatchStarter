from pandas import DataFrame
from sklearn.linear_model import LogisticRegression
from datetime import datetime
import joblib

class Machine:

    def __init__(self, df: DataFrame):
        self.name = "Logistic Regression Model"
        #target = df["Rarity"]
        #features = df.drop(columns=['Name', 'Type', 'Damage', 'Timestamp', 'Rarity'])
        #features = df.drop(columns=['Rarity'])
        #self.model = LogisticRegression()
        #self.model.fit(features, target)
        self.init_time = datetime.now()

    def __call__(self, pred_basis: DataFrame):
        prediction = self.model.predict(pred_basis)[0]
        confidence = self.model.predict_proba(pred_basis).max(axis=1)[0]
        return prediction, confidence

    def save(self, filepath):
        joblib.dump(self.model, filepath)

    @staticmethod
    def open(filepath):
        model = joblib.load(filepath)
        return model

    def info(self):
        model_name = self.name
        return model_name
        
