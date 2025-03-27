shopping_list = []

while True:
    product = input()
    if product != "구매":
        shopping_list.append(product)
    else:
        break


print(shopping_list)