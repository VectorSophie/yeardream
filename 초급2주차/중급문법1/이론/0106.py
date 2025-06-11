my_dict1 = {}

my_dict1[1] = "Integer"
my_dict1['a'] = "String"

print(my_dict1)

key_candidate1 = [1, 2, 3]
key_candidate2 = (1, 2, 3)

my_dict2 = {None : "I am Value!"}
del my_dict2[None]
my_dict2[key_candidate2] = "I am Value!"

print(my_dict2)