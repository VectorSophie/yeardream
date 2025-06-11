enter = ""
my_list = []
while len(my_list) != 5:
    enter = int(input())
    my_list.append(enter)

# 2번을 해보세요.
def comparison(l):
    return int(max(l)) - int(min(l))

print(comparison(my_list))