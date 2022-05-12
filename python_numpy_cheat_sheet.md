# NumPy cheat sheet 
_________________________________________________________________________________________________________________________________________________________________________________________________
code		                       | when writing arr or arr2 written referred to variable     							  						|
-----------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------:|
data = np.random.randn(2, 3)							| generating random data			 									|
data = data * 10								| multiplying data				 									|
data = data + data								| adding data on top of each other. whatever calculation, all elements in the array is addressed			|
arr2 > arr 									| broadcasting --> evaluating size between arrays			  	 					|
data.shape									| the shape is the number of rows and columns  					  	 			|
arr1 = np.array(data1) 							| ie. data1 = [6, 7.5, 8, 0, 1]. Making numpy array from a list	 						|
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]						| nested sequence													|
arr2 = np.array(data2)								| multidemensional array				  	 							|
arr2.ndim									| returns the number of lists stacked on top of each other   							|
arr1.dtype									| returns dtype, ie. float64 or int32 										|
np.zeros(10)									| creates array of zeros										 		|
np.zeros((3, 6))								| creates three rowns and six columns of zeros				 					|
np.empty((2, 3, 2))								| creates array without initializing patricular value. May return garbage value			 		|
arr = np.arange(10)								| creating array of number 1 to 9											|
print(arr[5])									| prints the number 5 in the array											|
arr[5:8]									| is a slice of the array, numbers 5, 6, 7										|
arr[5:8] = 12									| assigning a different value to number 5, 6, 7									|
arr_slice = arr[5:8]								| create a variable for a slice											|
arr_slice[1] = 12345								| pointing to index 1 in the slice and asssigning a new value							|
arr_slice[:] = 64								| assigning new value to all values in the slice									|
arr2d[2]									| example: arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) - points to index two in the array [7, 8, 9]	|
arr2d[0][2]									| first list, index 2 in array											|
arr2d.copy()									| copies the array, otherwise always modifications to original							|
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])	| 2x3 array. three numbers in each bracket. two brackets connected with each other. :2 index 0, 2:4 index 1	|
arr3d[1, 0]									| refers to [7, 8, 9]													|
arr2d[1, :2]									| index 1, 2 first number in the columns										|
arr2d[:2, 2]									| first 2 rows, columns with index 2											|
arr2d[:, :1]									| whole array, first number in each row										|
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Joe'], dtype='U4')		| arrang with string values												|
names == 'Bob'									| checking names with string to see how many Bobs									|
data[names == 'Bob']								| ie. data is data = np.random.randn(7, 4), then each of rows represent name in the same order as names in list	|
data[~(names == 'Bob')]							| all names that are not Bob												|
mask = (names == 'Bob') | (names == 'Will')					| condition, Bob or Will												|
data[names != "Joe"] = 7							| changing values in the data connected to all names that are not Joe						|
data[data < 0] = 0								| all negative data set to 0												|
arr1 = np.array([1, 2, 3], dtype=np.float64)					| specifying dtype													|
float_arr = arr.astype(np.float64)						| casting integers to floating points											|
arr[[-3, -5, -7]]								| selects rows counting from the end											|
arr[[4, 3, 0, 6]]								| selecting order for rows (in this case 1-10)									|
arr = np.arange(32).reshape((8, 4))						| array with numbers 1-31, with 8 rows and 4 columns									|
arr[[1, 5, 7, 2], [0, 3, 1, 2]]						| the first bracket selects the row, the second bracket selects the column						|
arr.T										| this displays the columns in the order of rows and rows as columns							|
np.dot(arr.T, arr)								| computing inner matrix product: row 1, index  0 * row 2, index 0 + row 2, index 1 + row 2, index 2 etc		|
arr.transpose((1, 0, 2))							| swapping axes to: row 1, row 3, row 2, row 4									|
arr.swapaxes(1, 2)								| each section changes to rows to columns and columns to rows							|
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	        
