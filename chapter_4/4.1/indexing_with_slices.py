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

# specifying slices
print(arr2d[1, :2])
# index one --> the last two list/rows
# the first two numbers/columns [4, 5]

print(arr2d[:2, 2])
# the first two rows
# colums with index two, meaning 3 and 6

print(arr2d[:, :1])
# colon means the whole array
# :1 means the first number in each row --> 1, 4, 7

arr2d[:2, 1:] = 0
# first two rows
# values from index 1 until the end
# replace with 0
print(arr2d)