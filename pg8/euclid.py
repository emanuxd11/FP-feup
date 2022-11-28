def gcd_rec(n1, n2):
    return [int, lambda *_ : gcd_rec(n2, n1 % n2)][n2 != 0](n1)

print(gcd_rec(12, 14))