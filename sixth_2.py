seconds = int(input("Введіть кількість секунд: "))

s_d = 24 * 60 * 60
s_h = 60 * 60
s_m = 60
#Days
days = seconds // s_d
seconds = seconds % s_d
#Hours
hours = seconds // s_h
seconds = seconds % s_h
#Minutes
minutes = seconds // s_m
seconds = seconds % s_m

if 11 <= days % 100 <= 14:
    day_word = "днів"
elif days % 10 == 1:
    day_word = "день"
elif 2 <= days % 10 <= 4:
    day_word = "дні"
else:
    day_word = "днів"

time_str = (
    str(hours).zfill(2) + ":" +
    str(minutes).zfill(2) + ":" +
    str(seconds).zfill(2)
)

print(f"{days} {day_word}, {time_str}")