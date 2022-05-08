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
# every array has a shape, which is a tuple indicating the size of each
# dimension
print('\n')
print(data.dtype)
# dtype is an object describing the data type  of the array
