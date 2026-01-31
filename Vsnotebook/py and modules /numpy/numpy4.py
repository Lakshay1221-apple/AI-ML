# IN THIS FILE WE WILL LEARN ABOUT AGGREGATE FUNCTION
''' Aggregate function = summarize data and typically return a single value as output '''

import numpy as np

array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]])

print("This is the sum of the array:", np.sum(array)) # Sum of all elements in the array
print("This is the mean of the array:", np.mean(array)) # Mean of all elements in the array
print("This is the median of the array:", np.median(array)) # Median of all elements in the array
print("This is the standard deviation of the array:", np.std(array)) # Standard deviation of all elements in the array
print("This is the variance of the array:", np.var(array)) # Variance of all elements in the array
print("This is the minimum element in the array:", np.min(array)) # Minimum element in the array
print("This is the maximum element in the array:", np.max(array)) # Maximum element in the array

print("THIS ARE THE AGGREGATE FUNCTIONS ALONG AXIS")


print("This is sum along the columns", np.sum(array, axis = 0)) # sum along  all the columns 
print("This is sum along the rows", np.sum(array, axis = 1)) # sum along all the rows