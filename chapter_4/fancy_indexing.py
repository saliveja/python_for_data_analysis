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