def adigits(a, b, c):
    digits = [a, b, c]
    digits.sort()
    return digits[0] * 100 + digits[1] * 10 + digits[2]

print(adigits(9, 2, 3))