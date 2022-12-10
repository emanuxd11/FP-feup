def primes_range(start, stop):
    for i in range(start, stop + 1):
        if [j for j in range(2, i) if i % j == 0] == [] \
            and i > 1:
            yield i
            
print(list(primes_range(1, 10)))