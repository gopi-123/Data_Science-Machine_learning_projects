
# Homework 10

Submit completed files to demonstrate your results. Please name your submission
after your last name. 

## Exercise 1 (Exploratory data analysis, visualization)-  10 points

a) Load the file “imdb_top_10000.csv” as a pandas data frame. This file
contains a number of top voted film entries with some descriptors like imdb
score and year of release. Drop the rows with missing values.
b) Fix the runtime column to have proper numerical entries; e.g. '177 mins.'
should become 177.
c) Split up the 'genre' column into multiple columns corresponding to specific
genre, which contains True Boolean value if the movie is of a column
genre, and False otherwise. Delete the original 'genre' column.
d) Print in console simple statistical description for the column’s 'runtime',
'score', 'votes', 'year' obtained with 'describe' method. Do you see any
suspicious values for 'runtime'? If so, remove the rows of the dataset with
these “suspicious” values, and make sure that there are no other
suspicious values.
e) Plot histogram which describes the number of movies released in every
year. What can you say about the histogram for the most recent movies
and most old ones? Report this in report.txt. Save the figure and include it
with the submission. The quality of plots that you produce will be graded.
f) Consider bars corresponding to year 2003 and 2004. What can you say
about the Lie factor for the graph in Exercise 1.e? Report your result.
g) Produce a scatter plot for 'year' against 'rating' values. Additionally,
compute the mean of the IMDB ratings for every year, and plot it on the
plot. For the latter, you might want to use “groupby” function. What can you
say about the relationship between the year and the rating? Report this in
report.txt. Save the figure and include it with submission.
h) Find the lowest and highest rated movies in the dataset. Report the names
of the movies together with their scores in report.txt
