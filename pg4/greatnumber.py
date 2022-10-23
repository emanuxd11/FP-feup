def greatest(num):
    digits = list(str(num))
    digits.sort(reverse = True)
    return int("".join(digits))

print(greatest(123))