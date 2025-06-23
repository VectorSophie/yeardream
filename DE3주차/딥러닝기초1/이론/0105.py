import numpy as np

def XOR_gate(x1, x2):
    
    x = np.array([x1,x2])
    
    weight = np.array([0.3,-0.5])
    
    bias = 0.7
    
    y = np.matmul(x,weight)+bias
    
    return Step_Function(y)
def Step_Function(y):
    
    return 1 if y>=0 else 0

def main():
    
    Input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])        
    Output = np.array([[0], [1], [1], [0]])
    
    print('XOR Gate 출력')
    
    XOR_list = []
    
    for x1, x2 in Input:
        print('Input: ',x1, x2, ' Output: ', XOR_gate(x1, x2))
        XOR_list.append(XOR_gate(x1, x2))
    
    hit = 0
    for i in range(len(Output)):
        if XOR_list[i] == Output[i]:
            hit += 1
    
    acc = float(hit/4)*100
    
    print('Accuracy: %.1lf%%' % (acc))

if __name__ == "__main__":
    main()