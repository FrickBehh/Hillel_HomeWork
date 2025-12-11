numbers = [22, 2, 3, 6, 7, 18, 23, 33]
count = len(numbers) // 2
firstlist = numbers[0 : count]
secondlist = numbers[count : ]

if count == 0:
    result = [[], []]
elif count % 2 == 0:
    result = [firstlist, secondlist]
else:
    firstlist = numbers[0 : count+1]
    secondlist = numbers[count+1 : ]
    result = [firstlist, secondlist]
print(result)