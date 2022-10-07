P = int(input())
r = float(input())
n = int(input())

A = P * (1 + r/n) ** (n*2)
print(round(A, 3))
