# data analysis with python

data = np.random.randn(2, 3)
- generating random data

data = data * 10
- multiplying data

data = data + data
- adding data on top of each other

data.shape
- printing the number of rows and columns

data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
- making numpy array out of list

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
- nested sequence

arr2 = np.array(data2)
- converted into multidemensional array
- like this: 
[[1 2 3 4]
 [5 6 7 8]]

arr2.ndim
- returns the number of lists stacked on top of each other

arr1.dtype
- returns dtype, ie. float64 or int32

np.zeros(10)
- creates array oif zeros

np.zeros((3, 6))
- creates three rowns and six columns of zeros

np.empty((2, 3, 2))
- creates array without initializing oatricular value
- may return uninitialized garbage value and not only zeros

arr = np.arange(10)
- array of number 1 to 9

print(arr[5])
- prints the number 5 in the array

arr[5:8]
- is a slice of the array, numbers 5, 6, 7

arr[5:8] = 12
- assigning a different value to number 5, 6, 7

arr_slice = arr[5:8]
- create a variable for a slice

arr_slice[1] = 12345
- pointing to index 1 in the slice and asssigning a new value

arr_slice[:] = 64
- assigning new value to all values in the slice

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d[2]
- points to index two in the array [7, 8, 9]

arr2d[0][2]
- first list, index 2 in array

arr2d.copy()
-copies the array
- otherwise always modifications to original

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
- 2x3 array
- three numbers in each bracket
- two brackets connected with each other
- the first two brackets are index 0 and the last two index 1

arr3d[1, 0]
- refers to [7, 8, 9]

