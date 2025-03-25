string_num = input()
result = []
for i in string_num:
    if i not in result:
        result.append(i)
decimal_result = int(''.join(result))
binary_result = bin(decimal_result)[2:]
print(binary_result)