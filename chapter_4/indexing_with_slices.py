import numpy as np

# slicing one-dimensional arrays
arr = np.arange(10)
# print(arr[1:6])
# one-dimensional slicing works like with python lists

# slicing two-dimensional arrays
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr2d)
print(arr2d[:2])
# slicing works differently with two-dimensional arrays
# this means --> select the two first rows of arr2d

# passing multiple indexes
print(arr2d[:2, 1:])
# this means to slice the first two rows
# from index one until the end
# in this case, two numbers will be printed for each row
