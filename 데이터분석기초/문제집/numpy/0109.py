import numpy as np

matrix = np.arange(8).reshape((2, 4))
print(matrix)

print(np.sum(matrix))

print(np.max(matrix))

print(np.min(matrix))

print(np.mean(matrix))

print(np.sum(matrix, axis = 0))

print(np.sum(matrix, axis = 1))

print(np.std(matrix))

print(matrix[matrix<5])