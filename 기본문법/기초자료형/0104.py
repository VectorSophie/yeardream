korean = 7000

chinese = 6000

western = 8500

discount_korean = korean * 0.9

total_price = discount_korean * 55 + chinese * 43 + western * 52

print("한식 : " + str(korean))
print("중식 : " + str(chinese))
print("양식 : " + str(western))
print("할인된 한식 : " + str(discount_korean))
print("전체 예산 : " + str(total_price))