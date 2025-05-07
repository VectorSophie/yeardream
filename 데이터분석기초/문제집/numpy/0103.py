import numpy as np

print("2차원 array")
matrix = np.arange(1, 16).reshape(3,5)  
print(matrix)

print(type(matrix))

print(matrix.ndim)

print(matrix.shape)

print(matrix.size)

print(matrix.dtype)

print(matrix[2,3])

print(matrix[0:2,1:4])