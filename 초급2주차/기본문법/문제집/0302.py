x = input().split( )

combination = [('치즈', '달걀'),
('고구마', '김치'),
('감자', '토마토')]

found = False
for a, b in combination:
    if a in x and b in x:
        found = True
        break
print(found)