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
print("\n")

# np.dot
arr = np.random.randn(6, 3)
print(arr)
print("\n")

print(np.dot(arr.T, arr))
# this mean row 1, index  0 * row 2, index 0 + row 2, index 1 + row 2, index 2
# it continues in the same fashion with all number addressing the row below

# higher dimensional arrays
arr = np.arange(16).reshape((2, 2, 4))
# two sections
# two rows
# four columns

print("\n")
# print(arr)
print("\n")

print(arr.transpose((1, 0, 2)))
# swapping axes to: row 1, row 3, row 2, row 4
print("\n")

# swapaxes()
print(arr.swapaxes(1, 2))
# each section changes to rows to columns and columns to rows