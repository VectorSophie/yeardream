import math

def sigmoid(x) :
    return 1 / (1 + math.exp(-x))

def getParameters(X, y) :
    
    f=len(X[0])
    w=[1,1,1,1,1]
  
    while True :

        wPrime = [0] * f
        vv=[]
        
        for i in range(len(y)) :
            r = 0
            for j in range(f) :
                r = r + X[i][j] * w[j]
            
            v = sigmoid(r)
            vv.append(v)
        
            for j in range(f) :
                wPrime[j] += -((v - y[i]) * v * (1-v) * X[i][j])
        
        flag = False
        
        for i in range(f) :
            if abs(wPrime[i])>=0.001 :
                flag = True
                break
        
        if flag == False :
            break
        
        for j in range(f) :
            w[j] = w[j] +wPrime[j]
    
    return w

def main():
    
    X = [(1, 0, 0), (1, 0, 1), (0, 0, 1)]
    y = [0, 1, 1]

    print(getParameters(X, y))

if __name__ == "__main__":
    main()