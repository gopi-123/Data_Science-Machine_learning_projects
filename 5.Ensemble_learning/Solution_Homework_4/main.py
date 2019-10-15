# main.py 

import pandas as pd
from sklearn.model_selection  import train_test_split

# read heart dataset
data     = pd.read_csv('heart.csv')

# split data into features and label
X = data.iloc[:,:-1]
y = data.iloc[:,-1]

# split X (features) and y (label) into training, validation, and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=10)



# test implementation (not required by exercise)
#from ensemble import BaggingClassifier_

from Ensemble_solution import BaggingClassifier_

clf = BaggingClassifier_(n_estimators=4)
clf.fit(X_train, y_train)
clf.predict(X_test)
print("\n Bagging Classifier prediction \n",clf.predict(X_test))
