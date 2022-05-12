import numpy as np

# indexing using integer arrays
arr = np.empty((8, 4))
# empty don't initialize the entries
# 8 is the number of rows
# 4 is the number of columns
for i in range(8):
    # for integer in range 8
    arr[i] = i

print(arr)

# selecting an order for the rows
print(arr[[4, 3, 0, 6]])
# note the double brackets
print("\n")

# negative indices
print(arr[[-3, -5, -7]])
# this selects rows counting from the end

# multiple index arrays
arr = np.arange(32).reshape((8, 4))
# array with numbers 1-31, with 8 rows and 4 columns
print("\n")
print(arr)
print("\n")
print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])
# the first bracket selects the row
# the second bracket selects the column
# fancy indexing unlike slicing always copies the data into a new array
print("\n")
print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])
# the order of the column is the first index
# the last index and the two in the middle
# [4, 5, 6, 7] becomes [4, 7, 5, 6]
