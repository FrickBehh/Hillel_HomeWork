nums = [6]

if nums:
    num = nums[::2]
    last_digit = nums[-1]
    total = 0
    for i in num:
        total += i
    print(total*last_digit)
else:
    print(0)
