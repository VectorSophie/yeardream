import numpy as np
from sklearn.model_selection import train_test_split

from elice_utils import EliceUtils
elice_utils = EliceUtils()

dataset = np.random.random([40,4]) 

feature = dataset[:, :3]

label = dataset[:,-1]

X_train, X_test, Y_train, Y_test = train_test_split(feature,label,test_size=0.25,random_state=121)

print("Case 1.")
print("X_train shape : {}".format(X_train.shape))
print("X_test shape : {}".format(X_test.shape))
print("Y_train shape : {}".format(Y_train.shape))
print("Y_test shape : {}".format(Y_test.shape))

X_train_2, X_test_2, Y_train_2, Y_test_2 = train_test_split(feature,label,test_size=0.3,random_state=121, shuffle=False)

print("\nCase 2.")
print("X_train_2 shape : {}".format(X_train_2.shape))   
print("X_test_2 shape : {}".format(X_test_2.shape))
print("Y_train_2 shape : {}".format(Y_train_2.shape))
print("Y_test_2 shape : {}".format(Y_test_2.shape))