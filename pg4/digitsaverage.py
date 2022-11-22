def digits_average(n):
    def roundUp(n):
        return int(n + 0.5)
    sum = 0 * (n > 9) + n * (n <= 9)
    while n > 9:
        sum = sum * 10 + roundUp((n % 10 + (n // 10) % 10) / 2)
        n = n // 10
    return (int, digits_average).__getitem__(sum > 9)(sum)

print(digits_average(158))
    
# For future reference (if I remember to come here lmao)
# return  [int, digits_average][sum > 9](sum)