# Homework 4

Use the dataset provided to complete the exercise below. Submit completed files to
demonstrate your results. Please name your submission after your last name. Include your
Full-name, Matriculation number and email id in your submission file.

# Exercise 1 (1+1+2 points)
1. Correlation and Ensemble methods
Ensemble methods such as Bagging combine multiple weak learners to create a
strong learner. Examine the relation between correlation among weak learners and
their impact on the performance of the ensemble methods.
2. Sensitivity towards outliers
Tree based models are generally robust while regression-based models tend to suffer
from outliers. Explain why Boosting is sensitive to outliers in the dataset. Use
residuals to support your case.
3. Gradient Boosting
There are several other boosting techniques in addition to AdaBoost. Gradient
boosting is one such general boosting technique which allows optimization of
arbitrary loss function.
Read and understand key differences between Gradient Boosting and Ada Boosting
from online sources (1 , 2, 3 etc.). Elaborate your findings.

#Exercise 2 (6 points)
Read the description of and get familiar with the “heart.csv” dataset. The task is to determine
whether a person has a certain heart related disease or not.
1. Read and convert the data similarly as in other exercises. Split the data into 60%
training, 20 % validation and 20% testing parts.
2. Fit a Decision Tree on the training set and cross validate using validation set.
3. Visualize the Decision tree using graphviz (Example) library and analyze the most
important features in decision.
4. Use ensemble.py as a template and implement a most basic Bagging Classifier.
Specifically,
1a.
Complete fit method
Create as many decision trees as ‘n_estimators’ and fit them to different
bootstrapped samples generated from ‘bootstrap’ method using training data
mentioned above.
b. Complete predict method
We use voting based bagging i.e. Final class for a sample is the most frequent
class in the predictions.
In the predict method, collect predictions from all decision trees fitted in the
previous step. Return the most frequent class for each sample.
5. Use the following ensemble methods from sklearn and report accuracy score on each
of them.
a. Bagging Classifier
b. Random Forest Classifier
c. Gradient Boosting Classifier
6. Examine Feature importance obtained from Gradient Boosting Classifier and
compare them against feature importance in Exercise 2.3.
