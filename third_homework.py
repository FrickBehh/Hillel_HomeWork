first_number = float(input("Введіть перше число: "))
second_numer = float(input("Введіть друге число: "))

operation = input("Виберіть дію (+, -, *, /): ")

if operation == "+":
    print("Результат: ", first_number + second_numer)
elif operation == "-":
    print("Результат: ", first_number - second_numer)
elif operation == "*":
    print("Результат: ", first_number * second_numer)
elif operation == "/":
    if second_numer != 0:
        print("Результат: ", first_number / second_numer)
    else:
        print("Помилка: не можна ділити на нуль")
else:
    print("Помилка: неправильна операція")