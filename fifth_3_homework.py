import string

Initial_text = input("Введіть текст: ")
End_result = "#"
new_word = True

for i in Initial_text:
    if i in string.punctuation or i == " ":
        new_word = True
        continue

    if new_word:
        End_result += i.upper()
        new_word = False

    else:
        End_result += i.lower()

End_result = End_result[:140]
print(End_result)