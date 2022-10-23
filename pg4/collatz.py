def collatz(n):
    term = n
    sequence = str(n)
    while term != 1:
        sequence += ','
        term = (term // 2) * (term % 2 == 0) + (term * 3 + 1) * (term % 2 != 0)
        sequence += str(term)
    return sequence

print(collatz(3))
