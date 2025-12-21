import keyword
import string

entered_information = input("Enter the information: ")
is_valid = True

if (
        entered_information == ""
        or entered_information[0].isdigit()
        or entered_information in keyword.kwlist
        or entered_information.count("_") > 1
):
    is_valid = False

for i in entered_information:
    if i.isupper() or i == " " or (i in string.punctuation and i != "_"):
        is_valid = False
        break

print(is_valid)