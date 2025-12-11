numbers = [22, 2, 3, 6, 7, 18, 23, 33]

if len(numbers) < 2:
    print(numbers)
else:
    firstnumber = numbers[0]
    lastnumber = numbers[-1]
    numbers.insert(0, lastnumber)
    numbers.pop()
    numbers.append(firstnumber)
    numbers.pop(1)
    print(numbers)