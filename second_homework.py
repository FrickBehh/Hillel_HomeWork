#1. Квадрат числа.
number = int(input("Введіть число: "))
print('Квадрат числа:', number**2)

#2. “Середнє трьох чисел”
first_number = int(input("Введіть перше число: "))
second_number = int(input("Введіть друге число: "))
third_number = int(input("Введіть третє число: "))
print('Середнє:',(first_number + second_number + third_number) / 3)

#3. “Перетворення хвилин у години”|
number_of_minutes = int(input("Введіть кількість хвилин: "))
hours, minutes = divmod(number_of_minutes, 60)
print(hours, "години ", minutes, 'хвилин')

#4  “Розрахунок знижки”
price, discount = int(input("Введіть ціну: ")), int(input('Введіть знижку (%): '))
discount_amount = (price*discount)/100
print('Ціна зі знижкою: ', price - discount_amount)

#5. “Остання цифра числа”
number = int(input("Введіть число: "))
print('Остання цифра: ', number%10)

#6. “Периметр прямокутника”
length, width = int(input("Введіть довжину: ")), int(input("Введіть ширину: "))
print('Периметр: ', (length+width)*2)

#7. Виведення числа в стовпчик
number = int(input("Введіть 4-х значне число: "))
print(number//1000)
print((number//100)%10)
print((number//10)%10)
print(number%10)