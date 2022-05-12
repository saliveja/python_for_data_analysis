import numpy as np

# slicing arrays
arr = np.arange(10)
print(arr)
print(arr[5])
# array slices is views from original array
# modification will be reflected in the source
print(arr[5:8])
arr[5:8] = 12
# assigning value 12 to numbers 5, 6 and 7
print(arr)

# modifying arrays
arr_slice = arr[5:8]
print(arr_slice)
arr_slice[1] = 12345
# assigning value 12345 to index 1 in the slice
# we can slice the array and slice the slice
print(arr)
arr_slice[:] = 64
# assigning value 64 to all values in the slice
# the modifications are permanent. NumPy makes no copies.
print(arr)
# to make a copy we can instead write arr[5:8].copy()

# addressing elements in an array
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[2])
# printing element in position 2 in the array --> [7, 8, 9]

# addressing individual elements within an array list
print(arr2d[0][2])
# this points to the first list in the array [1, 2, 3]
# index 2 which is number 3
# we can also write print(arr2d[0, 2])

# multidimensional arrays
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)
print(arr3d[0])
# this is a 2x3 array

# copying values in arrays
old_values = arr3d[0].copy()
# making a copy of the original values in index 0
arr3d[0] = 42
# position zero in the array is the first two lists
# all values in them are replaced by 42
print(arr3d)
arr3d[0] = old_values
# re-assigning the old values to index 0
print(arr3d)
print("\n")

# indexes with arrays
print(arr3d[1, 0])
# addresses the first position (as the two first and the two lists are
# respectively connected, index one is the third list
# the number 0 is referring to the first list of the last two
print("\n")
x = arr3d[1]
print(x)
# printing index 1 --> list three and four

