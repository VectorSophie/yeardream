import numpy as np

def AND_gate(x1,x2):
    x = np.array([x1, x2])
    weight = np.array([0.5, 0.5])
    bias = -0.7
    y = np.sum(weight*x) + bias
    
    return Step_Function(y)

def OR_gate(x1,x2):
    x = np.array([x1, x2])
    weight = np.array([0.5, 0.5])
    bias = -0.2
    y = np.sum(weight*x) + bias
    
    return Step_Function(y)

def NAND_gate(x1,x2):
    x = np.array([x1, x2])
    weight = np.array([-0.5, -0.5])
    bias = 0.7
    y = np.sum(weight*x) + bias
    
    return Step_Function(y)

def Step_Function(y):
    if y<=0:
        return 0
    else:
        return 1

def XOR_gate(x1, x2):
    
    nand_out=NAND_gate(x1,x2)
    or_out=OR_gate(x1,x2)
    
    return AND_gate(nand_out,or_out)

def main():
    
    array = np.array([[0,0], [0,1], [1,0], [1,1]])
    
    print('XOR Gate 출력')
    
    for x1, x2 in array:
        print('Input: ',x1, x2, ', Output: ', XOR_gate(x1, x2))

if __name__ == "__main__":
    main()