
#Data Preprocessing
#import the dataset
dataset = read.csv('Social_Network_Ads.csv')
dataset = dataset [,3:5]

#Encode categroical data :optional
#factor function transforms categorical variable into numeric categories. it will see variables as factors

# encode gender column
#dataset$Gender = factor(dataset$Gender, levels = c('Male', 'Female') , labels = c(0,1))

## Encoding the target feature as factor
#convert purchased column as  column of factors (c is a vector of elements values ie )
dataset$Purchased = factor(dataset$Purchased, levels = c(0, 1))



# Splitting the dataset into the Training set and Test set
#split ratio is for training set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.75)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)


#Feature Scaling 
#note: index of row/columns start from 1 in R language
# Scale only non categorical variable index 1 and 2  ex: age and salary in training set 
## -3  negative index in R , drops the element at that index which is 3rd element(Purchased) in the test set 
training_set[-3] = scale(training_set[-3])
test_set[-3] = scale(test_set[-3])



# Support Vector Machine (SVM) 

#install.packages('e1071') # if e1071 package is not installed execute this step
# import library
library(e1071)


#********* Create Classifer here ********

# Predict  dependent variable purchased  ~ w.r.t dot  (take all independent variable of our dataset -  age and estimated salray)
#linearly non-separable features often become linearly separable after they are mapped to a high dimensional feature space. Therefore we use RBF or Radial basis kernel
## Fitting Kernel SVM classifier to the Training set -- we use gaussian kernel which is radial basis function(RBF kernel)
classifier = svm(formula = Purchased ~ .,
                 data = training_set,
                 type = 'C-classification',
                 kernel = 'radial') 



# Predicting the Test set results
# -3  negative index in R , drops the element at that index which is 3rd element(Purchased) in the test set 
y_pred = predict(classifier, newdata = test_set[-3])


# Making the Confusion Matrix (actual vs predicted purchased) : to find number of correct and incorrect predictions
cm = table(test_set[, 3], y_pred)


#******** BEGIN Decision Tree Classifier **************

#Data Preprocessing
#import the dataset
dataset = read.csv('Social_Network_Ads.csv')
dataset = dataset [,3:5]

#Encode categroical data :optional
#factor function transforms categorical variable into numeric categories. it will see variables as factors

# encode gender column
#dataset$Gender = factor(dataset$Gender, levels = c('Male', 'Female') , labels = c(0,1))

## Encoding the target feature as factor
#convert purchased column as  column of factors (c is a vector of elements values ie )
dataset$Purchased = factor(dataset$Purchased, levels = c(0, 1))



# Splitting the dataset into the Training set and Test set
#split ratio is for training set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.75)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)


#Feature Scaling 
#note: index of row/columns start from 1 in R language
# Scale only non categorical variable index 1 and 2  ex: age and salary in training set 
## -3  negative index in R , drops the element at that index which is 3rd element(Purchased) in the test set 
training_set[-3] = scale(training_set[-3])
test_set[-3] = scale(test_set[-3])



# Support Vector Machine (SVM) 

#install.packages('rpart') # if rpart package is not installed execute this step
# import library
library(rpart)


#********* Create decision tree Classifer here ********

# Predict  dependent variable purchased  ~ w.r.t dot  (take all independent variable of our dataset -  age and estimated salray)

classifier = rpart(formula = Purchased ~ .,
                 data = training_set,
                 ) 



# Predicting the Test set results
# -3  negative index in R , drops the element at that index which is 3rd element(P  urchased) in the test set 
y_pred = predict(classifier, newdata = test_set[-3], type ='class')


# Making the Confusion Matrix (actual vs predicted purchased) : to find number of correct and incorrect predictions
cm = table(test_set[, 3], y_pred)





