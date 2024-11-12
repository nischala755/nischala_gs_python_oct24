import numpy as np
import scipy

array = np.array([[1, 1, 3, 3, 4, 4, 4, 5, 7, 7, 8, 9, 12]])

mean   = np.mean(array)
median = np.median(array)
mode   = scipy.mode(array)

print(f'Mean = ', mean)
print(f'Median = ', median)
print(f'Mode = ', mode)


import numpy as np

array1 = np.zeros(3)
print(f'Array1 = {array1}')

array2 = np.zeros((1, 4))
print(f'Array2 = {array2}')

array3 = np.zeros((2, 5))
print(f'Array3 = {array3}')
---------------------------------------------
import numpy as np

array1 = np.zeros(3)
array2 = np.zeros((1, 4))
array3 = np.zeros((2, 5))

print(array1[0], array1[2])
print(array2[0][0], array2[0][3])
print(array3[1][0], array3[1][3])
-------------------------------------------------
import numpy as np

array1 = np.zeros(3)
array2 = np.zeros((1, 4))
array3 = np.zeros((2, 5))

print(array1[4]) # IndexError
print(array1[0][0]) # SyntaxError array2 is not 2D
print(array2[2][0]) # IndexError
print(array3[3][3]) # IndexError
--------------------------------------------
import numpy as np

array1 = np.zeros(3)
array2 = np.zeros((1, 4))
array3 = np.zeros((2, 5))

print(type(array1))
print(type(array2))
print(type(array1[0]))
print(type(array2[0]))
print(type(array2[0][0]))
----------------------------------------------
import numpy as np

array1 = np.full((2, 4), 5)
print(array1)
array2 = np.full((1,5), 10)
# Here array2 is still a ndarray
print(array2)
------------------------------------------------
import numpy as np
# arange()

array1 = np.arange(10)
array2 = np.arange(10, 20)
array3 = np.arange(10, 30, 3)

print(type(array1))
print(array1)
print(array2)
print(array3)
------------------------------------------------------
import numpy as np
# ones()

array1 = np.ones(10)
array2 = np.ones((2, 8))
array3 = np.ones((3, 5))

print(type(array1))
print(array1)
print(array2)
print(array3)
---------------------------------------------
import numpy as np

vector = np.arange(5)
print('Vector shape:', vector.shape)

matrix = np.ones([3, 2])
print('Matrix:', matrix)
print('Matrix shape:', matrix.shape)

tensor = np.zeros([2, 3, 3])
print('Tensor:', tensor)
print("Tensor shape:", tensor.shape)
-------------------------------------------------
import numpy as np

arr = np.arange(1, 10)
print(arr, '\n')

# Reshape to 3x3 matrix
arr = arr.reshape(3, 3)
print(arr, '\n')

# Reshape back to the original size
arr = arr.reshape(9)
print(arr)

arr = arr.reshape(2, 5) # ValueError
print(arr)
-----------------------------------------------------
import numpy as np

arr1 = np.arange(12)

arr2 = arr1.reshape(2, 6)
arr3 = arr1.reshape(6, 2)
arr4 = arr1.reshape(3, 4)
arr5 = arr1.reshape(12, 1)
arr6 = arr1.reshape(4, 3)

print('Arr1:\n', arr1)
print('Arr2:\n', arr2)
print('Arr3:\n', arr3)
print('Arr4:\n', arr4)
print('Arr5:\n', arr5)
print('Arr6:\n', arr6)
-------------------------------------------------------
import numpy as np

arr = np.arange(1, 10).reshape(3, -1) # Here python infers/decides the number of columns by itself.
print(arr)
-------------------------------------------------------
import numpy as np

arr1 = np.arange(1, 10)
arr2 = np.arange(2, 25, 2)
arr3 = arr1.reshape(3, -1)
arr4 = arr2.reshape(4, -1)
arr5 = arr2.reshape(2, -1)
arr6 = arr2.reshape(3, -1)
arr7 = arr2.reshape(-1, 4) # Numpy predicts and fixes number of rows
arr8 = arr2.reshape(-1, -1) #ValueError. Can only specify one unknown dimension

print('Arr1:\n', arr1)
print('Arr2:\n', arr2)
print('Arr3:\n', arr3)
print('Arr4:\n', arr4)
print('Arr5:\n', arr5)
print('Arr6:\n', arr6)
print('Arr7:\n', arr7)
print('Arr8:\n', arr8)
---------------------------------------------------------
import numpy as np

array1 = np.array([1, 3, 5, 0, 2, 3, 4, 5, 13, 17, 23, 29])
print(array1.shape)
print(type(array1))
print(array1)
---------------------------------------
import numpy as np

