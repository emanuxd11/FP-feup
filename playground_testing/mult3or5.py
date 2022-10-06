n = int(input())

def int_sum(n):
    return n * (n+1) / 2

print(int(3*int_sum(int(n/3)) + 5*int_sum(int(n/5)) - 15*int_sum(int(n/15))))