# Homework 5
Use the dataset provided along with Jupyter notebook to complete the exercise below.
Submit completed Jupyter notebook to demonstrate your results. Please name your file after
your full name.

# Exercise 1: 10 points

Consider you own a shopping complex and want to improve your business through
advertising, pricing, branding, and other strategies. For this you are provided the information
about customers to understand customer behavior and purchasing data. “customers.csv” file
contains the basic customer related information like ID, Gender, Age, Income, Score.
(Unique ID assigned to the customer, Gender of the customer, Age of the customer, Annual
Income of the customer, Score assigned to the customer by the shopping complex based on
customer behavior and spending nature. Values of this score column ranges between 1 to
100. 1 is the least score which means the values closer to 1 indicates that the customer
spends less on shopping and score closer to 100 indicates that the customer spends more
on shopping).

## Part 1: Principle Component Analysis (3 points)
a) Import the data set using pandas library and standardize the inputs
b) Apply Principle Component Analysis on the dataset and Visualize explained variance
ratio. How much percentage of variance is explained by top two principle components? How
many top principle components do you think are necessary to explain most of the variance in
the dataset?

## Part 2: K -means clustering (3 points)
a) Import the data set using pandas library
b) Implement K -means clustering based on two features income and Score using dataset
“customers.csv” file - set number of clusters as 5.
c) Visualize the Cluster of customers results in 2D - Plot (label Annual Income in X-axis vs
Score in Y-axis)
d) Interpret the meaning of each cluster in terms of annual income and spending score.


## Part 3: Hierarchical Clustering (3 points)
a) Import the data set using pandas library
b) Fit Agglomerative Hierarchical Clustering based on two features income and Score using
dataset “customers.csv” file (set affinity parameter to Euclidean distance)
c) Plot dendrogram for different linkage strategies: Complete, Single, Average.

## Part 4: Compare the Cluster similarities and dissimilarities between the results of k - means
and hierarchical clustering. (1 points)
