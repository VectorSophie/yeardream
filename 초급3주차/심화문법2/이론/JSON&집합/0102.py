my_set = {3, 5}

submit1 = my_set.copy()

my_set.add(7)

submit2 = my_set.copy()

new_numbers = [1, 2, 3, 4, 5]
my_set.update(new_numbers)
 
submit3 = my_set.copy()

my_set = {num for num in my_set if num%2!=0}

submit4 = my_set.copy()