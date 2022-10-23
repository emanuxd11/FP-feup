def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primes_difference(n):   
    if n <= 3:
        return

    firstPrime = n + 1
    while not is_prime(firstPrime):
        firstPrime += 1
    
    secondPrime = n
    while not is_prime(secondPrime):
        secondPrime -= 1

    return firstPrime - secondPrime

print(primes_difference(193))
