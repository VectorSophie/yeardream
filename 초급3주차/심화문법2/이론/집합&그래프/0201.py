from viewers import dark_knight, iron_man

dark_knight_set = set(dark_knight)
iron_man_set = set(iron_man)

both = len(dark_knight_set & iron_man_set)

either = len(dark_knight_set | iron_man_set)

dark_knight_only = len(dark_knight_set - iron_man_set)

iron_man_only = len(iron_man_set - dark_knight_set)

print("두 작품 모두 시청: {}명".format(both))
print("하나 이상 시청: {}명".format(either))
print("다크나이트만 시청: {}명".format(dark_knight_only))
print("아이언맨만 시청: {}명".format(iron_man_only))