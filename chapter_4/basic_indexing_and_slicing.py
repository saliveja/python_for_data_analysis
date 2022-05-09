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
