import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.utils import resample
from sklearn.exceptions import NotFittedError
from scipy import stats

class BaggingClassifier_:
    def __init__(self,base_estimator=None,n_estimators=10, max_depth=None, max_features=None, random_state=10):
        self.base_estimator = base_estimator
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.max_features = max_features
        self.random_state = random_state
        self.estimators = []

    def bootstrap(self, X, y):
        X_re, y_re = resample(X,y, random_state=self.random_state)
        return X_re, y_re

    def create_estimators(self):
        if self.base_estimator:
            for i in range(self.n_estimators):
                    self.estimators.append(self.base_estimator)
        else:
            for i in range(self.n_estimators):
                    self.estimators.append(DecisionTreeClassifier(max_depth=self.max_depth,
                                                                  max_features=self.max_features,
                                                                  random_state=self.random_state))



    def fit(self, X, y):
        self.create_estimators()
        for i in range(self.n_estimators):
            X_b, y_b = self.bootstrap(X,y)
            self.estimators[i].fit(X_b, y_b)


    def predict(self, X, y=None):
        try:
            y_pred = [estimator.predict(X) for estimator in self.estimators]
            y_predx = np.array(y_pred)
            return np.mean(y_pred, axis=0)
        except NotFittedError as e:
            print(repr(e))









