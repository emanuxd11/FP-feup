import math

def compute_euler(n):
    e = 0
    for i in range(0, n+1):
        e += 1 / math.factorial(i)
    return round(e, 5)

print(compute_euler(50))