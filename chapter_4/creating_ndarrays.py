import numpy as np

# using list to create an array
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
print(arr1)
print('\n')

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
# nested sequence converted into multidimensional array
arr2 = np.array(data2)
print(arr2)
print('\n')
print(arr2.ndim)
# returns 2. lists stacked on top of each other.
print(arr2.shape)
# the shape of the array is four numbers in two rows.
print('\n')

print(arr1.dtype)
# float64
# 64 refers to the memory allocated to hold this character,
# numeric characters with decimals.
# If a column contains numbers and NaNs (see below),
# pandas will default to float64, in case your missing value has a decimal.
# In computing, NaN means 'Not a Number' - numeric data type that can be
# interpreted as a value that is undefined or unrepresentable.
print(arr2.dtype)
# int64 is for storing whole numbers
print('\n')
print(np.zeros(10))
# np.zeros creates arrays of 0 or 1s with given length or shape
# prints ten zeros
print(np.zeros((3, 6)))
# note the double brackets
# prints three rows of six zeros in each
print(np.empty((2, 3, 2)))
# np.empty creates an array without initializing any particular value
# np.empty don't necessarily print only zeros
# it may return uninitialized garbage values
