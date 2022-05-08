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
# the shape of the array is four numbers in two lines.