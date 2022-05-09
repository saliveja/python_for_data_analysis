import numpy as np

arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.int32)
print(arr1.dtype)
print(arr2.dtype)
# dtype is specified in arr1 and arr2
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)
# dtype is int64
float_arr = arr.astype(np.float64)
# casting integers to floating points
print(float_arr.dtype)
# float64
