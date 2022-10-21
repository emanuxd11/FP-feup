from calendar import c


def calc_triangular(n):
    k = 0
    for i in range(1, n+1):
        k += i
    return k
print(calc_triangular(int(input())))