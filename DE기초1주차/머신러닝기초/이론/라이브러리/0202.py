import numpy as np

array1 = np.array([[1,2,3],[4,5,6],[7,8,9]])

array2 = array1[:, 0] + array1[:, 1]
print("1st column of array1 + 2nd column of array1:\n", array2)

array3 = array1[0,:] - array1[1,:]
print("\n1st row of array1 - 2nd row of array1:\n", array3)

array4 = array2 * array3
print("\narray2 * array3:\n", array4)

array5 = np.c_[array2, array3, array4]

array6 = array1 / array5
print("\narray1 / array5:\n", array6)
