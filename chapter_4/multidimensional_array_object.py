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