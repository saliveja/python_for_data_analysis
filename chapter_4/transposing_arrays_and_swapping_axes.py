import numpy as np

# transpose method
arr = np.arange(15).reshape((3, 5))
# array is numbers 0-14
# three rows
# five columns
# this method doesn't copy anything
print(arr)
print("\n")

print(arr.T)
# this displays the columns in the order of rows
# and the rows in the order of columns
# [[0, 5, 10]] instead of [[0, 1, 2]]