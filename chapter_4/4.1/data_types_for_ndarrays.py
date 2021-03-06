import numpy as np

# specified dtype
arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.int32)
print(arr1.dtype)
print(arr2.dtype)

# casting int/float
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)
# dtype is int64
float_arr = arr.astype(np.float64)
# casting integers to floating points
# if floating points are cast to integers the decimal part will be truncated
print(float_arr.dtype)
# float64

# casting float to int, truncating decimals
arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
print(arr)
# printing the sequence as shown
print(arr.astype(np.int32))

# using astype to convert string to numeric form
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
print(numeric_strings.astype(float))

# using another arrays dtype attribute
int_array = np.arange(10)
calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
print(int_array.astype(calibers.dtype))

# shorthand code string for dtype
empty_uint32 = np.empty(8, dtype='u4')
print(empty_uint32)

