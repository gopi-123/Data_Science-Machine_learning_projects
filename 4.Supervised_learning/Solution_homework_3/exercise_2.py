import pandas as ps
#import cPickle as pc
import pickle as pc
from backend import HousingSolution

data = ps.read_csv("housing.csv", sep = ',')
XY = data.as_matrix()

for c in [None, 0.01, 1.0, 100.0]:
    print(" ")
    print("<<< Regularization " + str(c) + " >>>")
    obj = HousingSolution(C = c)
    obj.process(XY)

    # print the data for comparison
    for c, v in zip( data.columns.values[:-1], obj.model.p[:-1]):
        print(c,v)
