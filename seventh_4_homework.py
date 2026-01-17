def common_elements():
    multiples_3 = {x for x in range(100) if x % 3 == 0}
    multiples_5 = {x for x in range(100) if x % 5 == 0}
    return multiples_3 & multiples_5