def Perceptron(x_1,x_2,w_1,w_2):
    
    bias = -1
    
    output = (x_1*w_1+x_2*w_2+bias)
    
    y = 1 if output >0 else 0
    
    return output, y

def input_func():
    
    x_1 =  int(input("x_1 : 비가 오는 여부(1 or 0)을 입력하세요."))
    
    x_2 =  int(input("x_2 : 여친이 만나자고 하는 여부(1 or 0)을 입력하세요."))
    
    w_1 =  int(input("w_1 : 비를 좋아하는 정도 값(-5 ~ 5)을 입력하세요."))
    
    w_2 =  int(input("w_2 : 여친을 좋아하는 정도 값(-5 ~ 5)을 입력하세요."))
    
    return x_1, x_2, w_1, w_2
    
def main():
    
    x_1, x_2, w_1, w_2 = input_func()
    
    result, go_out = Perceptron(x_1,x_2,w_1,w_2)
    
    print("\n신호의 총합 : %d" % result)
    
    if go_out > 0:
        print("외출 여부 : %d\n ==> 외출한다!" % go_out)
    else:
        print("외출 여부 : %d\n ==> 외출하지 않는다!" % go_out)
    
if __name__ == "__main__":
    main()