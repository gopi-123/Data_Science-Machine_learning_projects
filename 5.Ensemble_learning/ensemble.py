import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.utils import resample
from sklearn.exceptions import NotFittedError


class BaggingClassifier_:
    def __init__(self,n_estimators=10, max_depth=None, max_features=None, random_state=10):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.max_features = max_features
        self.random_state = random_state
        self.estimators = []

    def bootstrap(self, X, y):
        X_re, y_re = resample(X,y, random_state=self.random_state)
        return X_re, y_re


    def fit(self, X, y):
        pass

    def predict(self, X):
        pass