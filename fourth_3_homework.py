import random
first_list = []
diapason = random.randint(3, 10)

for i in range(diapason):
    first_list.append(random.randint(1, 10))
second_list = [first_list[0], first_list[2], first_list[-2]]