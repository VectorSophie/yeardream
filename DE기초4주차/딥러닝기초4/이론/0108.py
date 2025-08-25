import numpy as np

np.random.seed(100)

def rnn(inputs, input_size, output_size, bias = False):
    
    input_size = len(inputs[0])
    
    state = np.zeros((output_size,))
    
    w = np.ones((output_size, input_size))
    
    u = np.ones((output_size, output_size))
    
    b = np.random.random((output_size,))
    
    if not bias:
        b = np.zeros((output_size,))
    
    outputs = []
    
    for _input in inputs:
        
        _output = np.tanh(np.dot(w, _input)+np.dot(u,state)+b)
        outputs.append(_output)
        state=_output
        
    return np.stack(outputs, axis=0)

def main():
    
    print("-----------------CASE 1-----------------")
    _input1 = [[0], [0], [0], [0], [0]]
    
    case1_a = rnn(_input1, input_size=1, output_size=1)
    print('\nCASE 1_a:', case1_a)
    case1_b = rnn(_input1, input_size=1, output_size=1, bias = True)
    print('\nCASE 1_b:', case1_b)
    
    
    print("\n-----------------CASE 2-----------------")
    _input2 = [[1], [1], [1], [1], [1]]
    
    case2_a = rnn(_input2, input_size=1, output_size=1)
    print('\nCASE 2_a:', case2_a)
    case2_b = rnn(_input2, input_size=1, output_size=1, bias = True)
    print('\nCASE 2_b:', case2_b)
    
    
    print("\n-----------------CASE 3-----------------")
    _input3 = [[1], [2], [3], [4], [5]]
    
    case3_a = rnn(_input3, input_size=1, output_size=2)
    print('\nCASE 3_a:', case3_a)
    case3_b = rnn(_input3, input_size=1, output_size=2, bias = True)
    print('\nCASE 3_b:', case3_b)
    
    return case1_a, case1_b, case2_a, case2_b, case3_a, case3_b

if __name__ == '__main__':
    main()