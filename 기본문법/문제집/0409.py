# string_num = input()
# result = []
# for i in string_num:
#     if i not in result:
#         result.append(i)
# decimal_result = int(''.join(result))
# binary_result = bin(decimal_result)[2:]
# print(binary_result)

string_num = input()

result = []
i = 0
while i < len(string_num):
    count = 1
    while i + 1 < len(string_num) and string_num[i] == string_num[i + 1]:
        count += 1
        i += 1
    result.append(string_num[i] * (count // 2 + count % 2))
    i += 1

decimal_result = int(''.join(result))
binary_result = bin(decimal_result)[2:]
print(binary_result)
