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
print("\n")

# multiple arrays with unfunc
arr = np.random.randn(7) * 5
print(arr)
print("\n")

remainder, whole_part = np.modf(arr)
# modf return the fractional and integral parts of an array
# for example:np.modf([0, 3.5]), will return:
# (array([ 0. ,  0.5]), array([ 0.,  3.]))
print(remainder)
print(whole_part)



