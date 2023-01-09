def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_composites(n):
    for i in range(n +1 ):
        if not isprime(i):
            yield i 