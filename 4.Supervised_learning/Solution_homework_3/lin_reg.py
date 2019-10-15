from sklearn.metrics import r2_score
from scipy.optimize import minimize
import numpy as np


class LinReg():
    """
    This class trains linear model with intercept (bias)
    """
    def __init__(self, C = None):
        self.p = None # parameters field of model
        self.C = C

    def predict(self, X):
        if self.p is None:
            raise ("Please train the model first!")

        return self._predict(X, self.p)

    def _predict(self, X, p):
        # this is used for optimization of objective
        # returns a vector where i-th elemnt corresponds to
        # the output of the model with i-th input row

        return np.dot(X, p[:-1]) + p[-1]

    def fit(self, X,Y):
        # objective: minimize squared deviation
        def obj(p):
            Yp = self._predict(X, p)
            loss = np.mean((Yp -Y) ** 2)

            # check if regularization is used
            if self.C is None:
                return loss

            return loss +  (self.C * np.sum( np.abs(p) ))

        # this does minimizatoin of the objective w.r.t. parameters
        # using gradient descent (most of machine learning algos
        # use gradient descent internally)
        p0 = np.zeros(X.shape[1] + 1)
        sol = minimize(obj, p0, method="L-BFGS-B", tol=1e-6)
        self.p = sol.x

    def score(self, Xv, Yv):
        Yp = self.predict(Xv)
        return r2_score(Yv, Yp)