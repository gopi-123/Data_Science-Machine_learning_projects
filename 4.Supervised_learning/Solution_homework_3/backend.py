"""
This file contains classes needed for data preprocessing
"""

from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.linear_model import LinearRegression
from lin_reg import LinReg
from sklearn.neighbors import KNeighborsClassifier

class HousingSolution():

    def __init__(self, C = None):
        self.C = C

    def process(self, XY):
        """
        This creates all the data needed for preprocessing of the housing dataset

        :param XY: Contents of CSV file as a numpy array
        :return: None
        """

        # there is no need for one hot encoding

        # get input / output arrays
        X = XY[:,:-1]
        Y = XY[:,-1]

        # separate datasaet into training, testing, validation parts:
        # [ training: 60%               | validtn.: 20% | testing: 20% ]
        tr_ix = int(len(X) * 0.6)
        vl_ix = tr_ix + int(len(X) * 0.2)

        X, Xv, Xt = X[:tr_ix], X[tr_ix:vl_ix], X[vl_ix:]
        Y, Yv, Yt = Y[:tr_ix], Y[tr_ix:vl_ix], Y[vl_ix:]

        # perform data normalization
        sc = StandardScaler()
        sc.fit(X)

        X = sc.transform(X)
        Xv = sc.transform(Xv)
        Xt = sc.transform(Xt)

        # create and train predictive model
        model = LinReg(C = self.C)

        XXv = np.concatenate([X, Xv])
        YYv = np.concatenate([Y, Yv])

        model.fit(XXv, YYv)
        print("Test R^2:", model.score(Xt, Yt))
        self.model = model

