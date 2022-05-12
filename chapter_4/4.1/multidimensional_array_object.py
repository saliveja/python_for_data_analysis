import numpy as np

# generating random data
data = np.random.randn(2, 3)
print(data)
print('\n')

# multiplying random data with ten
data = data * 10
print(data)
print('\n')

# adding the randomly generated data on top of each other
data = data + data
print(data)
print('\n')

# in ndarray all elements need to be the same type
print(data.shape)
# every array has a shape
# this is described in rows and columns
# this has the shape of two rows and three columns
# [[-22.48067429 -14.38353356 -17.15618111]
#  [-45.0115981   30.68710922  21.5613913 ]]
print('\n')
print(data.dtype)
# dtype is an object describing the data type  of the array
# here: float64
