import string
user_input = input("Введіть дві літери через дефіс: ")

start_letter, end_letter = user_input.split("-")
letters = string.ascii_letters
start_index = letters.index(start_letter)
end_index = letters.index(end_letter)
result = letters[start_index:end_index + 1]

print(result)