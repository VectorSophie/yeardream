s = input()

o1 = s[0] 
o2 = s[-1] 

num = int(s[1:-1]) 

if num % 5 == 0 and num % 3 == 0:
        print("")  
elif num % 5 == 0:
    print(o1 * num)  
elif num % 3 == 0:
    print(o2 * num)  
else:
    print(o1 * num + o2 * num) 