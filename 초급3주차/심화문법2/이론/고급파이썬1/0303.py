def _square(num):
    return num * num

square = lambda x: x * x

def _first_letter(string):
    return string[0] if string else ''

first_letter = lambda string: string[0] if string else ''

testcases1 = [3, 10, 7, 1, -5]
for num in testcases1:
    assert(_square(num) == square(num))

testcases2 = ['', 'hello', 'elice', 'abracadabra', '  abcd  ']
for string in testcases2:
    assert(_first_letter(string) == first_letter(string))

print("성공했습니다!")