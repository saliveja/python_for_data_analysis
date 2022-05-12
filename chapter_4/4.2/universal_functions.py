import numpy as np

arr = np.arange(10)
print(arr)
print("\n")

# sqrt
print(np.sqrt(arr))
# sqrt return the non-negative square-root of an array
print("\n")

# exp
print(np.exp(arr))
# calculate the exponential of all elements in the input array
print("\n")

# unary ufuncs
x = np.random.randn(8)
y = np.random.randn(8)
print(x)
print("\n")
print(y)
print("\n")

print(np.maximum(x, y))
# returns the biggest numbers from x and y into a single array




