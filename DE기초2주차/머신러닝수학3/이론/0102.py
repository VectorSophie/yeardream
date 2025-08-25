import numpy as np
import scipy
import scipy.linalg

A = np.array([[1, 2, 3],[2, -1, -1], [3, 1, 2]])
b = np.array([[1],[2],[3]])

rank_A = np.linalg.matrix_rank(A)

if rank_A == max(A.shape):
    print("행렬 A는 유일한 해를 가짐\n")
else:
    print("행렬 A는 무한한 해를 가짐\n")

ns = scipy.linalg.null_space(A)

print("행렬 A의 null space 벡터: \n{}\n".format(ns))

x1 = np.array([[1],[0],[0]])
x2 = np.array([[1],[0],[0]]) + ns

print("Ax1 = \n{}".format(np.dot(A,x1)))
print("Ax2 = \n{}".format(np.dot(A,x2)))