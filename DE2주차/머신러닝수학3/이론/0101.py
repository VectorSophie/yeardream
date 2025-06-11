import numpy as np

A = np.array([3,1,-1])

x_axis = np.array([1,0,0])
y_axis = np.array([0,1,0])
z_axis = np.array([0,0,1])

A_proj_x = np.dot(A,x_axis)

A_proj_y = np.dot(A,y_axis)

A_proj_z = np.dot(A,z_axis)

if (A == A_proj_x * x_axis + A_proj_y * y_axis + A_proj_z * z_axis).all:
    print('3차원 축으로 분해 완료')
else:
    print('3차원 축으로 분해 실패')