def main():
    
    x = [1,2,3,4]
    
    w = [0.3,0.5,0.1,0.7]
    b = 2
    
    output, y = perceptron(w,x,b)
    
    print('output: ', output)
    print('y: ', y)

def perceptron(w, x, b):
    
    output = x[0]*w[0]+x[1]*w[1]+x[2]*w[2]+x[3]*w[3]+b
    
    y = 1 if output >= 0 else 0
    
    return output, y

if __name__ == "__main__":
    main()