array1 = np.array([1, 3, 5, 0, 2, 3, 4, 5, 13, 17, 23, 29])

array1.shape = (6, 2)
print(array1.shape)
print(array1)

array1.shape = (3, 4)
print(array1.shape)
print(array1)

array1.shape = (4, 3)
print(array1.shape)
print(array1)

#array1.shape = (4, 2) # Error New shape of the array must consist of same number of elements as that of original array
#print(array1.shape)
#print(array1)
import numpy as np

matrix1 = np.array([[3, 4, 5], [2, 6, 9]])
matrix2 = np.array([[3, 4], [3, 5], [2, 6]])

matrix3 = np.dot(matrix1, matrix2)

print('Matrix3=\n', matrix3)

import numpy as np

array = np.array([2, 4, 6, 8, 9, 19])

array2 = array + 5 # Broadcasting. Adding a scalar quantity to every element of the array

print(array)
print(array2)
import numpy as np

array = np.array([[2, 4, 6, 8], [9, 19, 4, 10]])

array2 = array + 5 # Broadcasting. Adding a scalar quantity to every element of the array

print(array)
print(array2)
import numpy as np

matrix1 = np.array([[3, 3, 4], [2, 3, 9]])
matrix2 = np.array([[2, 5, 4], [2, 3, 19]])

sum_matrix = matrix1 + matrix2
difference_matrix = matrix1 - matrix2
product_matrix = matrix1 * matrix2
quotient_matrix = matrix1 / matrix2

print(sum_matrix)
print(difference_matrix)
print(product_matrix)
print(quotient_matrix)

import numpy as np
import scipy

array = np.array([[1, 1, 3, 3, 4, 4, 4, 5, 7, 7, 8, 9, 12]])

mean   = np.mean(array)
median = np.median(array)
mode   = scipy.mode(array)

print(f'Mean = ', mean)
print(f'Median = ', median)
print(f'Mode = ', mode)

import numpy as np

array1 = np.array([1, 3, 5, 0, 2, 3, 4, 5, 13, 17, 23, 29])
print(array1.shape)
print(type(array1))
print(array1)
---------------------------------------
import numpy as np

array1 = np.array([1, 3, 5, 0, 2, 3, 4, 5, 13, 17, 23, 29])

array1.shape = (6, 2)
print(array1.shape)
print(array1)

array1.shape = (3, 4)
print(array1.shape)
print(array1)

array1.shape = (4, 3)
print(array1.shape)
print(array1)

#array1.shape = (4, 2) # Error New shape of the array must consist of same number of elements as that of original array
#print(array1.shape)
#print(array1)
-------------------------------------------------
import numpy as np

matrix1 = np.array([[3, 4, 5], [2, 6, 9]])
matrix2 = np.array([[3, 4], [3, 5], [2, 6]])

matrix3 = np.dot(matrix1, matrix2)

print('Matrix3=\n', matrix3)
---------------------------------------------
import numpy as np

array = np.array([2, 4, 6, 8, 9, 19])

array2 = array + 5 # Broadcasting. Adding a scalar quantity to every element of the array

print(array)
print(array2)
------------------------------------
import numpy as np

array = np.array([[2, 4, 6, 8], [9, 19, 4, 10]])

array2 = array + 5 # Broadcasting. Adding a scalar quantity to every element of the array

print(array)
print(array2)
--------------------------------------
import numpy as np

matrix1 = np.array([[3, 3, 4], [2, 3, 9]])
matrix2 = np.array([[2, 5, 4], [2, 3, 19]])

sum_matrix = matrix1 + matrix2
difference_matrix = matrix1 - matrix2
product_matrix = matrix1 * matrix2
quotient_matrix = matrix1 / matrix2

print(sum_matrix)
print(difference_matrix)
print(product_matrix)
print(quotient_matrix)
------------------------------------------
import numpy as np
import scipy

array = np.array([[1, 1, 3, 3, 4, 4, 4, 5, 7, 7, 8, 9, 12]])

mean   = np.mean(array)
median = np.median(array)
mode   = scipy.mode(array)

print(f'Mean = ', mean)
print(f'Median = ', median)
print(f'Mode = ', mode)
---------------------------------------------
num = 50

while(num < 50):
	# do something
	pass
else:
	# do something else
	pass
---------------------------------------------
To enforce elements of same type to encapsulated, we must use array from the module array
array.array stores elements of same type only.
-----------------------------------------------------

{"airline" : "akasa", "source" : "chennai", "destination" : "jaipur", 
"duration" : 3.25, "fare" : 9200, "id" : 1}