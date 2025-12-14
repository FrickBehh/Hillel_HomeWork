num = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
non_zeros = []
number_of_zeros = []

for nums in num:
    if nums != 0:
        non_zeros += [nums]
    else:
        number_of_zeros += [0]
print(non_zeros + number_of_zeros)
