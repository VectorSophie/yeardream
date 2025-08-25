import numpy as np
import pandas as pd

A = pd.DataFrame(np.random.randint(0, 10, (2, 2)))
B = pd.DataFrame(np.random.randint(0, 10, (3, 3)))

print("DataFrame A \n", A)
print("DataFrame B \n", B)

add = A.add(B, fill_value=0)
print(add,'\n')

sub = A.sub(B,fill_value=0)
print(sub,'\n')

mul = A.mul(B,fill_value=0)
print(mul,'\n')

div = A.div(B,fill_value=0)
print(div,'\n')

C = pd.DataFrame([[1,3,5],[15,10,5],[2,8,5]], index = ['a','b','c'], columns = ['d','e','f'])

row_C = C.sort_values('c',ascending=True, axis=1)

column_C = C.sort_values('e',ascending=False, axis=0)

print(row_C,'\n')
print(column_C,'\n')

row_C.to_csv("./data.csv",index=False)
load_C = pd.read_csv("./data.csv")

print(load_C)
