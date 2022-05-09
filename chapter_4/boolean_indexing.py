import numpy as np

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'],
                 dtype='U4')
data = np.random.randn(7, 4)
print(names)
print(data)
print(names == 'Bob')
# comparing names with the string 'Bob with boolean array

# data for boolean index
print(data[names == 'Bob'])
# the data rows which have the position like Bob have become the
# representation of Bob
print(data[names == 'Bob', 2:])
# from the rows that are Bob
# we print the last two values of each row
print(data[names == 'Bob', 3])
# printing index three in each row
