def sum_digits_rec(n):
    sum = n % 10
    sum += [int, lambda *_ : sum_digits_rec(n // 10)][n > 9](0)
    return sum

print(sum_digits_rec(12))