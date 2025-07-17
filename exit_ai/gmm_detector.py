# exit_ai

from sklearn.mixture import GaussianMixture
import numpy as np

class GMMDetector:
    def __init__(self, n_components=3):
        self.model = GaussianMixture(n_components=n_components)

    def train(self, X):
        self.model.fit(X)

    def detect(self, X):
        probs = self.model.score_samples(X)
        return np.where(probs < -15, 1, 0)
