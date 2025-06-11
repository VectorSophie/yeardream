import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9])

array1 = x.reshape((3,3))
print("(3x3) 배열 x:\n", array1)

array2 = np.reshape(array1[:,1],(3,1))
print("\narray1의 2번째 column :\n", array2)

array3 = np.c_[array1,array2]
print("\narray1에 column 방향으로 array2 붙이기:\n", array3)

array4 = np.reshape(array3,(3,2,2))
print("\n(3,2,2) array4:\n", array4)

array5 = array4[0,:,:]
print("\narray4의 3개의 (2,2)행렬 중 첫 번째 행렬:\n", array5)

