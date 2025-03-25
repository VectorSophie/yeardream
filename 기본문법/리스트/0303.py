my_list = list(map(int, input().split( )))

average = int(sum(map(int, my_list)) / len(my_list))
print(average)