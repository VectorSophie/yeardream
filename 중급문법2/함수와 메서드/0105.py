def pyramid(floor):
    for i in range(floor):
        print(" " * (floor - i - 1), end="")
        print("*" * (i * 2 + 1))
        
# 정수를 입력받고 피라미드를 출력하는 부분입니다. 수정하지 마세요!
var = int(input())
pyramid(var)