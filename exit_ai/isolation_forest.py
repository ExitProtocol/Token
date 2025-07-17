# exit_ai

from sklearn.ensemble import IsolationForest

class IsolationForestDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.02)

    def train(self, X):
        self.model.fit(X)

    def detect(self, X):
        return self.model.predict(X)
