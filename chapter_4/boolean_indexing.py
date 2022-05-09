import numpy as np

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'],
                 dtype='U4')
data = np.random.randn(7, 4)
print(names)
print("\n")
print(data)
print("\n")
print(names == 'Bob')
# comparing names with the string 'Bob with boolean array
print("\n")
# data for boolean index
print(data[names == 'Bob'])
# the data rows which have the position like Bob have become the
# representation of Bob
print("\n")
print(data[names == 'Bob', 2:])
# from the rows that are Bob
# we print the last two values of each row
print("\n")
print(data[names == 'Bob', 3])
# printing index three in each row
print("\n")

# negating condition
print(names != 'Bob')
# printing True for all names that are not Bob
print("\n")

print(data[~(names == 'Bob')])
# printing all data that is not Bob
# ~ used to invert a general condition
print("\n")

cond = names == 'Bob'
print("\n")
print(data[~cond])

# multiple boolean conditions
mask = (names == 'Bob') | (names == 'Will')
# '&' is used instead of 'and' for conditions
# | is used for 'or'
# the usually used and , or will not work
# mask = Bob or Will
print(mask)
print("\n")
print(data[mask])
