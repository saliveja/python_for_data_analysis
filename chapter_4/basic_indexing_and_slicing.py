import numpy as np

# slicing arrays
arr = np.arange(10)
print(arr)
print(arr[5])
# array slices is views from original array
# modification will be reflected in the source
print(arr[5:8])
arr[5:8] = 12
# replacing the numbers 5, 6 and 8 with the number 12
print(arr)