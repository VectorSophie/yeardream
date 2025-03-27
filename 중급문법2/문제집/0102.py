def check_record(s):
    count = 0  
    for i in range(len(s)):
        if s[i] == 'A':
            count += 1
        if count >= 2:  
            return False
        if s[i] == 'L' and s[i + 1] == 'L' and s[i + 2] == 'L':
            return False  
    
    return True

students =['AAPPPPPPPP', 'PPPLLLPPPP', 'APPPPPLLPP', 'PPPLLLAAPP']

for s in students:
    print(check_record(s))