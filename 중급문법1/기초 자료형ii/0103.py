dress_code = list()

enter = ""
while enter != "end":
    enter = input()
    dress_code.append(enter)
dress_code.remove('end')

print(dress_code)

dress_code = [color for color in dress_code if color != "red"]

print(dress_code)