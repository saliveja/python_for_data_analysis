import numpy as np

arr = np.array([[1., 2., 3.], [4., 5., 6.]])
# pay attention to the number of brackets
# when using arrays we don't have to use for loops
print(arr)
print(arr * arr)
print(arr - arr)
print(1 / arr)
print(arr ** 0.5)
# whatever calculation, all elements are addressed

# boolean arrays
arr2 = np.array([[0., 4., 1.], [7., 2., 12]])
print(arr2)
print(arr2 > arr)
# evaluating operations between differently sized arrays is called broadcasting